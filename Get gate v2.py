try:
 import requests
 from bs4 import BeautifulSoup
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

Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
k = ("                                    𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )" )
print(C + k)
print('      ----------------------------\<>/-------------------------')
def search_and_save_links(query, number_of_links):
    number_text = int(number_of_links) / 10
    urls = []
    for page_num in range(int(number_text)):
        url = f"https://www.google.com/search?q={query}&start={page_num * 10}&sourceid=chrome&ie=UTF-8"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links_on_page = soup.find_all('a', href=True)

        for link in links_on_page:
            url = link['href']
            if url.startswith('/url?q='):
                url = url[7:].split('&')[0]
                if 'google' not in url and url not in urls:
                    urls.append(url)

    for url in urls:
        print(url)
        with open('𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤.txt', 'a') as file:
            file.write(f'{url}\n')

print('                                    𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇩🇿⃤ . ( Legendary )')
search_query = input("Enter search query: ")
num_links = input("Enter number of links: ")

search_and_save_links(search_query, num_links)
