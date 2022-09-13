import re
import time
from requests_html import HTMLSession
from telegram_lib import sendMessage

session = HTMLSession()
url = "https://www.binance.com/zh-CN/support/announcement/c-48?navId=48"
lastAnn = ''
while True:
	r = session.get(url)
	ann = re.findall('"幣安將.*?",',r.html.text)
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