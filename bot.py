import os
from telegram import Update
from telegram.ext import Application, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text("اهلا بك في بوت المدرسة")

def main():
    token = os.getenv("BOT_TOKEN")

    app = (
        Application.builder()
        .token(token)
        .connect_timeout(60)
        .read_timeout(60)
        .write_timeout(60)
        .pool_timeout(60)
        .build()
    )

    app.add_handler(CommandHandler("start", start))

    print("Bot is running")
    app.run_polling()

if __name__ == "__main__":
    main()
