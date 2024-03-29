# -*- coding: utf-8 -*-
import logging
from random import random as rand
from time import sleep
import numpy as np
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, NetworkError)
from behaviours import behaviours
from speak import produce_sentence
# enable logging
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)


def start(bot, update):
    """Start off with an anectode"""
    update.message.reply_text(text="Oh raga, l'altro giorno la vale mi fa "
                                   "'oh raga'",
                              quote=False)


def no_dai_Geeeeerry(bot, update):
    """Rebut Gerry's argument vigorously"""
    voice_file_id = 'AwADBAADCwADzPSlEYhD8dBXfH8LAg'
    update.message.reply_voice(voice=voice_file_id, quote=False)


def talk(bot, update):
    """Engage in meaningful conversation"""
    text = update.message.text
    msg = update.message

    # ad-hoc replies to interesting messages
    for bhv in behaviours:
        for s in bhv['trigger']:
            if s in text:
                rep_type = bhv['reply_type']
                reply = np.random.choice(bhv['reply'])
                if rep_type == 'text':
                    msg.reply_text(text=reply)
                elif rep_type == 'sticker':
                    msg.reply_sticker(sticker=reply)

    # random replies to uninteresting messages
    if rand() < 6.9/420.:
        # N.B. until we switch to async processing,
        # bl4ckst0ne is completely paralysed while asking for BBQ confirmation
        seconds_before_nagging = 15
        sleep(seconds_before_nagging)
        msg.reply_text(text='oh raga ma la grigliata è confermata?',
                       quote=False)
    if rand() < 6.9/420.:
        vignati_hat = 'BQADBAADRAADnWzWBo9KlpThN0OQAg'
        vignati_bw = 'BQADBAADcQADnWzWBjwXcOqPvseKAg'
        stickers = [vignati_hat, vignati_bw]
        msg.reply_sticker(sticker=np.random.choice(stickers), quote=False)


def speak(bot, update, args):
    """Say what's on your mind"""
    word = args[0] if len(args) > 0 else None
    update.message.reply_text(text=produce_sentence(word), quote=False)


def print_msg_info(bot, update):
    """Take notes - print logs to console"""
    print update.message


def print_error_info(bot, update, error):
    """Take notes - print errors to console"""
    # create a logger with function scope ("static object")
    error.logger = logging.getLogger(__name__)
    error.logger.warn('Update "%s" caused error "%s"' % (update, error))
