from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AndroidMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    Contains properties for the minimum operating system required for an Android mobile app.
    """
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
        Instantiates a new androidMinimumOperatingSystem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Version 10.0 or later.
        self._v10_0: Optional[bool] = None
        # Version 11.0 or later.
        self._v11_0: Optional[bool] = None
        # Version 4.0 or later.
        self._v4_0: Optional[bool] = None
        # Version 4.0.3 or later.
        self._v4_0_3: Optional[bool] = None
        # Version 4.1 or later.
        self._v4_1: Optional[bool] = None
        # Version 4.2 or later.
        self._v4_2: Optional[bool] = None
        # Version 4.3 or later.
        self._v4_3: Optional[bool] = None
        # Version 4.4 or later.
        self._v4_4: Optional[bool] = None
        # Version 5.0 or later.
        self._v5_0: Optional[bool] = None
        # Version 5.1 or later.
        self._v5_1: Optional[bool] = None
        # Version 6.0 or later.
        self._v6_0: Optional[bool] = None
        # Version 7.0 or later.
        self._v7_0: Optional[bool] = None
        # Version 7.1 or later.
        self._v7_1: Optional[bool] = None
        # Version 8.0 or later.
        self._v8_0: Optional[bool] = None
        # Version 8.1 or later.
        self._v8_1: Optional[bool] = None
        # Version 9.0 or later.
        self._v9_0: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidMinimumOperatingSystem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v11_0": lambda n : setattr(self, 'v11_0', n.get_bool_value()),
            "v4_0": lambda n : setattr(self, 'v4_0', n.get_bool_value()),
            "v4_0_3": lambda n : setattr(self, 'v4_0_3', n.get_bool_value()),
            "v4_1": lambda n : setattr(self, 'v4_1', n.get_bool_value()),
            "v4_2": lambda n : setattr(self, 'v4_2', n.get_bool_value()),
            "v4_3": lambda n : setattr(self, 'v4_3', n.get_bool_value()),
            "v4_4": lambda n : setattr(self, 'v4_4', n.get_bool_value()),
            "v5_0": lambda n : setattr(self, 'v5_0', n.get_bool_value()),
            "v5_1": lambda n : setattr(self, 'v5_1', n.get_bool_value()),
            "v6_0": lambda n : setattr(self, 'v6_0', n.get_bool_value()),
            "v7_0": lambda n : setattr(self, 'v7_0', n.get_bool_value()),
            "v7_1": lambda n : setattr(self, 'v7_1', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
            "v8_1": lambda n : setattr(self, 'v8_1', n.get_bool_value()),
            "v9_0": lambda n : setattr(self, 'v9_0', n.get_bool_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("v10_0", self.v10_0)
        writer.write_bool_value("v11_0", self.v11_0)
        writer.write_bool_value("v4_0", self.v4_0)
        writer.write_bool_value("v4_0_3", self.v4_0_3)
        writer.write_bool_value("v4_1", self.v4_1)
        writer.write_bool_value("v4_2", self.v4_2)
        writer.write_bool_value("v4_3", self.v4_3)
        writer.write_bool_value("v4_4", self.v4_4)
        writer.write_bool_value("v5_0", self.v5_0)
        writer.write_bool_value("v5_1", self.v5_1)
        writer.write_bool_value("v6_0", self.v6_0)
        writer.write_bool_value("v7_0", self.v7_0)
        writer.write_bool_value("v7_1", self.v7_1)
        writer.write_bool_value("v8_0", self.v8_0)
        writer.write_bool_value("v8_1", self.v8_1)
        writer.write_bool_value("v9_0", self.v9_0)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def v10_0(self,) -> Optional[bool]:
        """
        Gets the v10_0 property value. Version 10.0 or later.
        Returns: Optional[bool]
        """
        return self._v10_0
    
    @v10_0.setter
    def v10_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_0 property value. Version 10.0 or later.
        Args:
            value: Value to set for the v10_0 property.
        """
        self._v10_0 = value
    
    @property
    def v11_0(self,) -> Optional[bool]:
        """
        Gets the v11_0 property value. Version 11.0 or later.
        Returns: Optional[bool]
        """
        return self._v11_0
    
    @v11_0.setter
    def v11_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v11_0 property value. Version 11.0 or later.
        Args:
            value: Value to set for the v11_0 property.
        """
        self._v11_0 = value
    
    @property
    def v4_0(self,) -> Optional[bool]:
        """
        Gets the v4_0 property value. Version 4.0 or later.
        Returns: Optional[bool]
        """
        return self._v4_0
    
    @v4_0.setter
    def v4_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v4_0 property value. Version 4.0 or later.
        Args:
            value: Value to set for the v4_0 property.
        """
        self._v4_0 = value
    
    @property
    def v4_0_3(self,) -> Optional[bool]:
        """
        Gets the v4_0_3 property value. Version 4.0.3 or later.
        Returns: Optional[bool]
        """
        return self._v4_0_3
    
    @v4_0_3.setter
    def v4_0_3(self,value: Optional[bool] = None) -> None:
        """
        Sets the v4_0_3 property value. Version 4.0.3 or later.
        Args:
            value: Value to set for the v4_0_3 property.
        """
        self._v4_0_3 = value
    
    @property
    def v4_1(self,) -> Optional[bool]:
        """
        Gets the v4_1 property value. Version 4.1 or later.
        Returns: Optional[bool]
        """
        return self._v4_1
    
    @v4_1.setter
    def v4_1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v4_1 property value. Version 4.1 or later.
        Args:
            value: Value to set for the v4_1 property.
        """
        self._v4_1 = value
    
    @property
    def v4_2(self,) -> Optional[bool]:
        """
        Gets the v4_2 property value. Version 4.2 or later.
        Returns: Optional[bool]
        """
        return self._v4_2
    
    @v4_2.setter
    def v4_2(self,value: Optional[bool] = None) -> None:
        """
        Sets the v4_2 property value. Version 4.2 or later.
        Args:
            value: Value to set for the v4_2 property.
        """
        self._v4_2 = value
    
    @property
    def v4_3(self,) -> Optional[bool]:
        """
        Gets the v4_3 property value. Version 4.3 or later.
        Returns: Optional[bool]
        """
        return self._v4_3
    
    @v4_3.setter
    def v4_3(self,value: Optional[bool] = None) -> None:
        """
        Sets the v4_3 property value. Version 4.3 or later.
        Args:
            value: Value to set for the v4_3 property.
        """
        self._v4_3 = value
    
    @property
    def v4_4(self,) -> Optional[bool]:
        """
        Gets the v4_4 property value. Version 4.4 or later.
        Returns: Optional[bool]
        """
        return self._v4_4
    
    @v4_4.setter
    def v4_4(self,value: Optional[bool] = None) -> None:
        """
        Sets the v4_4 property value. Version 4.4 or later.
        Args:
            value: Value to set for the v4_4 property.
        """
        self._v4_4 = value
    
    @property
    def v5_0(self,) -> Optional[bool]:
        """
        Gets the v5_0 property value. Version 5.0 or later.
        Returns: Optional[bool]
        """
        return self._v5_0
    
    @v5_0.setter
    def v5_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v5_0 property value. Version 5.0 or later.
        Args:
            value: Value to set for the v5_0 property.
        """
        self._v5_0 = value
    
    @property
    def v5_1(self,) -> Optional[bool]:
        """
        Gets the v5_1 property value. Version 5.1 or later.
        Returns: Optional[bool]
        """
        return self._v5_1
    
    @v5_1.setter
    def v5_1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v5_1 property value. Version 5.1 or later.
        Args:
            value: Value to set for the v5_1 property.
        """
        self._v5_1 = value
    
    @property
    def v6_0(self,) -> Optional[bool]:
        """
        Gets the v6_0 property value. Version 6.0 or later.
        Returns: Optional[bool]
        """
        return self._v6_0
    
    @v6_0.setter
    def v6_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v6_0 property value. Version 6.0 or later.
        Args:
            value: Value to set for the v6_0 property.
        """
        self._v6_0 = value
    
    @property
    def v7_0(self,) -> Optional[bool]:
        """
        Gets the v7_0 property value. Version 7.0 or later.
        Returns: Optional[bool]
        """
        return self._v7_0
    
    @v7_0.setter
    def v7_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v7_0 property value. Version 7.0 or later.
        Args:
            value: Value to set for the v7_0 property.
        """
        self._v7_0 = value
    
    @property
    def v7_1(self,) -> Optional[bool]:
        """
        Gets the v7_1 property value. Version 7.1 or later.
        Returns: Optional[bool]
        """
        return self._v7_1
    
    @v7_1.setter
    def v7_1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v7_1 property value. Version 7.1 or later.
        Args:
            value: Value to set for the v7_1 property.
        """
        self._v7_1 = value
    
    @property
    def v8_0(self,) -> Optional[bool]:
        """
        Gets the v8_0 property value. Version 8.0 or later.
        Returns: Optional[bool]
        """
        return self._v8_0
    
    @v8_0.setter
    def v8_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v8_0 property value. Version 8.0 or later.
        Args:
            value: Value to set for the v8_0 property.
        """
        self._v8_0 = value
    
    @property
    def v8_1(self,) -> Optional[bool]:
        """
        Gets the v8_1 property value. Version 8.1 or later.
        Returns: Optional[bool]
        """
        return self._v8_1
    
    @v8_1.setter
    def v8_1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v8_1 property value. Version 8.1 or later.
        Args:
            value: Value to set for the v8_1 property.
        """
        self._v8_1 = value
    
    @property
    def v9_0(self,) -> Optional[bool]:
        """
        Gets the v9_0 property value. Version 9.0 or later.
        Returns: Optional[bool]
        """
        return self._v9_0
    
    @v9_0.setter
    def v9_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v9_0 property value. Version 9.0 or later.
        Args:
            value: Value to set for the v9_0 property.
        """
        self._v9_0 = value
    

