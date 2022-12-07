from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class IosDeviceType(AdditionalDataHolder, Parsable):
    """
    Contains properties of the possible iOS device types the mobile app can run on.
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
        Instantiates a new iosDeviceType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether the app should run on iPads.
        self._i_pad: Optional[bool] = None
        # Whether the app should run on iPhones and iPods.
        self._i_phone_and_i_pod: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDeviceType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosDeviceType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosDeviceType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "i_pad": lambda n : setattr(self, 'i_pad', n.get_bool_value()),
            "i_phone_and_i_pod": lambda n : setattr(self, 'i_phone_and_i_pod', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def i_pad(self,) -> Optional[bool]:
        """
        Gets the iPad property value. Whether the app should run on iPads.
        Returns: Optional[bool]
        """
        return self._i_pad
    
    @i_pad.setter
    def i_pad(self,value: Optional[bool] = None) -> None:
        """
        Sets the iPad property value. Whether the app should run on iPads.
        Args:
            value: Value to set for the iPad property.
        """
        self._i_pad = value
    
    @property
    def i_phone_and_i_pod(self,) -> Optional[bool]:
        """
        Gets the iPhoneAndIPod property value. Whether the app should run on iPhones and iPods.
        Returns: Optional[bool]
        """
        return self._i_phone_and_i_pod
    
    @i_phone_and_i_pod.setter
    def i_phone_and_i_pod(self,value: Optional[bool] = None) -> None:
        """
        Sets the iPhoneAndIPod property value. Whether the app should run on iPhones and iPods.
        Args:
            value: Value to set for the iPhoneAndIPod property.
        """
        self._i_phone_and_i_pod = value
    
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
        writer.write_bool_value("iPad", self.i_pad)
        writer.write_bool_value("iPhoneAndIPod", self.i_phone_and_i_pod)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

