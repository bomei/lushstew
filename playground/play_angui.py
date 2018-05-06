import requests

resp = requests.get('https://www.random.org/integers/?num=32&min=0&max=15&col=32&base=2&format=plain&rnd=new')
res = hex(int(resp.text.replace('\t', '').replace('\n', ''), 2))[2:].upper()
print(resp)
