from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OcrSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new ocrSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether or not OCR is enabled for the case.
        self._is_enabled: Optional[bool] = None
        # Maximum image size that will be processed in KB).
        self._max_image_size: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The timeout duration for the OCR engine. A longer timeout might increase success of OCR, but might add to the total processing time.
        self._timeout: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OcrSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OcrSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OcrSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "max_image_size": lambda n : setattr(self, 'max_image_size', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeout": lambda n : setattr(self, 'timeout', n.get_object_value(Timedelta)),
        }
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether or not OCR is enabled for the case.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether or not OCR is enabled for the case.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def max_image_size(self,) -> Optional[int]:
        """
        Gets the maxImageSize property value. Maximum image size that will be processed in KB).
        Returns: Optional[int]
        """
        return self._max_image_size
    
    @max_image_size.setter
    def max_image_size(self,value: Optional[int] = None) -> None:
        """
        Sets the maxImageSize property value. Maximum image size that will be processed in KB).
        Args:
            value: Value to set for the maxImageSize property.
        """
        self._max_image_size = value
    
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("maxImageSize", self.max_image_size)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("timeout", self.timeout)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def timeout(self,) -> Optional[Timedelta]:
        """
        Gets the timeout property value. The timeout duration for the OCR engine. A longer timeout might increase success of OCR, but might add to the total processing time.
        Returns: Optional[Timedelta]
        """
        return self._timeout
    
    @timeout.setter
    def timeout(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the timeout property value. The timeout duration for the OCR engine. A longer timeout might increase success of OCR, but might add to the total processing time.
        Args:
            value: Value to set for the timeout property.
        """
        self._timeout = value
    

