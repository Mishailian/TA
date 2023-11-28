import g4f
import time

# НАСТРОЙКИ CHAT_GPT

def ask_gpt(promt) -> str:
    g4f.logging = True
    g4f.check_version = False
    time_start = time.time()
    
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
                "role": "user",
                "content": promt,
                }
            ],
        stream=True,
    )
    ans_message = ''
    for message in response:
        ans_message += message
    print(f'work in sec - "{time.time() - time_start}"')
    return ans_message

result = ask_gpt('hello')
print(result)
