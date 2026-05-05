from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WebauthnPublicKeyCredentialDescriptor(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The id property
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The transports property
    transports: Optional[list[str]] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebauthnPublicKeyCredentialDescriptor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebauthnPublicKeyCredentialDescriptor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebauthnPublicKeyCredentialDescriptor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "transports": lambda n : setattr(self, 'transports', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("transports", self.transports)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

