from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_attribute_collection_input_configuration import AuthenticationAttributeCollectionInputConfiguration

@dataclass
class AuthenticationAttributeCollectionPageViewConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The description of the page.
    description: Optional[str] = None
    # The display configuration of attributes being collected on the attribute collection page. You must specify all attributes that you want to retain, otherwise they're removed from the user flow.
    inputs: Optional[list[AuthenticationAttributeCollectionInputConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The title of the attribute collection page.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationAttributeCollectionPageViewConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAttributeCollectionPageViewConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationAttributeCollectionPageViewConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_attribute_collection_input_configuration import AuthenticationAttributeCollectionInputConfiguration

        from .authentication_attribute_collection_input_configuration import AuthenticationAttributeCollectionInputConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "inputs": lambda n : setattr(self, 'inputs', n.get_collection_of_object_values(AuthenticationAttributeCollectionInputConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("inputs", self.inputs)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

