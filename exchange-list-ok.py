import re
import time
from requests_html import HTMLSession
from telegram_lib import sendMessage

session = HTMLSession()
url = "https://www.okx.com/support/hc/zh-cn/sections/360000030652-%E6%9C%80%E6%96%B0%E5%85%AC%E5%91%8A"
lastAnn = ''
while True:
	r = session.get(url)
	ann = re.findall('\n欧易关于.*?\n',r.html.text)
	if lastAnn == '':
		lastAnn = ann
		print('init new ann\n' + ann[0])
		sendMessage('init new ann\n' + ann[0])
		continue
	if ann[0] == lastAnn[0]:
		print('no change')
	else:
		print('new ann\n' + ann[0])
		sendMessage('new ann\n' + ann[0])
	time.sleep(5)