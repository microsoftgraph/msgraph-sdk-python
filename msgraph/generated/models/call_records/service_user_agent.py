from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .service_role import ServiceRole
    from .user_agent import UserAgent

from .user_agent import UserAgent

@dataclass
class ServiceUserAgent(UserAgent):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.callRecords.serviceUserAgent"
    # The role property
    role: Optional[ServiceRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceUserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceUserAgent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceUserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .service_role import ServiceRole
        from .user_agent import UserAgent

        from .service_role import ServiceRole
        from .user_agent import UserAgent

        fields: Dict[str, Callable[[Any], None]] = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(ServiceRole)),
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
        writer.write_enum_value("role", self.role)
    

