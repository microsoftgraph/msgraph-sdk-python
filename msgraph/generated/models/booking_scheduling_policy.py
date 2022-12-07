from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BookingSchedulingPolicy(AdditionalDataHolder, Parsable):
    """
    This type represents the set of policies that dictate how bookings can be created in a Booking Calendar.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allow_staff_selection(self,) -> Optional[bool]:
        """
        Gets the allowStaffSelection property value. True if to allow customers to choose a specific person for the booking.
        Returns: Optional[bool]
        """
        return self._allow_staff_selection
    
    @allow_staff_selection.setter
    def allow_staff_selection(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowStaffSelection property value. True if to allow customers to choose a specific person for the booking.
        Args:
            value: Value to set for the allowStaffSelection property.
        """
        self._allow_staff_selection = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingSchedulingPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # True if to allow customers to choose a specific person for the booking.
        self._allow_staff_selection: Optional[bool] = None
        # Maximum number of days in advance that a booking can be made. It follows the ISO 8601 format.
        self._maximum_advance: Optional[Timedelta] = None
        # The minimum amount of time before which bookings and cancellations must be made. It follows the ISO 8601 format.
        self._minimum_lead_time: Optional[Timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # True to notify the business via email when a booking is created or changed. Use the email address specified in the email property of the bookingBusiness entity for the business.
        self._send_confirmations_to_owner: Optional[bool] = None
        # Duration of each time slot, denoted in ISO 8601 format.
        self._time_slot_interval: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingSchedulingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingSchedulingPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingSchedulingPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_staff_selection": lambda n : setattr(self, 'allow_staff_selection', n.get_bool_value()),
            "maximum_advance": lambda n : setattr(self, 'maximum_advance', n.get_object_value(Timedelta)),
            "minimum_lead_time": lambda n : setattr(self, 'minimum_lead_time', n.get_object_value(Timedelta)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "send_confirmations_to_owner": lambda n : setattr(self, 'send_confirmations_to_owner', n.get_bool_value()),
            "time_slot_interval": lambda n : setattr(self, 'time_slot_interval', n.get_object_value(Timedelta)),
        }
        return fields
    
    @property
    def maximum_advance(self,) -> Optional[Timedelta]:
        """
        Gets the maximumAdvance property value. Maximum number of days in advance that a booking can be made. It follows the ISO 8601 format.
        Returns: Optional[Timedelta]
        """
        return self._maximum_advance
    
    @maximum_advance.setter
    def maximum_advance(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maximumAdvance property value. Maximum number of days in advance that a booking can be made. It follows the ISO 8601 format.
        Args:
            value: Value to set for the maximumAdvance property.
        """
        self._maximum_advance = value
    
    @property
    def minimum_lead_time(self,) -> Optional[Timedelta]:
        """
        Gets the minimumLeadTime property value. The minimum amount of time before which bookings and cancellations must be made. It follows the ISO 8601 format.
        Returns: Optional[Timedelta]
        """
        return self._minimum_lead_time
    
    @minimum_lead_time.setter
    def minimum_lead_time(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the minimumLeadTime property value. The minimum amount of time before which bookings and cancellations must be made. It follows the ISO 8601 format.
        Args:
            value: Value to set for the minimumLeadTime property.
        """
        self._minimum_lead_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def send_confirmations_to_owner(self,) -> Optional[bool]:
        """
        Gets the sendConfirmationsToOwner property value. True to notify the business via email when a booking is created or changed. Use the email address specified in the email property of the bookingBusiness entity for the business.
        Returns: Optional[bool]
        """
        return self._send_confirmations_to_owner
    
    @send_confirmations_to_owner.setter
    def send_confirmations_to_owner(self,value: Optional[bool] = None) -> None:
        """
        Sets the sendConfirmationsToOwner property value. True to notify the business via email when a booking is created or changed. Use the email address specified in the email property of the bookingBusiness entity for the business.
        Args:
            value: Value to set for the sendConfirmationsToOwner property.
        """
        self._send_confirmations_to_owner = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowStaffSelection", self.allow_staff_selection)
        writer.write_object_value("maximumAdvance", self.maximum_advance)
        writer.write_object_value("minimumLeadTime", self.minimum_lead_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("sendConfirmationsToOwner", self.send_confirmations_to_owner)
        writer.write_object_value("timeSlotInterval", self.time_slot_interval)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_slot_interval(self,) -> Optional[Timedelta]:
        """
        Gets the timeSlotInterval property value. Duration of each time slot, denoted in ISO 8601 format.
        Returns: Optional[Timedelta]
        """
        return self._time_slot_interval
    
    @time_slot_interval.setter
    def time_slot_interval(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the timeSlotInterval property value. Duration of each time slot, denoted in ISO 8601 format.
        Args:
            value: Value to set for the timeSlotInterval property.
        """
        self._time_slot_interval = value
    

