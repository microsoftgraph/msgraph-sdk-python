from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ModifiedProperty(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new modifiedProperty and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the property name of the target attribute that was changed.
        self._display_name: Optional[str] = None
        # Indicates the updated value for the propery.
        self._new_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the previous value (before the update) for the property.
        self._old_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ModifiedProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ModifiedProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ModifiedProperty()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Indicates the property name of the target attribute that was changed.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Indicates the property name of the target attribute that was changed.
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
            "new_value": lambda n : setattr(self, 'new_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "old_value": lambda n : setattr(self, 'old_value', n.get_str_value()),
        }
        return fields
    
    @property
    def new_value(self,) -> Optional[str]:
        """
        Gets the newValue property value. Indicates the updated value for the propery.
        Returns: Optional[str]
        """
        return self._new_value
    
    @new_value.setter
    def new_value(self,value: Optional[str] = None) -> None:
        """
        Sets the newValue property value. Indicates the updated value for the propery.
        Args:
            value: Value to set for the newValue property.
        """
        self._new_value = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def old_value(self,) -> Optional[str]:
        """
        Gets the oldValue property value. Indicates the previous value (before the update) for the property.
        Returns: Optional[str]
        """
        return self._old_value
    
    @old_value.setter
    def old_value(self,value: Optional[str] = None) -> None:
        """
        Sets the oldValue property value. Indicates the previous value (before the update) for the property.
        Args:
            value: Value to set for the oldValue property.
        """
        self._old_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("newValue", self.new_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("oldValue", self.old_value)
        writer.write_additional_data_value(self.additional_data)
    

