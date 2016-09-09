import logging
import os
import SystemCommands
import random
import re

logger = logging.getLogger(__name__)


class Jarvis(object):
    # Built-in words
    LISTENING_COGNATES = ["jarvis", "javed", "gervais", "jarvis wake up", "wake up jarvis", "okay jarvis", "ok jarvis"]
    SLEEP_COGNATES = ["go to sleep", "jarvis go to sleep", "jarvis sleep now", "sleep now"]
    DATETIME_COGNATES = ["what is the time right now", "and time", "tell me about time", "i lost my watch"]
    STOP_LISTENING_COGNATES = ["go away", "stop listening", "take rest", "take rest now"]
    AGREE_COGNATES = ["do you think deepika is mad", "do you think deepika is crazy", "i think my wife is beautiful",
                      "i think my voice is beautiful", "do you think my voice is beautiful",
                      "do you think my wife is beautiful"]
    WHO_IS_MASTER_COGNATES = ["jarvis who is your boss", "jarvis who is your master", "who is your master",
                              "who is your boss"]
    FACEBOOK_COGNATES = ["open my facebook", "give me facebook updates", "give me my facebook updates", "open facebook"]
    WHAT_DOING_COGNATES = ["what are you doing"]
    WHERE_AM_I_COGNATES = ["where am i right now", "what is this place", "where are we"]

    # @classmethod
    # def is_actionable_command(cls, command):
    #     return any(cognate in command for cognate in cls.LISTENING_COGNATES)

    @classmethod
    def handle_action(cls, command, **kwargs):
        speak_message = None
        # Use lowercase for processing.
        command = command.lower()
        print("Arpit: " + command)

        if command in cls.LISTENING_COGNATES:
            speak_message = random.choice(["Yes Sir?", "I am here Sir", "I am listening Sir", "Oh hello Sir"])
        elif command in cls.SLEEP_COGNATES:
            # System now goes to sleep mode
            SystemCommands.system_goto_sleep()
        elif command in cls.DATETIME_COGNATES:
            # Get current time
            SystemCommands.get_system_time()
        elif command in cls.WHO_IS_MASTER_COGNATES:
            SystemCommands.get_boss_name()
        elif command in cls.AGREE_COGNATES:
            speak_message = random.choice(["I agree", "Absolutely", "No doubt Sir"])
        elif command in cls.FACEBOOK_COGNATES:
            SystemCommands.open_facebook_in_browser()
        elif command in cls.WHAT_DOING_COGNATES:
            SystemCommands.get_what_doing_speech()
        elif command in cls.WHERE_AM_I_COGNATES:
            SystemCommands.get_current_location()
        elif "where is" in command:
            speech_data = command.split("where is")
            SystemCommands.open_map(str(speech_data[1]).strip())
        elif command in cls.STOP_LISTENING_COGNATES:
            speak_message = random.choice(["Sure Sir", "Okay Sir", "Absolutely"])
            print("JARVIS: " + speak_message)
            os.system("say " + speak_message)
            exit()
        else:
            # speak_message = random.choice(["Oh ho, I got confused", "Could not hear you properly"])
            print("JARVIS: Could not hear you properly")

        if speak_message is not None:
            print("JARVIS: " + speak_message)
            os.system("say " + speak_message)
