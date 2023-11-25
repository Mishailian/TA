

#hello worlsd--------
import json
from telebot import types
import telebot
import webbrowser
#не надо в код сувать диалог бота нужно создать файл с константами откуда их имопртируешь и используешь
bot = telebot.TeleBot('6886812015:AAEApmY1oXvh5IT6_Mf5cLiuwOYs-fOeI7c')
my_chat_id = 1158846931
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

n_data = read('C:/klasss/data.json')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text=n_data['questions'][0]['inf'])
    keyboard1.row(button1)
    button2 = types.KeyboardButton(text=n_data['questions'][0]['edu'])
    button3 = types.KeyboardButton(text= n_data['questions'][0]['play'])
    keyboard1.row(button2, button3)
    bot.send_message(message.chat.id, 'Привет, этот чат бот поможет тебе в создании видеоконтента. Он расскажет, как вести себя в кадре, напишет сценарий'
                                      ', может сгенерировать видеоролик и создать картинку для превью.')
    bot.send_message(message.chat.id, n_data['questions'][0]['content_type'], reply_markup = keyboard1)
    bot.register_next_step_handler(message, question1)
def question1(message):
    step = False
    if message.text == n_data['questions'][0]['inf']:
        bot.send_message(message.chat.id, 'Inf')
        step = True
    elif message.text == n_data['questions'][0]['edu']:
        step = True
        bot.send_message(message.chat.id, 'обр')
    elif message.text == n_data['questions'][0]['play']:
        step = True
        bot.send_message(message.chat.id, 'play')
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
        bot.send_message(message.chat.id, 'shortVideo')
        step = True
    elif message.text == n_data['questions'][1]['video_blog']:
        bot.send_message(message.chat.id, 'video_blog')
        step = True
    elif message.text == n_data['questions'][1]['youTube']:
        bot.send_message(message.chat.id, 'YouTube')
        step = True
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][2]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][2]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][2]['shot'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question3)
def question3(message):
    step = False
    if message.text == n_data['questions'][2]['yes']:
        bot.send_message(message.chat.id, 'presence_in_frame')
        step = True
    elif message.text == n_data['questions'][2]['no']:
        bot.send_message(message.chat.id, 'absence_in_frame')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][3]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][3]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][3]['advice'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question4)
    elif step == False:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][5]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][5]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][5]['script'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question6)
def question4(message):
    step = False
    if message.text == n_data['questions'][3]['yes']:
        bot.send_message(message.chat.id, 'instruction_frame')
        step = True
    elif message.text == n_data['questions'][3]['no']:
        bot.send_message(message.chat.id, 'Хорошо, понял вас')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][4]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][4]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][4]['light'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question5)
    else:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][5]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][5]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][5]['script'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question6)
def question5(message):
    step = False
    if message.text == n_data['questions'][4]['yes']:
        bot.send_message(message.chat.id, 'light_not_needed')
        step = True
    elif message.text == n_data['questions'][4]['no']:
        bot.send_message(message.chat.id, 'light_needed')
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text=n_data['questions'][5]['yes'])
    button2 = types.KeyboardButton(text=n_data['questions'][5]['no'])
    keyboard1.row(button1, button2)
    bot.send_message(message.chat.id, n_data['questions'][5]['script'], reply_markup=keyboard1)
    bot.register_next_step_handler(message, question6)
def question6(message):
    step = False
    if message.text == n_data['questions'][5]['yes']:
        bot.send_message(message.chat.id, 'script_needed')
        step = True
    elif message.text == n_data['questions'][5]['no']:
        step = True
        bot.send_message(message.chat.id, 'script_not_needed')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text=n_data['questions'][6]['yes'])
        button2 = types.KeyboardButton(text=n_data['questions'][6]['no'])
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][6]['music'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question7)
def question7(message):
    step = False
    if message.text == n_data['questions'][6]['yes']:
        bot.send_message(message.chat.id, 'music_needed')
        step = True
    elif message.text == n_data['questions'][6]['no']:
        step = True
        bot.send_message(message.chat.id, 'music_not_needed')
    if step:
        if step:
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton(text=n_data['questions'][7]['yes'])
            button2 = types.KeyboardButton(text=n_data['questions'][7]['no'])
            keyboard1.row(button1, button2)
            bot.send_message(message.chat.id, n_data['questions'][7]['screensaver'], reply_markup=keyboard1)
            bot.register_next_step_handler(message, question8)
def question8(message):
    step = False
    if message.text == n_data['questions'][7]['yes']:
        bot.send_message(message.chat.id, 'scr_need')
        step = True
    elif message.text == n_data['questions'][7]['no']:
        bot.send_message(message.chat.id, 'Заставка не нужна')
    if step:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(text="")
        button2 = types.KeyboardButton(text="")
        keyboard1.row(button1, button2)
        bot.send_message(message.chat.id, n_data['questions'][8]['description_screensaver'], reply_markup=keyboard1)
        bot.register_next_step_handler(message, question9)
        print(1)
@bot.message_handler(commands=['getInfo'])
def het_info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Ссылка на наш сайт", url="https://github.com/Mishailian/TA")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Информация о проекте", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def question9(message):
    screensaver = []
    screensaver.append(message.text)
    bot.send_message(message.chat.id, n_data['questions'][9]['idea_video'])
    bot.register_next_step_handler(message, question10)

def question10(message):
    idea_video = []
    idea_video.append(message.text)
    bot.send_message(message.chat.id, "Пожалуйста, подождите пару минут, бот обрабатывает все ваши запросы.")

if __name__ =="__main__":
    bot.infinity_polling()
