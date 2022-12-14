# Реализовать какой-либо функционал при помощи телеграм-бота. OR
# Добавить систему логирования к программе из предыдущего ДЗ.

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import os
from pathlib import Path
import requests

api_key = '5463989628:AAHRIzmOhxMBdiWk3Gp_KE09Nu9oidOfg8U'

from datetime import datetime

def sample_responses(input_text, effective_user):
    user_message = str(input_text).lower()
    
    if user_message in ('hello', 'hi', 'привет', 'ghbdtn', 'hallo', 'хай', 'хелло', 'добрый день', 'здравствуй', 'здравствуйте'):
        return f'Halo, {effective_user["first_name"]}!'

    if user_message in ('время', 'время?', 'time', 'what time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return str(date_time)

    if user_message in ('ты кто', 'ты кто?', 'кто ты', 'кто ты?'):
        return 'Я бот Кармы.'
    
    if user_message in ('курсы валют'):
        rates_url = 'https://www.cbr-xml-daily.ru/latest.js'
        res = requests.get(rates_url)
        res = res.content.decode('utf-8')
        return res
    
    return 'Неизвестная команда.'

print('Бот начал работу...')

async def start_command(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton('Поздороваться', callback_data='привет'),
            InlineKeyboardButton('Спросить время', callback_data='время'),
        ],
        [
            InlineKeyboardButton('Узнать, кто я', callback_data = 'ты кто'),
            InlineKeyboardButton('Узнать курсы валют', callback_data = 'курсы валют'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Eсли вы хотите узнать, что я умею, выберите из списка ниже:", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Помочь вам нечем. Помогите себе сами!\nА если вы хотите узнать, что я умею, запустите команду "/start"')

async def handle_message(update: Update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text, update.effective_user)

    await update.message.reply_text(response)

async def error(update: Update, context):
    print(f'Ваше сообщение "{update}" вызвало ошибку: {context}.')
    await update.message.reply_text('Что-то пошло не так.')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    response = sample_responses(query.data, update.effective_user)
    # await query.answer()
    await query.edit_message_text(response)

async def msg(update: Update, context):
    file_path = Path(__file__).parent.joinpath('script.py')
    file_to_download = await update.message.document.get_file()
    with open(file_path, mode='bw') as f:
        await file_to_download.download_to_memory(f)

    os.system(f'python {file_path} > {str(file_path)}.out 2> {str(file_path)}.error')

    text_message = None
    with open(str(file_path) + '.out') as f:
        text_message = f.read()
    
    if text_message == '':
        with open(str(file_path) + '.error') as f:
            text_message = f.read()

    if text_message == '':
        text_message = 'Nothing to output'

    await update.message.reply_text(text_message)

def main():
    dp = Application.builder().token(api_key).build()

    dp.add_handler(MessageHandler(filters.Document.FileExtension('py'), msg))
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(filters.TEXT, handle_message))

    dp.add_error_handler(error)

    dp.run_polling()

main()






