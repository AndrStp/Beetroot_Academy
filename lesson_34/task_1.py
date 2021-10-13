"""
Task 1

Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc.
"""

import requests


def main():
    web_site = input('Enter the web-page address: ')
    if not web_site:
        print('No web_site provided')
        exit()
        
    content = get_content(web_site)
    directory = input('Enter the directory: ')
    save_content(content, directory)


def get_content(page: str) -> str:
    """Returns web-page content as string"""
    r = requests.get(page)
    return r.text


def save_content(content: str, dir_: str = 'robots.txt') -> None:
    """Saves the content of the web-page to the file"""
    if not dir_:
        dir_ = 'robots.txt'
    
    with open(dir_, 'a+', encoding='utf-8') as f:
        f.write(content)
    


if __name__ == '__main__':
    main()