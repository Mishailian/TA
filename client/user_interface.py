import json
from telebot import types
import telebot
from static import BOT_TOKEN

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

def question(message, answer1, answer2, answer3, answer4, question1, choice, request1=''):
    step = False
    if message.text == answer1:
        step = True
        request.append(request1)
    elif message.text == answer2:
        step = False
        if message.text ==n_data['questions'][5]['no']:
            step == True
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton(text=answer3)
        button2 = types.KeyboardButton(text=answer4)
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, question1, reply_markup=keyboard1)
    elif step == False and choice == True:
        script(message)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text=n_data['questions'][0]['inf'])
    keyboard1.row(button1)
    button2 = types.KeyboardButton(text=n_data['questions'][0]['edu'])
    button3 = types.KeyboardButton(text= n_data['questions'][0]['play'])
    keyboard1.row(button2, button3)
    bot.send_message(message.chat.id, 'Мы хотим, максимально эффективно, помочь вам в создании видеоконтента. Мы зададим вам пару вопросов, которые помогут нам определить, какая конкретно информация для вас требуется. ')
    bot.send_message(message.chat.id, n_data['questions'][0]['content_type'], reply_markup = keyboard1)
    bot.register_next_step_handler(message, question1)
def question1(message):
    step = False
    if message.text == n_data['questions'][0]['inf']:
        step = True
        request.append('type_inf')
    elif message.text == n_data['questions'][0]['edu']:
        step = True
        request.append('type_questions')
    elif message.text == n_data['questions'][0]['play']:
        step = True
        request.append('type_play')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][1]['shorts'])
        keyboard1.row(button1)
        button2 = types.KeyboardButton(text=n_data['questions'][1]['video_blog'])
        button3 = types.KeyboardButton(text=n_data['questions'][1]['youTube'])
        keyboard1.row(button2, button3)
        bot.send_message(message.chat.id, n_data['questions'][1]['format_video'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question2)
def question2(message):
    step = False
    if message.text == n_data['questions'][1]['shorts']:
        request.append('format_short')
        step = True
    elif message.text == n_data['questions'][1]['video_blog']:
        step = True
        request.append('format_video_blog')
    elif message.text == n_data['questions'][1]['youTube']:
        step = True
        request.append('format_YouTube')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][2]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][2]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][2]['shot'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question3)
def question3(message):
   
    question(message, n_data['questions'][2]['yes'], n_data['questions'][2]['no'], n_data['questions'][3]['yes'], n_data['questions'][3]['no'], n_data['questions'][3]['advice'], True)
    if glob:
        bot.register_next_step_handler(message, question4)

def question4(message):
    question(message, n_data['questions'][3]['yes'], n_data['questions'][3]['no'], n_data['questions'][4]['yes'],
             n_data['questions'][4]['no'], n_data['questions'][4]['light'], True, 'get_instruction_frame')
    bot.register_next_step_handler(message, question5)
             


def question5(message):
    step = False
    if message.text == n_data['questions'][4]['yes']:
        bot.send_message(message.chat.id, 'Понял вас, свет не нужен')
        script(message)
    elif message.text == n_data['questions'][4]['no']:
        bot.send_message(message.chat.id, 'Так и запишем!')
        request.append('get_light')
        script(message)
    

def question6(message):
    step = False
    if message.text == n_data['questions'][5]['yes']:
        step = True
        request.append('get_script')
    elif message.text == n_data['questions'][5]['no']:
        step = True
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][6]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][6]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][6]['music'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question7)
def question7(message):
    step = False
    if message.text == n_data['questions'][6]['yes']:
        step = True
        request.append('get_music')
    elif message.text == n_data['questions'][6]['no']:
        step = True
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][7]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][7]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][7]['screensaver'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question8)
def question8(message):
    step = False
    if message.text == n_data['questions'][7]['yes']:
        step = True
        request.append('')
    elif message.text == n_data['questions'][7]['no']:
        step = False
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][8]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][8]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][8]['description_screensaver'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question9)
    else:

        bot.register_next_step_handler(message, question10)


@bot.message_handler(commands=['getInfo'])
def het_info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Ссылка на наш сайт", url="https://github.com/Mishailian/TA")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Информация о проекте", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def question9(message):
    request.append(f"Заставка должна быть такой: {message.text}")
    bot.send_message(message.chat.id, n_data['questions'][9]['idea_video'])
    bot.register_next_step_handler(message, question10)

def question10(message):
    request.append(f"Идея видео: {message.text}")
    bot.send_message(message.chat.id, "Пожалуйста, подождите пару минут, бот обрабатывает все ваши запросы.")
    print(request)

if __name__ =="__main__":
    bot.infinity_polling()
