from telethon.sync import TelegramClient, events

api_id = 1054981
api_hash = '341e29114e1bb38d1fda9f1a22b59b28'

with TelegramClient('userbot', api_id, api_hash) as client:
    @client.on(events.NewMessage(pattern='-delit', outgoing=True))
    async def delit(event):
        print("-delit\t ->\trunning")
        target = await event.get_reply_message()
        if event.reply_to_msg_id:
            try:
                await target.delete()
            except:
                print("delit error")
        await event.delete()
        print("-delit\t ->\tdone")

    @client.on(events.NewMessage(pattern='-delall', outgoing=True))
    async def delall(event):
        print("-delall\t ->\trunning")
        input_chat = await event.get_input_chat()
        messages = []
        async for message in event.client.iter_messages(input_chat):
            if (message.id==1):
                if messages:
                    await event.client.delete_messages(input_chat, messages)
                break
            messages.append(message)
            if len(messages) == 100:
                await event.client.delete_messages(input_chat, messages)
        print("-delall\t ->\tdone")

    @client.on(events.NewMessage(pattern='-delme', outgoing=True))
    async def delme(event):
        print("-delme\t ->\trunning")
        input_chat = await event.get_input_chat()
        messages = []
        loop = 0
        async for message in event.client.iter_messages(input_chat):
            if (message.id==1):
                if messages:
                    await event.client.delete_messages(input_chat, messages)
                break
            loop += 1
            if (message.from_id.user_id == myid):
                messages.append(message)
            if loop == 100:
                if messages:
                    await event.client.delete_messages(input_chat, messages)
                loop = 0
        print("-delme\t ->\tdone")

    @client.on(events.NewMessage(pattern='-delfrom', outgoing=True))
    async def delfrom(event):
        print("-delfrom ->\trunning")
        if not event.reply_to_msg_id:
            await event.delete()
            return
        input_chat = await event.get_input_chat()
        messages = []
        async for message in event.client.iter_messages(input_chat, min_id=event.reply_to_msg_id-1):
            messages.append(message)
            if len(messages) == 100:
                await event.client.delete_messages(input_chat, messages)
        if messages:
            await event.client.delete_messages(input_chat, messages)
        print("-delfrom ->\tdone")
    myid = client.get_me().id
    print("Usage:\n\t-delit\t ->\tDetele a message you reply\n\t-delme\t ->\tDetele all messages you send\n\t-delall\t ->\tDetele all messages\n\t-delfrom ->\tDetele messages from where you reply\n")
    client.run_until_disconnected()
