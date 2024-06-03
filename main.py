try:
    from bs4 import BeautifulSoup
    import requests
except:
    import subproccess,sys
    subproccess.call("pip install requests")
    subproccess.call("pip install beautifulsoup")
    print("Please Restart.")
    sys.exit(1)
url = input("URL:")
try:
    html = requests.get(url)
    bs = BeautifulSoup(html.text,'html.parser')
    content = bs.find_all("h5")
    content2 = bs.find_all("h2")
    cont = bs.find_all('p')
    print("Title:"+bs.find('title').text)
    for c in content:
        print("[H5]"+c.text)
    
    
    for c2 in content2:
        print("[H2]"+c2.text)
    for co in cont:
        print("[P]"+c2.text)
except:
    import sys
    print("Error!")
    sys.exit(1)
    