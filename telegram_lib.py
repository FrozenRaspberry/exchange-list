import config_telegram
import telegram

bot = telegram.Bot(token=api_key)

def sendMessage(msg):
	bot.send_message(chat_id, text=msg)