
#安装python3.5以上
#pip install itchat-uos
# coding:utf-8

from threading import Thread

import itchat
from itchat.content import TEXT


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.user.NickName == "广州乱斗堂Guangzhou Smash":
        print(msg.actualNickName)
        print(msg.text)


itchat.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')


def send_msg():
    res = itchat.search_chatrooms(name='广州乱斗堂Guangzhou Smash')[0]
    while True:
        input_msg = input("")
        res.send(msg=input_msg)


thread = Thread(target=send_msg)
thread.start()
itchat.run()
