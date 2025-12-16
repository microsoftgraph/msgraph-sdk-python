from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bookings_availability_status import BookingsAvailabilityStatus
    from .date_time_time_zone import DateTimeTimeZone

@dataclass
class AvailabilityItem(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the service ID for 1:n appointments. If the appointment is of type 1:n, this field is present, otherwise, null.
    service_id: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    # The status of the staff member. The possible values are: available, busy, slotsAvailable, outOfOffice, unknownFutureValue.
    status: Optional[BookingsAvailabilityStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AvailabilityItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AvailabilityItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AvailabilityItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bookings_availability_status import BookingsAvailabilityStatus
        from .date_time_time_zone import DateTimeTimeZone

        from .bookings_availability_status import BookingsAvailabilityStatus
        from .date_time_time_zone import DateTimeTimeZone

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BookingsAvailabilityStatus)),
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
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceId", self.service_id)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

