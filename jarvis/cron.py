import os
from sys import argv
from SystemCommands import get_random_from_list
from SystemCommands import get_system_battery_percent


def check_battery_percent():
    message_list = ["I am running critically low on power", "please find me a power source",
                    "Have you brought your charger today?", "Please see if you have my charger nearby"]
    battery_percent, battery_status = get_system_battery_percent()
    if battery_percent <= 15 and battery_status is 'discharging':
        speak_message = get_random_from_list(message_list)
        os.system("say sir, I am at " + str(battery_percent) + " percent charge")
        os.system("say " + speak_message)
    elif battery_percent == 100 and battery_status is 'charging':
        os.system("say sir, I am at " + str(battery_percent) + " percent charge now, you can remove the charger")


script, keyword = argv
if keyword == 'battery_check':
    check_battery_percent()
exit()
