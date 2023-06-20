from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object

from . import directory_object

@dataclass
class Endpoint(directory_object.DirectoryObject):
    odata_type = "#microsoft.graph.endpoint"
    # The capability property
    capability: Optional[str] = None
    # The providerId property
    provider_id: Optional[str] = None
    # The providerName property
    provider_name: Optional[str] = None
    # The providerResourceId property
    provider_resource_id: Optional[str] = None
    # The uri property
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Endpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Endpoint
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Endpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object

        from . import directory_object

        fields: Dict[str, Callable[[Any], None]] = {
            "capability": lambda n : setattr(self, 'capability', n.get_str_value()),
            "providerId": lambda n : setattr(self, 'provider_id', n.get_str_value()),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "providerResourceId": lambda n : setattr(self, 'provider_resource_id', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("capability", self.capability)
        writer.write_str_value("providerId", self.provider_id)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_str_value("providerResourceId", self.provider_resource_id)
        writer.write_str_value("uri", self.uri)
    

