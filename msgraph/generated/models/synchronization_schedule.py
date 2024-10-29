from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_schedule_state import SynchronizationScheduleState

@dataclass
class SynchronizationSchedule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Date and time when this job expires. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration: Optional[datetime.datetime] = None
    # The interval between synchronization iterations. The value is represented in ISO 8601  format for durations. For example, P1M represents a period of one month and PT1M represents a period of one minute.
    interval: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[SynchronizationScheduleState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_schedule_state import SynchronizationScheduleState

        from .synchronization_schedule_state import SynchronizationScheduleState

        fields: Dict[str, Callable[[Any], None]] = {
            "expiration": lambda n : setattr(self, 'expiration', n.get_datetime_value()),
            "interval": lambda n : setattr(self, 'interval', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SynchronizationScheduleState)),
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
        from .synchronization_schedule_state import SynchronizationScheduleState

        writer.write_datetime_value("expiration", self.expiration)
        writer.write_timedelta_value("interval", self.interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

