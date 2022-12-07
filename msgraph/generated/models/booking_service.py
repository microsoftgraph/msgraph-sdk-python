from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_price_type = lazy_import('msgraph.generated.models.booking_price_type')
booking_question_assignment = lazy_import('msgraph.generated.models.booking_question_assignment')
booking_reminder = lazy_import('msgraph.generated.models.booking_reminder')
booking_scheduling_policy = lazy_import('msgraph.generated.models.booking_scheduling_policy')
entity = lazy_import('msgraph.generated.models.entity')
location = lazy_import('msgraph.generated.models.location')

class BookingService(entity.Entity):
    """
    Represents a particular service offered by a booking business.
    """
    @property
    def additional_information(self,) -> Optional[str]:
        """
        Gets the additionalInformation property value. Additional information that is sent to the customer when an appointment is confirmed.
        Returns: Optional[str]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInformation property value. Additional information that is sent to the customer when an appointment is confirmed.
        Args:
            value: Value to set for the additionalInformation property.
        """
        self._additional_information = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingService and sets the default values.
        """
        super().__init__()
        # Additional information that is sent to the customer when an appointment is confirmed.
        self._additional_information: Optional[str] = None
        # Contains the set of custom questions associated with a particular service.
        self._custom_questions: Optional[List[booking_question_assignment.BookingQuestionAssignment]] = None
        # The default length of the service, represented in numbers of days, hours, minutes, and seconds. For example, P11D23H59M59.999999999999S.
        self._default_duration: Optional[Timedelta] = None
        # The default physical location for the service.
        self._default_location: Optional[location.Location] = None
        # The default monetary price for the service.
        self._default_price: Optional[float] = None
        # Represents the type of pricing of a booking service.
        self._default_price_type: Optional[booking_price_type.BookingPriceType] = None
        # The default set of reminders for an appointment of this service. The value of this property is available only when reading this bookingService by its ID.
        self._default_reminders: Optional[List[booking_reminder.BookingReminder]] = None
        # A text description for the service.
        self._description: Optional[str] = None
        # A service name.
        self._display_name: Optional[str] = None
        # The isAnonymousJoinEnabled property
        self._is_anonymous_join_enabled: Optional[bool] = None
        # True means this service is not available to customers for booking.
        self._is_hidden_from_customers: Optional[bool] = None
        # True indicates that the appointments for the service will be held online. Default value is false.
        self._is_location_online: Optional[bool] = None
        # The languageTag property
        self._language_tag: Optional[str] = None
        # The maximum number of customers allowed in a service. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
        self._maximum_attendees_count: Optional[int] = None
        # Additional information about this service.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The time to buffer after an appointment for this service ends, and before the next customer appointment can be booked.
        self._post_buffer: Optional[Timedelta] = None
        # The time to buffer before an appointment for this service can start.
        self._pre_buffer: Optional[Timedelta] = None
        # The set of policies that determine how appointments for this type of service should be created and managed.
        self._scheduling_policy: Optional[booking_scheduling_policy.BookingSchedulingPolicy] = None
        # True indicates SMS notifications can be sent to the customers for the appointment of the service. Default value is false.
        self._sms_notifications_enabled: Optional[bool] = None
        # Represents those staff members who provide this service.
        self._staff_member_ids: Optional[List[str]] = None
        # The URL a customer uses to access the service.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingService
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingService()
    
    @property
    def custom_questions(self,) -> Optional[List[booking_question_assignment.BookingQuestionAssignment]]:
        """
        Gets the customQuestions property value. Contains the set of custom questions associated with a particular service.
        Returns: Optional[List[booking_question_assignment.BookingQuestionAssignment]]
        """
        return self._custom_questions
    
    @custom_questions.setter
    def custom_questions(self,value: Optional[List[booking_question_assignment.BookingQuestionAssignment]] = None) -> None:
        """
        Sets the customQuestions property value. Contains the set of custom questions associated with a particular service.
        Args:
            value: Value to set for the customQuestions property.
        """
        self._custom_questions = value
    
    @property
    def default_duration(self,) -> Optional[Timedelta]:
        """
        Gets the defaultDuration property value. The default length of the service, represented in numbers of days, hours, minutes, and seconds. For example, P11D23H59M59.999999999999S.
        Returns: Optional[Timedelta]
        """
        return self._default_duration
    
    @default_duration.setter
    def default_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the defaultDuration property value. The default length of the service, represented in numbers of days, hours, minutes, and seconds. For example, P11D23H59M59.999999999999S.
        Args:
            value: Value to set for the defaultDuration property.
        """
        self._default_duration = value
    
    @property
    def default_location(self,) -> Optional[location.Location]:
        """
        Gets the defaultLocation property value. The default physical location for the service.
        Returns: Optional[location.Location]
        """
        return self._default_location
    
    @default_location.setter
    def default_location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the defaultLocation property value. The default physical location for the service.
        Args:
            value: Value to set for the defaultLocation property.
        """
        self._default_location = value
    
    @property
    def default_price(self,) -> Optional[float]:
        """
        Gets the defaultPrice property value. The default monetary price for the service.
        Returns: Optional[float]
        """
        return self._default_price
    
    @default_price.setter
    def default_price(self,value: Optional[float] = None) -> None:
        """
        Sets the defaultPrice property value. The default monetary price for the service.
        Args:
            value: Value to set for the defaultPrice property.
        """
        self._default_price = value
    
    @property
    def default_price_type(self,) -> Optional[booking_price_type.BookingPriceType]:
        """
        Gets the defaultPriceType property value. Represents the type of pricing of a booking service.
        Returns: Optional[booking_price_type.BookingPriceType]
        """
        return self._default_price_type
    
    @default_price_type.setter
    def default_price_type(self,value: Optional[booking_price_type.BookingPriceType] = None) -> None:
        """
        Sets the defaultPriceType property value. Represents the type of pricing of a booking service.
        Args:
            value: Value to set for the defaultPriceType property.
        """
        self._default_price_type = value
    
    @property
    def default_reminders(self,) -> Optional[List[booking_reminder.BookingReminder]]:
        """
        Gets the defaultReminders property value. The default set of reminders for an appointment of this service. The value of this property is available only when reading this bookingService by its ID.
        Returns: Optional[List[booking_reminder.BookingReminder]]
        """
        return self._default_reminders
    
    @default_reminders.setter
    def default_reminders(self,value: Optional[List[booking_reminder.BookingReminder]] = None) -> None:
        """
        Sets the defaultReminders property value. The default set of reminders for an appointment of this service. The value of this property is available only when reading this bookingService by its ID.
        Args:
            value: Value to set for the defaultReminders property.
        """
        self._default_reminders = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A text description for the service.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A text description for the service.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. A service name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. A service name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_information": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "custom_questions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(booking_question_assignment.BookingQuestionAssignment)),
            "default_duration": lambda n : setattr(self, 'default_duration', n.get_object_value(Timedelta)),
            "default_location": lambda n : setattr(self, 'default_location', n.get_object_value(location.Location)),
            "default_price": lambda n : setattr(self, 'default_price', n.get_float_value()),
            "default_price_type": lambda n : setattr(self, 'default_price_type', n.get_enum_value(booking_price_type.BookingPriceType)),
            "default_reminders": lambda n : setattr(self, 'default_reminders', n.get_collection_of_object_values(booking_reminder.BookingReminder)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_anonymous_join_enabled": lambda n : setattr(self, 'is_anonymous_join_enabled', n.get_bool_value()),
            "is_hidden_from_customers": lambda n : setattr(self, 'is_hidden_from_customers', n.get_bool_value()),
            "is_location_online": lambda n : setattr(self, 'is_location_online', n.get_bool_value()),
            "language_tag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "maximum_attendees_count": lambda n : setattr(self, 'maximum_attendees_count', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "post_buffer": lambda n : setattr(self, 'post_buffer', n.get_object_value(Timedelta)),
            "pre_buffer": lambda n : setattr(self, 'pre_buffer', n.get_object_value(Timedelta)),
            "scheduling_policy": lambda n : setattr(self, 'scheduling_policy', n.get_object_value(booking_scheduling_policy.BookingSchedulingPolicy)),
            "sms_notifications_enabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "staff_member_ids": lambda n : setattr(self, 'staff_member_ids', n.get_collection_of_primitive_values(str)),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_anonymous_join_enabled(self,) -> Optional[bool]:
        """
        Gets the isAnonymousJoinEnabled property value. The isAnonymousJoinEnabled property
        Returns: Optional[bool]
        """
        return self._is_anonymous_join_enabled
    
    @is_anonymous_join_enabled.setter
    def is_anonymous_join_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAnonymousJoinEnabled property value. The isAnonymousJoinEnabled property
        Args:
            value: Value to set for the isAnonymousJoinEnabled property.
        """
        self._is_anonymous_join_enabled = value
    
    @property
    def is_hidden_from_customers(self,) -> Optional[bool]:
        """
        Gets the isHiddenFromCustomers property value. True means this service is not available to customers for booking.
        Returns: Optional[bool]
        """
        return self._is_hidden_from_customers
    
    @is_hidden_from_customers.setter
    def is_hidden_from_customers(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHiddenFromCustomers property value. True means this service is not available to customers for booking.
        Args:
            value: Value to set for the isHiddenFromCustomers property.
        """
        self._is_hidden_from_customers = value
    
    @property
    def is_location_online(self,) -> Optional[bool]:
        """
        Gets the isLocationOnline property value. True indicates that the appointments for the service will be held online. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_location_online
    
    @is_location_online.setter
    def is_location_online(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLocationOnline property value. True indicates that the appointments for the service will be held online. Default value is false.
        Args:
            value: Value to set for the isLocationOnline property.
        """
        self._is_location_online = value
    
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
    def maximum_attendees_count(self,) -> Optional[int]:
        """
        Gets the maximumAttendeesCount property value. The maximum number of customers allowed in a service. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
        Returns: Optional[int]
        """
        return self._maximum_attendees_count
    
    @maximum_attendees_count.setter
    def maximum_attendees_count(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumAttendeesCount property value. The maximum number of customers allowed in a service. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
        Args:
            value: Value to set for the maximumAttendeesCount property.
        """
        self._maximum_attendees_count = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Additional information about this service.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Additional information about this service.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def post_buffer(self,) -> Optional[Timedelta]:
        """
        Gets the postBuffer property value. The time to buffer after an appointment for this service ends, and before the next customer appointment can be booked.
        Returns: Optional[Timedelta]
        """
        return self._post_buffer
    
    @post_buffer.setter
    def post_buffer(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the postBuffer property value. The time to buffer after an appointment for this service ends, and before the next customer appointment can be booked.
        Args:
            value: Value to set for the postBuffer property.
        """
        self._post_buffer = value
    
    @property
    def pre_buffer(self,) -> Optional[Timedelta]:
        """
        Gets the preBuffer property value. The time to buffer before an appointment for this service can start.
        Returns: Optional[Timedelta]
        """
        return self._pre_buffer
    
    @pre_buffer.setter
    def pre_buffer(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the preBuffer property value. The time to buffer before an appointment for this service can start.
        Args:
            value: Value to set for the preBuffer property.
        """
        self._pre_buffer = value
    
    @property
    def scheduling_policy(self,) -> Optional[booking_scheduling_policy.BookingSchedulingPolicy]:
        """
        Gets the schedulingPolicy property value. The set of policies that determine how appointments for this type of service should be created and managed.
        Returns: Optional[booking_scheduling_policy.BookingSchedulingPolicy]
        """
        return self._scheduling_policy
    
    @scheduling_policy.setter
    def scheduling_policy(self,value: Optional[booking_scheduling_policy.BookingSchedulingPolicy] = None) -> None:
        """
        Sets the schedulingPolicy property value. The set of policies that determine how appointments for this type of service should be created and managed.
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
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_collection_of_object_values("customQuestions", self.custom_questions)
        writer.write_object_value("defaultDuration", self.default_duration)
        writer.write_object_value("defaultLocation", self.default_location)
        writer.write_float_value("defaultPrice", self.default_price)
        writer.write_enum_value("defaultPriceType", self.default_price_type)
        writer.write_collection_of_object_values("defaultReminders", self.default_reminders)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAnonymousJoinEnabled", self.is_anonymous_join_enabled)
        writer.write_bool_value("isHiddenFromCustomers", self.is_hidden_from_customers)
        writer.write_bool_value("isLocationOnline", self.is_location_online)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_int_value("maximumAttendeesCount", self.maximum_attendees_count)
        writer.write_str_value("notes", self.notes)
        writer.write_object_value("postBuffer", self.post_buffer)
        writer.write_object_value("preBuffer", self.pre_buffer)
        writer.write_object_value("schedulingPolicy", self.scheduling_policy)
        writer.write_bool_value("smsNotificationsEnabled", self.sms_notifications_enabled)
        writer.write_collection_of_primitive_values("staffMemberIds", self.staff_member_ids)
    
    @property
    def sms_notifications_enabled(self,) -> Optional[bool]:
        """
        Gets the smsNotificationsEnabled property value. True indicates SMS notifications can be sent to the customers for the appointment of the service. Default value is false.
        Returns: Optional[bool]
        """
        return self._sms_notifications_enabled
    
    @sms_notifications_enabled.setter
    def sms_notifications_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smsNotificationsEnabled property value. True indicates SMS notifications can be sent to the customers for the appointment of the service. Default value is false.
        Args:
            value: Value to set for the smsNotificationsEnabled property.
        """
        self._sms_notifications_enabled = value
    
    @property
    def staff_member_ids(self,) -> Optional[List[str]]:
        """
        Gets the staffMemberIds property value. Represents those staff members who provide this service.
        Returns: Optional[List[str]]
        """
        return self._staff_member_ids
    
    @staff_member_ids.setter
    def staff_member_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the staffMemberIds property value. Represents those staff members who provide this service.
        Args:
            value: Value to set for the staffMemberIds property.
        """
        self._staff_member_ids = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The URL a customer uses to access the service.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The URL a customer uses to access the service.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

