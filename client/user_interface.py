import json
from telebot import types
import telebot
from static import BOT_TOKEN
from translator_and_image_generator import get_picture, interpreter
from generation_text import get_text



glob = True
bot = telebot.TeleBot(BOT_TOKEN)
request = []
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)



n_data = read('./data.json')
def script(message):
    global glob
    glob = False
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text=n_data['questions'][5]['yes'])
    button2 = types.KeyboardButton(text=n_data['questions'][5]['no'])
    keyboard1.row(button1, button2)
    bot.send_message(message.chat.id, n_data['questions'][5]['script'], reply_markup=keyboard1)
    bot.register_next_step_handler(message, question6)

def path(**kwargs):
    return n_data['questions'][number][kwargs['mean']]

def repath(**kwargs):
    return n_data['questions'][renumber][kwargs['mean']]


def given(dict):
    for el in dict:
        return el
    
def question(message, *args, **kwargs):
    global number, renumber
    step = False
    if message.text == kwargs['answer1']:
        step = True
        request.append(kwargs['request1'])
    elif message.text == kwargs['answer2']:
        request.append(kwargs['request2'])
        step = True
        if message.text ==n_data['questions'][2]['no'] or message.text ==n_data['questions'][3]['no'] or message.text ==n_data['questions'][4]['no']:
            step = False
    if message.text == kwargs['answer3']:
        request.append(kwargs['request3'])
        step = True
    if step:
        number += 1
        renumber += 1
        keyboard(message, *args, **kwargs)
    elif not step and kwargs['choice'] :
        if message.text == n_data['questions'][2]['no'] or message.text == n_data['questions'][3]['yes']:
            number += 3
            renumber += 3
            request.append("не нужен совет")
            request.append("не нужен свет")
        elif  message.text == n_data['questions'][3]['no']:
            number += 2
            renumber += 2
            request.append("не нужен свет")
        else:
            number += 1
            renumber += 1

        script(message)

def keyboard(message, *args, **kwargs):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for butText in args:
        keyboard1.row(types.KeyboardButton(butText))
    bot.send_message(message.chat.id, kwargs['question0'], reply_markup=keyboard1)

@bot.message_handler(commands=['start'])
def start_message(message):
    global number, renumber
    request = []
    number = 1
    renumber = 0
    request.clear
    bot.send_message(message.chat.id, 'Мы хотим, максимально эффективно, помочь вам в создании видеоконтента. Мы зададим вам пару вопросов, которые помогут нам определить, какая конкретно информация для вас требуется. ')
    keyboard(message, repath(mean = 'inf'), repath(mean = 'edu'), repath(mean = 'play'), question0 = repath(mean = 'content_type'))
    bot.register_next_step_handler(message, question1)

def question1(message):
    print(number, renumber)
    question(message, path(mean ='shorts'), path(mean = 'video_blog'),path(mean = 'youTube'), answer1 = repath(mean = 'inf'), request1 = 'информационный', answer2 = repath(mean = 'edu'), request2 = 'образовательный', answer3 = repath(mean = 'play'), request3 = 'развлекательный', question0 = path(mean = 'format_video'), choice = False)
    bot.register_next_step_handler(message, question2)

def question2(message):
    question(message, path(mean = 'yes'), path(mean = 'no'), answer1 = repath(mean ='shorts'), request1 = 'короткое видео', answer2 = repath(mean = 'video_blog'), request2 = 'video_blog', answer3 = repath(mean = 'youTube'), request3 = 'видео для YouTube', question0 = path(mean = 'shot'), choice = False)
    bot.register_next_step_handler(message, question3)

def question3(message):
    question(message, path(mean = 'yes'),  path(mean = 'no'), answer1 = repath(mean ='yes'), request1 = '', answer2 = repath(mean ='no'), request2 = '', answer3 = '', request3 = '', question0 = path(mean ='advice'), choice = True)
    if glob:
        bot.register_next_step_handler(message, question4)

def question4(message):
    question(message, path(mean = 'yes'), path(mean = 'no'), answer1 = repath(mean ='yes'), request1 = 'need_advice', answer2 = repath(mean ='no'), request2 = '', answer3 = '', request3 = '', question0 = path(mean ='light'), choice = True)
    bot.register_next_step_handler(message, question5)
             
def question5(message):
    question(message, path(mean = 'yes'), path(mean = 'no'), answer1 = repath(mean ='yes'), request1 = 'no_light', answer2 = repath(mean ='no'), request2 = 'need_light', answer3 = '', request3 = '', question0 = path(mean ='script'), choice = True)
    bot.register_next_step_handler(message, question6)
    
def question6(message):
    print(number)
    question(message, path(mean = 'yes'), path(mean = 'no'), answer1 = repath(mean ='yes'), request1 = 'need_script', answer2 = repath(mean ='no'), request2 = '', answer3 = '', request3 = '', question0 = path(mean ='screensaver'), choice = False)
    bot.register_next_step_handler(message, question7)



def question7(message):
    global number, renumber

    if message.text == repath(mean ='yes'):

        bot.send_message(message.chat.id,path(mean = 'description_screensaver'))
        number += 1
        renumber += 1
        bot.register_next_step_handler(message, question8)
    elif message.text == repath(mean ='no'):
        request.append('')
        number += 1
        renumber += 1

        bot.send_message(message.chat.id, path(mean = 'idea_video'))
        bot.register_next_step_handler(message, question9)


@bot.message_handler(commands=['getInfo'])
def het_info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Ссылка на наш сайт", url="https://github.com/Mishailian/TA")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Информация о проекте", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def question8(message):
    
    request.append(message.text)
    bot.send_message(message.chat.id, path(mean = 'idea_video'))
    bot.register_next_step_handler(message, question9)
def advice_message(message):
    bot.send_message(message.chat.id, 'Советы по тому, как вести себя в кадре:')
    for i in range(1, 9):
        bot.send_message(message.chat.id, (n_data['questions'][9][f'advice{i}']))

def light_message(message):
    bot.send_message(message.chat.id, 'Советы по тому, как настроить свет:')
    for i in range(1, 7):
        bot.send_message(message.chat.id, (n_data['questions'][10][f'light{i}']))

def question9(message):
    request.append(message.text)
    bot.send_message(message.chat.id, "Пожалуйста, подождите пару минут, бот обрабатывает все ваши запросы.")
    print('Запрос отправлен')
    print(request)
    #bot.send_message(message.chat.id, ask_gpt(str(request[8])))

    if request[3] == 'need_advice':
         advice_message(message)
    if request[4] == 'need_light':
        light_message(message)
    if request[5] == 'need_script':
        bot.send_message(message.chat.id, get_text(f"Действуй, как опытный видеоблогер со стажем 30 лет. Составь для меня подробный и интересный сценарий на тему {request[7]}, но учти, что видео должно быть записано в таком формате: {request[1]}"))
    if len(request[6]) > 1:
        picture = request[6]
        bot.send_message(message.chat.id, f'Вот ссылка на вашу картинку: {get_picture(interpreter(picture))}')



if __name__ =="__main__":
    bot.infinity_polling()
