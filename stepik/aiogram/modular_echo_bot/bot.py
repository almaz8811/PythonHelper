from config_data.config import load_config

config = load_config('.env')
bot_token = config.tg_bot.token  # Сохраняем token в переменную bot_token
super_admin = config.tg_bot.admin_ids  # Сохраняем ID админа в переменную super_admin

# Выводим значения полей экземпляра класса Config на печать,
# чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
print('BOT_TOKEN:', config.tg_bot.token)
print('ADMIN_IDS:', config.tg_bot.admin_ids)
print()
print('DATABASE:', config.db.database)
print('DB_HOST:', config.db.db_host)
print('DB_USER:', config.db.db_user)
print('DB_PASSWORD:', config.db.db_password)
