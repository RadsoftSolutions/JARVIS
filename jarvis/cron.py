import os
from sys import argv
import SystemCommands


def check_battery_percent():
    message_list = ["I am running critically low on power", "please find me a power source",
                    "Have you brought your charger today?", "Please see if you have my charger nearby"]
    battery_percent, battery_status = SystemCommands.get_system_battery_percent()
    if battery_percent <= 15 and battery_status == 'discharging':
        os.system("say sir, I am at " + str(battery_percent) + " percent charge")
        SystemCommands.message_list_to_speech(message_list)
    elif battery_percent == 100 and battery_status == 'charged':
        os.system("say Sir, I am at " + str(battery_percent) + " percent charge. You can remove my power source.")


script, keyword = argv
if keyword == 'battery_check':
    check_battery_percent()
exit()
