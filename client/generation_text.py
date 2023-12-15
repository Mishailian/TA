import telebot
import openai
import requests
from static import BOT_TOKEN

# Установите ваш токен от BotFather и токен от OpenAI
OPENAI_API_KEY = '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'

# Настройте бота и OpenAI  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
bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# Прокси-настройки
PROXY = {
    'http': 'http://194.5.94.219:8000'
}


def get_text(text):

    proxies = PROXY if PROXY else None

    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        },
        json={"prompt": text, "max_tokens": 2000},
        proxies=proxies,
    )
    print(response)
    response_data = response.json()
    print(response_data)
    bot_reply = response_data['choices'][0]['text'].strip()
    return bot_reply

