from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

client_platform = lazy_import('msgraph.generated.models.call_records.client_platform')
product_family = lazy_import('msgraph.generated.models.call_records.product_family')
user_agent = lazy_import('msgraph.generated.models.call_records.user_agent')

class ClientUserAgent(user_agent.UserAgent):
    @property
    def azure_a_d_app_id(self,) -> Optional[str]:
        """
        Gets the azureADAppId property value. The unique identifier of the Azure AD application used by this endpoint.
        Returns: Optional[str]
        """
        return self._azure_a_d_app_id
    
    @azure_a_d_app_id.setter
    def azure_a_d_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureADAppId property value. The unique identifier of the Azure AD application used by this endpoint.
        Args:
            value: Value to set for the azureADAppId property.
        """
        self._azure_a_d_app_id = value
    
    @property
    def communication_service_id(self,) -> Optional[str]:
        """
        Gets the communicationServiceId property value. Immutable resource identifier of the Azure Communication Service associated with this endpoint based on Communication Services APIs.
        Returns: Optional[str]
        """
        return self._communication_service_id
    
    @communication_service_id.setter
    def communication_service_id(self,value: Optional[str] = None) -> None:
        """
        Sets the communicationServiceId property value. Immutable resource identifier of the Azure Communication Service associated with this endpoint based on Communication Services APIs.
        Args:
            value: Value to set for the communicationServiceId property.
        """
        self._communication_service_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ClientUserAgent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callRecords.clientUserAgent"
        # The unique identifier of the Azure AD application used by this endpoint.
        self._azure_a_d_app_id: Optional[str] = None
        # Immutable resource identifier of the Azure Communication Service associated with this endpoint based on Communication Services APIs.
        self._communication_service_id: Optional[str] = None
        # The platform property
        self._platform: Optional[client_platform.ClientPlatform] = None
        # The productFamily property
        self._product_family: Optional[product_family.ProductFamily] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClientUserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClientUserAgent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClientUserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_a_d_app_id": lambda n : setattr(self, 'azure_a_d_app_id', n.get_str_value()),
            "communication_service_id": lambda n : setattr(self, 'communication_service_id', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(client_platform.ClientPlatform)),
            "product_family": lambda n : setattr(self, 'product_family', n.get_enum_value(product_family.ProductFamily)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def platform(self,) -> Optional[client_platform.ClientPlatform]:
        """
        Gets the platform property value. The platform property
        Returns: Optional[client_platform.ClientPlatform]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[client_platform.ClientPlatform] = None) -> None:
        """
        Sets the platform property value. The platform property
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def product_family(self,) -> Optional[product_family.ProductFamily]:
        """
        Gets the productFamily property value. The productFamily property
        Returns: Optional[product_family.ProductFamily]
        """
        return self._product_family
    
    @product_family.setter
    def product_family(self,value: Optional[product_family.ProductFamily] = None) -> None:
        """
        Sets the productFamily property value. The productFamily property
        Args:
            value: Value to set for the productFamily property.
        """
        self._product_family = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("azureADAppId", self.azure_a_d_app_id)
        writer.write_str_value("communicationServiceId", self.communication_service_id)
        writer.write_enum_value("platform", self.platform)
        writer.write_enum_value("productFamily", self.product_family)
    

