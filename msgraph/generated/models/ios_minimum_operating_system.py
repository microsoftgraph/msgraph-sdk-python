from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class IosMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    Contains properties of the minimum operating system required for an iOS mobile app.
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
        Instantiates a new iosMinimumOperatingSystem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Version 10.0 or later.
        self._v10_0: Optional[bool] = None
        # Version 11.0 or later.
        self._v11_0: Optional[bool] = None
        # Version 12.0 or later.
        self._v12_0: Optional[bool] = None
        # Version 13.0 or later.
        self._v13_0: Optional[bool] = None
        # Version 14.0 or later.
        self._v14_0: Optional[bool] = None
        # Version 8.0 or later.
        self._v8_0: Optional[bool] = None
        # Version 9.0 or later.
        self._v9_0: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosMinimumOperatingSystem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v11_0": lambda n : setattr(self, 'v11_0', n.get_bool_value()),
            "v12_0": lambda n : setattr(self, 'v12_0', n.get_bool_value()),
            "v13_0": lambda n : setattr(self, 'v13_0', n.get_bool_value()),
            "v14_0": lambda n : setattr(self, 'v14_0', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
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
        writer.write_bool_value("v12_0", self.v12_0)
        writer.write_bool_value("v13_0", self.v13_0)
        writer.write_bool_value("v14_0", self.v14_0)
        writer.write_bool_value("v8_0", self.v8_0)
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
    def v12_0(self,) -> Optional[bool]:
        """
        Gets the v12_0 property value. Version 12.0 or later.
        Returns: Optional[bool]
        """
        return self._v12_0
    
    @v12_0.setter
    def v12_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v12_0 property value. Version 12.0 or later.
        Args:
            value: Value to set for the v12_0 property.
        """
        self._v12_0 = value
    
    @property
    def v13_0(self,) -> Optional[bool]:
        """
        Gets the v13_0 property value. Version 13.0 or later.
        Returns: Optional[bool]
        """
        return self._v13_0
    
    @v13_0.setter
    def v13_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v13_0 property value. Version 13.0 or later.
        Args:
            value: Value to set for the v13_0 property.
        """
        self._v13_0 = value
    
    @property
    def v14_0(self,) -> Optional[bool]:
        """
        Gets the v14_0 property value. Version 14.0 or later.
        Returns: Optional[bool]
        """
        return self._v14_0
    
    @v14_0.setter
    def v14_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v14_0 property value. Version 14.0 or later.
        Args:
            value: Value to set for the v14_0 property.
        """
        self._v14_0 = value
    
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
    

