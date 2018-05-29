from login import login_website
from download import makedir
from download import download_pic
url_login = "https://cas.xjtu.edu.cn/login?service=http%3A%2F%2F202.117.1.179%2FcasLogin.do"
url_pic = "http://202.117.1.179/student/loadPhoto.do?studentNumber="
if (__name__=='__main__'):
    session_login = login_website(url_login)
    makedir()
    download_pic(session_login= session_login, url_pic= url_pic, limit= 144)

