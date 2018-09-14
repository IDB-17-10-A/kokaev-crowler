import re 
import requests


if __name__ == '__main__':
    pattern = re.compile(r'href="(?P<http_address>[a-zA-Z0-9:?&=\/.]+)"')
    r = requests.get('http://stankin.ru/')
    text = r.text

    print(pattern.findall(text))
