import requests
import json
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import numpy as np
import jieba
import xlwt
import sys
import os
import shutil
import time
import random

if len(sys.argv) < 4:
    print("必须输入商品 ID 和店铺 ID prefix")
    sys.exit()
itemId = sys.argv[1]
sellerId = sys.argv[2]
prefix = sys.argv[3]
cnt = 0

Target_File = "output/{}_{}_{}".format(prefix, itemId, sellerId)
# 这里需要替换为你自己的 Cookie
YourCookie = "enc=%2Fic54yXpiVqkdb1%2BHVZRyYNJ2kCI0yF9qn7MA%2B4NACLSH1RNTkVejLnvTj7%2FoRfHhcppQqR7FMeE87sPAU75hA%3D%3D; dnk=nskyzone; hng=CN%7Czh-CN%7CCNY%7C156; t=b7908c8c8e1cec0033da94ff54e3f930; tracknick=nskyzone; _tb_token_=eaeee51347e13; cookie2=18fc2bd3b8be07894a78e33b3d2c9b5d; cna=HzCBEwc1GhACAXlFKsJvjZQ9; _m_h5_tk=efe6bfdde974919d4ca36e3f6161801a_1590161592999; _m_h5_tk_enc=e32f115ca676f3b8c1992057de9670c3; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&tag=8&cart_m=0&cookie21=W5iHLLyFe3xm&cookie14=UoTV7NTZ6IXEOA%3D%3D&pas=0&existShop=false&lng=zh_CN; uc3=lg2=URm48syIIVrSKA%3D%3D&id2=UU23A4e1e61O&nk2=DfRa06PWDrs%3D&vt3=F8dBxGZiR0AoWFe50DQ%3D; lid=nskyzone; uc4=nk4=0%40DyERZS5nO7MEAGxW%2FPM99K8CWA%3D%3D&id4=0%40U2%2Fwt2jG5LzCGqWhufpNwuWdVTA%3D; lgc=nskyzone; sgcookie=E%2B74XIaY5D5VZSE6c1nMC; csg=a19181a0; x5sec=7b22726174656d616e616765723b32223a226235303630306330623165343236326437346236616461343163386437336233434c502b702f5946454a6577774a756d774d7a2f6e41453d227d; l=eBrGmjGrvrqVK6I6BO5Churza77TfCAf1PVzaNbMiInca1ulG13hXNQD1472Pdtjgt5fhexrhV5GsRnpS8ULRx_ceTwhKXIpBBvw8e1..; isg=BOjoVwmCIkIhWgsOLQN9dfddudb6EUwbQl5I96IdWmOF_YtnSCJPq8x79ZUNSATz"
# 获取字符串长度，一个中文的长度为2
def len_byte(value):
    length = len(value)
    utf8_length = len(value.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)*256

def getMaxLength(value, oldLength):
    return max(oldLength, len_byte(value))
