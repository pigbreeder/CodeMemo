#!/usr/bin/env python
# encoding: utf-8

#图像大小范围设置
#plt.figure(figsize(3,2))
#图像标注
#    标题 plt.title(title)
#    坐标轴 plt.xlabel('this is x-axis')
#    图例 plt.legend(loc=[1.1, 0.5])
#
#直方图
#    plt.hist(x)   bins 参数可指定分组数
#
#plt.plot(x1, y1)
#plt.show()
#plt.plot(x,y) 是绘图 可以多次再plt.show()
#参数color表示颜色，常用的颜色如下。 - g: green - r: red - c: cyan - m: magenta - y: yellow - k: black - w: white
#参数marker，我们可以画出每个点，并设置点的外形。 - 'o'表示圆点 - 's'表示方点 - ','表示小像素点 - '^'表示上三角 - 'v'表示下三角
#参数alpha表示透明度，取值0到1之间，1表示不透明。
#参数lw 表示线宽
import numpy
import pandas
from matplotlib.pyplot import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,4,9,endpoint=True))

# 设置纵轴的上下限
ylim(-1.0,1.0)

# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()
