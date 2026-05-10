import random
import hashlib
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
def get_id(name):
    return hashlib.md5(name.encode()).hexdigest() 
API_TOKEN = '8734155157:AAF7SBBYKtiAzZ7M3Ye5UDdwBQ0K5p8caJk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Базы данных для игр
TRUTHS = ["Какой твой самый стыдный поступок?", "Кто тебе нравится в этом чате?", "Твоя последняя ложь?"]
DARES = ["Скинь последнее фото из галереи", "Напиши бывшему/бывшей 'я скучаю'", "Сделай 10 отжиманий"]
FRUITS = ["🍎 Яблочко", "🍌 Бананчик", "🍍 Ананас", "🍑 Персик", "🥑 Авокадо"]
EIGHT_BALL = ["Да", "Нет", "Возможно", "Скорее всего да", "Даже не думай", "Спроси позже", "Определенно точно!"]
WHO_MOST_LIKELY = ["станет миллионером", "сядет в тюрьму за глупость", "забудет ключи дома", "первым выйдет замуж/женится", "станет известным блогером"]
LOVE_METER = ["0%", "15%", "45%", "69%", "80%", "100%", "Бесконечно! ❤️"]
ZODIAC = ["Овен ♈", "Телец ♉", "Близнецы ♊", "Рак ♋", "Лев ♌", "Дева ♍", "Весы ♎", "Скорпион ♏", "Стрелец ♐", "Козерог ♑", "Водолей ♒", "Рыбы ♓"]
MEME_ROLES = ["Скуф", "Альтушка", "Сигма", "Гигачад", "Нормис", "Босс КФС", "Тюбик"]
PREDICTIONS = ["Тебя ждет денежный перевод", "Сегодня лучше поспать", "Кто-то тайно о тебе думает", "Купи лотерейный билет"]


@dp.inline_query()
async def inline_handler(query: types.InlineQuery):
    results = []

# Вспомогательная функция для генерации ID
return hashlib.md5(name.encode()).hexdigest()

# 1. Игра "Правда"
truth_text = random.choice(TRUTHS)
results.append(InlineQueryResultArticle(
id=get_id('truth'),
title='❓ Игра: Правда',
description='Выдать случайный вопрос',
input_message_content=InputTextMessageContent(
message_text=f"Игра: ПРАВДА\n\nВопрос: {truth_text}",
parse_mode="HTML"
    )
))

# 2. Игра "Действие"
dare_text = random.choice(DARES)
results.append(
    types.InlineQueryResultArticle(
    id='1',
    title='КТО Я?',
    input_message_content=types.InputTextMessageContent(
    message_text='Я – легенда кодинга (нет)'

    ) 
)) 

id=get_id('dare'),
title='⚡️ Игра: Действие',
description='Выдать жесткое задание',
input_message_content=InputTextMessageContent(
message_text=f"Игра: ДЕЙСТВИЕ\n\nЗадание: {dare_text}",
parse_mode="HTML"

    ) 

# 3. Кто ты сегодня?
fruit_text = random.choice(FRUITS)
results.append(InlineQueryResultArticle(
id=get_id('fruit'),
title='🍏 Какой ты фрукт?',
description='Узнай свою судьбу на сегодня',
input_message_content=InputTextMessageContent(
message_text=f"Я сегодня: {fruit_text}"
    )
))

# 4. Шар судьбы (8-Ball)
results.append(InlineQueryResultArticle(
id=get_id('8ball'),
title='🔮 Магический шар',
description='Задай вопрос и получи ответ',
input_message_content=InputTextMessageContent(
message_text=f"❓ Вопрос: {query.query if query.query else '...'}\n🔮 Ответ шара: {random.choice(EIGHT_BALL)}",
parse_mode="HTML"
    )
))

# 5. Кто из нас?
results.append(InlineQueryResultArticle(
id=get_id('who'),
title='🤔 Кто из нас...',
description='Случайная ситуация',
input_message_content=InputTextMessageContent(
message_text=f"У кого больше шансов, что он(а) {random.choice(WHO_MOST_LIKELY)}?",
parse_mode="HTML"
    )
))

# 6. Любовный метр
results.append(InlineQueryResultArticle(
id=get_id('love'),
title='❤️ Любовный метр',
description='Проверь вашу совместимость',
input_message_content=InputTextMessageContent(
message_text=f"💖 Совместимость сегодня составляет: {random.choice(LOVE_METER)}"
    )
))

# 7. Камень, ножницы, бумага
knb = random.choice(['💎 Камень', '✂️ Ножницы', '📄 Бумага'])
results.append(InlineQueryResultArticle(
id=get_id('knb'),
title='✊ Камень, Ножницы, Бумага',
description='Бот сделает выбор за тебя',
input_message_content=InputTextMessageContent(
message_text=f"Мой выбор: {knb}!",
parse_mode="HTML"
    )
))

# 8. Орел или Решка
coin = random.choice(['Орёл 🦅', 'Решка 🪙'])
results.append(InlineQueryResultArticle(
id=get_id('coin'),
title='🪙 Подбросить монетку',
description='Орел или Решка?',
input_message_content=InputTextMessageContent(
message_text=f"Выпало: {coin}",
parse_mode="HTML"
    )
))

# 9. Твой знак судьбы
results.append(InlineQueryResultArticle(
id=get_id('zodiac'),
title='✨ Твой знак судьбы',
description='Кем тебе лучше быть сегодня',
input_message_content=InputTextMessageContent(
message_text=f"Твой вайб дня: {random.choice(ZODIAC)}",
parse_mode="HTML"
    )
))

# 10. Кто ты из мемов?
results.append(InlineQueryResultArticle(
id=get_id('meme'),
title='🤡 Кто ты из мемов?',
description='Узнай свой статус',
input_message_content=InputTextMessageContent(
message_text=f"Сегодня твой статус: {random.choice(MEME_ROLES)}",
parse_mode="HTML"
    )
))

# 11. Случайное число
num = random.randint(1, 100)
results.append(InlineQueryResultArticle(
id=get_id('random_num'),
title='🔢 Случайное число',
description='От 1 до 100',
input_message_content=InputTextMessageContent(
message_text=f"Мое случайное число: {num}"
    )
))

# 12. Предсказание на день
results.append(InlineQueryResultArticle(
id=get_id('pred'),
title='🔮 Предсказание на день',
description='Что тебя ждет?',
input_message_content=InputTextMessageContent(
message_text=f"📜 Предсказание: {random.choice(PREDICTIONS)}",
parse_mode="HTML"
    )
))

# 13. Бутылочка
results.append(InlineQueryResultArticle(
id=get_id('bottle'),
title='🍾 Крутить бутылочку',
description='Выбрать случайного человека',
input_message_content=InputTextMessageContent(
message_text="🍾 Бутылочка крутится... и указывает на тебя!",
parse_mode="HTML"
    )
))

    # Отправляем весь список (максимум 50 результатов за раз)
await query.answer(results, cache_time=1)

async def main():
        app.router.add_get('/'h) 
    runner=web.AppRunner(app)
    await runner.setup() 
    site=web.TCPSite(runner,'0.0.0.0',10000) 
    await site.start() 
    await dp.start_polling(bot) 
