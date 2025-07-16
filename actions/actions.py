import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionUrbanDictionary(Action):
    def name(self) -> Text:
        return "action_urban_dictionary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_input = tracker.latest_message.get('text')
        url = f"https://api.urbandictionary.com/v0/define?term={user_input}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data["list"]:
                definition = data["list"][0]["definition"]
                dispatcher.utter_message(text=f"Urban Dictionary says:\n\n{definition}")
            else:
                dispatcher.utter_message(response="utter_no_slang_found")
        else:
            dispatcher.utter_message(text="Couldn't connect to Urban Dictionary. Try again later.")

        return []
