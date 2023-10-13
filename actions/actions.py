from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractNameEntity(Action):

    def name(self) -> Text:
        return "action_extract_name_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_entity = next(tracker.get_latest_entity_values("ten"), None)
        cust_sex_entity = next(tracker.get_latest_entity_values("cust_sex"), None)

        if ten_entity and cust_sex_entity:
            dispatcher.utter_message(text=f"Dạ em xin chào {cust_sex_entity} {ten_entity}")
        else:
            dispatcher.utter_message(text="Xin loi hinh nhu ten cua ban chua dung")
        return []