import os
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def makedir():
    os.makedirs('./image/',exist_ok=True)
    logging.info("make a new dir successfully!")

def download_pic(session_login, url_pic, limit):
    student_number = 2140505001
    for i in range(1, limit, 1):
        url_pic_student_number = url_pic + str(student_number)
        pic = session_login.get(
            url_pic_student_number,
            headers = dict(referer = url_pic)
        ).content
        with open("./image/" + str(student_number) + ".png","wb") as f:
            f.write(pic)
        logging.info("Download the picture: "+ str(student_number))
        student_number = student_number + 1