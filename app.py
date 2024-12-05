import os
from telegram import Update, BotCommand
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

commands = [
    BotCommand("start", "Inicia el bot"),
    BotCommand("chatid", "Obtén tu chat ID"),
]

async def set_commands(application: Application) -> None:
    bot = application.bot
    await bot.set_my_commands(commands)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Envía /chatid para obtener tu chat ID.')

async def chatid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f'Tu chat ID es: `{chat_id}`', parse_mode='Markdown')

async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chatid", chatid))

    await set_commands(application)

    print("Bot está corriendo correctamente...")
    await application.run_polling(stop_signals=None)

if __name__ == '__main__':
    print("Bot está corriendo correctamente...")

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chatid", chatid))
    application.run_polling(stop_signals=None)
