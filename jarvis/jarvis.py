import logging
import os
import random
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import SystemCommands

logger = logging.getLogger(__name__)


class Jarvis(object):
    # Built-in words
    LISTENING_COGNATES = ["jarvis", "javed", "gervais", "jarvis wake up", "wake up jarvis", "okay jarvis",
                          "ok jarvis", "jarvis are you there", "you there jarvis", "are you there jarvis",
                          "are you there"]
    SLEEP_COGNATES = ["go to sleep", "jarvis go to sleep", "jarvis sleep now", "sleep now"]
    DATETIME_COGNATES = ["what is the time right now", "and time", "tell me about time", "i lost my watch",
                         "what time it is"]
    STOP_LISTENING_COGNATES = ["go away", "stop listening", "take rest", "take rest now"]
    AGREE_COGNATES = ["do you think deepika is mad", "do you think deepika is crazy", "i think my wife is beautiful",
                      "i think my voice is beautiful", "do you think my voice is beautiful",
                      "do you think my wife is beautiful"]
    WHO_IS_MASTER_COGNATES = ["jarvis who is your boss", "jarvis who is your master", "who is your master",
                              "who is your boss"]
    FACEBOOK_COGNATES = ["open my facebook", "give me facebook updates", "give me my facebook updates", "open facebook"]
    WHAT_DOING_COGNATES = ["what are you doing"]
    WHERE_AM_I_COGNATES = ["where am i right now", "what is this place", "where are we"]
    POWER_STATUS_COGNATES = ["what is your power status", "what is your battery status", "are you charged",
                             "is the charger working"]

    @classmethod
    def remove_listening_cognate(self, command):
        is_exists = False
        for wrd in self.LISTENING_COGNATES:
            if wrd in command:
                is_exists = True
                command = command.replace(wrd, " ")
                command = command.replace("  ", " ")
        return is_exists, command.strip()

    @classmethod
    def analyse_sentiments(self,command):
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

    @classmethod
    def handle_action(self, command, **kwargs):
        speak_message = None
        # Use lowercase for processing.
        command = command.lower()

        if command == "jarvis":
            is_exists = True
        else:
            is_exists, command = self.remove_listening_cognate(command)

        if is_exists:
            print("User: " + command)

            if command in self.LISTENING_COGNATES:
                speak_message = random.choice(["Yes Sir?", "I am here Sir", "I am listening Sir", "Oh hello Sir"])
            elif command in self.SLEEP_COGNATES:
                # System now goes to sleep mode
                SystemCommands.system_goto_sleep()
            elif command in self.DATETIME_COGNATES:
                # Get current time
                SystemCommands.get_system_time()
            elif command in self.WHO_IS_MASTER_COGNATES:
                SystemCommands.get_boss_name()
            elif command in self.AGREE_COGNATES:
                speak_message = random.choice(["I agree", "Absolutely", "No doubt Sir"])
            elif command in self.FACEBOOK_COGNATES:
                SystemCommands.open_facebook_in_browser()
            elif command in self.WHAT_DOING_COGNATES:
                SystemCommands.get_what_doing_speech()
            elif command in self.WHERE_AM_I_COGNATES:
                SystemCommands.get_current_location()
            elif command in self.POWER_STATUS_COGNATES:
                SystemCommands.speak_battery_info()
            elif "where is" in command:
                speech_data = command.split("where is")
                SystemCommands.open_map(str(speech_data[1]).strip())
            elif command in self.STOP_LISTENING_COGNATES:
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
