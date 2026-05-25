import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8542666311:AAGGhu__zarnnKJD0s8irEKd_wFIbEpWOdA"

async def start(update, context):
    await update.message.reply_text("✅ 双向机器人已启动！直接跟我聊天即可～")

async def echo(update, context):
    await update.message.reply_text(f"收到：{update.message.text}")

def main():
    logging.basicConfig(level=logging.INFO)
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🚀 机器人启动成功！")
    app.run_polling()

if __name__ == "__main__":
    main()
