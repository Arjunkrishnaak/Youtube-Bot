"""

███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██████╗░░░░░░░██╗░░░██╗██████╗░████████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗░░░░░░██║░░░██║██╔══██╗╚══██╔══╝╚██╗██╔╝
██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░██║█████╗╚██╗░██╔╝██████╔╝░░░██║░░░░╚███╔╝░
██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░██║╚════╝░╚████╔╝░██╔══██╗░░░██║░░░░██╔██╗░
██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██████╔╝░░░░░░░░╚██╔╝░░██║░░██║░░░██║░░░██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["github"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("GROUP", url="https://t.me/youtube_video_downloade_grp")],
    ])
    Aww = f"""Hey <b>{message.from_user.first_name}</b>
If you liked my project and want to be a GitHub contributor then:
- 🗣️ You may contact at **@TeleRoid14**

- 🧾 You can personal message me in Telegram **@HelpLessBoi**   

- Star & Fork my GitHub Repo else You are Gay.\n

If you liked my project and want and want to Donate then you can:
- [ARJUN](https://t.me/lvx2_edz) 
    
**<b>{message.from_user.first_name}</b> 😁 Thanks a lot for using my bot**

[@Yt_dwnld_robot](https://te.legra.ph/file/1cfc29eeaa8eebc7ce550.jpg)
"""      
    await message.reply_text(Aww, reply_markup=joinButton)
    raise StopPropagation
