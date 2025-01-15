from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_price_type import BookingPriceType
    from .booking_question_assignment import BookingQuestionAssignment
    from .booking_reminder import BookingReminder
    from .booking_scheduling_policy import BookingSchedulingPolicy
    from .entity import Entity
    from .location import Location

from .entity import Entity

@dataclass
class BookingService(Entity, Parsable):
    """
    Represents a particular service offered by a booking business.
    """
    # Additional information that is sent to the customer when an appointment is confirmed.
    additional_information: Optional[str] = None
    # The date, time, and time zone when the service was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Contains the set of custom questions associated with a particular service.
    custom_questions: Optional[list[BookingQuestionAssignment]] = None
    # The default length of the service, represented in numbers of days, hours, minutes, and seconds. For example, P11D23H59M59.999999999999S.
    default_duration: Optional[datetime.timedelta] = None
    # The default physical location for the service.
    default_location: Optional[Location] = None
    # The default monetary price for the service.
    default_price: Optional[float] = None
    # Represents the type of pricing of a booking service.
    default_price_type: Optional[BookingPriceType] = None
    # The default set of reminders for an appointment of this service. The value of this property is available only when reading this bookingService by its ID.
    default_reminders: Optional[list[BookingReminder]] = None
    # A text description for the service.
    description: Optional[str] = None
    # A service name.
    display_name: Optional[str] = None
    # Indicates if an anonymousJoinWebUrl(webrtcUrl) is generated for the appointment booked for this service. The default value is false.
    is_anonymous_join_enabled: Optional[bool] = None
    # Indicates that the customer can manage bookings created by the staff. The default value is false.
    is_customer_allowed_to_manage_booking: Optional[bool] = None
    # True indicates that this service isn't available to customers for booking.
    is_hidden_from_customers: Optional[bool] = None
    # Indicates that the appointments for the service are held online. The default value is false.
    is_location_online: Optional[bool] = None
    # The language of the self-service booking page.
    language_tag: Optional[str] = None
    # The date, time, and time zone when the service was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The maximum number of customers allowed in a service. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
    maximum_attendees_count: Optional[int] = None
    # Additional information about this service.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time to buffer after an appointment for this service ends, and before the next customer appointment can be booked.
    post_buffer: Optional[datetime.timedelta] = None
    # The time to buffer before an appointment for this service can start.
    pre_buffer: Optional[datetime.timedelta] = None
    # The set of policies that determine how appointments for this type of service should be created and managed.
    scheduling_policy: Optional[BookingSchedulingPolicy] = None
    # True indicates SMS notifications can be sent to the customers for the appointment of the service. Default value is false.
    sms_notifications_enabled: Optional[bool] = None
    # Represents those staff members who provide this service.
    staff_member_ids: Optional[list[str]] = None
    # The URL a customer uses to access the service.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingService
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingService()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_price_type import BookingPriceType
        from .booking_question_assignment import BookingQuestionAssignment
        from .booking_reminder import BookingReminder
        from .booking_scheduling_policy import BookingSchedulingPolicy
        from .entity import Entity
        from .location import Location

        from .booking_price_type import BookingPriceType
        from .booking_question_assignment import BookingQuestionAssignment
        from .booking_reminder import BookingReminder
        from .booking_scheduling_policy import BookingSchedulingPolicy
        from .entity import Entity
        from .location import Location

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customQuestions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(BookingQuestionAssignment)),
            "defaultDuration": lambda n : setattr(self, 'default_duration', n.get_timedelta_value()),
            "defaultLocation": lambda n : setattr(self, 'default_location', n.get_object_value(Location)),
            "defaultPrice": lambda n : setattr(self, 'default_price', n.get_float_value()),
            "defaultPriceType": lambda n : setattr(self, 'default_price_type', n.get_enum_value(BookingPriceType)),
            "defaultReminders": lambda n : setattr(self, 'default_reminders', n.get_collection_of_object_values(BookingReminder)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAnonymousJoinEnabled": lambda n : setattr(self, 'is_anonymous_join_enabled', n.get_bool_value()),
            "isCustomerAllowedToManageBooking": lambda n : setattr(self, 'is_customer_allowed_to_manage_booking', n.get_bool_value()),
            "isHiddenFromCustomers": lambda n : setattr(self, 'is_hidden_from_customers', n.get_bool_value()),
            "isLocationOnline": lambda n : setattr(self, 'is_location_online', n.get_bool_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "maximumAttendeesCount": lambda n : setattr(self, 'maximum_attendees_count', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "postBuffer": lambda n : setattr(self, 'post_buffer', n.get_timedelta_value()),
            "preBuffer": lambda n : setattr(self, 'pre_buffer', n.get_timedelta_value()),
            "schedulingPolicy": lambda n : setattr(self, 'scheduling_policy', n.get_object_value(BookingSchedulingPolicy)),
            "smsNotificationsEnabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "staffMemberIds": lambda n : setattr(self, 'staff_member_ids', n.get_collection_of_primitive_values(str)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customQuestions", self.custom_questions)
        writer.write_timedelta_value("defaultDuration", self.default_duration)
        writer.write_object_value("defaultLocation", self.default_location)
        writer.write_float_value("defaultPrice", self.default_price)
        writer.write_enum_value("defaultPriceType", self.default_price_type)
        writer.write_collection_of_object_values("defaultReminders", self.default_reminders)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAnonymousJoinEnabled", self.is_anonymous_join_enabled)
        writer.write_bool_value("isCustomerAllowedToManageBooking", self.is_customer_allowed_to_manage_booking)
        writer.write_bool_value("isHiddenFromCustomers", self.is_hidden_from_customers)
        writer.write_bool_value("isLocationOnline", self.is_location_online)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("maximumAttendeesCount", self.maximum_attendees_count)
        writer.write_str_value("notes", self.notes)
        writer.write_timedelta_value("postBuffer", self.post_buffer)
        writer.write_timedelta_value("preBuffer", self.pre_buffer)
        writer.write_object_value("schedulingPolicy", self.scheduling_policy)
        writer.write_bool_value("smsNotificationsEnabled", self.sms_notifications_enabled)
        writer.write_collection_of_primitive_values("staffMemberIds", self.staff_member_ids)
    

