from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("start")
)
async def alive(_, message):
    await message.reply(
        f"Hello! {message.from_user.mention} 😑, This is a Music Finder Telegram Bot.\n\nYou can send me an audio, video or a voice note so that I can parse to Shazam and send you the results."
    )
