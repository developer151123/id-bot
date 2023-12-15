#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.


from telebot.credentials import bot_token
from telegram.ext import (
    Application,
    CommandHandler
)


async def start(update, context):
    """Usage: /get uuid"""
    await update.message.reply_text(update.effective_user.id)
    if update.effective_user.username:
        await update.message.reply_text(update.effective_user.username)


def main() -> None:
    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()


if __name__ == '__main__':
    main()