print('asdf')
class TaoBao:
    lastPage = 1
    url="https://rate.tmall.com/list_detail_rate.htm"
    header={
        "cookie":YourCookie,
        "referer":"https://detail.tmall.com/item.htm",
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.37",
    }
    params={                                #必带信息
        "itemId":"",                       #商品id  
        "sellerId":"",
        "currentPage":"",                  #页码
        "order":"3",                        #排序方式:1:按时间降序  3：默认排序
        "callback":"jsonp775",
        }
    def __init__(self, id:str, sellerId:str):
        self.params['itemId']=id
        self.params['sellerId']=sellerId

    def getPageData(self,pageIndex:int):
        self.params["currentPage"]=str(pageIndex)
        print("正在请求第 {} 页评论".format(pageIndex))
        req=requests.get(self.url,self.params,headers=self.header,timeout = 2).content.decode('utf-8');     #解码，并且去除str中影响json转换的字符（\n\rjsonp(...)）;
        req=req[req.find('{'):req.rfind('}')+1]
        ret = json.loads(req);
        return ret;

    def setOrder(self,way:int):
        self.params["order"]=way;

    def getAllData(self):
        Data=self.getPageData(1)
        self.lastPage= Data['rateDetail']['paginator']['lastPage']
        rateCount = Data['rateDetail']['rateCount']['total']
        print("一共有 {} 条评论，共计 {} 页".format(rateCount, self.lastPage))

        for i in range(2,self.lastPage+1):
            try:
                time.sleep(0.1+random.random()*10)
                tmp_data = self.getPageData(i)
                Data['rateDetail']['rateList'].extend(tmp_data['rateDetail']['rateList'])
            except Exception as e:
                print(e,tmp_data)
        return Data;

    def simplifyData(self, data):
        ret = []
        global cnt
        for comment in data['rateDetail']['rateList']:
            item = {};
            for pic in comment['pics']:
                html = requests.get('http:'+pic)
                with open(Target_File + '/%s_%s_%s_%s.jpg' %(prefix, itemId, sellerId,cnt), 'wb') as file:
                    file.write(html.content)
                cnt += 1
            item['pics'] = ','.join(comment['pics'])
            item['commentTime'] = comment['rateDate']
            item['comment'] = comment['rateContent']
            item['type'] = comment['auctionSku']
            item['appendComment'] = ''
            if comment['appendComment']:
                item['appendComment'] = comment['appendComment']['content']
            ret.append(item);
            
        return ret;

    def analyze(self, data):
        #导入停用词
        stoplist = [line.strip() for line in open('stop.txt','r',encoding="utf8").readlines() ]
        #打开本地数据文件，注意文件名不能用中文
        # text_from_file_with_apath = open('new.txt',encoding="utf8").read()
        text_from_file_with_apath = data
        #去除停用词
        for stop in stoplist:
            jieba.del_word(stop)
        
        #用jieba模块进行挖掘关键词
        wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=False)
        wl_space_split = " ".join(wordlist_after_jieba)
        
        coloring=np.array(Image.open("cat_new.jpg"))
        my_wordcloud = WordCloud(background_color="white",
                                 mask=coloring,
                                 width=2000, height=1000,
                                 font_path="Hiragino Sans GB.ttc",
                                 max_words=400,
                                 max_font_size=80,
                                 min_font_size=10,
                                 random_state=40).generate(wl_space_split)
        my_wordcloud.to_file(Target_File+'/WordCloud.png');

    def toExcel(self, data):
        wb = xlwt.Workbook()
        # 添加一个表
        ws = wb.add_sheet('test')
        style = xlwt.XFStyle()
        style.alignment.wrap = 1

        line = 0;
        # 3个参数分别为行号，列号，和内容
        # 需要注意的是行号和列号都是从0开始的
        ws.write(line, 0, '时间')
        ws.write(line, 1, '评论')
        ws.write(line, 2, '追加评论')
        ws.write(line, 3, '分类')
        ws.write(line, 4, '图片')

        time_len = 10*256
        comment_len = 10*256
        appendComment_len = 10*256
        itemType_len = 10*256
        picsType_len = 10*256

        for item in data:
            line += 1
            picsType_len = max(len_byte(item['pics']), picsType_len)
            time_len = max(len_byte(item['commentTime']), time_len)
            comment_len = max(len_byte(item['comment']), comment_len)
            appendComment_len = max(len_byte(item['appendComment']), appendComment_len)
            itemType_len = max(len_byte(item['type']), itemType_len);

            ws.write(line, 0, item['commentTime'])
            ws.write(line, 1, item['comment'], style)
            ws.write(line, 2, item['appendComment'], style)
            ws.write(line, 3, item['type'])
            ws.write(line, 4, item['pics'])

        ws.col(0).width = min(time_len, 80*256)
        ws.col(1).width = min(comment_len, 80*256)
        ws.col(2).width = min(appendComment_len, 80*256)
        ws.col(3).width = min(itemType_len, 80*256)
        ws.col(3).width = min(itemType_len, 80*256)
        # 保存excel文件
        wb.save(Target_File+'/data.xls')


taobao=TaoBao(itemId, sellerId)
myJsonData = {}

if os.path.exists(Target_File):
    shutil.rmtree(Target_File)
os.makedirs(Target_File);

# myJsonData=taobao.getPageData(1)

myJsonData=taobao.getAllData()
with open(Target_File+'/data.json', 'w',encoding='utf8') as f:
    json.dump(myJsonData, f, ensure_ascii=False, indent=4, separators=(',', ':'))


simplifyData = taobao.simplifyData(myJsonData)

taobao.toExcel(simplifyData)

allComment = ""
for item in simplifyData:
    allComment = allComment+"\n"+item['comment']+"\n"+item['appendComment']+"\n"
taobao.analyze(allComment)

# subprocess.call(["open", Target_File])