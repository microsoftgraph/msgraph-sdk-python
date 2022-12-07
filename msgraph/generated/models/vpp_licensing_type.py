from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VppLicensingType(AdditionalDataHolder, Parsable):
    """
    Contains properties for iOS Volume-Purchased Program (Vpp) Licensing Type.
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
        Instantiates a new vppLicensingType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Whether the program supports the device licensing type.
        self._supports_device_licensing: Optional[bool] = None
        # Whether the program supports the user licensing type.
        self._supports_user_licensing: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VppLicensingType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VppLicensingType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VppLicensingType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supports_device_licensing": lambda n : setattr(self, 'supports_device_licensing', n.get_bool_value()),
            "supports_user_licensing": lambda n : setattr(self, 'supports_user_licensing', n.get_bool_value()),
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
        writer.write_bool_value("supportsDeviceLicensing", self.supports_device_licensing)
        writer.write_bool_value("supportsUserLicensing", self.supports_user_licensing)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def supports_device_licensing(self,) -> Optional[bool]:
        """
        Gets the supportsDeviceLicensing property value. Whether the program supports the device licensing type.
        Returns: Optional[bool]
        """
        return self._supports_device_licensing
    
    @supports_device_licensing.setter
    def supports_device_licensing(self,value: Optional[bool] = None) -> None:
        """
        Sets the supportsDeviceLicensing property value. Whether the program supports the device licensing type.
        Args:
            value: Value to set for the supportsDeviceLicensing property.
        """
        self._supports_device_licensing = value
    
    @property
    def supports_user_licensing(self,) -> Optional[bool]:
        """
        Gets the supportsUserLicensing property value. Whether the program supports the user licensing type.
        Returns: Optional[bool]
        """
        return self._supports_user_licensing
    
    @supports_user_licensing.setter
    def supports_user_licensing(self,value: Optional[bool] = None) -> None:
        """
        Sets the supportsUserLicensing property value. Whether the program supports the user licensing type.
        Args:
            value: Value to set for the supportsUserLicensing property.
        """
        self._supports_user_licensing = value
    

