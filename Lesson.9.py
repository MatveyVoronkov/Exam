import requests
res_parse_list=[]

response = requests.get('https://coinmarketcap.com/')
response_text= response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
     if parse_elem_1.startswith('$'):
         for parse_elem_2 in parse_elem_1.split('</span>'):
             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                 res_parse_list.append(parse_elem_2)
print("___Your course in dollar___")
print('Enter for example: Гривна = G, Рубль = R, Юань = U')
z = input("Your value: ")
x = int(input("Enter price: "))
if z=='G':
     g = x * 0.027
     print(g)
f = input("Your value: ")
x = int(input("Enter price: "))
if z=='R':
     r = x * 0.01
print(r)
h = input("Your value: ")
x = int(input("Enter price: "))
if z=='U':
     u = x * 0.03
print(u)