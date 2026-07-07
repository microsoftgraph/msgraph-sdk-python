from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_action import DeliveryAction
    from .delivery_location import DeliveryLocation

@dataclass
class AnalyzedEmailDeliveryDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The delivery action of the email. The possible values are: unknown, deliveredToJunk, delivered, blocked, replaced, unknownFutureValue.
    action: Optional[DeliveryAction] = None
    # Latest known threat on the email.
    latest_threats: Optional[str] = None
    # The delivery location of the email. The possible values are: unknown, inboxfolder, junkFolder, deletedFolder, quarantine, onpremexternal, failed, dropped, others, unknownFutureValue.
    location: Optional[DeliveryLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Threats identified at the time of delivery.
    original_threats: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyzedEmailDeliveryDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailDeliveryDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailDeliveryDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_action import DeliveryAction
        from .delivery_location import DeliveryLocation

        from .delivery_action import DeliveryAction
        from .delivery_location import DeliveryLocation

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(DeliveryAction)),
            "latestThreats": lambda n : setattr(self, 'latest_threats', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_enum_value(DeliveryLocation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "originalThreats": lambda n : setattr(self, 'original_threats', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("latestThreats", self.latest_threats)
        writer.write_enum_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("originalThreats", self.original_threats)
        writer.write_additional_data_value(self.additional_data)
    

