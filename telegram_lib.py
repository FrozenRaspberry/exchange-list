import config_telegram
import telegram

# api_key = '5282794877:AAHlAPZ6Nq0i3oUVMNfRCd_4pZ48Rep5C-M'
# user_id = 'hometruck'

bot = telegram.Bot(token=api_key)

def sendMessage(msg):
	bot.send_message(chat_id, text=msg)