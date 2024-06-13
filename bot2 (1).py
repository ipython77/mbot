import requests
import telebot,time,random
from telebot import types
from gatet import Tele
import os
token = '7127316532:AAF4dBLavsx8pmHKENAh7T6ENS9hNbY39Nk'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber ='5123986264'
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )")
		return
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )")
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➤ 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary ) ''', reply_markup=mes)
				msg = f'''✘ 𝗖𝗮𝗿𝗱  ➤ {cc} 
✘ 𝐬𝐭𝐚𝐭𝐮𝐬 ➤ 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝  ✅ 
✘ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➤ Insufficient Funds
✘ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➤ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 1$
━━━━━━━━━━━━━━━━━
✘ 𝗕𝗜𝗡 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➤ {cn} - {emj} 
✘ 𝐈𝐬𝐬𝐮𝐞𝐫 ➤ {bank}
✘ 𝐮𝐫𝐥 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝑩𝒀 ➤ @u_1_1_6
✘ 𝑷𝑹𝑶𝑿𝒀𝑺 ➤ 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				print(last)
				if "Funds" in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'success' in last:
					msg=f'''✘ 𝗖𝗮𝗿𝗱  ➜ {cc} 
✘ 𝐬𝐭𝐚𝐭𝐮𝐬 ➤ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
✘ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➤ 𝑺𝑼𝑪𝑪𝑬𝑺𝑺
✘ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➤ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 1$
━━━━━━━━━━━━━━━━━
✘ 𝗕𝗜𝗡 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➤ {cn} - {emj} 
✘ 𝐈𝐬𝐬𝐮𝐞𝐫 ➤ {bank}
✘ 𝐮𝐫𝐥 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝑩𝒀 ➤ @u_1_1_6
✘ 𝑷𝑹𝑶𝑿𝒀𝑺 ➤ 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg)
				else:
					dd += 1
				random_number = random.randint(1, 3)

				time.sleep(random_number)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➤ @u_1_1_6')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
@bot.message_handler(commands=["chk"])
def start(message):
	name='𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 𝙲𝚅𝚅 1$'
	if not str(message.chat.id) == subscriber:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @u_1_1_6")
	try:
		cc=message.text.replace('/chk ', '')
	except:
		bot.reply_to(message, "Wrong format ❌")
		return
	try:
		data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
	except:
		pass
	try:
		bank=(data['bank']['name'])
	except:
				bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		emj=(data['country']['emoji'])
	except:
				emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		cn=(data['country']['name'])
	except:
				cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		dicr=(data['scheme'])
	except:
				dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		typ=(data['type'])
	except:
				typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		url=(data['bank']['url'])
	except:
		url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		last = str(Tele(cc))
	except Exception as e:
		print(e)
		last='ERROR'
		
	if "live" in last or 'Funds' in last:
		msg=f'''✘ 𝗖𝗮𝗿𝗱  ➜ <code>{cc}</code> 
✘ 𝐬𝐭𝐚𝐭𝐮𝐬 ➤ 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝  ✅ 
✘ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➤ {last}
✘ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➤ {name} 
━━━━━━━━━━━━━━━━━
✘ 𝗕𝗜𝗡 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➤ {cn} - {emj} 
✘ 𝐈𝐬𝐬𝐮𝐞𝐫 ➤ {bank}
✘ 𝐮𝐫𝐥 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝒅𝒆𝒗 ➤ 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary ) [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
	elif 'successfully' in last:
		msg=f'''✘ 𝗖𝗮𝗿𝗱  ➤ <code>{cc}</code>
✘ 𝐬𝐭𝐚𝐭𝐮𝐬 ➤ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
✘ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➤ {last}
✘ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➤ {name} 
━━━━━━━━━━━━━━━━━
✘ 𝗕𝗜𝗡 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➤ {cn} - {emj} 
✘ 𝐈𝐬𝐬𝐮𝐞𝐫 ➤ {bank}
✘ 𝐮𝐫𝐥 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝑩𝒀 ➤ @u_1_1_6
✘ 𝒅𝒆𝒗 ➤ 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary ) [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
	else:
		msg=f'''✘ 𝗖𝗮𝗿𝗱  ➤ <code>{cc}</code> 
✘ 𝐬𝐭𝐚𝐭𝐮𝐬 ➤ 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ 
✘ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ➤ {last}
✘ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➤ 
━━━━━━━━━━━━━━━━━
✘ 𝗕𝗜𝗡 ➤ {cc[:6]} - {dicr} - {typ} 
✘ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➤ {cn} - {emj} 
✘ 𝐈𝐬𝐬𝐮𝐞𝐫 ➤ {bank}
✘ 𝐮𝐫𝐥 ➤ {url}
━━━━━━━━━━━━━━━━━
✘ 𝑩𝒀 ➤ @u_1_1_6
✘ 𝒅𝒆𝒗 ➤ 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary ) [ <code>Owner</code> ]'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode='HTML')
print("تم تشغيل البوت")
bot.polling()