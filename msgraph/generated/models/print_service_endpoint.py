from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PrintServiceEndpoint(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new printServiceEndpoint and sets the default values.
        """
        super().__init__()
        # A human-readable display name for the endpoint.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The URI that can be used to access the service.
        self._uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintServiceEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintServiceEndpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintServiceEndpoint()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. A human-readable display name for the endpoint.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. A human-readable display name for the endpoint.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("uri", self.uri)
    
    @property
    def uri(self,) -> Optional[str]:
        """
        Gets the uri property value. The URI that can be used to access the service.
        Returns: Optional[str]
        """
        return self._uri
    
    @uri.setter
    def uri(self,value: Optional[str] = None) -> None:
        """
        Sets the uri property value. The URI that can be used to access the service.
        Args:
            value: Value to set for the uri property.
        """
        self._uri = value
    

