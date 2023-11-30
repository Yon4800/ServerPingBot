import os
from dotenv import load_dotenv
from wakeonlan import send_magic_packet

import discord

import pings

import paramiko

# .envファイルの内容を読み込見込む
load_dotenv()

#HOSTNAME = os.environ["SSH"]
#USERNAME = os.environ["RUSERNAME"]
#PASSWORD = os.environ["RPASSWD"]
#LINUX_COMMAND1 = f"echo {os.environ['RPASSWD']} | sudo -S shutdown -h now"
#LINUX_COMMAND2 = f"echo {os.environ['RPASSWD']} | sudo -S reboot"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# ログインしたとき
@client.event
async def on_ready():
    print(f"{client.user} としてログインしました")


# メッセージ反応
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # サーバー起動
    if message.content.startswith("$サーバーは起動している？"):
        # Ping
        p = pings.Ping()
        res = p.ping(os.environ["SSH"])
        if res.is_reached():
            await message.channel.send("サーバーは既に起動しています")
        else:
            await message.channel.send("サーバーは閉じています。")

# os.environを用いて環境変数を表示させます
client.run(os.environ["DISTOKEN"])
