from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

service_role = lazy_import('msgraph.generated.models.call_records.service_role')
user_agent = lazy_import('msgraph.generated.models.call_records.user_agent')

class ServiceUserAgent(user_agent.UserAgent):
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceUserAgent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callRecords.serviceUserAgent"
        # The role property
        self._role: Optional[service_role.ServiceRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceUserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceUserAgent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceUserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(service_role.ServiceRole)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role(self,) -> Optional[service_role.ServiceRole]:
        """
        Gets the role property value. The role property
        Returns: Optional[service_role.ServiceRole]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[service_role.ServiceRole] = None) -> None:
        """
        Sets the role property value. The role property
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("role", self.role)
    

