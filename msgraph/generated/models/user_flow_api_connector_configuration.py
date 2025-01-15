from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_api_connector import IdentityApiConnector

@dataclass
class UserFlowApiConnectorConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The postAttributeCollection property
    post_attribute_collection: Optional[IdentityApiConnector] = None
    # The postFederationSignup property
    post_federation_signup: Optional[IdentityApiConnector] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserFlowApiConnectorConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserFlowApiConnectorConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserFlowApiConnectorConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_api_connector import IdentityApiConnector

        from .identity_api_connector import IdentityApiConnector

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postAttributeCollection": lambda n : setattr(self, 'post_attribute_collection', n.get_object_value(IdentityApiConnector)),
            "postFederationSignup": lambda n : setattr(self, 'post_federation_signup', n.get_object_value(IdentityApiConnector)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("postAttributeCollection", self.post_attribute_collection)
        writer.write_object_value("postFederationSignup", self.post_federation_signup)
        writer.write_additional_data_value(self.additional_data)
    

