# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests
import json

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

conversationFood = []
conversationBar = []
conversationCafe = []
conversationDelivery = []
conversationTakeaway = []
conversationRestaurant = []

myLat = "-33.8670522"
myLong = "151.1957362"
apiKey = "AIzaSyCyZAHJOZWN0Qs6bbNJjTndFH9vvTDWtZM"
distance = "500"
placeType = "restaurant"

class Suggestion(Action):

    def name(self) -> Text:
        return "scan_rasa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+myLat+','+myLong+'&radius='+distance+'&type='+placeType+'&keyword=cruise&key='+apiKey+'&sensor=true')
        data = json.loads(response.text)
        # data = json.dumps(data) 
        dispatcher.utter_message(text=data['results'][0]['name'])
        dispatcher.utter_message(text=data['results'][1]['name'])
        dispatcher.utter_message(text=data['results'][2]['name'])

        # dispatcher.utter_message(text="Food:")
        # for x in conversationFood:
        #     dispatcher.utter_message(text=x)

        # dispatcher.utter_message(text="Bar:")
        # for y in conversationBar:
        #     dispatcher.utter_message(text=y)

        # dispatcher.utter_message(text="Cafe:")
        # for z in conversationCafe:
        #     dispatcher.utter_message(text=z)

        # dispatcher.utter_message(text="Delivery:")
        # for a in conversationDelivery:
        #     dispatcher.utter_message(text=a)

        # dispatcher.utter_message(text="Takeaway:")
        # for b in conversationTakeaway:
        #     dispatcher.utter_message(text=b)

        # dispatcher.utter_message(text="Restaurant:")
        # for c in conversationRestaurant:
        #     dispatcher.utter_message(text=c)

        return []

class ScanFood(Action):

    def name(self) -> Text:
        return "scan_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message['intent'].get('confidence') > 0.6:
            conversationFood.append((tracker.latest_message)['text'])

        return []

class ScanBar(Action):

    def name(self) -> Text:
        return "scan_bar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message['intent'].get('confidence') > 0.6:
            conversationBar.append((tracker.latest_message)['text'])
            placeType = tracker.latest_message['intent'].get('name')

        return []

class ScanCafe(Action):

    def name(self) -> Text:
        return "scan_cafe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message['intent'].get('confidence') > 0.6:
            conversationCafe.append((tracker.latest_message)['text'])
            placeType = tracker.latest_message['intent'].get('name')

        return []

class ScanDelivery(Action):

    def name(self) -> Text:
        return "scan_meal_delivery"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message['intent'].get('confidence') > 0.6:
            conversationDelivery.append((tracker.latest_message)['text'])
            placeType = tracker.latest_message['intent'].get('name')

        return []

class ScanTakeaway(Action):

    def name(self) -> Text:
        return "scan_meal_takeaway"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message['intent'].get('confidence') > 0.6:
            conversationTakeaway.append((tracker.latest_message)['text'])
            placeType = tracker.latest_message['intent'].get('name')

        return []

class ScanTakeaway(Action):

    def name(self) -> Text:
        return "scan_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.latest_message['intent'].get('confidence') > 0.6:
            conversationRestaurant.append((tracker.latest_message)['text'])
            placeType = tracker.latest_message['intent'].get('name')

        return []
