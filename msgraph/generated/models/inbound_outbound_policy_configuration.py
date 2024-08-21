from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class InboundOutboundPolicyConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Defines whether external users coming inbound are allowed.
    inbound_allowed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines whether internal users are allowed to go outbound.
    outbound_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InboundOutboundPolicyConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InboundOutboundPolicyConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InboundOutboundPolicyConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "inboundAllowed": lambda n : setattr(self, 'inbound_allowed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outboundAllowed": lambda n : setattr(self, 'outbound_allowed', n.get_bool_value()),
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
        writer.write_bool_value("inboundAllowed", self.inbound_allowed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("outboundAllowed", self.outbound_allowed)
        writer.write_additional_data_value(self.additional_data)
    

