import telebot
from urllib.request import urlopen, Request
import urllib
from bs4 import BeautifulSoup
import constants

try:
    bot=telebot.TeleBot(constants.tokenTelegram)

    @bot.message_handler(content_types=["text"])
    def repeat_all_messages(message):
        try:
            searchRequest = urlopen(Request('https://www.startpage.com/do/search?q=' + urllib.parse.quote(message.text) + '&l=russian',
                headers={'User-Agent': 'Mozilla'})).read()
            resultList = bsObj.findAll('div', {'class': 'result'})
            ansver = "____"
            for result in resultList:
                ansver += result.get_text()
                bot.send_message(message.chat.id, ansver)
            except Exception as e:
                bot.send_message(message.chat.id, e)

                if __name__ == '__main__':
                    bot.polling(none_stop=True)

                except E as e:
