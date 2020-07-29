import requests

url = "http://challenge01.root-me.org/programmation/ch1/"
r = requests.get(url)

page = str(r.text)
page = page.split(' ')
a = int(page[12])
b = int(page[20])
current = int(page[24][:len(page[24])-4])
looking_for = int(page[28][6:len(page[28])-9])

if page[16]=='-':
    for i in range(looking_for):
        current = (a + current) - (i*b)

else:
    for i in range(looking_for):
        current = (a + current) + (i*b)

url = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="+str(current)
r = requests.get(url,cookies = r.cookies)

print(str(r.text))
