from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class AttributeSet(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new attributeSet and sets the default values.
        """
        super().__init__()
        # The description property
        self._description: Optional[str] = None
        # The maxAttributesPerSet property
        self._max_attributes_per_set: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeSet()
    
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
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "maxAttributesPerSet": lambda n : setattr(self, 'max_attributes_per_set', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_attributes_per_set(self,) -> Optional[int]:
        """
        Gets the maxAttributesPerSet property value. The maxAttributesPerSet property
        Returns: Optional[int]
        """
        return self._max_attributes_per_set
    
    @max_attributes_per_set.setter
    def max_attributes_per_set(self,value: Optional[int] = None) -> None:
        """
        Sets the maxAttributesPerSet property value. The maxAttributesPerSet property
        Args:
            value: Value to set for the max_attributes_per_set property.
        """
        self._max_attributes_per_set = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_int_value("maxAttributesPerSet", self.max_attributes_per_set)
    

