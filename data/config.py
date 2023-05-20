from environs import Env

# environs 
env = Env()
env.read_env()
# .env 
BOT_TOKEN = env.str("BOT_TOKEN")  # Токен бота
ADMINS = env.list("ADMINS")  # ID Администраторов
IP = env.str("ip")  # Местоположение хостинга (IP)
