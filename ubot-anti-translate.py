from telethon.sync import TelegramClient, events

api_id = 1054981
api_hash = '341e29114e1bb38d1fda9f1a22b59b28'


def mod(text):
    newtext = ''
    for character in text[:-1]:
        newtext += character
        newtext += '\uFEFF'
    newtext += text[-1]
    return newtext


with TelegramClient('userbot', api_id, api_hash) as client:
    @client.on(events.NewMessage(outgoing=True))
    async def antiTranslate(event):
        await client.edit_message(event.message, mod(event.message.message))
    client.run_until_disconnected()
