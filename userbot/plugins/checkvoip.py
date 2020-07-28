import asyncio

from userbot.events import register
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

@register(outgoing=True, pattern="^[.]checkvoip")
async def checkVoip(e):
  if e.is_reply:
    msg = await e.get_reply_message()
    try:
      user = await e.client(GetFullUserRequest(msg.sender_id))
      dc_id, location = get_input_location(user.profile_photo)
      if user.user.username != None:
        name = "@" + user.user.username
      else:
        name = user.user.first_name
      if dc_id == 4:
        await e.edit(f"**✔️ {name}\n non è un VoIP.**")
      else:
        await e.edit(f"**⚠️ {name}\n è un VoIP.**")
    except:
      await e.edit("**❌ Errore:** L'Utente non ha l'immagine profilo.")
  else:
    get = e.text.split(" ", 1)[1]
    try:
      usr = await e.client.get_entity(get)
      user = await e.client(GetFullUserRequest(usr.id))
      dc_id, location = get_input_location(user.profile_photo)
      if user.user.username != None:
        name = "@" + user.user.username
      else:
        name = user.user.first_name
      if dc_id == 4:
        await e.edit(f"**✔️ {name} non è un VoIP.**")
      else:
        await e.edit(f"**⚠️ {name} è un VoIP.**")
    except:
      await e.edit("**❌ Utente Non Trovato ❌**")