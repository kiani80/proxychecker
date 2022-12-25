from telethon import TelegramClient
# import TelethonFakeTLS

# Use your own values from my.telegram.org
api_id = 20635210
api_hash = 'ab16f0e9db71ca775b94d3c156ebf9cd'

# _proxy = _proxy = ('50.7.42.106', 443, '1603010200010001fc030386e24c3add6170706c652e636f6d')
# _con=TelethonFakeTLS.ConnectionTcpMTProxyFakeTLS

client = TelegramClient('anon', api_id, api_hash)

# client = TelegramClient(
#     'anon', api_id, api_hash,
#     connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
#     proxy=('185.181.10.190', 3255, '00000000000000000000000000000000')
# )
# messages=[]
def get_proxy(messages,channal):
    async def main():
        # Getting information about yourself
        me = await client.get_me()

        # "me" is a user object. You can pretty-print
        # any Telegram object with the "stringify" method:
        # sprint(me.stringify())

        # You can print all the dialogs/conversations that you are part of:
        #async for dialog in client.iter_dialogs():
        #    print(dialog.name, 'has ID', dialog.id)

        # You can, of course, use markdown in your messages:
        # message = await client.send_message(
        #     'me',
        #     'This message has **bold**, `code`, __italics__ and '
        #     'a [nice website](https://example.com)!',
        #     link_preview=False
        # )

        # Sending a message returns the sent message object, which you can use
        # print(message.raw_text)

        # You can reply to messages directly if you have a message object
    

        # Or send files, songs, documents, albums...
        #https://t.me/MTP_roto   ,,https://t.me/DeamNet_proxy
        counter =0 
        # You can print the message history of any chat:
        async for message in client.iter_messages(channal):
            # print(message.id, message.text)
            messages.append(message.text)
            counter = counter +1
            if counter == 4:
                break

            # You can download media from messages, too!
            # The method will return the path where the file was saved.
        

    with client:
        client.loop.run_until_complete(main())

messages=[]
channal ="https://t.me/DeamNet_proxy"
get_proxy(messages,channal)
print(messages)
