import discord
from discord.ext import commands
import asyncio
from flask import Flask
from threading import Thread

# Настройки бота
TOKEN = 'MTM2NTI4NjE0NDI3OTA1NjQxNQ.G41DCq.nItKyLi3Gx-76sx80SUIUuhAf9jsT6aKr3XDjA'  # Замените на токен вашего бота
TARGET_USER_IDS = [395946187804639241, 486463118743044098, 852653654205005895, 326260912795418624, 435425529852723202]  # Замените на ID нужных пользователей
MESSAGE = "СБОР ПАТИ 5 НА РАССЛАБУХЕ"

# Создаем бота с префиксом команды
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов к работе!')


@bot.command(name='gribs')
async def notify_users(ctx):
    try:
        for user_id in TARGET_USER_IDS:
            user = await bot.fetch_user(user_id)
            await user.send(MESSAGE)
            print(f"Сообщение отправлено пользователю {user.name}")
            await asyncio.sleep(0.2)  # Небольшая задержка между сообщениями

        await ctx.send("ПИДОРАСЫ СОЗВАНЫ!")
    except Exception as e:
        await ctx.send(f"Произошла ошибка: {e}")
        print(f"Ошибка: {e}")


# Запускаем бота
if __name__ == '__main__':
    bot.run(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()