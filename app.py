import os
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Envía /chatid para obtener tu chat ID.')

async def chatid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f'Tu chat ID es: `{chat_id}`', parse_mode='Markdown')

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chatid", chatid))

    print("Bot está corriendo correctamente...") 
    application.run_polling(stop_signals=None)

if __name__ == '__main__':
    main()
