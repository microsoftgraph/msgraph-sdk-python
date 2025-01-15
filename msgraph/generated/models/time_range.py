from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TimeRange(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # End time for the time range.
    end_time: Optional[datetime.time] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Start time for the time range.
    start_time: Optional[datetime.time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeRange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeRange()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "endTime": lambda n : setattr(self, 'end_time', n.get_time_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_time_value()),
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
        writer.write_time_value("endTime", self.end_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("startTime", self.start_time)
        writer.write_additional_data_value(self.additional_data)
    

