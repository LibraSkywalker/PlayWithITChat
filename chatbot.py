#coding=utf-8
import itchat
from qqbot import _bot as bot
from itchat.content import *
import datetime
import time

fname = time.strftime("%Y-%m-%d") + ".txt"
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_text(msg):
	f = open(fname,"a+",encoding='gbk')
	dude = bot.List('buddy','菜鸟天堂')
	content = msg['Text']
	print(content,file = f)
	print(content)
	bot.SendTo(dude[0],content)
	f.close()

itchat.auto_login(enableCmdQR=True)
bot.Login(['-q','973231279'])
itchat.run()