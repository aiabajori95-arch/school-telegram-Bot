import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا بك في بوت المدرسة")

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running")
    app.run_polling()

if __name__ == "__main__":
    main()
