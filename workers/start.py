"""

███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██████╗░░░░░░░██╗░░░██╗██████╗░████████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗░░░░░░██║░░░██║██╔══██╗╚══██╔══╝╚██╗██╔╝
██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░██║█████╗╚██╗░██╔╝██████╔╝░░░██║░░░░╚███╔╝░
██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░██║╚════╝░╚████╔╝░██╔══██╗░░░██║░░░░██╔██╗░
██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██████╔╝░░░░░░░░╚██╔╝░░██║░░██║░░░██║░░░██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍃 Channel", url="https://t.me/Mo_Tech_YT"),
         InlineKeyboardButton("🛡 Support", url="https://t.me/Group")],
        [InlineKeyboardButton("🎗️ Deploy", url="https://github.com/PR0FESS0R-99"),
         InlineKeyboardButton("🤖 BotsList", url="https://t.me/MT_Botz")],
    ])
    welcomed = f"""
    Hello 🙋,
Dear User<b>{message.from_user.first_name}</b>
This Is A YouTube Uploader Bot. Click /help for More info About the Bot.
    [📥](https://telegra.ph/file/39812237fd7a1bfc02532.jpg)"""
  
    
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
