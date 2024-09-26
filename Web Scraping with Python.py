import requests
response = requests.get('https://www.example.com')
content = response.content
content = response.text
status_code = response.status_code
headers = response.headers
from bs4 import BeautifulSoup
html_content = '<html><head><title>Example</title></head><body><p>This is a sample HTML document.</p></body></html>'
soup = BeautifulSoup(html_content, 'html.parser')
p_tag = soup.find('p')
p_text = p_tag.text
print(p_text)
a_tag = soup.find('a')
if a_tag:
    href_value = a_tag.get('href')
    print(href_value)
else:
    print("No 'a' tag found!")
    soup.get_text()
    import requests
    from bs4 import BeautifulSoup
    import re

    page = requests.get('https://example.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all(class_='product_pod')
    content = str(content)
    number = r'\d{3}-\d{3}-\d{4}'
    import csv
    data = [
        ['Jay', 'Dominic', 25],
        ['Justin', 'Seam', 30],
        ['Bob', 'Lans', 40]
    ]
    with open('data.csv', mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(data)
    import json
    data = [
        {'name': 'John', 'surname': 'Doe', 'age': 25},
        {'name': 'Jane', 'surname': 'Smith', 'age': 30},
        {'name': 'Bob', 'surname': 'Johnson', 'age': 40}
    ]
    with open('data.json', mode='w') as file:
     json.dump(data, file)
    import requests
    from bs4 import BeautifulSoup

    url = "https://example.com"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
     print("An error occurred while making the request:", e)
    except Exception as e:
     print("An error occurred:", e)
    finally:
     import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from gologin import GoLogin
    from gologin import get_random_port
    gl = GoLogin({
        "token": "yU0token",
        "profile_id": "yU0Pr0f1leiD",
    })
    from gologin import GoLogin

    gl = GoLogin({
        "token": "yU0token",
    })
    profile_id = gl.create({
        "name": 'profile_windows',
        "os": 'win',
        "navigator": {
            "language": 'en-US',
            "userAgent": 'random',
            "resolution": '1920x1080',
            "platform": 'Win32',
        },
        'proxyEnabled': True,
        'proxy': {
            'mode': 'gologin',
            'autoProxyRegion': 'us'
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
        },
    })
    profile = gl.getProfile(profile_id)
    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("THE URL TO BE SCRAPED")
    driver.close()
    time.sleep(3)
    gl.stop()