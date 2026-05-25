import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from collections import defaultdict

TOKEN = "8542666311:AAGGhu__zarnnKJD0s8irEKd_wFIbEpWOdA"

bot = Bot(token=TOKEN)
dp = Dispatcher()
chat_history = defaultdict(list)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("✅ 新版双向机器人已启动！直接聊天即可～")

@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    text = message.text or "[非文本]"
    chat_history[user_id].append(f"用户: {text}")
    reply = f"收到：{text}\n当前记录 {len(chat_history[user_id])} 条"
    chat_history[user_id].append(f"机器人: {reply}")
    await message.answer(reply)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("🚀 最稳版机器人启动成功！")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
