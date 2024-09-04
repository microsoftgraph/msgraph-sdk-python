from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .client_platform import ClientPlatform
    from .product_family import ProductFamily
    from .user_agent import UserAgent

from .user_agent import UserAgent

@dataclass
class ClientUserAgent(UserAgent):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.callRecords.clientUserAgent"
    # The unique identifier of the Microsoft Entra application used by this endpoint.
    azure_a_d_app_id: Optional[str] = None
    # Immutable resource identifier of the Azure Communication Service associated with this endpoint based on Communication Services APIs.
    communication_service_id: Optional[str] = None
    # The platform property
    platform: Optional[ClientPlatform] = None
    # The productFamily property
    product_family: Optional[ProductFamily] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClientUserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClientUserAgent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClientUserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .client_platform import ClientPlatform
        from .product_family import ProductFamily
        from .user_agent import UserAgent

        from .client_platform import ClientPlatform
        from .product_family import ProductFamily
        from .user_agent import UserAgent

        fields: Dict[str, Callable[[Any], None]] = {
            "azureADAppId": lambda n : setattr(self, 'azure_a_d_app_id', n.get_str_value()),
            "communicationServiceId": lambda n : setattr(self, 'communication_service_id', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(ClientPlatform)),
            "productFamily": lambda n : setattr(self, 'product_family', n.get_enum_value(ProductFamily)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("azureADAppId", self.azure_a_d_app_id)
        writer.write_str_value("communicationServiceId", self.communication_service_id)
        writer.write_enum_value("platform", self.platform)
        writer.write_enum_value("productFamily", self.product_family)
    

