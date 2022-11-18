# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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

FACILITY_TYPES = {
    "hospital":
        {
            "name": "hospital 👩‍⚕️",
            "resource": "rbry-mqwu"
        },
    "nursing_home":
        {
            "name": "pet home",
            "resource": "b27b-2uc7"
        },
    "home_health":
        {
            "name": "pet shop/agency",
            "resource": "9wzi-peqs"
        }
}


class FindFacilityTypes(Action):
    """
    This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_welcome_petocare_facility_types"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons=[
            {'payload': '/hospital{"content_type":"hospital"}', 'title': 'Hospital'},
            {'payload': '/ngo{"content_type":"ngo"}', 'title': 'NGO'}
            # ,{'payload': '/petshop{"content_type":"petshop"}', 'title': "Pet Shop (Service isn't available)"}
        ]
        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_welcome_bot", buttons, tracker)
        return []


class FindHospitalOptions(Action):
    """
    This action class allows to display buttons for doctor and patient option"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_hospital_options"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = [
            {'payload': '/doctor{"content_type":"doctor"}', 'title': 'Doctor'},
            {'payload': '/patient{"content_type":"patient"}', 'title': 'Patient'}
            # ,{'payload': '/petshop{"content_type":"petshop"}', 'title': "Pet Shop (Service isn't available)"}
        ]

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_hospital_options", buttons, tracker)
        return []


class FindDoctorOptions(Action):
    """
    This action class allows to display buttons for doctor signup and signin options"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_doctor_options"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = [
            {'payload': '/doctor_signup{"content_type":"doctor_signup"}', 'title': 'Doctor Signup'},
            {'payload': '/doctor_signin{"content_type":"doctor_signin"}', 'title': 'Doctor Signin'}
        ]

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_doctor_options", buttons, tracker)
        return []


class FindPatientOptions(Action):
    """
    This action class allows to display buttons for patient signup and signin options"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_patient_options"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = [
            {'payload': '/patient_signup{"content_type":"patient_signup"}', 'title': 'Patient Signup'},
            {'payload': '/patient_signin{"content_type":"patient_signin"}', 'title': 'Patient Signin'}
        ]

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_patient_options",buttons, tracker)
        return []


class FindNGOOptions(Action):
    """
    This action class allows to display buttons for doctor signup and signin options"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_doctor_options"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = [
            {'payload': '/ngo{"content_type":"ngo"}', 'title': 'NGO'},
            {'payload': '/petcare_user{"content_type":"petcare_user"}', 'title': 'Petcare User'}
        ]

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_ngo_options",buttons, tracker)
        return []


class FindPetoCareOptions(Action):
    """
    This action class allows to display buttons for patient signup and signin options"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_patient_options"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        buttons = [
            {'payload': '/patient_signup{"content_type":"patient_signup"}', 'title': 'Patient Signup'},
            {'payload': '/patient_signin{"content_type":"patient_signin"}', 'title': 'Patient Signin'}
        ]

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("Patient Login Options",buttons, tracker)
        return []



# class FindWelcomeFacilityTypes(Action):
#     """
#     This action class allows to display buttons for each facility type
#     for the user to chose from to fill the facility_type entity slot."""
#
#     def name(self) -> Text:
#         """Unique identifier of the action"""
#         return "find_facility_types"
#
#     def run(
#             self,
#             dispatcher: "CollectingDispatcher",
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         buttons = []
#         for t in FACILITY_TYPES:
#             facility_type = FACILITY_TYPES[t]
#             payload = "/inform{\"facility_type\": \"" + facility_type.get(
#                 "resource") + "\"}"
#
#             buttons.append(
#                 {"title": "{}".format(facility_type.get("name").title()),
#                  "payload": payload})
#
#         # TODO: update rasa core version for configurable `button_type`
#         dispatcher.utter_button_template("utter_welcome_bot", buttons, tracker)
#         return []
