import logging
import os
import time
import random
import json
import webbrowser

import requests
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

logger = logging.getLogger(__name__)


def message_list_to_speech(message_list):
    speak_message = random.choice(message_list)
    logger.debug("JARVIS: " + speak_message)
    os.system("say " + speak_message)


def open_browser(webpage_url):
    # open a public URL, in this case, the webbrowser docs
    webbrowser.open(webpage_url)


def get_system_battery_percent():
    battery_percent = os.popen(
        'pmset -g batt | egrep "([0-9]+\%).*" -o --colour=auto | cut -f1 -d\';\'').read().strip()
    battery_status = os.popen(
        'pmset -g batt | egrep "([0-9]+\%).*" -o --colour=auto | cut -f2 -d\';\'').read().strip()

    return int(battery_percent.split('%')[0]), battery_status


def system_goto_sleep():
    message_list = ["Thank you sir", "I needed it much",
                    "Thank you sir, enjoy your time",
                    "Thank you, enjoy your day, sir"]
    message_list_to_speech(message_list)
    os.system("pmset sleepnow")


def get_system_time():
    current_time = str(time.strftime('%l:%M %p'))
    message_list = ["It is " + current_time, "It is " + current_time + ", sir"]
    message_list_to_speech(message_list)


def speak_battery_info():
    battery_percent, battery_status = get_system_battery_percent()
    message_list = [
        "sir, I am at " + str(battery_percent) + " percent charge and " + str(
            battery_status)]
    message_list_to_speech(message_list)


def get_boss_name():
    message_list = ["Mister Arpit is the who commands me", "Mister Arpit is my boss"]
    message_list_to_speech(message_list)


def get_what_doing_speech():
    message_list = ["Nothing much Sir, I was just debugging myself",
                    "Nothing much Sir, just waiting for your command",
                    "Always free for you sir", "I am at your service Sir",
                    "I was just processing some data for you, Sir",
                    "I am having this delicious chocolate ice cream, do you like ice creams sir?"]
    message_list_to_speech(message_list)


def open_facebook_in_browser():
    message_list = ["Sure sir", "Are you sure that you are wasting any time?"]
    message_list_to_speech(message_list)
    open_browser("https://www.facebook.com")


def get_current_location():
    r = requests.get("http://freegeoip.net/json")
    j = json.loads(r.text)

    message_list = ["Sir, I could only get the city name, you are in " + j[
        "city"] + " right now.",
                    "You are in " + j["city"] + " Sir."]
    message_list_to_speech(message_list)


def analyse_sentiments(command):
    lines_list = tokenize.sent_tokenize(command)
    sid = SentimentIntensityAnalyzer()

    for sentence in lines_list:
        scores = sid.polarity_scores(sentence)
        pos_score = scores["pos"]
        neg_score = scores["neg"]
        if pos_score > neg_score:
            return 'positive'
        elif neg_score > pos_score:
            return 'negative'
        elif pos_score == neg_score:
            return 'nuetral'


def get_sentiment_response(command):
    user_sentiment = analyse_sentiments(command)
    if user_sentiment == 'positive':
        message_list = [
            "I am glad to hear that you are happy with my service."]
    elif user_sentiment == "negative":
        message_list = [
            "I am so sorry that you are not very happy with it. But at the moment there is only so much I can do."]
    else:
        message_list = [
            "I am not able to process your command at the moment. I will ask Mr. Arpit to train me more on it."]

    message_list_to_speech(message_list)


def open_map(place_name):
    message_list = ["Hold on Sir! While I open it for you. Here is " + str(
        place_name) + ".",
                    "Hold on Sir, I will show you where " + str(
                        place_name) + " is.",
                    "Sir, I am opening Google Maps for you, so that you can see where " + str(
                        place_name) + " is."]

    message_list_to_speech(message_list)
    open_browser("https://www.google.co.in/maps/place/" + str(place_name))
