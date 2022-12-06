from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OnPremisesExtensionAttributes(AdditionalDataHolder, Parsable):
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
        Instantiates a new onPremisesExtensionAttributes and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # First customizable extension attribute.
        self._extension_attribute1: Optional[str] = None
        # Tenth customizable extension attribute.
        self._extension_attribute10: Optional[str] = None
        # Eleventh customizable extension attribute.
        self._extension_attribute11: Optional[str] = None
        # Twelfth customizable extension attribute.
        self._extension_attribute12: Optional[str] = None
        # Thirteenth customizable extension attribute.
        self._extension_attribute13: Optional[str] = None
        # Fourteenth customizable extension attribute.
        self._extension_attribute14: Optional[str] = None
        # Fifteenth customizable extension attribute.
        self._extension_attribute15: Optional[str] = None
        # Second customizable extension attribute.
        self._extension_attribute2: Optional[str] = None
        # Third customizable extension attribute.
        self._extension_attribute3: Optional[str] = None
        # Fourth customizable extension attribute.
        self._extension_attribute4: Optional[str] = None
        # Fifth customizable extension attribute.
        self._extension_attribute5: Optional[str] = None
        # Sixth customizable extension attribute.
        self._extension_attribute6: Optional[str] = None
        # Seventh customizable extension attribute.
        self._extension_attribute7: Optional[str] = None
        # Eighth customizable extension attribute.
        self._extension_attribute8: Optional[str] = None
        # Ninth customizable extension attribute.
        self._extension_attribute9: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesExtensionAttributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesExtensionAttributes
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesExtensionAttributes()
    
    @property
    def extension_attribute1(self,) -> Optional[str]:
        """
        Gets the extensionAttribute1 property value. First customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute1
    
    @extension_attribute1.setter
    def extension_attribute1(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute1 property value. First customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute1 property.
        """
        self._extension_attribute1 = value
    
    @property
    def extension_attribute10(self,) -> Optional[str]:
        """
        Gets the extensionAttribute10 property value. Tenth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute10
    
    @extension_attribute10.setter
    def extension_attribute10(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute10 property value. Tenth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute10 property.
        """
        self._extension_attribute10 = value
    
    @property
    def extension_attribute11(self,) -> Optional[str]:
        """
        Gets the extensionAttribute11 property value. Eleventh customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute11
    
    @extension_attribute11.setter
    def extension_attribute11(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute11 property value. Eleventh customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute11 property.
        """
        self._extension_attribute11 = value
    
    @property
    def extension_attribute12(self,) -> Optional[str]:
        """
        Gets the extensionAttribute12 property value. Twelfth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute12
    
    @extension_attribute12.setter
    def extension_attribute12(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute12 property value. Twelfth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute12 property.
        """
        self._extension_attribute12 = value
    
    @property
    def extension_attribute13(self,) -> Optional[str]:
        """
        Gets the extensionAttribute13 property value. Thirteenth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute13
    
    @extension_attribute13.setter
    def extension_attribute13(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute13 property value. Thirteenth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute13 property.
        """
        self._extension_attribute13 = value
    
    @property
    def extension_attribute14(self,) -> Optional[str]:
        """
        Gets the extensionAttribute14 property value. Fourteenth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute14
    
    @extension_attribute14.setter
    def extension_attribute14(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute14 property value. Fourteenth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute14 property.
        """
        self._extension_attribute14 = value
    
    @property
    def extension_attribute15(self,) -> Optional[str]:
        """
        Gets the extensionAttribute15 property value. Fifteenth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute15
    
    @extension_attribute15.setter
    def extension_attribute15(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute15 property value. Fifteenth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute15 property.
        """
        self._extension_attribute15 = value
    
    @property
    def extension_attribute2(self,) -> Optional[str]:
        """
        Gets the extensionAttribute2 property value. Second customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute2
    
    @extension_attribute2.setter
    def extension_attribute2(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute2 property value. Second customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute2 property.
        """
        self._extension_attribute2 = value
    
    @property
    def extension_attribute3(self,) -> Optional[str]:
        """
        Gets the extensionAttribute3 property value. Third customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute3
    
    @extension_attribute3.setter
    def extension_attribute3(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute3 property value. Third customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute3 property.
        """
        self._extension_attribute3 = value
    
    @property
    def extension_attribute4(self,) -> Optional[str]:
        """
        Gets the extensionAttribute4 property value. Fourth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute4
    
    @extension_attribute4.setter
    def extension_attribute4(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute4 property value. Fourth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute4 property.
        """
        self._extension_attribute4 = value
    
    @property
    def extension_attribute5(self,) -> Optional[str]:
        """
        Gets the extensionAttribute5 property value. Fifth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute5
    
    @extension_attribute5.setter
    def extension_attribute5(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute5 property value. Fifth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute5 property.
        """
        self._extension_attribute5 = value
    
    @property
    def extension_attribute6(self,) -> Optional[str]:
        """
        Gets the extensionAttribute6 property value. Sixth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute6
    
    @extension_attribute6.setter
    def extension_attribute6(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute6 property value. Sixth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute6 property.
        """
        self._extension_attribute6 = value
    
    @property
    def extension_attribute7(self,) -> Optional[str]:
        """
        Gets the extensionAttribute7 property value. Seventh customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute7
    
    @extension_attribute7.setter
    def extension_attribute7(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute7 property value. Seventh customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute7 property.
        """
        self._extension_attribute7 = value
    
    @property
    def extension_attribute8(self,) -> Optional[str]:
        """
        Gets the extensionAttribute8 property value. Eighth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute8
    
    @extension_attribute8.setter
    def extension_attribute8(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute8 property value. Eighth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute8 property.
        """
        self._extension_attribute8 = value
    
    @property
    def extension_attribute9(self,) -> Optional[str]:
        """
        Gets the extensionAttribute9 property value. Ninth customizable extension attribute.
        Returns: Optional[str]
        """
        return self._extension_attribute9
    
    @extension_attribute9.setter
    def extension_attribute9(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionAttribute9 property value. Ninth customizable extension attribute.
        Args:
            value: Value to set for the extensionAttribute9 property.
        """
        self._extension_attribute9 = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "extension_attribute1": lambda n : setattr(self, 'extension_attribute1', n.get_str_value()),
            "extension_attribute10": lambda n : setattr(self, 'extension_attribute10', n.get_str_value()),
            "extension_attribute11": lambda n : setattr(self, 'extension_attribute11', n.get_str_value()),
            "extension_attribute12": lambda n : setattr(self, 'extension_attribute12', n.get_str_value()),
            "extension_attribute13": lambda n : setattr(self, 'extension_attribute13', n.get_str_value()),
            "extension_attribute14": lambda n : setattr(self, 'extension_attribute14', n.get_str_value()),
            "extension_attribute15": lambda n : setattr(self, 'extension_attribute15', n.get_str_value()),
            "extension_attribute2": lambda n : setattr(self, 'extension_attribute2', n.get_str_value()),
            "extension_attribute3": lambda n : setattr(self, 'extension_attribute3', n.get_str_value()),
            "extension_attribute4": lambda n : setattr(self, 'extension_attribute4', n.get_str_value()),
            "extension_attribute5": lambda n : setattr(self, 'extension_attribute5', n.get_str_value()),
            "extension_attribute6": lambda n : setattr(self, 'extension_attribute6', n.get_str_value()),
            "extension_attribute7": lambda n : setattr(self, 'extension_attribute7', n.get_str_value()),
            "extension_attribute8": lambda n : setattr(self, 'extension_attribute8', n.get_str_value()),
            "extension_attribute9": lambda n : setattr(self, 'extension_attribute9', n.get_str_value()),
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
        writer.write_str_value("extensionAttribute1", self.extension_attribute1)
        writer.write_str_value("extensionAttribute10", self.extension_attribute10)
        writer.write_str_value("extensionAttribute11", self.extension_attribute11)
        writer.write_str_value("extensionAttribute12", self.extension_attribute12)
        writer.write_str_value("extensionAttribute13", self.extension_attribute13)
        writer.write_str_value("extensionAttribute14", self.extension_attribute14)
        writer.write_str_value("extensionAttribute15", self.extension_attribute15)
        writer.write_str_value("extensionAttribute2", self.extension_attribute2)
        writer.write_str_value("extensionAttribute3", self.extension_attribute3)
        writer.write_str_value("extensionAttribute4", self.extension_attribute4)
        writer.write_str_value("extensionAttribute5", self.extension_attribute5)
        writer.write_str_value("extensionAttribute6", self.extension_attribute6)
        writer.write_str_value("extensionAttribute7", self.extension_attribute7)
        writer.write_str_value("extensionAttribute8", self.extension_attribute8)
        writer.write_str_value("extensionAttribute9", self.extension_attribute9)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

