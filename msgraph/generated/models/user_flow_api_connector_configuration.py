from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_api_connector

@dataclass
class UserFlowApiConnectorConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The postAttributeCollection property
    post_attribute_collection: Optional[identity_api_connector.IdentityApiConnector] = None
    # The postFederationSignup property
    post_federation_signup: Optional[identity_api_connector.IdentityApiConnector] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserFlowApiConnectorConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserFlowApiConnectorConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserFlowApiConnectorConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_api_connector

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postAttributeCollection": lambda n : setattr(self, 'post_attribute_collection', n.get_object_value(identity_api_connector.IdentityApiConnector)),
            "postFederationSignup": lambda n : setattr(self, 'post_federation_signup', n.get_object_value(identity_api_connector.IdentityApiConnector)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("postAttributeCollection", self.post_attribute_collection)
        writer.write_object_value("postFederationSignup", self.post_federation_signup)
        writer.write_additional_data_value(self.additional_data)
    

