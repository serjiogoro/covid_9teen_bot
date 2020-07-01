
from my_utils import main_keyboard, stat_keyboard, karantin_keyboard, que_en_mundo_keyboard, meri_keyboard
import bot19

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

def error_callback(update, error):
    try:
        raise error
    except:
        print("Telegram Error")
        print(f'Error with {update.message.text}')
        update.message.reply_text(f'Error with {update.message.text}. Try again')
        print(error)

