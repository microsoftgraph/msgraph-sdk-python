from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ChoiceColumn(AdditionalDataHolder, Parsable):
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
    
    @property
    def allow_text_entry(self,) -> Optional[bool]:
        """
        Gets the allowTextEntry property value. If true, allows custom values that aren't in the configured choices.
        Returns: Optional[bool]
        """
        return self._allow_text_entry
    
    @allow_text_entry.setter
    def allow_text_entry(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowTextEntry property value. If true, allows custom values that aren't in the configured choices.
        Args:
            value: Value to set for the allowTextEntry property.
        """
        self._allow_text_entry = value
    
    @property
    def choices(self,) -> Optional[List[str]]:
        """
        Gets the choices property value. The list of values available for this column.
        Returns: Optional[List[str]]
        """
        return self._choices
    
    @choices.setter
    def choices(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the choices property value. The list of values available for this column.
        Args:
            value: Value to set for the choices property.
        """
        self._choices = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new choiceColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If true, allows custom values that aren't in the configured choices.
        self._allow_text_entry: Optional[bool] = None
        # The list of values available for this column.
        self._choices: Optional[List[str]] = None
        # How the choices are to be presented in the UX. Must be one of checkBoxes, dropDownMenu, or radioButtons
        self._display_as: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChoiceColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChoiceColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChoiceColumn()
    
    @property
    def display_as(self,) -> Optional[str]:
        """
        Gets the displayAs property value. How the choices are to be presented in the UX. Must be one of checkBoxes, dropDownMenu, or radioButtons
        Returns: Optional[str]
        """
        return self._display_as
    
    @display_as.setter
    def display_as(self,value: Optional[str] = None) -> None:
        """
        Sets the displayAs property value. How the choices are to be presented in the UX. Must be one of checkBoxes, dropDownMenu, or radioButtons
        Args:
            value: Value to set for the displayAs property.
        """
        self._display_as = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_text_entry": lambda n : setattr(self, 'allow_text_entry', n.get_bool_value()),
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_primitive_values(str)),
            "display_as": lambda n : setattr(self, 'display_as', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowTextEntry", self.allow_text_entry)
        writer.write_collection_of_primitive_values("choices", self.choices)
        writer.write_str_value("displayAs", self.display_as)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

