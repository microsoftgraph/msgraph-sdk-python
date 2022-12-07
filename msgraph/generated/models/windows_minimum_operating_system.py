from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WindowsMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    The minimum operating system required for a Windows mobile app.
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
        Instantiates a new windowsMinimumOperatingSystem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Windows version 10.0 or later.
        self._v10_0: Optional[bool] = None
        # Windows version 8.0 or later.
        self._v8_0: Optional[bool] = None
        # Windows version 8.1 or later.
        self._v8_1: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMinimumOperatingSystem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
            "v8_1": lambda n : setattr(self, 'v8_1', n.get_bool_value()),
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
        writer.write_bool_value("v8_0", self.v8_0)
        writer.write_bool_value("v8_1", self.v8_1)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def v10_0(self,) -> Optional[bool]:
        """
        Gets the v10_0 property value. Windows version 10.0 or later.
        Returns: Optional[bool]
        """
        return self._v10_0
    
    @v10_0.setter
    def v10_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_0 property value. Windows version 10.0 or later.
        Args:
            value: Value to set for the v10_0 property.
        """
        self._v10_0 = value
    
    @property
    def v8_0(self,) -> Optional[bool]:
        """
        Gets the v8_0 property value. Windows version 8.0 or later.
        Returns: Optional[bool]
        """
        return self._v8_0
    
    @v8_0.setter
    def v8_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v8_0 property value. Windows version 8.0 or later.
        Args:
            value: Value to set for the v8_0 property.
        """
        self._v8_0 = value
    
    @property
    def v8_1(self,) -> Optional[bool]:
        """
        Gets the v8_1 property value. Windows version 8.1 or later.
        Returns: Optional[bool]
        """
        return self._v8_1
    
    @v8_1.setter
    def v8_1(self,value: Optional[bool] = None) -> None:
        """
        Sets the v8_1 property value. Windows version 8.1 or later.
        Args:
            value: Value to set for the v8_1 property.
        """
        self._v8_1 = value
    

