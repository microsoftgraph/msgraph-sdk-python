from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import client_user_agent, service_user_agent

@dataclass
class UserAgent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Identifies the version of application software used by this endpoint.
    application_version: Optional[str] = None
    # User-agent header value reported by this endpoint.
    header_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAgent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.clientUserAgent".casefold():
            from . import client_user_agent

            return client_user_agent.ClientUserAgent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.serviceUserAgent".casefold():
            from . import service_user_agent

            return service_user_agent.ServiceUserAgent()
        return UserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import client_user_agent, service_user_agent

        from . import client_user_agent, service_user_agent

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationVersion": lambda n : setattr(self, 'application_version', n.get_str_value()),
            "headerValue": lambda n : setattr(self, 'header_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("applicationVersion", self.application_version)
        writer.write_str_value("headerValue", self.header_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

