from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MacOSMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    The minimum operating system required for a macOS app.
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
        Instantiates a new macOSMinimumOperatingSystem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # When TRUE, indicates OS X 10.10 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_10: Optional[bool] = None
        # When TRUE, indicates OS X 10.11 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_11: Optional[bool] = None
        # When TRUE, indicates macOS 10.12 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_12: Optional[bool] = None
        # When TRUE, indicates macOS 10.13 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_13: Optional[bool] = None
        # When TRUE, indicates macOS 10.14 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_14: Optional[bool] = None
        # When TRUE, indicates macOS 10.15 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_15: Optional[bool] = None
        # When TRUE, indicates Mac OS X 10.7 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_7: Optional[bool] = None
        # When TRUE, indicates OS X 10.8 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_8: Optional[bool] = None
        # When TRUE, indicates OS X 10.9 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v10_9: Optional[bool] = None
        # When TRUE, indicates macOS 11.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v11_0: Optional[bool] = None
        # When TRUE, indicates macOS 12.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v12_0: Optional[bool] = None
        # When TRUE, indicates macOS 13.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        self._v13_0: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSMinimumOperatingSystem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_10": lambda n : setattr(self, 'v10_10', n.get_bool_value()),
            "v10_11": lambda n : setattr(self, 'v10_11', n.get_bool_value()),
            "v10_12": lambda n : setattr(self, 'v10_12', n.get_bool_value()),
            "v10_13": lambda n : setattr(self, 'v10_13', n.get_bool_value()),
            "v10_14": lambda n : setattr(self, 'v10_14', n.get_bool_value()),
            "v10_15": lambda n : setattr(self, 'v10_15', n.get_bool_value()),
            "v10_7": lambda n : setattr(self, 'v10_7', n.get_bool_value()),
            "v10_8": lambda n : setattr(self, 'v10_8', n.get_bool_value()),
            "v10_9": lambda n : setattr(self, 'v10_9', n.get_bool_value()),
            "v11_0": lambda n : setattr(self, 'v11_0', n.get_bool_value()),
            "v12_0": lambda n : setattr(self, 'v12_0', n.get_bool_value()),
            "v13_0": lambda n : setattr(self, 'v13_0', n.get_bool_value()),
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
        writer.write_bool_value("v10_10", self.v10_10)
        writer.write_bool_value("v10_11", self.v10_11)
        writer.write_bool_value("v10_12", self.v10_12)
        writer.write_bool_value("v10_13", self.v10_13)
        writer.write_bool_value("v10_14", self.v10_14)
        writer.write_bool_value("v10_15", self.v10_15)
        writer.write_bool_value("v10_7", self.v10_7)
        writer.write_bool_value("v10_8", self.v10_8)
        writer.write_bool_value("v10_9", self.v10_9)
        writer.write_bool_value("v11_0", self.v11_0)
        writer.write_bool_value("v12_0", self.v12_0)
        writer.write_bool_value("v13_0", self.v13_0)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def v10_10(self,) -> Optional[bool]:
        """
        Gets the v10_10 property value. When TRUE, indicates OS X 10.10 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_10
    
    @v10_10.setter
    def v10_10(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_10 property value. When TRUE, indicates OS X 10.10 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_10 property.
        """
        self._v10_10 = value
    
    @property
    def v10_11(self,) -> Optional[bool]:
        """
        Gets the v10_11 property value. When TRUE, indicates OS X 10.11 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_11
    
    @v10_11.setter
    def v10_11(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_11 property value. When TRUE, indicates OS X 10.11 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_11 property.
        """
        self._v10_11 = value
    
    @property
    def v10_12(self,) -> Optional[bool]:
        """
        Gets the v10_12 property value. When TRUE, indicates macOS 10.12 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_12
    
    @v10_12.setter
    def v10_12(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_12 property value. When TRUE, indicates macOS 10.12 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_12 property.
        """
        self._v10_12 = value
    
    @property
    def v10_13(self,) -> Optional[bool]:
        """
        Gets the v10_13 property value. When TRUE, indicates macOS 10.13 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_13
    
    @v10_13.setter
    def v10_13(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_13 property value. When TRUE, indicates macOS 10.13 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_13 property.
        """
        self._v10_13 = value
    
    @property
    def v10_14(self,) -> Optional[bool]:
        """
        Gets the v10_14 property value. When TRUE, indicates macOS 10.14 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_14
    
    @v10_14.setter
    def v10_14(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_14 property value. When TRUE, indicates macOS 10.14 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_14 property.
        """
        self._v10_14 = value
    
    @property
    def v10_15(self,) -> Optional[bool]:
        """
        Gets the v10_15 property value. When TRUE, indicates macOS 10.15 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_15
    
    @v10_15.setter
    def v10_15(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_15 property value. When TRUE, indicates macOS 10.15 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_15 property.
        """
        self._v10_15 = value
    
    @property
    def v10_7(self,) -> Optional[bool]:
        """
        Gets the v10_7 property value. When TRUE, indicates Mac OS X 10.7 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_7
    
    @v10_7.setter
    def v10_7(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_7 property value. When TRUE, indicates Mac OS X 10.7 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_7 property.
        """
        self._v10_7 = value
    
    @property
    def v10_8(self,) -> Optional[bool]:
        """
        Gets the v10_8 property value. When TRUE, indicates OS X 10.8 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_8
    
    @v10_8.setter
    def v10_8(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_8 property value. When TRUE, indicates OS X 10.8 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_8 property.
        """
        self._v10_8 = value
    
    @property
    def v10_9(self,) -> Optional[bool]:
        """
        Gets the v10_9 property value. When TRUE, indicates OS X 10.9 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v10_9
    
    @v10_9.setter
    def v10_9(self,value: Optional[bool] = None) -> None:
        """
        Sets the v10_9 property value. When TRUE, indicates OS X 10.9 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v10_9 property.
        """
        self._v10_9 = value
    
    @property
    def v11_0(self,) -> Optional[bool]:
        """
        Gets the v11_0 property value. When TRUE, indicates macOS 11.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v11_0
    
    @v11_0.setter
    def v11_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v11_0 property value. When TRUE, indicates macOS 11.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v11_0 property.
        """
        self._v11_0 = value
    
    @property
    def v12_0(self,) -> Optional[bool]:
        """
        Gets the v12_0 property value. When TRUE, indicates macOS 12.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v12_0
    
    @v12_0.setter
    def v12_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v12_0 property value. When TRUE, indicates macOS 12.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v12_0 property.
        """
        self._v12_0 = value
    
    @property
    def v13_0(self,) -> Optional[bool]:
        """
        Gets the v13_0 property value. When TRUE, indicates macOS 13.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._v13_0
    
    @v13_0.setter
    def v13_0(self,value: Optional[bool] = None) -> None:
        """
        Sets the v13_0 property value. When TRUE, indicates macOS 13.0 or later is required to install the app. When FALSE, indicates some other OS version is the minimum OS to install the app. Default value is FALSE.
        Args:
            value: Value to set for the v13_0 property.
        """
        self._v13_0 = value
    

