from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_customer_information_base import BookingCustomerInformationBase
    from .booking_question_answer import BookingQuestionAnswer
    from .location import Location

from .booking_customer_information_base import BookingCustomerInformationBase

@dataclass
class BookingCustomerInformation(BookingCustomerInformationBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.bookingCustomerInformation"
    # It consists of the list of custom questions and answers given by the customer as part of the appointment
    custom_question_answers: Optional[list[BookingQuestionAnswer]] = None
    # The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
    customer_id: Optional[str] = None
    # The SMTP address of the bookingCustomer who is booking the appointment
    email_address: Optional[str] = None
    # Represents location information for the bookingCustomer who is booking the appointment.
    location: Optional[Location] = None
    # The customer's name.
    name: Optional[str] = None
    # Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
    notes: Optional[str] = None
    # The customer's phone number.
    phone: Optional[str] = None
    # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
    time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingCustomerInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomerInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingCustomerInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_customer_information_base import BookingCustomerInformationBase
        from .booking_question_answer import BookingQuestionAnswer
        from .location import Location

        from .booking_customer_information_base import BookingCustomerInformationBase
        from .booking_question_answer import BookingQuestionAnswer
        from .location import Location

        fields: dict[str, Callable[[Any], None]] = {
            "customQuestionAnswers": lambda n : setattr(self, 'custom_question_answers', n.get_collection_of_object_values(BookingQuestionAnswer)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(Location)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("customQuestionAnswers", self.custom_question_answers)
        writer.write_str_value("customerId", self.customer_id)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_object_value("location", self.location)
        writer.write_str_value("name", self.name)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("timeZone", self.time_zone)
    

