import asyncio
import random
import hashlib
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiohttp import web

API_TOKEN = '8734155157:AAF7SBBYKtiAzZ7M3Ye5UDdwBQ0K5p8caJk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.inline_query()
async def inline_handler(query: types.InlineQuery):
    results = [
        InlineQueryResultArticle(
            id=hashlib.md5(str(random.random()).encode()).hexdigest(),
            title="КТО Я СЕГОДНЯ?",
            input_message_content=InputTextMessageContent(message_text=f"Я сегодня: {random.choice(['Сигма','Скуф','Тюбик'])}")
        )
    ]
    await query.answer(results, cache_time=1)

async def handle(request):
    return web.Response(text="OK")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 10000)))
    await site.start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
