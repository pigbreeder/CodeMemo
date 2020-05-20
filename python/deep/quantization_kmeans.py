
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time
 

def get_model(image_array, n_bins=64):
    
    w, h, d = image_array.shape
    image_array = np.reshape(image, (w * h, d)) #每个点作为一个样本，维数为3
    print("Fitting model on a small sub-sample of the data")
    t0 = time()
    image_array_sample = shuffle(image_array, random_state=0)[:1000]
    #将所有点打乱顺序，取前1000个点，不使用所有点主要是为了训练模型的速度
    kmeans = KMeans(n_clusters=n_bins, random_state=0).fit(image_array_sample)
    print("fit done in %0.3fs." % (time() - t0))
     
    # Get labels for all points
    print("Predicting color indices on the full image (k-means)")
    t0 = time()
    labels = kmeans.predict(image_array)
    print("predict done in %0.3fs." % (time() - t0))
    return kmeans.cluster_centers_, labels # 获取聚类中心和每个点对应的聚类中心
 
 
def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    #每个像素查询码本（对应0~63），取得其对应的像素值
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

n_bins = 2

# Load the Summer Palace photo
image = cv2.imread("123.jpg")
 
# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow behaves works well on float data (need to
# be in the range [0-1])
# imshow(winname, mat) -> None
#. The function may scale the image, depending on its depth:
#. - If the image is 8-bit unsigned, it is displayed as is.
#. - If the image is 16-bit unsigned or 32-bit integer, the pixels are divided by 256. 
#    That is, the value range [0,255\*256] is mapped to [0,255].
#. - If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255. That is, the
#.   value range [0,1] is mapped to [0,255].
image = np.array(image, dtype=np.float64) / 255
 
# Load Image and transform to a 2D numpy array.
w, h, d = original_shape = tuple(image.shape)
assert d == 3   #一定要是彩色图像，不是3会报错

cluster_centers_, labels = get_model(image, n_bins)
# Display all results, alongside original image
 
cv2.namedWindow('Original image')
cv2.imshow('Original image',image)
name = 'Quantized image ('+str(n_bins)+' colors, K-Means)'
cv2.namedWindow(name)
cv2.imshow(name, cluster_centers_[labels].reshape(w,h,-1))
cv2.imshow(name+' 2',recreate_image(cluster_centers_, labels, w, h))

cv2.waitKey(0)