from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PlannerCategoryDescriptions(AdditionalDataHolder, Parsable):
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
    def category1(self,) -> Optional[str]:
        """
        Gets the category1 property value. The label associated with Category 1
        Returns: Optional[str]
        """
        return self._category1
    
    @category1.setter
    def category1(self,value: Optional[str] = None) -> None:
        """
        Sets the category1 property value. The label associated with Category 1
        Args:
            value: Value to set for the category1 property.
        """
        self._category1 = value
    
    @property
    def category10(self,) -> Optional[str]:
        """
        Gets the category10 property value. The label associated with Category 10
        Returns: Optional[str]
        """
        return self._category10
    
    @category10.setter
    def category10(self,value: Optional[str] = None) -> None:
        """
        Sets the category10 property value. The label associated with Category 10
        Args:
            value: Value to set for the category10 property.
        """
        self._category10 = value
    
    @property
    def category11(self,) -> Optional[str]:
        """
        Gets the category11 property value. The label associated with Category 11
        Returns: Optional[str]
        """
        return self._category11
    
    @category11.setter
    def category11(self,value: Optional[str] = None) -> None:
        """
        Sets the category11 property value. The label associated with Category 11
        Args:
            value: Value to set for the category11 property.
        """
        self._category11 = value
    
    @property
    def category12(self,) -> Optional[str]:
        """
        Gets the category12 property value. The label associated with Category 12
        Returns: Optional[str]
        """
        return self._category12
    
    @category12.setter
    def category12(self,value: Optional[str] = None) -> None:
        """
        Sets the category12 property value. The label associated with Category 12
        Args:
            value: Value to set for the category12 property.
        """
        self._category12 = value
    
    @property
    def category13(self,) -> Optional[str]:
        """
        Gets the category13 property value. The label associated with Category 13
        Returns: Optional[str]
        """
        return self._category13
    
    @category13.setter
    def category13(self,value: Optional[str] = None) -> None:
        """
        Sets the category13 property value. The label associated with Category 13
        Args:
            value: Value to set for the category13 property.
        """
        self._category13 = value
    
    @property
    def category14(self,) -> Optional[str]:
        """
        Gets the category14 property value. The label associated with Category 14
        Returns: Optional[str]
        """
        return self._category14
    
    @category14.setter
    def category14(self,value: Optional[str] = None) -> None:
        """
        Sets the category14 property value. The label associated with Category 14
        Args:
            value: Value to set for the category14 property.
        """
        self._category14 = value
    
    @property
    def category15(self,) -> Optional[str]:
        """
        Gets the category15 property value. The label associated with Category 15
        Returns: Optional[str]
        """
        return self._category15
    
    @category15.setter
    def category15(self,value: Optional[str] = None) -> None:
        """
        Sets the category15 property value. The label associated with Category 15
        Args:
            value: Value to set for the category15 property.
        """
        self._category15 = value
    
    @property
    def category16(self,) -> Optional[str]:
        """
        Gets the category16 property value. The label associated with Category 16
        Returns: Optional[str]
        """
        return self._category16
    
    @category16.setter
    def category16(self,value: Optional[str] = None) -> None:
        """
        Sets the category16 property value. The label associated with Category 16
        Args:
            value: Value to set for the category16 property.
        """
        self._category16 = value
    
    @property
    def category17(self,) -> Optional[str]:
        """
        Gets the category17 property value. The label associated with Category 17
        Returns: Optional[str]
        """
        return self._category17
    
    @category17.setter
    def category17(self,value: Optional[str] = None) -> None:
        """
        Sets the category17 property value. The label associated with Category 17
        Args:
            value: Value to set for the category17 property.
        """
        self._category17 = value
    
    @property
    def category18(self,) -> Optional[str]:
        """
        Gets the category18 property value. The label associated with Category 18
        Returns: Optional[str]
        """
        return self._category18
    
    @category18.setter
    def category18(self,value: Optional[str] = None) -> None:
        """
        Sets the category18 property value. The label associated with Category 18
        Args:
            value: Value to set for the category18 property.
        """
        self._category18 = value
    
    @property
    def category19(self,) -> Optional[str]:
        """
        Gets the category19 property value. The label associated with Category 19
        Returns: Optional[str]
        """
        return self._category19
    
    @category19.setter
    def category19(self,value: Optional[str] = None) -> None:
        """
        Sets the category19 property value. The label associated with Category 19
        Args:
            value: Value to set for the category19 property.
        """
        self._category19 = value
    
    @property
    def category2(self,) -> Optional[str]:
        """
        Gets the category2 property value. The label associated with Category 2
        Returns: Optional[str]
        """
        return self._category2
    
    @category2.setter
    def category2(self,value: Optional[str] = None) -> None:
        """
        Sets the category2 property value. The label associated with Category 2
        Args:
            value: Value to set for the category2 property.
        """
        self._category2 = value
    
    @property
    def category20(self,) -> Optional[str]:
        """
        Gets the category20 property value. The label associated with Category 20
        Returns: Optional[str]
        """
        return self._category20
    
    @category20.setter
    def category20(self,value: Optional[str] = None) -> None:
        """
        Sets the category20 property value. The label associated with Category 20
        Args:
            value: Value to set for the category20 property.
        """
        self._category20 = value
    
    @property
    def category21(self,) -> Optional[str]:
        """
        Gets the category21 property value. The label associated with Category 21
        Returns: Optional[str]
        """
        return self._category21
    
    @category21.setter
    def category21(self,value: Optional[str] = None) -> None:
        """
        Sets the category21 property value. The label associated with Category 21
        Args:
            value: Value to set for the category21 property.
        """
        self._category21 = value
    
    @property
    def category22(self,) -> Optional[str]:
        """
        Gets the category22 property value. The label associated with Category 22
        Returns: Optional[str]
        """
        return self._category22
    
    @category22.setter
    def category22(self,value: Optional[str] = None) -> None:
        """
        Sets the category22 property value. The label associated with Category 22
        Args:
            value: Value to set for the category22 property.
        """
        self._category22 = value
    
    @property
    def category23(self,) -> Optional[str]:
        """
        Gets the category23 property value. The label associated with Category 23
        Returns: Optional[str]
        """
        return self._category23
    
    @category23.setter
    def category23(self,value: Optional[str] = None) -> None:
        """
        Sets the category23 property value. The label associated with Category 23
        Args:
            value: Value to set for the category23 property.
        """
        self._category23 = value
    
    @property
    def category24(self,) -> Optional[str]:
        """
        Gets the category24 property value. The label associated with Category 24
        Returns: Optional[str]
        """
        return self._category24
    
    @category24.setter
    def category24(self,value: Optional[str] = None) -> None:
        """
        Sets the category24 property value. The label associated with Category 24
        Args:
            value: Value to set for the category24 property.
        """
        self._category24 = value
    
    @property
    def category25(self,) -> Optional[str]:
        """
        Gets the category25 property value. The label associated with Category 25
        Returns: Optional[str]
        """
        return self._category25
    
    @category25.setter
    def category25(self,value: Optional[str] = None) -> None:
        """
        Sets the category25 property value. The label associated with Category 25
        Args:
            value: Value to set for the category25 property.
        """
        self._category25 = value
    
    @property
    def category3(self,) -> Optional[str]:
        """
        Gets the category3 property value. The label associated with Category 3
        Returns: Optional[str]
        """
        return self._category3
    
    @category3.setter
    def category3(self,value: Optional[str] = None) -> None:
        """
        Sets the category3 property value. The label associated with Category 3
        Args:
            value: Value to set for the category3 property.
        """
        self._category3 = value
    
    @property
    def category4(self,) -> Optional[str]:
        """
        Gets the category4 property value. The label associated with Category 4
        Returns: Optional[str]
        """
        return self._category4
    
    @category4.setter
    def category4(self,value: Optional[str] = None) -> None:
        """
        Sets the category4 property value. The label associated with Category 4
        Args:
            value: Value to set for the category4 property.
        """
        self._category4 = value
    
    @property
    def category5(self,) -> Optional[str]:
        """
        Gets the category5 property value. The label associated with Category 5
        Returns: Optional[str]
        """
        return self._category5
    
    @category5.setter
    def category5(self,value: Optional[str] = None) -> None:
        """
        Sets the category5 property value. The label associated with Category 5
        Args:
            value: Value to set for the category5 property.
        """
        self._category5 = value
    
    @property
    def category6(self,) -> Optional[str]:
        """
        Gets the category6 property value. The label associated with Category 6
        Returns: Optional[str]
        """
        return self._category6
    
    @category6.setter
    def category6(self,value: Optional[str] = None) -> None:
        """
        Sets the category6 property value. The label associated with Category 6
        Args:
            value: Value to set for the category6 property.
        """
        self._category6 = value
    
    @property
    def category7(self,) -> Optional[str]:
        """
        Gets the category7 property value. The label associated with Category 7
        Returns: Optional[str]
        """
        return self._category7
    
    @category7.setter
    def category7(self,value: Optional[str] = None) -> None:
        """
        Sets the category7 property value. The label associated with Category 7
        Args:
            value: Value to set for the category7 property.
        """
        self._category7 = value
    
    @property
    def category8(self,) -> Optional[str]:
        """
        Gets the category8 property value. The label associated with Category 8
        Returns: Optional[str]
        """
        return self._category8
    
    @category8.setter
    def category8(self,value: Optional[str] = None) -> None:
        """
        Sets the category8 property value. The label associated with Category 8
        Args:
            value: Value to set for the category8 property.
        """
        self._category8 = value
    
    @property
    def category9(self,) -> Optional[str]:
        """
        Gets the category9 property value. The label associated with Category 9
        Returns: Optional[str]
        """
        return self._category9
    
    @category9.setter
    def category9(self,value: Optional[str] = None) -> None:
        """
        Sets the category9 property value. The label associated with Category 9
        Args:
            value: Value to set for the category9 property.
        """
        self._category9 = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerCategoryDescriptions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The label associated with Category 1
        self._category1: Optional[str] = None
        # The label associated with Category 10
        self._category10: Optional[str] = None
        # The label associated with Category 11
        self._category11: Optional[str] = None
        # The label associated with Category 12
        self._category12: Optional[str] = None
        # The label associated with Category 13
        self._category13: Optional[str] = None
        # The label associated with Category 14
        self._category14: Optional[str] = None
        # The label associated with Category 15
        self._category15: Optional[str] = None
        # The label associated with Category 16
        self._category16: Optional[str] = None
        # The label associated with Category 17
        self._category17: Optional[str] = None
        # The label associated with Category 18
        self._category18: Optional[str] = None
        # The label associated with Category 19
        self._category19: Optional[str] = None
        # The label associated with Category 2
        self._category2: Optional[str] = None
        # The label associated with Category 20
        self._category20: Optional[str] = None
        # The label associated with Category 21
        self._category21: Optional[str] = None
        # The label associated with Category 22
        self._category22: Optional[str] = None
        # The label associated with Category 23
        self._category23: Optional[str] = None
        # The label associated with Category 24
        self._category24: Optional[str] = None
        # The label associated with Category 25
        self._category25: Optional[str] = None
        # The label associated with Category 3
        self._category3: Optional[str] = None
        # The label associated with Category 4
        self._category4: Optional[str] = None
        # The label associated with Category 5
        self._category5: Optional[str] = None
        # The label associated with Category 6
        self._category6: Optional[str] = None
        # The label associated with Category 7
        self._category7: Optional[str] = None
        # The label associated with Category 8
        self._category8: Optional[str] = None
        # The label associated with Category 9
        self._category9: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerCategoryDescriptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerCategoryDescriptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerCategoryDescriptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category1": lambda n : setattr(self, 'category1', n.get_str_value()),
            "category10": lambda n : setattr(self, 'category10', n.get_str_value()),
            "category11": lambda n : setattr(self, 'category11', n.get_str_value()),
            "category12": lambda n : setattr(self, 'category12', n.get_str_value()),
            "category13": lambda n : setattr(self, 'category13', n.get_str_value()),
            "category14": lambda n : setattr(self, 'category14', n.get_str_value()),
            "category15": lambda n : setattr(self, 'category15', n.get_str_value()),
            "category16": lambda n : setattr(self, 'category16', n.get_str_value()),
            "category17": lambda n : setattr(self, 'category17', n.get_str_value()),
            "category18": lambda n : setattr(self, 'category18', n.get_str_value()),
            "category19": lambda n : setattr(self, 'category19', n.get_str_value()),
            "category2": lambda n : setattr(self, 'category2', n.get_str_value()),
            "category20": lambda n : setattr(self, 'category20', n.get_str_value()),
            "category21": lambda n : setattr(self, 'category21', n.get_str_value()),
            "category22": lambda n : setattr(self, 'category22', n.get_str_value()),
            "category23": lambda n : setattr(self, 'category23', n.get_str_value()),
            "category24": lambda n : setattr(self, 'category24', n.get_str_value()),
            "category25": lambda n : setattr(self, 'category25', n.get_str_value()),
            "category3": lambda n : setattr(self, 'category3', n.get_str_value()),
            "category4": lambda n : setattr(self, 'category4', n.get_str_value()),
            "category5": lambda n : setattr(self, 'category5', n.get_str_value()),
            "category6": lambda n : setattr(self, 'category6', n.get_str_value()),
            "category7": lambda n : setattr(self, 'category7', n.get_str_value()),
            "category8": lambda n : setattr(self, 'category8', n.get_str_value()),
            "category9": lambda n : setattr(self, 'category9', n.get_str_value()),
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
        writer.write_str_value("category1", self.category1)
        writer.write_str_value("category10", self.category10)
        writer.write_str_value("category11", self.category11)
        writer.write_str_value("category12", self.category12)
        writer.write_str_value("category13", self.category13)
        writer.write_str_value("category14", self.category14)
        writer.write_str_value("category15", self.category15)
        writer.write_str_value("category16", self.category16)
        writer.write_str_value("category17", self.category17)
        writer.write_str_value("category18", self.category18)
        writer.write_str_value("category19", self.category19)
        writer.write_str_value("category2", self.category2)
        writer.write_str_value("category20", self.category20)
        writer.write_str_value("category21", self.category21)
        writer.write_str_value("category22", self.category22)
        writer.write_str_value("category23", self.category23)
        writer.write_str_value("category24", self.category24)
        writer.write_str_value("category25", self.category25)
        writer.write_str_value("category3", self.category3)
        writer.write_str_value("category4", self.category4)
        writer.write_str_value("category5", self.category5)
        writer.write_str_value("category6", self.category6)
        writer.write_str_value("category7", self.category7)
        writer.write_str_value("category8", self.category8)
        writer.write_str_value("category9", self.category9)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

