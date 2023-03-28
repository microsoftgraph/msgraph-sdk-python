from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class PersonType(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new personType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of data source, such as Person.
        self._class_: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The secondary type of data source, such as OrganizationUser.
        self._subclass: Optional[str] = None
    
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
    def class_(self,) -> Optional[str]:
        """
        Gets the class property value. The type of data source, such as Person.
        Returns: Optional[str]
        """
        return self._class_
    
    @class_.setter
    def class_(self,value: Optional[str] = None) -> None:
        """
        Sets the class property value. The type of data source, such as Person.
        Args:
            value: Value to set for the class_ property.
        """
        self._class_ = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersonType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersonType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersonType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "class": lambda n : setattr(self, 'class_', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "subclass": lambda n : setattr(self, 'subclass', n.get_str_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("class", self.class_)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("subclass", self.subclass)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subclass(self,) -> Optional[str]:
        """
        Gets the subclass property value. The secondary type of data source, such as OrganizationUser.
        Returns: Optional[str]
        """
        return self._subclass
    
    @subclass.setter
    def subclass(self,value: Optional[str] = None) -> None:
        """
        Sets the subclass property value. The secondary type of data source, such as OrganizationUser.
        Args:
            value: Value to set for the subclass property.
        """
        self._subclass = value
    

