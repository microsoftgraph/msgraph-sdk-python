from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_appointment = lazy_import('msgraph.generated.models.booking_appointment')
booking_custom_question = lazy_import('msgraph.generated.models.booking_custom_question')
booking_customer_base = lazy_import('msgraph.generated.models.booking_customer_base')
booking_scheduling_policy = lazy_import('msgraph.generated.models.booking_scheduling_policy')
booking_service = lazy_import('msgraph.generated.models.booking_service')
booking_staff_member_base = lazy_import('msgraph.generated.models.booking_staff_member_base')
booking_work_hours = lazy_import('msgraph.generated.models.booking_work_hours')
entity = lazy_import('msgraph.generated.models.entity')
physical_address = lazy_import('msgraph.generated.models.physical_address')

class BookingBusiness(entity.Entity):
    """
    Represents a Microsot Bookings Business.
    """
    @property
    def address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the address property value. The street address of the business. The address property, together with phone and webSiteUrl, appear in the footer of a business scheduling page. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the address property value. The street address of the business. The address property, together with phone and webSiteUrl, appear in the footer of a business scheduling page. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    @property
    def appointments(self,) -> Optional[List[booking_appointment.BookingAppointment]]:
        """
        Gets the appointments property value. All the appointments of this business. Read-only. Nullable.
        Returns: Optional[List[booking_appointment.BookingAppointment]]
        """
        return self._appointments
    
    @appointments.setter
    def appointments(self,value: Optional[List[booking_appointment.BookingAppointment]] = None) -> None:
        """
        Sets the appointments property value. All the appointments of this business. Read-only. Nullable.
        Args:
            value: Value to set for the appointments property.
        """
        self._appointments = value
    
    @property
    def business_hours(self,) -> Optional[List[booking_work_hours.BookingWorkHours]]:
        """
        Gets the businessHours property value. The hours of operation for the business.
        Returns: Optional[List[booking_work_hours.BookingWorkHours]]
        """
        return self._business_hours
    
    @business_hours.setter
    def business_hours(self,value: Optional[List[booking_work_hours.BookingWorkHours]] = None) -> None:
        """
        Sets the businessHours property value. The hours of operation for the business.
        Args:
            value: Value to set for the businessHours property.
        """
        self._business_hours = value
    
    @property
    def business_type(self,) -> Optional[str]:
        """
        Gets the businessType property value. The type of business.
        Returns: Optional[str]
        """
        return self._business_type
    
    @business_type.setter
    def business_type(self,value: Optional[str] = None) -> None:
        """
        Sets the businessType property value. The type of business.
        Args:
            value: Value to set for the businessType property.
        """
        self._business_type = value
    
    @property
    def calendar_view(self,) -> Optional[List[booking_appointment.BookingAppointment]]:
        """
        Gets the calendarView property value. The set of appointments of this business in a specified date range. Read-only. Nullable.
        Returns: Optional[List[booking_appointment.BookingAppointment]]
        """
        return self._calendar_view
    
    @calendar_view.setter
    def calendar_view(self,value: Optional[List[booking_appointment.BookingAppointment]] = None) -> None:
        """
        Sets the calendarView property value. The set of appointments of this business in a specified date range. Read-only. Nullable.
        Args:
            value: Value to set for the calendarView property.
        """
        self._calendar_view = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingBusiness and sets the default values.
        """
        super().__init__()
        # The street address of the business. The address property, together with phone and webSiteUrl, appear in the footer of a business scheduling page. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
        self._address: Optional[physical_address.PhysicalAddress] = None
        # All the appointments of this business. Read-only. Nullable.
        self._appointments: Optional[List[booking_appointment.BookingAppointment]] = None
        # The hours of operation for the business.
        self._business_hours: Optional[List[booking_work_hours.BookingWorkHours]] = None
        # The type of business.
        self._business_type: Optional[str] = None
        # The set of appointments of this business in a specified date range. Read-only. Nullable.
        self._calendar_view: Optional[List[booking_appointment.BookingAppointment]] = None
        # All the customers of this business. Read-only. Nullable.
        self._customers: Optional[List[booking_customer_base.BookingCustomerBase]] = None
        # All the custom questions of this business. Read-only. Nullable.
        self._custom_questions: Optional[List[booking_custom_question.BookingCustomQuestion]] = None
        # The code for the currency that the business operates in on Microsoft Bookings.
        self._default_currency_iso: Optional[str] = None
        # The name of the business, which interfaces with customers. This name appears at the top of the business scheduling page.
        self._display_name: Optional[str] = None
        # The email address for the business.
        self._email: Optional[str] = None
        # The scheduling page has been made available to external customers. Use the publish and unpublish actions to set this property. Read-only.
        self._is_published: Optional[bool] = None
        # The languageTag property
        self._language_tag: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The telephone number for the business. The phone property, together with address and webSiteUrl, appear in the footer of a business scheduling page.
        self._phone: Optional[str] = None
        # The URL for the scheduling page, which is set after you publish or unpublish the page. Read-only.
        self._public_url: Optional[str] = None
        # Specifies how bookings can be created for this business.
        self._scheduling_policy: Optional[booking_scheduling_policy.BookingSchedulingPolicy] = None
        # All the services offered by this business. Read-only. Nullable.
        self._services: Optional[List[booking_service.BookingService]] = None
        # All the staff members that provide services in this business. Read-only. Nullable.
        self._staff_members: Optional[List[booking_staff_member_base.BookingStaffMemberBase]] = None
        # The URL of the business web site. The webSiteUrl property, together with address, phone, appear in the footer of a business scheduling page.
        self._web_site_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingBusiness:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingBusiness
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingBusiness()
    
    @property
    def customers(self,) -> Optional[List[booking_customer_base.BookingCustomerBase]]:
        """
        Gets the customers property value. All the customers of this business. Read-only. Nullable.
        Returns: Optional[List[booking_customer_base.BookingCustomerBase]]
        """
        return self._customers
    
    @customers.setter
    def customers(self,value: Optional[List[booking_customer_base.BookingCustomerBase]] = None) -> None:
        """
        Sets the customers property value. All the customers of this business. Read-only. Nullable.
        Args:
            value: Value to set for the customers property.
        """
        self._customers = value
    
    @property
    def custom_questions(self,) -> Optional[List[booking_custom_question.BookingCustomQuestion]]:
        """
        Gets the customQuestions property value. All the custom questions of this business. Read-only. Nullable.
        Returns: Optional[List[booking_custom_question.BookingCustomQuestion]]
        """
        return self._custom_questions
    
    @custom_questions.setter
    def custom_questions(self,value: Optional[List[booking_custom_question.BookingCustomQuestion]] = None) -> None:
        """
        Sets the customQuestions property value. All the custom questions of this business. Read-only. Nullable.
        Args:
            value: Value to set for the customQuestions property.
        """
        self._custom_questions = value
    
    @property
    def default_currency_iso(self,) -> Optional[str]:
        """
        Gets the defaultCurrencyIso property value. The code for the currency that the business operates in on Microsoft Bookings.
        Returns: Optional[str]
        """
        return self._default_currency_iso
    
    @default_currency_iso.setter
    def default_currency_iso(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultCurrencyIso property value. The code for the currency that the business operates in on Microsoft Bookings.
        Args:
            value: Value to set for the defaultCurrencyIso property.
        """
        self._default_currency_iso = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the business, which interfaces with customers. This name appears at the top of the business scheduling page.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the business, which interfaces with customers. This name appears at the top of the business scheduling page.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address for the business.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address for the business.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "appointments": lambda n : setattr(self, 'appointments', n.get_collection_of_object_values(booking_appointment.BookingAppointment)),
            "business_hours": lambda n : setattr(self, 'business_hours', n.get_collection_of_object_values(booking_work_hours.BookingWorkHours)),
            "business_type": lambda n : setattr(self, 'business_type', n.get_str_value()),
            "calendar_view": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(booking_appointment.BookingAppointment)),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(booking_customer_base.BookingCustomerBase)),
            "custom_questions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(booking_custom_question.BookingCustomQuestion)),
            "default_currency_iso": lambda n : setattr(self, 'default_currency_iso', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "is_published": lambda n : setattr(self, 'is_published', n.get_bool_value()),
            "language_tag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "public_url": lambda n : setattr(self, 'public_url', n.get_str_value()),
            "scheduling_policy": lambda n : setattr(self, 'scheduling_policy', n.get_object_value(booking_scheduling_policy.BookingSchedulingPolicy)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(booking_service.BookingService)),
            "staff_members": lambda n : setattr(self, 'staff_members', n.get_collection_of_object_values(booking_staff_member_base.BookingStaffMemberBase)),
            "web_site_url": lambda n : setattr(self, 'web_site_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_published(self,) -> Optional[bool]:
        """
        Gets the isPublished property value. The scheduling page has been made available to external customers. Use the publish and unpublish actions to set this property. Read-only.
        Returns: Optional[bool]
        """
        return self._is_published
    
    @is_published.setter
    def is_published(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPublished property value. The scheduling page has been made available to external customers. Use the publish and unpublish actions to set this property. Read-only.
        Args:
            value: Value to set for the isPublished property.
        """
        self._is_published = value
    
    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. The languageTag property
        Returns: Optional[str]
        """
        return self._language_tag
    
    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. The languageTag property
        Args:
            value: Value to set for the languageTag property.
        """
        self._language_tag = value
    
    @property
    def phone(self,) -> Optional[str]:
        """
        Gets the phone property value. The telephone number for the business. The phone property, together with address and webSiteUrl, appear in the footer of a business scheduling page.
        Returns: Optional[str]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[str] = None) -> None:
        """
        Sets the phone property value. The telephone number for the business. The phone property, together with address and webSiteUrl, appear in the footer of a business scheduling page.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    @property
    def public_url(self,) -> Optional[str]:
        """
        Gets the publicUrl property value. The URL for the scheduling page, which is set after you publish or unpublish the page. Read-only.
        Returns: Optional[str]
        """
        return self._public_url
    
    @public_url.setter
    def public_url(self,value: Optional[str] = None) -> None:
        """
        Sets the publicUrl property value. The URL for the scheduling page, which is set after you publish or unpublish the page. Read-only.
        Args:
            value: Value to set for the publicUrl property.
        """
        self._public_url = value
    
    @property
    def scheduling_policy(self,) -> Optional[booking_scheduling_policy.BookingSchedulingPolicy]:
        """
        Gets the schedulingPolicy property value. Specifies how bookings can be created for this business.
        Returns: Optional[booking_scheduling_policy.BookingSchedulingPolicy]
        """
        return self._scheduling_policy
    
    @scheduling_policy.setter
    def scheduling_policy(self,value: Optional[booking_scheduling_policy.BookingSchedulingPolicy] = None) -> None:
        """
        Sets the schedulingPolicy property value. Specifies how bookings can be created for this business.
        Args:
            value: Value to set for the schedulingPolicy property.
        """
        self._scheduling_policy = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("address", self.address)
        writer.write_collection_of_object_values("appointments", self.appointments)
        writer.write_collection_of_object_values("businessHours", self.business_hours)
        writer.write_str_value("businessType", self.business_type)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_collection_of_object_values("customQuestions", self.custom_questions)
        writer.write_str_value("defaultCurrencyIso", self.default_currency_iso)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("phone", self.phone)
        writer.write_object_value("schedulingPolicy", self.scheduling_policy)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_collection_of_object_values("staffMembers", self.staff_members)
        writer.write_str_value("webSiteUrl", self.web_site_url)
    
    @property
    def services(self,) -> Optional[List[booking_service.BookingService]]:
        """
        Gets the services property value. All the services offered by this business. Read-only. Nullable.
        Returns: Optional[List[booking_service.BookingService]]
        """
        return self._services
    
    @services.setter
    def services(self,value: Optional[List[booking_service.BookingService]] = None) -> None:
        """
        Sets the services property value. All the services offered by this business. Read-only. Nullable.
        Args:
            value: Value to set for the services property.
        """
        self._services = value
    
    @property
    def staff_members(self,) -> Optional[List[booking_staff_member_base.BookingStaffMemberBase]]:
        """
        Gets the staffMembers property value. All the staff members that provide services in this business. Read-only. Nullable.
        Returns: Optional[List[booking_staff_member_base.BookingStaffMemberBase]]
        """
        return self._staff_members
    
    @staff_members.setter
    def staff_members(self,value: Optional[List[booking_staff_member_base.BookingStaffMemberBase]] = None) -> None:
        """
        Sets the staffMembers property value. All the staff members that provide services in this business. Read-only. Nullable.
        Args:
            value: Value to set for the staffMembers property.
        """
        self._staff_members = value
    
    @property
    def web_site_url(self,) -> Optional[str]:
        """
        Gets the webSiteUrl property value. The URL of the business web site. The webSiteUrl property, together with address, phone, appear in the footer of a business scheduling page.
        Returns: Optional[str]
        """
        return self._web_site_url
    
    @web_site_url.setter
    def web_site_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webSiteUrl property value. The URL of the business web site. The webSiteUrl property, together with address, phone, appear in the footer of a business scheduling page.
        Args:
            value: Value to set for the webSiteUrl property.
        """
        self._web_site_url = value
    

