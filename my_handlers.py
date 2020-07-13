from my_utils import main_keyboard, stat_keyboard, karantin_keyboard, que_en_mundo_keyboard, meri_keyboard, news_keyboard
import parsers.NewsParser, parsers.WikiParser, parsers.C1MapsParser

cards = parsers.NewsParser.ParserNews().get_small_cards()
cards_handler = 0
c = parsers.C1MapsParser.C1maps()
wiki1 = parsers.WikiParser.get_wiki_covid()

def show_news(update, context):
    if cards[cards_handler]['title'] != None:
        update.message.reply_text(cards[cards_handler]['title'], reply_markup=news_keyboard())
    update.message.reply_text(cards[cards_handler]['image'], reply_markup=news_keyboard())
    update.message.reply_text(cards[cards_handler]['href'], reply_markup=news_keyboard())
    update.message.reply_text(cards[cards_handler]['time'], reply_markup=news_keyboard())


def greet_user(update, context):
    update.message.reply_text('Меню', reply_markup=main_keyboard())

def stat(update, context):
    update.message.reply_text('Вы вошли в меню статистики', reply_markup=stat_keyboard())

def stat_rf(update, context):
    l = c.getRusData()
    for key, value in l:
        update.message.reply_text(key + '->' + str(value), reply_markup=stat_keyboard())

def stat_wrld(update, context):
    lw = c.getWorldData()
    for key, value in lw:
        update.message.reply_text(key + '->' + str(value), reply_markup=stat_keyboard())

def back(update, context):
    update.message.reply_text('Возвращаемся назад', reply_markup=main_keyboard())

def karantin(update, context):
    update.message.reply_text('Вы вошли в меню карантина', reply_markup=karantin_keyboard())

def en_mmundo(update, context):
    update.message.reply_text('Вы вошли в меню по ситуации в мире', reply_markup=que_en_mundo_keyboard())

def meri(update, context):
    myFile = open('recommendations.txt', 'r')
    with myFile:
        for c in range(20):
            update.message.reply_text(myFile.readline(), reply_markup=meri_keyboard())

def meri_all(update, context):
    myFile = open('recommendations.txt', 'r')
    with myFile:
        for c in range(27):
            update.message.reply_text(myFile.readline(), reply_markup=main_keyboard())

def wiki(update, context):
    update.message.reply_text(wiki1['title'], reply_markup=main_keyboard())
    update.message.reply_text(wiki1['url'], reply_markup=main_keyboard())

def news(update, context):
    global cards_handler
    cards_handler = 0
    show_news(update, context)

def news_back(update, context):
    global cards_handler
    if cards_handler > 0:
        cards_handler = cards_handler - 1
    show_news(update, context)

def news_forward(update, context):
    global cards_handler
    if cards_handler < len(cards) - 1:
        cards_handler = cards_handler + 1
    show_news(update, context)

def error_callback(update, error):
    try:
        raise error
    except:
        print("Telegram Error")
        print(f'Error with {update.message.text}')
        update.message.reply_text(f'Error with {update.message.text}. Try again')
        print(error)

