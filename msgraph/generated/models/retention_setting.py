from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RetentionSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The backup frequency, expressed as an ISO 8601 repeating interval. The service defines the backup intervals: R/PT10M for 10-minute copies and R/P1W for weekly copies. Use R/P1W when specifying the policy retention period in a create or update request.
    interval: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The period of time to retain the protected data for a single Microsoft 365 service, expressed as an ISO 8601 duration. The supported policy retention periods in create and update requests are: P90D, P180D, P365D, P730D, P1095D, P1460D, P1825D, P2190D, P2555D, P2920D, P3285D, and P3650D. Other policy retention periods aren't supported.
    period: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "interval": lambda n : setattr(self, 'interval', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "period": lambda n : setattr(self, 'period', n.get_timedelta_value()),
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
        writer.write_str_value("interval", self.interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_timedelta_value("period", self.period)
        writer.write_additional_data_value(self.additional_data)
    

