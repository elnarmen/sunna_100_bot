import os
import time

from dotenv import load_dotenv
import telegram


load_dotenv()


def send_post(bot, chat_id):
    bot.send_message(
        chat_id=chat_id,
        text="I'm sorry Dave I'm afraid I can't do that."
    )


def run_bot():
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
    chat_id = os.getenv('CHAT_ID')
    chat_id_for_logs = os.getenv('CHAT_ID_FOR_LOGS')
    try:
        while True:
            publication_interval = os.getenv('INTERVAL')
            send_post(bot, chat_id)
            time.sleep(int(publication_interval))
    except Exception as e:
        bot.send_message(
            chat_id=chat_id_for_logs,
            text=f"An error occurred: {e}",
        )
