from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bookings_availability import BookingsAvailability
    from .bookings_availability_window import BookingsAvailabilityWindow

@dataclass
class BookingSchedulingPolicy(AdditionalDataHolder, BackedModel, Parsable):
    """
    This type represents the set of policies that dictate how bookings can be created in a Booking Calendar.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # True to allow customers to choose a specific person for the booking.
    allow_staff_selection: Optional[bool] = None
    # Custom availability of the service in a given time frame.
    custom_availabilities: Optional[list[BookingsAvailabilityWindow]] = None
    # General availability of the service defined by the scheduling policy.
    general_availability: Optional[BookingsAvailability] = None
    # Indicates whether the meeting invite is sent to the customers. The default value is false.
    is_meeting_invite_to_customers_enabled: Optional[bool] = None
    # Maximum number of days in advance that a booking can be made. It follows the ISO 8601 format.
    maximum_advance: Optional[datetime.timedelta] = None
    # The minimum amount of time before which bookings and cancellations must be made. It follows the ISO 8601 format.
    minimum_lead_time: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # True to notify the business via email when a booking is created or changed. Use the email address specified in the email property of the bookingBusiness entity for the business.
    send_confirmations_to_owner: Optional[bool] = None
    # Duration of each time slot, denoted in ISO 8601 format.
    time_slot_interval: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingSchedulingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingSchedulingPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingSchedulingPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bookings_availability import BookingsAvailability
        from .bookings_availability_window import BookingsAvailabilityWindow

        from .bookings_availability import BookingsAvailability
        from .bookings_availability_window import BookingsAvailabilityWindow

        fields: dict[str, Callable[[Any], None]] = {
            "allowStaffSelection": lambda n : setattr(self, 'allow_staff_selection', n.get_bool_value()),
            "customAvailabilities": lambda n : setattr(self, 'custom_availabilities', n.get_collection_of_object_values(BookingsAvailabilityWindow)),
            "generalAvailability": lambda n : setattr(self, 'general_availability', n.get_object_value(BookingsAvailability)),
            "isMeetingInviteToCustomersEnabled": lambda n : setattr(self, 'is_meeting_invite_to_customers_enabled', n.get_bool_value()),
            "maximumAdvance": lambda n : setattr(self, 'maximum_advance', n.get_timedelta_value()),
            "minimumLeadTime": lambda n : setattr(self, 'minimum_lead_time', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sendConfirmationsToOwner": lambda n : setattr(self, 'send_confirmations_to_owner', n.get_bool_value()),
            "timeSlotInterval": lambda n : setattr(self, 'time_slot_interval', n.get_timedelta_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allowStaffSelection", self.allow_staff_selection)
        writer.write_collection_of_object_values("customAvailabilities", self.custom_availabilities)
        writer.write_object_value("generalAvailability", self.general_availability)
        writer.write_bool_value("isMeetingInviteToCustomersEnabled", self.is_meeting_invite_to_customers_enabled)
        writer.write_timedelta_value("maximumAdvance", self.maximum_advance)
        writer.write_timedelta_value("minimumLeadTime", self.minimum_lead_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("sendConfirmationsToOwner", self.send_confirmations_to_owner)
        writer.write_timedelta_value("timeSlotInterval", self.time_slot_interval)
        writer.write_additional_data_value(self.additional_data)
    

