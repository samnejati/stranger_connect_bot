import telebot
import os
from loguru import logger 
# print(f'printing the environment variables: start... \n\n\n{os.environ}\n\n\n\... end')
# print(f'printing telegam API:\n\n{os.environ["TELEGRAMBOT_TOKEN"]}')

class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(
        os.environ['TELEGRAMBOT_TOKEN']
        , parse_mode=None
        ) # You can set parse_mode by default. HTML or MARKDOWN

		#using the wrapping logic:
		self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
		
	# @bot.message_handler(commands=['start', 'help']) ==> no longer used
	def send_welcome(message):
		bot.reply_to(message, "Howdy, how are you doing?")
	
	def run (self):
		logger.info('Running bot...')
		self.bot.polling()

if __name__ == '__main__':
	bot = Bot()
	bot.run()
	


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# print('Starting bot...')
# bot.polling()
