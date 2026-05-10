import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiohttp import web

API_TOKEN = '8734155157:AAFDBBUKtiAzZ7M3Ye5UDwBQ0Kp8caJk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.inline_query()
async def i_q(q: types.InlineQuery):
    i = types.InlineQueryResultArticle(
        id='1', title='КТО Я?',
        input_message_content=types.InputTextMessageContent(message_text='Я Сигма!')
    )
    await q.answer([i], cache_time=1)

async def h(r):
    return web.Response(text="OK")

async def main():
    app = web.Application()
    app.router.add_get('/', h)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 10000))).start()
    await dp.start_polling(bot)

if _namee__ == '__main__':
    asyncio.run(main())
