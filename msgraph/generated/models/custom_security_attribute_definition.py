from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import allowed_value, entity

from . import entity

class CustomSecurityAttributeDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomSecurityAttributeDefinition and sets the default values.
        """
        super().__init__()
        # The allowedValues property
        self._allowed_values: Optional[List[allowed_value.AllowedValue]] = None
        # The attributeSet property
        self._attribute_set: Optional[str] = None
        # The description property
        self._description: Optional[str] = None
        # The isCollection property
        self._is_collection: Optional[bool] = None
        # The isSearchable property
        self._is_searchable: Optional[bool] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[str] = None
        # The type property
        self._type: Optional[str] = None
        # The usePreDefinedValuesOnly property
        self._use_pre_defined_values_only: Optional[bool] = None
    
    @property
    def allowed_values(self,) -> Optional[List[allowed_value.AllowedValue]]:
        """
        Gets the allowedValues property value. The allowedValues property
        Returns: Optional[List[allowed_value.AllowedValue]]
        """
        return self._allowed_values
    
    @allowed_values.setter
    def allowed_values(self,value: Optional[List[allowed_value.AllowedValue]] = None) -> None:
        """
        Sets the allowedValues property value. The allowedValues property
        Args:
            value: Value to set for the allowed_values property.
        """
        self._allowed_values = value
    
    @property
    def attribute_set(self,) -> Optional[str]:
        """
        Gets the attributeSet property value. The attributeSet property
        Returns: Optional[str]
        """
        return self._attribute_set
    
    @attribute_set.setter
    def attribute_set(self,value: Optional[str] = None) -> None:
        """
        Sets the attributeSet property value. The attributeSet property
        Args:
            value: Value to set for the attribute_set property.
        """
        self._attribute_set = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomSecurityAttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomSecurityAttributeDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomSecurityAttributeDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import allowed_value, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedValues": lambda n : setattr(self, 'allowed_values', n.get_collection_of_object_values(allowed_value.AllowedValue)),
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
    
    @property
    def is_collection(self,) -> Optional[bool]:
        """
        Gets the isCollection property value. The isCollection property
        Returns: Optional[bool]
        """
        return self._is_collection
    
    @is_collection.setter
    def is_collection(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCollection property value. The isCollection property
        Args:
            value: Value to set for the is_collection property.
        """
        self._is_collection = value
    
    @property
    def is_searchable(self,) -> Optional[bool]:
        """
        Gets the isSearchable property value. The isSearchable property
        Returns: Optional[bool]
        """
        return self._is_searchable
    
    @is_searchable.setter
    def is_searchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSearchable property value. The isSearchable property
        Args:
            value: Value to set for the is_searchable property.
        """
        self._is_searchable = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def use_pre_defined_values_only(self,) -> Optional[bool]:
        """
        Gets the usePreDefinedValuesOnly property value. The usePreDefinedValuesOnly property
        Returns: Optional[bool]
        """
        return self._use_pre_defined_values_only
    
    @use_pre_defined_values_only.setter
    def use_pre_defined_values_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the usePreDefinedValuesOnly property value. The usePreDefinedValuesOnly property
        Args:
            value: Value to set for the use_pre_defined_values_only property.
        """
        self._use_pre_defined_values_only = value
    

