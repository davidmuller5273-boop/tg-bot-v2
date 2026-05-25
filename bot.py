import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

TOKEN = "8542666311:AAGGhu__zarnnKJD0s8irEKd_wFIbEpWOdA"

def start(update, context):
    update.message.reply_text("✅ 双向机器人已启动！直接跟我聊天即可～")

def echo(update, context):
    update.message.reply_text(f"收到：{update.message.text}")

def main():
    logging.basicConfig(level=logging.INFO)
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🚀 机器人启动成功！")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
