from telethon import TelegramClient, sync, events



api_id = '#'
api_hash = '#'

chat_ids = 'Your chat id'

client = TelegramClient('session',api_id,api_hash)
client.start()
#HERE CHECKS TO NEW MESSAGES
@client.on(events.NewMessage(chats=('New')))
async def normal_handler1(event):
	last_msg = event.message.message
	specific_words = ['Trade type','Entry zone','Target','Exchange','My apologize']
	for i in specific_words:
		if i in last_msg:
			print("works")
			await send_msg(event.message.to_dict()['message'])

		else:
			print("dont")
#####################

async def send_msg(msg):
	print(msg)
	await client.send_message('Daulet', msg)####----WRITE HERE YOUR CHANELLS NAME TO SEND MESSAGE---------#######
###########


client.run_until_disconnected()
