from telethon.sync import TelegramClient, utils, events
from telethon.tl.types import InputPeerChannel
import re
import datetime

api_id = 26031213
api_hash = '15df916e4e17260afc4fa4ecde520968'
phone_number = '213667894166'

subscribers = {}

async def get_channel_messages(channel_entity, keyword, target_chat_id, num_messages):
    messages = []  
    
    async for message in client.iter_messages(channel_entity):
        if message.raw_text is not None and keyword in message.raw_text:
            messages.append(message.raw_text)  
            if len(messages) >= num_messages:
                break  
    
    if messages:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'MODCA.({timestamp}).txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for message in messages:
                file.write(message + '\n')
        
        await client.send_file(target_chat_id, filename)  

async def handle_command(event):
    chat = await event.get_chat()
    user_input = event.raw_text
    match = re.match(r'/modca\s?(@\w+)\s+(\d+)', user_input)
    if match:
        keyword = '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅'  
        channel_username = match.group(1)
        num_messages = int(match.group(2))
        
        if num_messages > 0:
            channel_entity = await client.get_input_entity(channel_username)
            await get_channel_messages(channel_entity, keyword, event.chat_id, num_messages)
        else:
            await client.send_message(event.chat_id, "خطأ في تنسيق الأمر")
    
    else:
        match = re.match(r'/modca\s+(.+)\s+(@\w+)\s+(\d+)', user_input)
        if match:
            custom_keyword = match.group(1)
            channel_username = match.group(2)
            num_messages = int(match.group(3))
            
            channel_entity = await client.get_input_entity(channel_username)
            await get_channel_messages(channel_entity, custom_keyword, event.chat_id, num_messages)

with TelegramClient(phone_number, api_id, api_hash) as client:
    @client.on(events.NewMessage(pattern='/modca'))
    async def handler(event):
        await handle_command(event)

    client.run_until_disconnected()
