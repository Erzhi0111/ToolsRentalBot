import telebot
from telebot import types

token = '7043732039:AAEOdcCTISzF0YCJv1v6dk2vM4Dj4NsnisQ'
bot = telebot.TeleBot(token=token, parse_mode=None)


@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Добро пожаловать в мир инструментов! {message.from_user.first_name}\n /menu \n Ссылка на наш сайт \n /site')



@bot.message_handler(commands=['site'])
def site(message):
    bot.reply_to(message, f'Вот ссылка на наш сайт \n http://naprokat.kg')

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, f'Вы в главном меню {message.from_user.first_name}')

    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Генераторы')
    btn2 = types.KeyboardButton('Бетономешалки')
    btn3 = types.KeyboardButton('Алмазное бурение')
    btn4 = types.KeyboardButton('Лестницы и стремянки')
    btn5 = types.KeyboardButton('Домкраты гидравлические')
    btn6 = types.KeyboardButton('Трамбовки')
    btn7 = types.KeyboardButton('Сварочные аппараты')
    btn8 = types.KeyboardButton('Шуруповёрты')
    btn9 = types.KeyboardButton('Строительные фены')
    btn10 = types.KeyboardButton('Лобзики')
    btn11 = types.KeyboardButton('Миксер')
    btn12 = types.KeyboardButton('Болгарки')
    btn13 = types.KeyboardButton('Пилы и плиткорезы')
    btn14 = types.KeyboardButton('Дрели')
    btn15 = types.KeyboardButton('Штроборезы')
    btn16 = types.KeyboardButton('Отбойные молотки')
    btn17 = types.KeyboardButton('Трубогибы')
    btn18 = types.KeyboardButton('Углорез')
    btn19 = types.KeyboardButton('Пчелки')
    btn20 = types.KeyboardButton('Перфораторы')
    btn21 = types.KeyboardButton('Строительные пылесосы')
    btn22 = types.KeyboardButton('Лазерные уровни')
    btn23 = types.KeyboardButton('Детекторы проводки')
    btn24 = types.KeyboardButton('Компрессоры')
    btn25 = types.KeyboardButton('Пистолеты')
    btn26 = types.KeyboardButton('Бензобуры')
    btn27 = types.KeyboardButton('Вибраторы глубинные')
    btn28 = types.KeyboardButton('Триммеры')
    btn29 = types.KeyboardButton('Тепловые пушки')
    btn30 = types.KeyboardButton('Утюг')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, 
    btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, 
    btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30)

    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)


        
# product_categories = {
#     'Генераторы': 'elektrogeneratory',
#     'Бетономешалки': 'betonomeshalki',
#     'Алмазное бурение': 'almaznoe-burenie',
#     'Лестницы и стремянки': 'lestnicy-i-stremyanki',
#     'Домкраты гидравлические': 'domkraty-gidravlicheskie',
#     'Трамбовки': 'trambovki',
#     'Сварочные аппараты': 'svarochnye-apparaty',
#     'Шуруповёрты': 'shurupoverty',
#     'Строительные фены': 'stroitelnie-feny',
#     'Лобзики': 'lobziki',
#     'Миксер': 'miksery',
#     'Болгарки': 'bolgarki',
#     'Пилы и плиткорезы': 'pily-i-plitkorezy',
#     'Дрели': 'dreli',
#     'Штроборезы': 'shtroborezy',
#     'Отбойные молотки': 'otboinye-molotki',
#     'Трубогибы': 'trubogiby',
#     'Углорез': 'ugloresy',
#     'Пчелки': 'pchelki',
#     'Перфораторы': 'perforatory',
#     'Строительные пылесосы': 'stroitelnie-pylesosy',
#     'Лазерные уровни': 'lazernye-urovni',
#     'Детекторы проводки': 'detektory-provodki',
#     'Компрессоры': 'kompressory',
#     'Пистолеты': 'pistolety',
#     'Бензобуры': 'benzobury',
#     'Вибраторы глубинные': 'vibratory-glubinnye',
#     'Триммеры': 'trimmery',
#     'Тепловые пушки': 'teplovye-pushki',
#     'Утюг': 'utyug',
# }
                
@bot.message_handler(func=lambda x: True)
def echoall(message):
    bot.reply_to(message, f'GOOD JOB \n {message.text}')

bot.polling()