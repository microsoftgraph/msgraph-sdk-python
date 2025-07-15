from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
    from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation
    from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
    from .virtual_event_session import VirtualEventSession

from .entity import Entity

@dataclass
class VirtualEventRegistration(Entity, Parsable):
    # Date and time when the registrant cancels their registration for the virtual event. Only appears when applicable. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    cancelation_date_time: Optional[datetime.datetime] = None
    # Email address of the registrant.
    email: Optional[str] = None
    # The external information for a virtual event registration.
    external_registration_information: Optional[VirtualEventExternalRegistrationInformation] = None
    # First name of the registrant.
    first_name: Optional[str] = None
    # Last name of the registrant.
    last_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The registrant's preferred language.
    preferred_language: Optional[str] = None
    # The registrant's time zone details.
    preferred_timezone: Optional[str] = None
    # Date and time when the registrant registers for the virtual event. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    registration_date_time: Optional[datetime.datetime] = None
    # The registrant's answer to the registration questions.
    registration_question_answers: Optional[list[VirtualEventRegistrationQuestionAnswer]] = None
    # Sessions for a registration.
    sessions: Optional[list[VirtualEventSession]] = None
    # Registration status of the registrant. Read-only. Possible values are registered, canceled, waitlisted, pendingApproval, rejectedByOrganizer, and unknownFutureValue.
    status: Optional[VirtualEventAttendeeRegistrationStatus] = None
    # The registrant's ID in Microsoft Entra ID. Only appears when the registrant is registered in Microsoft Entra ID.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
        from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation
        from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
        from .virtual_event_session import VirtualEventSession

        from .entity import Entity
        from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
        from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation
        from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
        from .virtual_event_session import VirtualEventSession

        fields: dict[str, Callable[[Any], None]] = {
            "cancelationDateTime": lambda n : setattr(self, 'cancelation_date_time', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalRegistrationInformation": lambda n : setattr(self, 'external_registration_information', n.get_object_value(VirtualEventExternalRegistrationInformation)),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "preferredTimezone": lambda n : setattr(self, 'preferred_timezone', n.get_str_value()),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "registrationQuestionAnswers": lambda n : setattr(self, 'registration_question_answers', n.get_collection_of_object_values(VirtualEventRegistrationQuestionAnswer)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(VirtualEventSession)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(VirtualEventAttendeeRegistrationStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_datetime_value("cancelationDateTime", self.cancelation_date_time)
        writer.write_str_value("email", self.email)
        writer.write_object_value("externalRegistrationInformation", self.external_registration_information)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_str_value("preferredTimezone", self.preferred_timezone)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_collection_of_object_values("registrationQuestionAnswers", self.registration_question_answers)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
    

