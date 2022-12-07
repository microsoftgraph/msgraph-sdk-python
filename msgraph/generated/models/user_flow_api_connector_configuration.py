from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_api_connector = lazy_import('msgraph.generated.models.identity_api_connector')

class UserFlowApiConnectorConfiguration(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userFlowApiConnectorConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The postAttributeCollection property
        self._post_attribute_collection: Optional[identity_api_connector.IdentityApiConnector] = None
        # The postFederationSignup property
        self._post_federation_signup: Optional[identity_api_connector.IdentityApiConnector] = None
    
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
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "post_attribute_collection": lambda n : setattr(self, 'post_attribute_collection', n.get_object_value(identity_api_connector.IdentityApiConnector)),
            "post_federation_signup": lambda n : setattr(self, 'post_federation_signup', n.get_object_value(identity_api_connector.IdentityApiConnector)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def post_attribute_collection(self,) -> Optional[identity_api_connector.IdentityApiConnector]:
        """
        Gets the postAttributeCollection property value. The postAttributeCollection property
        Returns: Optional[identity_api_connector.IdentityApiConnector]
        """
        return self._post_attribute_collection
    
    @post_attribute_collection.setter
    def post_attribute_collection(self,value: Optional[identity_api_connector.IdentityApiConnector] = None) -> None:
        """
        Sets the postAttributeCollection property value. The postAttributeCollection property
        Args:
            value: Value to set for the postAttributeCollection property.
        """
        self._post_attribute_collection = value
    
    @property
    def post_federation_signup(self,) -> Optional[identity_api_connector.IdentityApiConnector]:
        """
        Gets the postFederationSignup property value. The postFederationSignup property
        Returns: Optional[identity_api_connector.IdentityApiConnector]
        """
        return self._post_federation_signup
    
    @post_federation_signup.setter
    def post_federation_signup(self,value: Optional[identity_api_connector.IdentityApiConnector] = None) -> None:
        """
        Sets the postFederationSignup property value. The postFederationSignup property
        Args:
            value: Value to set for the postFederationSignup property.
        """
        self._post_federation_signup = value
    
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
    

