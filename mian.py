
#安装python3.5以上
#pip install itchat-uos
# coding:utf-8
from threading import Thread
import datetime
import itchat
from itchat.content import TEXT
import time



@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.user.NickName == "广州乱斗堂Guangzhou Smash":
        print("\033[0;32;10m%s\033[0m" % msg.actualNickName)
        print(msg.text)
        if msg.actualNickName in message_user:
            message_dict[msg.actualNickName] += 1
        else:
            message_user.append(msg.actualNickName)
            message_dict[msg.actualNickName] = 1


itchat.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')


def send_msg():
    res = itchat.search_chatrooms(name='广州乱斗堂Guangzhou Smash')[0]
    while True:
        input_msg = input("")
        res.send(msg=input_msg)


thread = Thread(target=send_msg)
thread.start()
itchat.run()

