from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_answer = lazy_import('msgraph.generated.models.access_package_answer')

class AccessPackageAnswerString(access_package_answer.AccessPackageAnswer):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageAnswerString and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageAnswerString"
        # The value stored on the requestor's user profile, if this answer is configured to be stored as a specific attribute.
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAnswerString:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswerString
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAnswerString()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("value", self.value)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. The value stored on the requestor's user profile, if this answer is configured to be stored as a specific attribute.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. The value stored on the requestor's user profile, if this answer is configured to be stored as a specific attribute.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

