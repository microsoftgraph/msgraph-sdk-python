from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_in_method import CheckInMethod

@dataclass
class CheckInClaim(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The unique identifier for an Outlook calendar event associated with the checkInClaim object. For more information, see the iCalUId property in event.
    calendar_event_id: Optional[str] = None
    # The checkInMethod property
    check_in_method: Optional[CheckInMethod] = None
    # The date and time when the checkInClaim object was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckInClaim:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckInClaim
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckInClaim()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_in_method import CheckInMethod

        from .check_in_method import CheckInMethod

        fields: dict[str, Callable[[Any], None]] = {
            "calendarEventId": lambda n : setattr(self, 'calendar_event_id', n.get_str_value()),
            "checkInMethod": lambda n : setattr(self, 'check_in_method', n.get_enum_value(CheckInMethod)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("calendarEventId", self.calendar_event_id)
        writer.write_enum_value("checkInMethod", self.check_in_method)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

