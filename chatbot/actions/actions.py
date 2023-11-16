from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionInform(Action):
    def name(self):
        return "utter_inform"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Sure, I can help you with that.")
        return []
