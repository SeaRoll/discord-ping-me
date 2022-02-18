"""
A flask server that gets a user's message
and queues the message, the server will then use a discord bot to send the message
to the specific player by their discord id.
"""

from dotenv import load_dotenv
import threading
from flask import Flask
import asyncio
import discord
from discord.ext import tasks
load_dotenv()
import os

app = Flask(__name__)
client = discord.Client()
host_name = os.environ.get("HOST_NAME")
port = int(os.environ.get("PORT_NUMBER"))
channel_id = int(os.environ.get("CHANNEL_ID"))
discord_bot_token = os.environ.get("BOT_TOKEN")

user_ping_list = []
lock = threading.Lock()

@app.route('/done/<user_id>')
def ping_user(user_id):
  global lock, user_ping_list
  with lock:
    user_ping_list.append(user_id)
  return 'ok'


@app.route('/')
def index():
  return "Hello, World!"


@tasks.loop(seconds = 2) # repeat after 2
async def ping_user():
  global user_ping_list, lock, channel_id

  await client.wait_until_ready()
  print('listening on queue')
  channel = client.get_channel(channel_id)
  while True:
    if len(user_ping_list) > 0:
      print('An user was online')
      with lock:
        the_user = await client.fetch_user(user_ping_list.pop(0))
        await the_user.send("You are online!")
    await asyncio.sleep(2) # task runs every 60 seconds


if __name__ == "__main__":
  client.loop.create_task(ping_user())
  threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()
  client.run(discord_bot_token)