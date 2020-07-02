from telegram import ReplyKeyboardMarkup, KeyboardButton
import settings

def main_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Статистика')],
                                [KeyboardButton('Карантин')],
                                [KeyboardButton('Меры предосторожности')],
                                [KeyboardButton('Опрос')],
                                [KeyboardButton('О вирусе')]
                                ])

def meri_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Показать все')],
                                [KeyboardButton('Назад')]
                                ])

def stat_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('РФ')],
                                [KeyboardButton('Весь мир')],
                                [KeyboardButton('Назад')]
                                ])

def karantin_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Ситуация в мире')],
                                [KeyboardButton('Галерея')],
                                [KeyboardButton('Назад')]
                                ])

def que_en_mundo_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Новости')],
                                [KeyboardButton('Страны в изоляции')],
                                [KeyboardButton('Назад/')]
                                ])
def news_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('<-'), KeyboardButton('Вверх'), KeyboardButton('->')]
                                ])