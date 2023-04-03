import asyncio
from day_l import*
from telethon import TelegramClient, events
async def main():
 bot = await TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
 async with bot:
      print("Signed in")
      @bot.on(events.NewMessage())
      async def handle_message(message):
        #print(message.message.message)
        await message.reply("Hello")
        await bot.run_until_disconnected()
 asyncio.run(main())

  