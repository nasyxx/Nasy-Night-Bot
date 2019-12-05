#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Dec  4, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : bot.py
project  : nasy_night_bot
license  : GPL-3.0+

At pick'd leisure
  Which shall be shortly, single I'll resolve you,
Which to you shall seem probable, of every
  These happen'd accidents
                          -- The Tempest
"""
# Telegram
from telegram.ext import CallbackContext, CommandHandler, Updater
from telegram.update import Update

# Config
from config import TOKEN


def clean(update: Update, context: CallbackContext) -> None:
    """Clean useless commands records"""
    context.bot.delete_message(
        update.message.chat.id, update.message.message_id
    )


def main() -> None:
    """Main function."""
    bot = Updater(token=TOKEN, use_context=True)
    bot.dispatcher.add_handler(CommandHandler("challenge", clean))
    bot.start_polling()


if __name__ == "__main__":
    main()
