import hashlib
import requests
from bs4 import BeautifulSoup

get_rand = 'http://www.reliance.home/mark_lang.w.xml'
login_url = 'http://www.reliance.home/wxml/post_login.xml'
username = 'admin'  # Username
password = 'admin'  # Password


def main():
    with requests.session() as session:
        response = session.get(get_rand)
        soup = BeautifulSoup(response.text, 'xml')
        rand = soup.find('rand').text
        encrypted_password = hashlib.md5(
            bytes(rand + password, encoding='utf8')).hexdigest()  # Encrypted Password Generation
        post_data = {
            'Name': username,
            'password': encrypted_password,
            'rand': rand
        }
        post = session.post(login_url, data=post_data)
        soup = BeautifulSoup(post.text, 'xml')
        login_check = soup.find('login_check').text
        if login_check == '1':
            print('Invalid Password!')
        elif login_check == '2':
            print('Invalid Username!')
        elif login_check == '3':
            print('Login Success!')
        else:
            print('Invalid error!')


if __name__ == '__main__':
    main()
