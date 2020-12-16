from telethon.sync import TelegramClient, events

api_id = 1054981
api_hash = '341e29114e1bb38d1fda9f1a22b59b28'

with TelegramClient('userbot', api_id, api_hash) as client:
    @client.on(events.NewMessage(pattern='-delit', outgoing=True))
    async def delit(event):
        print("delit is running")
        target = await event.get_reply_message()
        if event.reply_to_msg_id:
            try:
                await target.delete()
            except:
                print("delit error")
        await event.delete()

    @client.on(events.NewMessage(pattern='-delall', outgoing=True))
    async def delall(event):
        print("delall is running")
        async for message in event.client.iter_messages(event.chat_id):
            await message.delete()

    @client.on(events.NewMessage(pattern='-delme', outgoing=True))
    async def delme(event):
        print("delme is running")
        input_chat = await event.get_input_chat()
        messages = []
        async for message in event.client.iter_messages(input_chat, from_user="me"):
            messages.append(message)
            if len(messages) == 100:
                await event.client.delete_messages(input_chat, messages)
        if messages:
            await event.client.delete_messages(input_chat, messages)

    @client.on(events.NewMessage(pattern='-delfrom', outgoing=True))
    async def delfrom(event):
        print("delfrom is running")
        if not event.reply_to_msg_id:
            await event.delete()
            return
        input_chat = await event.get_input_chat()
        messages = []
        async for message in event.client.iter_messages(input_chat, min_id=event.reply_to_msg_id):
            messages.append(message)
            if len(messages) == 100:
                await event.client.delete_messages(input_chat, messages)
        if messages:
            await event.client.delete_messages(input_chat, messages)
        await event.client.delete_messages(input_chat, event.reply_to_msg_id)
    client.run_until_disconnected()
