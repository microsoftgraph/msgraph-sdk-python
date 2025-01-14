from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_customer_information_base import BookingCustomerInformationBase
    from .booking_price_type import BookingPriceType
    from .booking_reminder import BookingReminder
    from .date_time_time_zone import DateTimeTimeZone
    from .entity import Entity
    from .location import Location

from .entity import Entity

@dataclass
class BookingAppointment(Entity, Parsable):
    """
    Represents a booked appointment of a service by a customer in a business.
    """
    # Additional information that is sent to the customer when an appointment is confirmed.
    additional_information: Optional[str] = None
    # The URL of the meeting to join anonymously.
    anonymous_join_web_url: Optional[str] = None
    # The custom label that can be stamped on this appointment by users.
    appointment_label: Optional[str] = None
    # The date, time, and time zone when the appointment was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The SMTP address of the bookingCustomer who books the appointment.
    customer_email_address: Optional[str] = None
    # The customer's name.
    customer_name: Optional[str] = None
    # Notes from the customer associated with this appointment. You can get the value only when you read this bookingAppointment by its ID. You can set this property only when you initially create an appointment with a new customer.
    customer_notes: Optional[str] = None
    # The customer's phone number.
    customer_phone: Optional[str] = None
    # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
    customer_time_zone: Optional[str] = None
    # A collection of customer properties for an appointment. An appointment contains a list of customer information and each unit will indicate the properties of a customer who is part of that appointment. Optional.
    customers: Optional[list[BookingCustomerInformationBase]] = None
    # The length of the appointment, denoted in ISO8601 format.
    duration: Optional[datetime.timedelta] = None
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The current number of customers in the appointment.
    filled_attendees_count: Optional[int] = None
    # Indicates that the customer can manage bookings created by the staff. The default value is false.
    is_customer_allowed_to_manage_booking: Optional[bool] = None
    # Indicates that the appointment is held online. The default value is false.
    is_location_online: Optional[bool] = None
    # The URL of the online meeting for the appointment.
    join_web_url: Optional[str] = None
    # The date, time, and time zone when the booking business was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The maximum number of customers allowed in an appointment. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
    maximum_attendees_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If true indicates that the bookingCustomer for this appointment doesn't wish to receive a confirmation for this appointment.
    opt_out_of_customer_email: Optional[bool] = None
    # The amount of time to reserve after the appointment ends, for cleaning up, as an example. The value is expressed in ISO8601 format.
    post_buffer: Optional[datetime.timedelta] = None
    # The amount of time to reserve before the appointment begins, for preparation, as an example. The value is expressed in ISO8601 format.
    pre_buffer: Optional[datetime.timedelta] = None
    # The regular price for an appointment for the specified bookingService.
    price: Optional[float] = None
    # Represents the type of pricing of a booking service.
    price_type: Optional[BookingPriceType] = None
    # The collection of customer reminders sent for this appointment. The value of this property is available only when reading this bookingAppointment by its ID.
    reminders: Optional[list[BookingReminder]] = None
    # Another tracking ID for the appointment, if the appointment was created directly by the customer on the scheduling page, as opposed to by a staff member on behalf of the customer.
    self_service_appointment_id: Optional[str] = None
    # The ID of the bookingService associated with this appointment.
    service_id: Optional[str] = None
    # The location where the service is delivered.
    service_location: Optional[Location] = None
    # The name of the bookingService associated with this appointment.This property is optional when creating a new appointment. If not specified, it's computed from the service associated with the appointment by the serviceId property.
    service_name: Optional[str] = None
    # Notes from a bookingStaffMember. The value of this property is available only when reading this bookingAppointment by its ID.
    service_notes: Optional[str] = None
    # If true, indicates SMS notifications will be sent to the customers for the appointment. Default value is false.
    sms_notifications_enabled: Optional[bool] = None
    # The ID of each bookingStaffMember who is scheduled in this appointment.
    staff_member_ids: Optional[list[str]] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingAppointment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingAppointment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingAppointment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_customer_information_base import BookingCustomerInformationBase
        from .booking_price_type import BookingPriceType
        from .booking_reminder import BookingReminder
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .location import Location

        from .booking_customer_information_base import BookingCustomerInformationBase
        from .booking_price_type import BookingPriceType
        from .booking_reminder import BookingReminder
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .location import Location

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "anonymousJoinWebUrl": lambda n : setattr(self, 'anonymous_join_web_url', n.get_str_value()),
            "appointmentLabel": lambda n : setattr(self, 'appointment_label', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customerEmailAddress": lambda n : setattr(self, 'customer_email_address', n.get_str_value()),
            "customerName": lambda n : setattr(self, 'customer_name', n.get_str_value()),
            "customerNotes": lambda n : setattr(self, 'customer_notes', n.get_str_value()),
            "customerPhone": lambda n : setattr(self, 'customer_phone', n.get_str_value()),
            "customerTimeZone": lambda n : setattr(self, 'customer_time_zone', n.get_str_value()),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(BookingCustomerInformationBase)),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "filledAttendeesCount": lambda n : setattr(self, 'filled_attendees_count', n.get_int_value()),
            "isCustomerAllowedToManageBooking": lambda n : setattr(self, 'is_customer_allowed_to_manage_booking', n.get_bool_value()),
            "isLocationOnline": lambda n : setattr(self, 'is_location_online', n.get_bool_value()),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "maximumAttendeesCount": lambda n : setattr(self, 'maximum_attendees_count', n.get_int_value()),
            "optOutOfCustomerEmail": lambda n : setattr(self, 'opt_out_of_customer_email', n.get_bool_value()),
            "postBuffer": lambda n : setattr(self, 'post_buffer', n.get_timedelta_value()),
            "preBuffer": lambda n : setattr(self, 'pre_buffer', n.get_timedelta_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "priceType": lambda n : setattr(self, 'price_type', n.get_enum_value(BookingPriceType)),
            "reminders": lambda n : setattr(self, 'reminders', n.get_collection_of_object_values(BookingReminder)),
            "selfServiceAppointmentId": lambda n : setattr(self, 'self_service_appointment_id', n.get_str_value()),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "serviceLocation": lambda n : setattr(self, 'service_location', n.get_object_value(Location)),
            "serviceName": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "serviceNotes": lambda n : setattr(self, 'service_notes', n.get_str_value()),
            "smsNotificationsEnabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "staffMemberIds": lambda n : setattr(self, 'staff_member_ids', n.get_collection_of_primitive_values(str)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
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
        writer.write_str_value("anonymousJoinWebUrl", self.anonymous_join_web_url)
        writer.write_str_value("appointmentLabel", self.appointment_label)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("customerEmailAddress", self.customer_email_address)
        writer.write_str_value("customerName", self.customer_name)
        writer.write_str_value("customerNotes", self.customer_notes)
        writer.write_str_value("customerPhone", self.customer_phone)
        writer.write_str_value("customerTimeZone", self.customer_time_zone)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_bool_value("isCustomerAllowedToManageBooking", self.is_customer_allowed_to_manage_booking)
        writer.write_bool_value("isLocationOnline", self.is_location_online)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_int_value("maximumAttendeesCount", self.maximum_attendees_count)
        writer.write_bool_value("optOutOfCustomerEmail", self.opt_out_of_customer_email)
        writer.write_timedelta_value("postBuffer", self.post_buffer)
        writer.write_timedelta_value("preBuffer", self.pre_buffer)
        writer.write_float_value("price", self.price)
        writer.write_enum_value("priceType", self.price_type)
        writer.write_collection_of_object_values("reminders", self.reminders)
        writer.write_str_value("selfServiceAppointmentId", self.self_service_appointment_id)
        writer.write_str_value("serviceId", self.service_id)
        writer.write_object_value("serviceLocation", self.service_location)
        writer.write_str_value("serviceName", self.service_name)
        writer.write_str_value("serviceNotes", self.service_notes)
        writer.write_bool_value("smsNotificationsEnabled", self.sms_notifications_enabled)
        writer.write_collection_of_primitive_values("staffMemberIds", self.staff_member_ids)
        writer.write_object_value("startDateTime", self.start_date_time)
    

