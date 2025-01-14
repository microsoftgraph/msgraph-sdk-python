from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .allowed_value import AllowedValue
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomSecurityAttributeDefinition(Entity, Parsable):
    # Values that are predefined for this custom security attribute. This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.
    allowed_values: Optional[list[AllowedValue]] = None
    # Name of the attribute set. Case insensitive.
    attribute_set: Optional[str] = None
    # Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.
    description: Optional[str] = None
    # Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.
    is_collection: Optional[bool] = None
    # Indicates whether custom security attribute values are indexed for searching on objects that are assigned attribute values. Cannot be changed later.
    is_searchable: Optional[bool] = None
    # Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether the custom security attribute is active or deactivated. Acceptable values are: Available and Deprecated. Can be changed later.
    status: Optional[str] = None
    # Data type for the custom security attribute values. Supported types are: Boolean, Integer, and String. Cannot be changed later.
    type: Optional[str] = None
    # Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.
    use_pre_defined_values_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomSecurityAttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomSecurityAttributeDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomSecurityAttributeDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .allowed_value import AllowedValue
        from .entity import Entity

        from .allowed_value import AllowedValue
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allowedValues": lambda n : setattr(self, 'allowed_values', n.get_collection_of_object_values(AllowedValue)),
            "attributeSet": lambda n : setattr(self, 'attribute_set', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "isCollection": lambda n : setattr(self, 'is_collection', n.get_bool_value()),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "usePreDefinedValuesOnly": lambda n : setattr(self, 'use_pre_defined_values_only', n.get_bool_value()),
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
        writer.write_collection_of_object_values("allowedValues", self.allowed_values)
        writer.write_str_value("attributeSet", self.attribute_set)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isCollection", self.is_collection)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_str_value("name", self.name)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
        writer.write_bool_value("usePreDefinedValuesOnly", self.use_pre_defined_values_only)
    

