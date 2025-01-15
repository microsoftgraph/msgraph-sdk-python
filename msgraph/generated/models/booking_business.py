from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_appointment import BookingAppointment
    from .booking_customer_base import BookingCustomerBase
    from .booking_custom_question import BookingCustomQuestion
    from .booking_page_settings import BookingPageSettings
    from .booking_scheduling_policy import BookingSchedulingPolicy
    from .booking_service import BookingService
    from .booking_staff_member_base import BookingStaffMemberBase
    from .booking_work_hours import BookingWorkHours
    from .entity import Entity
    from .physical_address import PhysicalAddress

from .entity import Entity

@dataclass
class BookingBusiness(Entity, Parsable):
    """
    Represents a Microsoft Bookings Business.
    """
    # The street address of the business. The address property, together with phone and webSiteUrl, appear in the footer of a business scheduling page. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
    address: Optional[PhysicalAddress] = None
    # All the appointments of this business. Read-only. Nullable.
    appointments: Optional[list[BookingAppointment]] = None
    # Settings for the published booking page.
    booking_page_settings: Optional[BookingPageSettings] = None
    # The hours of operation for the business.
    business_hours: Optional[list[BookingWorkHours]] = None
    # The type of business.
    business_type: Optional[str] = None
    # The set of appointments of this business in a specified date range. Read-only. Nullable.
    calendar_view: Optional[list[BookingAppointment]] = None
    # The date, time, and time zone when the booking business was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # All the custom questions of this business. Read-only. Nullable.
    custom_questions: Optional[list[BookingCustomQuestion]] = None
    # All the customers of this business. Read-only. Nullable.
    customers: Optional[list[BookingCustomerBase]] = None
    # The code for the currency that the business operates in on Microsoft Bookings.
    default_currency_iso: Optional[str] = None
    # The name of the business, which interfaces with customers. This name appears at the top of the business scheduling page.
    display_name: Optional[str] = None
    # The email address for the business.
    email: Optional[str] = None
    # The scheduling page has been made available to external customers. Use the publish and unpublish actions to set this property. Read-only.
    is_published: Optional[bool] = None
    # The language of the self-service booking page.
    language_tag: Optional[str] = None
    # The date, time, and time zone when the booking business was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The telephone number for the business. The phone property, together with address and webSiteUrl, appear in the footer of a business scheduling page.
    phone: Optional[str] = None
    # The URL for the scheduling page, which is set after you publish or unpublish the page. Read-only.
    public_url: Optional[str] = None
    # Specifies how bookings can be created for this business.
    scheduling_policy: Optional[BookingSchedulingPolicy] = None
    # All the services offered by this business. Read-only. Nullable.
    services: Optional[list[BookingService]] = None
    # All the staff members that provide services in this business. Read-only. Nullable.
    staff_members: Optional[list[BookingStaffMemberBase]] = None
    # The URL of the business web site. The webSiteUrl property, together with address, phone, appear in the footer of a business scheduling page.
    web_site_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingBusiness:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingBusiness
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingBusiness()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_appointment import BookingAppointment
        from .booking_customer_base import BookingCustomerBase
        from .booking_custom_question import BookingCustomQuestion
        from .booking_page_settings import BookingPageSettings
        from .booking_scheduling_policy import BookingSchedulingPolicy
        from .booking_service import BookingService
        from .booking_staff_member_base import BookingStaffMemberBase
        from .booking_work_hours import BookingWorkHours
        from .entity import Entity
        from .physical_address import PhysicalAddress

        from .booking_appointment import BookingAppointment
        from .booking_customer_base import BookingCustomerBase
        from .booking_custom_question import BookingCustomQuestion
        from .booking_page_settings import BookingPageSettings
        from .booking_scheduling_policy import BookingSchedulingPolicy
        from .booking_service import BookingService
        from .booking_staff_member_base import BookingStaffMemberBase
        from .booking_work_hours import BookingWorkHours
        from .entity import Entity
        from .physical_address import PhysicalAddress

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "appointments": lambda n : setattr(self, 'appointments', n.get_collection_of_object_values(BookingAppointment)),
            "bookingPageSettings": lambda n : setattr(self, 'booking_page_settings', n.get_object_value(BookingPageSettings)),
            "businessHours": lambda n : setattr(self, 'business_hours', n.get_collection_of_object_values(BookingWorkHours)),
            "businessType": lambda n : setattr(self, 'business_type', n.get_str_value()),
            "calendarView": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(BookingAppointment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customQuestions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(BookingCustomQuestion)),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(BookingCustomerBase)),
            "defaultCurrencyIso": lambda n : setattr(self, 'default_currency_iso', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "isPublished": lambda n : setattr(self, 'is_published', n.get_bool_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "publicUrl": lambda n : setattr(self, 'public_url', n.get_str_value()),
            "schedulingPolicy": lambda n : setattr(self, 'scheduling_policy', n.get_object_value(BookingSchedulingPolicy)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(BookingService)),
            "staffMembers": lambda n : setattr(self, 'staff_members', n.get_collection_of_object_values(BookingStaffMemberBase)),
            "webSiteUrl": lambda n : setattr(self, 'web_site_url', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_collection_of_object_values("appointments", self.appointments)
        writer.write_object_value("bookingPageSettings", self.booking_page_settings)
        writer.write_collection_of_object_values("businessHours", self.business_hours)
        writer.write_str_value("businessType", self.business_type)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customQuestions", self.custom_questions)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_str_value("defaultCurrencyIso", self.default_currency_iso)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("phone", self.phone)
        writer.write_object_value("schedulingPolicy", self.scheduling_policy)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_collection_of_object_values("staffMembers", self.staff_members)
        writer.write_str_value("webSiteUrl", self.web_site_url)
    

