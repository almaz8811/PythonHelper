import logging
from config_data.config import Config, load_config

config: Config = load_config()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.tg_bot.token)
# Диспетчер
dp = Dispatcher()
# В этом случае после выполнения хэндлера aiogram будет автоматически отвечать на колбэк
# dp.callback_query.middleware(CallbackAnswerMiddleware())
# Можно переопределить стандартные настройки и указать свои
dp.callback_query.middleware(CallbackAnswerMiddleware(pre=True, text='Готово', show_alert=True))



if __name__ == '__main__':
    dp.run_polling(bot)
