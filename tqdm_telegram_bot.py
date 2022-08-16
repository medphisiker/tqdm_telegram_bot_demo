# Сделано по материалам статьи
# https://towardsdatascience.com/tqdm-pytorch-and-telegram-check-training-from-your-smartphone-722566918ff6
# как найти telegram bot chat id
# https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

# документация
# https://pypi.org/project/telegram-send/
# https://www.rahielkasim.com/telegram-send/docs/api/

from tqdm.contrib.telegram import tqdm
import time
from my_telegram_bot_info import token, chat_id
import telegram_send

telegram_send.send(messages=["Начинаю обучение нейросети!"])
for i in tqdm(range(100), token=token, chat_id=chat_id):
    time.sleep(1)

telegram_send.send(messages=["обучение закончено!"])
