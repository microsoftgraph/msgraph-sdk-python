from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PersonOrGroupColumn(AdditionalDataHolder, Parsable):
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
    def allow_multiple_selection(self,) -> Optional[bool]:
        """
        Gets the allowMultipleSelection property value. Indicates whether multiple values can be selected from the source.
        Returns: Optional[bool]
        """
        return self._allow_multiple_selection
    
    @allow_multiple_selection.setter
    def allow_multiple_selection(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowMultipleSelection property value. Indicates whether multiple values can be selected from the source.
        Args:
            value: Value to set for the allowMultipleSelection property.
        """
        self._allow_multiple_selection = value
    
    @property
    def choose_from_type(self,) -> Optional[str]:
        """
        Gets the chooseFromType property value. Whether to allow selection of people only, or people and groups. Must be one of peopleAndGroups or peopleOnly.
        Returns: Optional[str]
        """
        return self._choose_from_type
    
    @choose_from_type.setter
    def choose_from_type(self,value: Optional[str] = None) -> None:
        """
        Sets the chooseFromType property value. Whether to allow selection of people only, or people and groups. Must be one of peopleAndGroups or peopleOnly.
        Args:
            value: Value to set for the chooseFromType property.
        """
        self._choose_from_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new personOrGroupColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether multiple values can be selected from the source.
        self._allow_multiple_selection: Optional[bool] = None
        # Whether to allow selection of people only, or people and groups. Must be one of peopleAndGroups or peopleOnly.
        self._choose_from_type: Optional[str] = None
        # How to display the information about the person or group chosen. See below.
        self._display_as: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonOrGroupColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonOrGroupColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonOrGroupColumn()
    
    @property
    def display_as(self,) -> Optional[str]:
        """
        Gets the displayAs property value. How to display the information about the person or group chosen. See below.
        Returns: Optional[str]
        """
        return self._display_as
    
    @display_as.setter
    def display_as(self,value: Optional[str] = None) -> None:
        """
        Sets the displayAs property value. How to display the information about the person or group chosen. See below.
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
            "allow_multiple_selection": lambda n : setattr(self, 'allow_multiple_selection', n.get_bool_value()),
            "choose_from_type": lambda n : setattr(self, 'choose_from_type', n.get_str_value()),
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
        writer.write_bool_value("allowMultipleSelection", self.allow_multiple_selection)
        writer.write_str_value("chooseFromType", self.choose_from_type)
        writer.write_str_value("displayAs", self.display_as)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

