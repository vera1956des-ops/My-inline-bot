import asyncio
import random
import hashlib
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiohttp import web

# ТВОЙ ТОКЕН
API_TOKEN = '8734155157:AAHq1JmyeI1xn6O7G-VWuR7TcGYik3RrAYM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Базы данных
TRUTHS = ["Стыдный поступок?", "Кто нравится в чате?", "Последняя ложь?"]
DARES = ["Скинь фото галереи", "Напиши бывшему 'скучаю'", "10 отжиманий"]
MEME_ROLES = ["Скуф", "Альтушка", "Сигма", "Гигачад", "Нормис", "Тюбик"]

@dp.inline_query()
async def inline_handler(query: types.InlineQuery):
    results = []
    def get_id(name):
        return hashlib.md5(name.encode()).hexdigest()

    games = [
        ('truth', '❓ Правда', f"Вопрос: {random.choice(TRUTHS)}"),
        ('dare', '⚡️ Действие', f"Задание: {random.choice(DARES)}"),
        ('meme', '🤡 Кто ты?', f"Сегодня ты: {random.choice(MEME_ROLES)}")
    ]

    for i, (uid, title, text) in enumerate(games):
        results.append(InlineQueryResultArticle(
            id=get_id(uid + str(i)),
            title=title,
            input_message_content=InputTextMessageContent(message_text=text)
        ))
    await query.answer(results, cache_time=1)

# Микро-сервер для Render
async def handle(request):
    return web.Response(text="Бот живой!")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', os.getenv('PORT', 10000))
    
    copy_task = asyncio.create_task(site.start())
    poll_task = asyncio.create_task(dp.start_polling(bot))
    await asyncio.gather(copy_task, poll_task)

if __name__ == '__main__':
    asyncio.run(main())
