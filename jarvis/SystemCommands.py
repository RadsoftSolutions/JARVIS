import logging
import os
import time
import random

logger = logging.getLogger(__name__)


def get_random_from_list(input_list):
    return random.choice(input_list)


def get_system_battery_percent():
    battery_percent = os.popen('pmset -g batt | egrep "([0-9]+\%).*" -o --colour=auto | cut -f1 -d\';\'').read().strip()
    battery_status = os.popen('pmset -g batt | egrep "([0-9]+\%).*" -o --colour=auto | cut -f2 -d\';\'').read().strip()

    return int(battery_percent.split('%')[0]), battery_status


def system_goto_sleep():
    message_list = ["Thank you sir", "I needed it much", "Thank you sir, enjoy your time",
                    "Thank you, enjoy your day, sir"]

    speak_message = get_random_from_list(message_list)
    print("JARVIS: " + speak_message)
    os.system("say " + speak_message)
    os.system("pmset sleepnow")


def get_system_time():
    current_time = str(time.strftime('%l:%M %p'))
    message_list = ["It is " + current_time, "It is " + current_time + ", sir"]

    speak_message = get_random_from_list(message_list)
    print("JARVIS: " + speak_message)
    os.system("say " + speak_message)


def speak_battery_info():
    battery_percent, battery_status = get_system_battery_percent()
    message_list = ["sir, I am at " + str(battery_percent) + " percent charge and " + str(battery_status)]

    speak_message = get_random_from_list(message_list)
    print("JARVIS: " + speak_message)
    os.system("say " + speak_message)


def get_boss_name():
    message_list = ["Mister Arpit is my master", "Mister Arpit is my boss"]

    speak_message = get_random_from_list(message_list)
    print("JARVIS: " + speak_message)
    os.system("say " + speak_message)


def open_facebook_in_browser():
    import webbrowser

    message_list = ["Sure sir", "Are you sure that you are wasting any time?"]

    speak_message = get_random_from_list(message_list)
    print("JARVIS: " + speak_message)
    os.system("say " + speak_message)

    new = 2  # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    url = "https://www.facebook.com"
    webbrowser.open(url, new=new)