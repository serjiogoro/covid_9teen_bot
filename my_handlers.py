from my_utils import main_keyboard, stat_keyboard, karantin_keyboard, que_en_mundo_keyboard, meri_keyboard, news_keyboard
import bot19_parser1

cards = bot19_parser1.ParserNews().get_small_cards()
cards_handler = 0

def show_news(update, context):
    update.message.reply_text(cards[cards_handler]['title'], reply_markup=news_keyboard())
    update.message.reply_text(cards[cards_handler]['image'], reply_markup=news_keyboard())
    update.message.reply_text(cards[cards_handler]['href'], reply_markup=news_keyboard())
    update.message.reply_text(cards[cards_handler]['time'], reply_markup=news_keyboard())


def greet_user(update, context):
    update.message.reply_text('Меню', reply_markup=main_keyboard())

def stat(update, context):
    update.message.reply_text('Вы вошли в меню статистики', reply_markup=stat_keyboard())

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
    #res = bot19.get_wiki_covid(dummy)
    update.message.reply_text('title', reply_markup=main_keyboard())

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

