from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .quarantine_reason import QuarantineReason
    from .synchronization_error import SynchronizationError

@dataclass
class SynchronizationQuarantine(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Date and time when the quarantine was last evaluated and imposed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    current_began: Optional[datetime.datetime] = None
    # Describes the error(s) that occurred when putting the synchronization job into quarantine.
    error: Optional[SynchronizationError] = None
    # Date and time when the next attempt to re-evaluate the quarantine will be made. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    next_attempt: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason property
    reason: Optional[QuarantineReason] = None
    # Date and time when the quarantine was first imposed in this series (a series starts when a quarantine is first imposed, and is reset as soon as the quarantine is lifted). The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    series_began: Optional[datetime.datetime] = None
    # Number of times in this series the quarantine was re-evaluated and left in effect (a series starts when quarantine is first imposed, and is reset as soon as quarantine is lifted).
    series_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationQuarantine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationQuarantine
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationQuarantine()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .quarantine_reason import QuarantineReason
        from .synchronization_error import SynchronizationError

        from .quarantine_reason import QuarantineReason
        from .synchronization_error import SynchronizationError

        fields: Dict[str, Callable[[Any], None]] = {
            "currentBegan": lambda n : setattr(self, 'current_began', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(SynchronizationError)),
            "nextAttempt": lambda n : setattr(self, 'next_attempt', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(QuarantineReason)),
            "seriesBegan": lambda n : setattr(self, 'series_began', n.get_datetime_value()),
            "seriesCount": lambda n : setattr(self, 'series_count', n.get_int_value()),
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
        writer.write_datetime_value("currentBegan", self.current_began)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("nextAttempt", self.next_attempt)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("reason", self.reason)
        writer.write_datetime_value("seriesBegan", self.series_began)
        writer.write_int_value("seriesCount", self.series_count)
        writer.write_additional_data_value(self.additional_data)
    

