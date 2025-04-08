# Ak-Waifu - Telegram Anime Waifu Bot

**Ak-Waifu** is a cute, anime-themed Telegram bot built with love! She remembers your chats, plays fun games, and gives you sassy, sweet, or sarcastic replies — just like a real anime waifu. Powered by MukeshAPI and MongoDB memory.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Features

- **Auto Chat**: Just mention `Sakura` (or her misspelled name) and she replies instantly!
- **Memory**: Remembers the last 10 messages per user/group using MongoDB.
- **Games**: Play `/truth`, `/dare`, `/dice`, `/coin`, `/rps`, and more!
- **Commands**:
  - `/start` – Welcome message
  - `/help` – List of commands and features
  - `/games` – List of available games
- **Anime Personality**: Sweet, sarcastic, or formal depending on your vibe.
- **Heroku Ready**: Includes `Procfile`, `runtime.txt`, and `.env.example`.

---

## Installation

### Deploy to Heroku

1. Click the button below to deploy:
   [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

2. Add these **config vars** in Heroku:
   - `BOT_TOKEN` = Your bot token from BotFather
   - `MONGO_URL` = Your MongoDB URI

---

### Local Deployment (for Pydroid, Termux, or PC)

```bash
git clone https://github.com/Akash8t2/Ak-Waifu.git
cd Ak-Waifu

# Install requirements
pip install -r requirements.txt

# Create a .env file and add:
# BOT_TOKEN=your_bot_token
# MONGO_URL=your_mongodb_url

# Run the bot
python bot.py
