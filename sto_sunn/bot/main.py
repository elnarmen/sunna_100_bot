import itertools
import os
import re
import time

import telegram
from bot.models import Interval, Post
from dotenv import load_dotenv

load_dotenv()


def escape_markdown_v2(text):
    url_pattern = r"[100 забытых Сунн]"
    parts = text.split(url_pattern)
    parts[0] = re.sub(r"([-().])", r"\\\1", parts[0])
    return "[100 забытых Сунн]".join(parts)


def send_post(bot, chat_id, post):
    with open(post.image.path, "rb") as image_file:
        escaped_text = escape_markdown_v2(post.text)
        bot.send_photo(
            chat_id=chat_id,
            photo=image_file,
            caption=escaped_text,
            parse_mode="MarkdownV2",
        )


def run_bot():
    bot = telegram.Bot(token=os.getenv("TG_TOKEN"))
    chat_id = os.getenv("CHAT_ID")
    chat_id_for_logs = os.getenv("CHAT_ID_FOR_LOGS")
    posts = Post.objects.all()
    interval = (
        Interval.objects.first()
    )  # set 24 hours by default if there is no Interval in the db
    hours_between_posts = interval.hours if interval else 24
    seconds_between_posts = hours_between_posts * 3600

    if not posts.exists():
        bot.send_message(
            chat_id=chat_id_for_logs,
            text="No posts available to send. The bot will not run.",
        )
        return

    posts_cycle = itertools.cycle(posts)

    for post in posts_cycle:
        try:
            send_post(bot, chat_id, post)
            time.sleep(seconds_between_posts)
        except Exception as e:
            bot.send_message(
                chat_id=chat_id_for_logs,
                text=f"An error occurred: {e}. PostID - {post.id}",
            )
