try:
    from bs4 import BeautifulSoup
    import requests
except:
    import subprocess,sys
    subprocess.call("pip install requests")
    subprocess.call("pip install beautifulsoup")
    print("Please Restart.")
    sys.exit(1)
url = input("URL:")
try:
    html = requests.get(url)
    bs = BeautifulSoup(html.text,'html.parser')
    content = bs.find_all("h5")
    content2 = bs.find_all("h2")
    cont = bs.find_all('p')
    con = bs.find_all('a')
    conn = bs.find_all('h4')
    cot = bs.find_all('h1')
    links = bs.get('href',con)
    print("Title:"+bs.find('title').text)
    for c in content:
        print("[H5]"+c.text)
    
    
    for c2 in content2:
        print("[H2]"+c2.text)
    for co in cont:
        print("[P]"+c2.text)
    for c in con:
        print("[A]"+c.text)
    for cc in conn:
        print("[H4]"+cc.text)
    for cc2 in cot:
        print("[H1]"+cc2.text)
except:
    import sys
    print("Error!")
    sys.exit(1)
    