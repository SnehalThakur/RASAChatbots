# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import utils.SQLiteDB as dbloader

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
        buttons = [
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
        dispatcher.utter_button_template("utter_patient_options", buttons, tracker)
        return []


# class FindPetoCareOptions(Action):
#     """ This action class allows to display buttons for patient signup and signin options """
#
#     def name(self) -> Text:
#         """Unique identifier of the action"""
#         return "find_patient_options"
#
#     def run(
#             self,
#             dispatcher: "CollectingDispatcher",
#             tracker: Tracker,
#             domain: "DomainDict") -> List[Dict[Text, Any]]:
#         buttons = [
#             {'payload': '/patient_signup{"content_type":"patient_signup"}', 'title': 'Patient Signup'},
#             {'payload': '/patient_signin{"content_type":"patient_signin"}', 'title': 'Patient Signin'}
#         ]
#
#         # TODO: update rasa core version for configurable `button_type`
#         dispatcher.utter_button_template("Patient Login Options",buttons, tracker)
#         return []


class FindNGOOptions(Action):
    """
    This action class allows to display buttons for doctor signup and signin options"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "find_ngo_options"

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
        dispatcher.utter_button_template("utter_ngo_options", buttons, tracker)
        return []


# class ValidateRegistrationForm(Action):
#     """ This action class allows to validate registration form"""
#
#     def name(self) -> Text:
#         return "user_details_form"
#
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["name", "number","address","email"]
#
#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]
#
#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]
#
#
# class ActionSubmit(Action):
#     """ This action class allows to display buttons for patient signup and signin options"""
#
#     def name(self) -> Text:
#         return "action_user_submit"
#
#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_user_details_thanks",
#                                  Name=tracker.get_slot("name"),
#                                  Mobile_number=tracker.get_slot("number"),
#                                  Address=tracker.get_slot("address"),
#                                  Email=tracker.get_slot("email")
#                                  # ,RegistrationNumber=tracker.get_slot("registration_number")
#                                  )


class ActionResetAllSlots(Action):
    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class SaveDoctorData(Action):
    """ This action class allows to save Doctor's data"""

    def name(self) -> Text:
        return "save_doctor_data"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        number = tracker.get_slot("number")
        address = tracker.get_slot("address")
        email = tracker.get_slot("email")
        medicalRegistrationNumber = tracker.get_slot("medical_registration_number")
        password = tracker.get_slot("password")
        dbloader.insertDoctorData(name, number, address, email, medicalRegistrationNumber, password)
        dispatcher.utter_message(text="Thanks for your registration. {}".format(name))
        print("Doctor Registration Data Saved to DB")
        return ["Thanks for your registration. {}".format(name)]


class SavePatientsData(Action):
    """ This action class allows to save Doctor's data"""

    def name(self) -> Text:
        return "save_patient_data"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        number = tracker.get_slot("number")
        address = tracker.get_slot("address")
        email = tracker.get_slot("email")
        password = tracker.get_slot("password")
        dbloader.insertPatientData(name, number, address, email, password)
        dispatcher.utter_message(text="Thanks for your registration. {}".format(name))
        print("Patient Registration Data Saved to DB")
        return ["Thanks for your registration. {}".format(name)]


class RetrieveDoctorData(Action):
    """ This action class allows to retrieve Doctor's data"""

    def name(self) -> Text:
        return "retrieve_doctor_data"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        doctorData = dbloader.retrieveDoctorDataWithEmail(email)
        print("doctorData =", doctorData)
        if doctorData.count()<1:
            dispatcher.utter_message(text="Doctor, you are not registered. Kindly Register to PetoCare.")
            return ["Doctor, you are not registered. Kindly Register to PetoCare."]
        else:
            dispatcher.utter_message(text="Welcome Doctor! How can I help you?")
            return ["Welcome Doctor! How can I help you?"]


class RetrievePatientsData(Action):
    """ This action class allows to retrieve Patient's data"""

    def name(self) -> Text:
        return "retrieve_patient_data"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        patientData = dbloader.retrievePatientDataWithEmail(email)
        print("patientData =", patientData)
        if patientData.count() < 1:
            dispatcher.utter_message(text="You are not registered. Kindly Register to PetoCare.")
            return ["You are not registered. Kindly Register to PetoCare."]
        else:
            dispatcher.utter_message(text="Welcome Doctor! How can I help you?")
            return ["Welcome. How can I help you?"]


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
