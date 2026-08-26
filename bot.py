import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏫 أهلاً بك في بوت مدارس رواد تاج الأصفـياء 💙\n"
        "البوت يعمل الآن، وسنضيف خدمات المدرسة قريبًا."
    )


def main():
    token = os.getenv("BOT_TOKEN")

    app = (
        Application.builder()
        .token(token)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
