import itchat, time
from itchat.content import TEXT
import json
import re
#name = ' '
roomslist = []
 
itchat.auto_login(enableCmdQR = False)

file = open('room_basic.txt','w',encoding='utf8')
def getroom_message(n):
  #获取群的username，对群成员进行分析需要用到
  itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
  RoomList = itchat.search_chatrooms(name=n)
  if RoomList is None:
    print("%s group is not found!" % (name))
  else:
    return RoomList[0]['UserName']
 
def getchatrooms():
  #获取群聊列表
  roomslist = itchat.get_chatrooms()
  json.dump(roomslist,file,indent=4, ensure_ascii=False)
  return roomslist
 
 
 
for i in getchatrooms():
  #print(i['NickName'])
  roomslist.append(i)
  # roomslist.append(i['NickName'])

img_number = 0
with open('群用户名.txt', 'w', encoding='utf-8')as f:
  for n in roomslist:
    # ChatRoomUserName = getroom_message(n)
    ChatRoomUserName = n['UserName']
    print(n)
    ChatRoomNickName = n['NickName']
    ChatRoom = itchat.update_chatroom(ChatRoomUserName, detailedMember=True)
    for i in ChatRoom['MemberList']:
      # json.dump(i,file,indent=4, ensure_ascii=False)
      if img_number % 500 == 0:
        print (i)
      
      img_file_name = '%s_%s_%s.jpg' %(ChatRoomNickName, i['NickName'], img_number)
      rstr = r"[\/\\\:\*\?\"\<\>\|\n\t]"  # '/ \ : * ? " < > |'
      img_file_name = 'pics/' + re.sub(rstr, "_", img_file_name)  # 替换为下划线
      img = itchat.get_head_img(userName=i["UserName"], chatroomUserName=ChatRoomUserName)

      fileImage = open(img_file_name,'wb')
      fileImage.write(img)
      fileImage.close()

      write_msg = '\t'.join(map(lambda x:str(x),[ChatRoomNickName, i['UserName'], i['NickName'], i['Province'],i['City'],i['Sex'], img_file_name]))
      img_number += 1
      print(write_msg,file=f)
      print('正在写入      ' +ChatRoomNickName+i['Province']+":",i['NickName'])

file.close()