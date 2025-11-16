import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен вашего бота от BotFather
TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Замените на реальный токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    await update.message.reply_text('Привет! Используй /search <слово>, чтобы сгенерировать 10 ссылок.')

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /search"""
    if not context.args:
        await update.message.reply_text('Пожалуйста, укажи слово после /search, например: /search SnoopDogg')
        return
    
    query = context.args[0].strip()  # Берем первое слово после команды
    if not query:
        await update.message.reply_text('Слово не может быть пустым.')
        return
    
    # Генерируем 10 случайных чисел от 1 до 540000
    links = []
    for _ in range(10):
        random_num = random.randint(1, 540000)
        link = f"t.me/nft/{query}-{random_num}"
        links.append(link)
    
    # Формируем ответ
    response = f"Вот 10 ссылок для '{query}':\n\n" + "\n".join(links)
    await update.message.reply_text(response)

def main() -> None:
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("search", search))

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()