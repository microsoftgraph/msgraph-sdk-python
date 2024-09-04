from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_member import ConversationMember

from .conversation_member import ConversationMember

@dataclass
class AzureCommunicationServicesUserConversationMember(ConversationMember):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.azureCommunicationServicesUserConversationMember"
    # Azure Communication Services ID of the user.
    azure_communication_services_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureCommunicationServicesUserConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureCommunicationServicesUserConversationMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureCommunicationServicesUserConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_member import ConversationMember

        from .conversation_member import ConversationMember

        fields: Dict[str, Callable[[Any], None]] = {
            "azureCommunicationServicesId": lambda n : setattr(self, 'azure_communication_services_id', n.get_str_value()),
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
        writer.write_str_value("azureCommunicationServicesId", self.azure_communication_services_id)
    

