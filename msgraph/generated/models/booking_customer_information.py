from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_customer_information_base = lazy_import('msgraph.generated.models.booking_customer_information_base')
booking_question_answer = lazy_import('msgraph.generated.models.booking_question_answer')
location = lazy_import('msgraph.generated.models.location')

class BookingCustomerInformation(booking_customer_information_base.BookingCustomerInformationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new BookingCustomerInformation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.bookingCustomerInformation"
        # The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        self._customer_id: Optional[str] = None
        # It consists of the list of custom questions and answers given by the customer as part of the appointment
        self._custom_question_answers: Optional[List[booking_question_answer.BookingQuestionAnswer]] = None
        # The SMTP address of the bookingCustomer who is booking the appointment
        self._email_address: Optional[str] = None
        # Represents location information for the bookingCustomer who is booking the appointment.
        self._location: Optional[location.Location] = None
        # The customer's name.
        self._name: Optional[str] = None
        # Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
        self._notes: Optional[str] = None
        # The customer's phone number.
        self._phone: Optional[str] = None
        # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        self._time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCustomerInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomerInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingCustomerInformation()
    
    @property
    def customer_id(self,) -> Optional[str]:
        """
        Gets the customerId property value. The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        Returns: Optional[str]
        """
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customerId property value. The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        Args:
            value: Value to set for the customerId property.
        """
        self._customer_id = value
    
    @property
    def custom_question_answers(self,) -> Optional[List[booking_question_answer.BookingQuestionAnswer]]:
        """
        Gets the customQuestionAnswers property value. It consists of the list of custom questions and answers given by the customer as part of the appointment
        Returns: Optional[List[booking_question_answer.BookingQuestionAnswer]]
        """
        return self._custom_question_answers
    
    @custom_question_answers.setter
    def custom_question_answers(self,value: Optional[List[booking_question_answer.BookingQuestionAnswer]] = None) -> None:
        """
        Sets the customQuestionAnswers property value. It consists of the list of custom questions and answers given by the customer as part of the appointment
        Args:
            value: Value to set for the customQuestionAnswers property.
        """
        self._custom_question_answers = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The SMTP address of the bookingCustomer who is booking the appointment
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The SMTP address of the bookingCustomer who is booking the appointment
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "customer_id": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "custom_question_answers": lambda n : setattr(self, 'custom_question_answers', n.get_collection_of_object_values(booking_question_answer.BookingQuestionAnswer)),
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(location.Location)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def location(self,) -> Optional[location.Location]:
        """
        Gets the location property value. Represents location information for the bookingCustomer who is booking the appointment.
        Returns: Optional[location.Location]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the location property value. Represents location information for the bookingCustomer who is booking the appointment.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The customer's name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The customer's name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def phone(self,) -> Optional[str]:
        """
        Gets the phone property value. The customer's phone number.
        Returns: Optional[str]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[str] = None) -> None:
        """
        Sets the phone property value. The customer's phone number.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("customerId", self.customer_id)
        writer.write_collection_of_object_values("customQuestionAnswers", self.custom_question_answers)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_object_value("location", self.location)
        writer.write_str_value("name", self.name)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("timeZone", self.time_zone)
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    

