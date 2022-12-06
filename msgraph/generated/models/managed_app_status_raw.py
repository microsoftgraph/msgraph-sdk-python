from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')
managed_app_status = lazy_import('msgraph.generated.models.managed_app_status')

class ManagedAppStatusRaw(managed_app_status.ManagedAppStatus):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedAppStatusRaw and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedAppStatusRaw"
        # Status report content.
        self._content: Optional[json.Json] = None
    
    @property
    def content(self,) -> Optional[json.Json]:
        """
        Gets the content property value. Status report content.
        Returns: Optional[json.Json]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the content property value. Status report content.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppStatusRaw:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppStatusRaw
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppStatusRaw()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(json.Json)),
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
        writer.write_object_value("content", self.content)
    

