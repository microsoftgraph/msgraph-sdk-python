from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
property = lazy_import('msgraph.generated.models.external_connectors.property')

class Schema(entity.Entity):
    @property
    def base_type(self,) -> Optional[str]:
        """
        Gets the baseType property value. Must be set to microsoft.graph.externalConnector.externalItem. Required.
        Returns: Optional[str]
        """
        return self._base_type
    
    @base_type.setter
    def base_type(self,value: Optional[str] = None) -> None:
        """
        Sets the baseType property value. Must be set to microsoft.graph.externalConnector.externalItem. Required.
        Args:
            value: Value to set for the baseType property.
        """
        self._base_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new schema and sets the default values.
        """
        super().__init__()
        # Must be set to microsoft.graph.externalConnector.externalItem. Required.
        self._base_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The properties defined for the items in the connection. The minimum number of properties is one, the maximum is 128.
        self._properties: Optional[List[property.Property]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Schema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Schema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Schema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "base_type": lambda n : setattr(self, 'base_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(property.Property)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def properties(self,) -> Optional[List[property.Property]]:
        """
        Gets the properties property value. The properties defined for the items in the connection. The minimum number of properties is one, the maximum is 128.
        Returns: Optional[List[property.Property]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[property.Property]] = None) -> None:
        """
        Sets the properties property value. The properties defined for the items in the connection. The minimum number of properties is one, the maximum is 128.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("baseType", self.base_type)
        writer.write_collection_of_object_values("properties", self.properties)
    

