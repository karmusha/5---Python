from telegram.ext import *

api_key = '5463989628:AAHRIzmOhxMBdiWk3Gp_KE09Nu9oidOfg8U'

from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'привет'):
        return 'Привет, как жись?'

    if user_message in ('ты кто', 'ты кто?'):
        return 'Я конфетный бот Кармы.'

    if user_message in ('время', 'время?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return str(date_time)
    
    return 'Неизвестная команда.'

print('Бот начал работу...')

def start_command(update, context):
    update.message.reply_text('Нажмите любую клавишу, чтобы начать.')

def help_command(update, context):
    update.message.reply_text('Помочь вам нечем. Помогите себе сами!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)

    update.message.reply_text(response)

def error(update,context):
    print(f'Ваше сообщение "{update}" вызвало ошибку: {context.error}.')

def main():
    updater = Updater(api_key, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1)
    updater.idle()

main()







