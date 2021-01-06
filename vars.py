from telethon import TelegramClient, sync, events



api_id = 'YOUR ID'
api_hash = 'YOUR HASH'

chat_ids = 'Your chat id'

client = TelegramClient('session',api_id,api_hash)



fin_res = []          ##############WRITE IN BRACKETS CHANNELS NAME LIKE ['CHANNELNAME','...'	}





#HERE CHECKS TO NEW MESSAGES
@client.on(events.newmessage.NewMessage(from_users=fin_res))######
async def normal_handler1(event):
	print(event.message)
	await send_msg(event.message.to_dict()['message'])
#####################




async def send_msg(msg):
	print(msg)
	await client.send_message('#', msg)####----WRITE HERE YOUR CHANELLS NAME TO SEND MESSAGE---------#######
###########






client.start()
client.run_until_disconnected()