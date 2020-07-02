import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from my_handlers import greet_user, error_callback, stat, back, karantin, en_mmundo, meri, meri_all, wiki, news, news_back, news_forward

def main():
    PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    logging.basicConfig(filename='bot.log', level=logging.INFO)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Статистика)$'), stat))
    dp.add_handler(MessageHandler(Filters.regex('^(Назад)$'), back))
    dp.add_handler(MessageHandler(Filters.regex('^(Карантин)$'), karantin))
    dp.add_handler(MessageHandler(Filters.regex('^(Ситуация в мире)$'), en_mmundo))
    dp.add_handler(MessageHandler(Filters.regex('^(Меры предосторожности)$'), meri))
    dp.add_handler(MessageHandler(Filters.regex('^(Показать все)$'), meri_all))
    dp.add_handler(MessageHandler(Filters.regex('^(О вирусе)$'), wiki))
    dp.add_handler(MessageHandler(Filters.regex('^(Новости)$'), news))
    dp.add_handler(MessageHandler(Filters.regex('^(Назад/)$'), karantin))
    dp.add_handler(MessageHandler(Filters.regex('^(Вверх)$'), en_mmundo))
    dp.add_handler(MessageHandler(Filters.regex('^(<-)$'), news_back))
    dp.add_handler(MessageHandler(Filters.regex('^(->)$'), news_forward))
    dp.add_error_handler(error_callback)

    logging.info("Bot has just started")
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()