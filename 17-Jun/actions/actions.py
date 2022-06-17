# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker ,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
from typing import Union
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "user_detail_form"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        required_slots=["ct","child","gr", "mail", "ay", "cdb", "rel", "parent", "sch", "par", "phone"]

        for slot_name in required_slots:
            if  tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot",slot_name)]
            
        return [SlotSet("requested_slot",None)]


class ValidateQForm(Action):
    def name(self) -> Text:
        return "validate_info_form"
    def validate_information(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
            msg="Please provide us with your First Name & Last Name"
            dispatcher.utter_message(text=msg)

            """Validate `Name` value."""
            dispatcher.utter_message(text=f"OK! Your Name is {slot_value}.")
            return {"full name": slot_value}


#     def validate_information(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         # required_slots=["ct","cn","gr", "mail", "ay", "cdb", "rel", "fnm", "sch", "par", "phone"]
#         # par= tracker.get_slot("par")
#         # sch= tracker.get_slot("sch")

#         # fnm= tracker.get_slot("fnm")
#         # phone= tracker.get_slot("phone")
#         # mail= tracker.get_slot("mail")
#         # ct = tracker.get_slot("ct")
#         msg="Please provide us with your Child's Name"
#         dispatcher.utter_message(text=msg)
#         # cn= tracker.get_slot("cn")
#         # gr= tracker.get_slot("gr")
#         # ay= tracker.get_slot("ay")
#         # cdb= tracker.get_slot("cdb")
#         # rel= tracker.get_slot("rel")
#         dispatcher.utter_message(text=f"OK! Your child's Name is {slot_value}.")
#         return {"Child's name:": slot_value}
#         # return {"Information:": ["par","sch","fnm","phone","mail","ct","cn","gr","ay","cdb","rel"]}
    


# class ActionSubmit(Action):
#         def name(self) -> Text:
#             return "action_submit"
#         async def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#             msg="Please provide us with your First Name & Last Name"
#             # par= tracker.get_slot("par")
#             # sch= tracker.get_slot("sch")
#             fnm= tracker.get_slot("fnm")
#             # phone= tracker.get_slot("phone")
#             # mail= tracker.get_slot("mail")
#             # ct = tracker.get_slot("ct")
#             cn= tracker.get_slot("cn")
#             # gr= tracker.get_slot("gr")
#             # ay= tracker.get_slot("ay")
#             # cdb= tracker.get_slot("cdb")
#             # rel= tracker.get_slot("rel")
            
#             dispatcher.utter_message("Thanks for the valuable information.")
#             return()
# class ValidateRestaurantForm(Action):
#     def name(self) -> Text:
#         return "validate_personal_info_form"

#     def validate_info(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate info."""
#         required_slots=["ct","cn","gr", "mail", "ay", "cdb", "rel", "fnm", "sch", "par", "phone"]

    # async def extract_outdoor_seating(
    #     self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    # ) -> Dict[Text, Any]:
    #     text_of_last_user_message = tracker.latest_message.get("text")
    #     sit_outside = "outdoor" in text_of_last_user_message

    #     return {"outdoor_seating": sit_outside}


# class ActionSayShirtSize(Action):

#     def name(self) -> Text:
#         return "user_form"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         required_slots=["ct","cn","gr", "mail", "ay", "cdb", "rel", "fnm", "sch", "par", "phone"]
#         X = tracker.get_slot(required_slots)
#         if not X:
#             dispatcher.utter_message(text="I don't understand this value.")
#         else:
#             dispatcher.utter_message(X)
#         return []



#         def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#            return {
#        "fname": [
#            self.from_entity(entity="fname", role="parent"),
#        ],
#        "cname": [
#            self.from_entity(entity="fname", role="child"),
#        ]
#    }