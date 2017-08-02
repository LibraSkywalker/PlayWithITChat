#coding=utf-8
import itchat
from qqbot import _bot as bot
from itchat.content import *
import datetime
import time

fname = time.strftime("%Y-%m-%d") + ".txt"
@itchat.msg_register([TEXT, SHARING], isGroupChat=True)
def group_text(msg):
	f = open(fname,"a+")
	dude = bot.List('buddy','菜鸟天堂')
	content = msg['Text']
	group = msg['Nickname']
	if '1708 GRE B班' in group:
		print(content,file = f)
		print(content)
		print(msg)
	bot.SendTo(dude[0],content)
	f.close()

itchat.auto_login(enableCmdQR=2)
bot.Login(['-u','somebody','-q','973231279'])
itchat.run()
