import csv
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetRandomNames(Action):

  def name(self) -> Text:
    return "action_get_random_names"

  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    names = []

    with open('rand_data/random_names.csv', newline='', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        names.append(row['name'])

    random.shuffle(names)
    selected_names = names[:5]  # Change the number to select more or less names

    dispatcher.utter_message(text=f"Here are some random names: {', '.join(selected_names)}")

    return []