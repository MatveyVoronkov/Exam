# import urllib.request
#
# opener = urllib.request.build_opener()
# resource = opener.open('https://httpbin.org/get')
#
# print(resource.read())
#
# import requests
#
# resource = requests.get('https://httpbin.org/get')
#
# print(resource.content)

# import requests
#
# resource = requests.get('https://httpbin.org/get')
# print(resource.text)
# print(f'Datatype - {type(resource.text)}')

# import requests
# response = requests.post('https://httpbin.org/get', data='Text data', headers={'h1':'Test title'})
# print(response.text)

# import requests
# res_parse_list=[]
#
# response = requests.get('https://coinmarketcap.com/')
# response_text= response.text
# response_parse = response_text.split('<span>')
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith('$'):
#         for parse_elem_2 in parse_elem_1.split('</span>'):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
# print("___The most popular prices___")
# z = input("Choose one: ")
# if z=='Bitcoin':
#     bitcoin_exchage_rate = res_parse_list[0]
#     print("Bitcoin price: ",bitcoin_exchage_rate)
# if z=='Ethereum':
#     ethereum_exchage_rate = res_parse_list[1]
#     print("Ethereum price: ",ethereum_exchage_rate)
# if z=='Tether':
#     tether_exchage_rate = res_parse_list[2]
#     print("Tether price: ",tether_exchage_rate)
# if z=='BNB':
#     bnb_exchage_rate = res_parse_list[3]
#     print("BNB price: ",bnb_exchage_rate)
# if z=='XRP':
#     xrp_exchage_rate = res_parse_list[4]
#     print("XRP price: ",xrp_exchage_rate)
# if z=='Cardano':
#     cardano_exchage_rate = res_parse_list[1]
#     print("Cardano price: ",cardano_exchage_rate)
# if z=='Solana':
#     solana_exchage_rate = res_parse_list[2]
#     print("Solana price: ",solana_exchage_rate)
# if z=='Tron':
#     tron_exchage_rate = res_parse_list[3]
#     print("Tron price: ",tron_exchage_rate)

from bs4 import BeautifulSoup
import requests

response=requests.get('https://coinmarketcap.com/')
print("___Welcome___")
z = input("Choose one: ")
if z == "Bitcoin":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/bitcoin/markets/'})
    #for elem in soup_list:
    #    print(elem)
    res = soup_list[0].find('span')
    print(res.text)
if z == "Ethereum":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/ethereum/markets/'})
    res = soup_list[0].find('span')
    print(res.text)
if z == "Tether":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/tether/markets/'})
    res = soup_list[0].find('span')
    print(res.text)
if z == "Bnb":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/bnb/markets/'})
    res = soup_list[0].find('span')
    print(res.text)
if z == "XRP":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/xrp/markets/'})
    res = soup_list[0].find('span')
    print(res.text)
if z == "Cardano":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/cardano/markets/'})
    res = soup_list[0].find('span')
    print(res.text)
if z == "Solana":
    soup=BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/solana/markets/'})
    res = soup_list[0].find('span')
    print(res.text)

