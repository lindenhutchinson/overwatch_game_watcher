from PIL import ImageGrab
import numpy as np
import time
import dotenv
import os
from password_manager import PasswordManager
from emailer import Emailer

dotenv.load_dotenv()

def get_screen_colour_avg():
    img = ImageGrab.grab()
    return np.mean(img)

if __name__ == "__main__":
    e_pw = os.getenv('EE')
    e_key = os.getenv('E_KEY')
    pw = PasswordManager.decrypt(e_pw, e_key)
    emailer = Emailer(os.getenv('SEND_EMAIL'), pw, os.getenv('RECEIVE_EMAIL'))

    print("Monitoring for screen changes")
    prev_avg = get_screen_colour_avg()
    while True:
        avg = get_screen_colour_avg()
        if abs(prev_avg - avg) > int(os.getenv('COLOUR_DIFF_THRESHOLD')):
            print("Screen changed!")
            emailer.send_email('Game has Started!', 'Get your ass to the desk')
            break

        prev_avg = avg

        time.sleep(int(os.getenv('SLEEP_TIME_S')))

