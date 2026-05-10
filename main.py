import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

# Вставь сюда свой токен от BotFather
API_TOKEN = '8734155157:AAF7SBBYKtiAzZ7M3Ye5UDdwBQ0K5p8caJk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Базы данных для игр
TRUTHS = ["Какой твой самый стыдный поступок?", "Кто тебе нравится в этом чате?", "Твоя последняя ложь?"]
DARES = ["Скинь последнее фото из галереи", "Напиши бывшему/бывшей 'я скучаю'", "Сделай 10 отжиманий"]
FRUITS = ["🍎 Яблочко", "🍌 Бананчик", "🍍 Ананас", "🍑 Персик", "🥑 Авокадо"]

@dp.inline_query()
async def inline_handler(query: types.InlineQuery):
    results = []

    # 1. Игра "Правда"
    truth_text = random.choice(TRUTHS)
    results.append(InlineQueryResultArticle(
        id='1',
        title='❓ Игра: Правда',
        description='Выдать случайный вопрос',
        input_message_content=InputTextMessageContent
        (message_text=f"Игра: ПРАВДА\n\nВопрос: {truth_text}", parse_mode="HTML")
    ))

    # 2. Игра "Действие"
    dare_text = random.choice(DARES)
    results.append(InlineQueryResultArticle(
        id='2',
        title='⚡️ Игра: Действие',
        description='Выдать жесткое задание',
        input_message_content=InputTextMessageContent(
            message_text=f"Игра: ДЕЙСТВИЕ\n\nЗадание: {dare_text}", parse_mode="HTML")
    ))

    # 3. Кто ты сегодня?
    fruit_text = random.choice(FRUITS)
    results.append(InlineQueryResultArticle(
        id='3',
        title='🍏 Какой ты фрукт?',
        description='Узнай свою судьбу на сегодня',
   inputinput_message_content=InputTextMessageContent(
           messagee_text=f"Я сегодня: {fruit_text}")
    )) 
    
    # 4.Отчет до смерти
        total_seconds=random.randint(10,86400)
        hours=total_seconds//3600
        minutes=(total_seconds %3600)//60
        seconds=total_seconds %60
    
        time_str=f"{hours}ч{minutes}м{seconds}с"

        results.append(
            types.InlineQueryResultArticle(
            id=get_id('random_timet') 
            title='⏳ Узнать время смерти'
            description='Выдаст от 10 секунд до 24 часов'
            input_message_content=types.InputTextMessageContent(
                message_text=f"🎲 Твое случайное время:{time_str}\n\nЖди, время пошло! ⏱"
    ))) 

    # Отправляем результаты пользователю в меню над строкой ввода
    await query.answer(results, cache_time=1)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
