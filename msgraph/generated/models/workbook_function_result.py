from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
json = lazy_import('msgraph.generated.models.json')

class WorkbookFunctionResult(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new WorkbookFunctionResult and sets the default values.
        """
        super().__init__()
        # The error property
        self._error: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The value property
        self._value: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookFunctionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookFunctionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookFunctionResult()
    
    @property
    def error(self,) -> Optional[str]:
        """
        Gets the error property value. The error property
        Returns: Optional[str]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[str] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(json.Json)),
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
        writer.write_str_value("error", self.error)
        writer.write_object_value("value", self.value)
    
    @property
    def value(self,) -> Optional[json.Json]:
        """
        Gets the value property value. The value property
        Returns: Optional[json.Json]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

