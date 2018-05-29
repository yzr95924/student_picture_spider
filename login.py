import requests
from lxml import html
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def login_website(url_login):
    username = input("username: ")
    password = input("password: ")
    session_login = requests.session()
    logging.info("start to login the website")
    text_result = session_login.get(url_login).text
    soup = BeautifulSoup(text_result,"lxml")
    lt = soup.body.findAll("div",{"id":"login_box_mobile"})[0].form.findAll("div",{"class":"row btn-row"})[0].findAll("input")[0]["value"]
    execution = soup.body.findAll("div",{"id":"login_box_mobile"})[0].form.findAll("div",{"class":"row btn-row"})[0].findAll("input")[1]["value"]
    _eventId = soup.body.findAll("div",{"id":"login_box_mobile"})[0].form.findAll("div",{"class":"row btn-row"})[0].findAll("input")[2]["value"]
    payload = {
        "username": str(username),
        "password": str(password),
        "code":"",
        "lt":str(lt),
        "execution":str(execution),
        "_eventId":str(_eventId),
        "submit":"登录"
    }
    result = session_login.post(
        url_login,
        data = payload,
        headers = dict(referer = url_login)
    )

    if (str(result)=="<Response [200]>"):
        logging.info("login successfully!")
        return session_login
    else:
        logging.info("login failure")
        return -1