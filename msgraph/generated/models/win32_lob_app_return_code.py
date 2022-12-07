from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_return_code_type = lazy_import('msgraph.generated.models.win32_lob_app_return_code_type')

class Win32LobAppReturnCode(AdditionalDataHolder, Parsable):
    """
    Contains return code properties for a Win32 App
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
        Instantiates a new win32LobAppReturnCode and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Return code.
        self._return_code: Optional[int] = None
        # Indicates the type of return code.
        self._type: Optional[win32_lob_app_return_code_type.Win32LobAppReturnCodeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppReturnCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppReturnCode
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppReturnCode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "return_code": lambda n : setattr(self, 'return_code', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(win32_lob_app_return_code_type.Win32LobAppReturnCodeType)),
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
    
    @property
    def return_code(self,) -> Optional[int]:
        """
        Gets the returnCode property value. Return code.
        Returns: Optional[int]
        """
        return self._return_code
    
    @return_code.setter
    def return_code(self,value: Optional[int] = None) -> None:
        """
        Sets the returnCode property value. Return code.
        Args:
            value: Value to set for the returnCode property.
        """
        self._return_code = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("returnCode", self.return_code)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[win32_lob_app_return_code_type.Win32LobAppReturnCodeType]:
        """
        Gets the type property value. Indicates the type of return code.
        Returns: Optional[win32_lob_app_return_code_type.Win32LobAppReturnCodeType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[win32_lob_app_return_code_type.Win32LobAppReturnCodeType] = None) -> None:
        """
        Sets the type property value. Indicates the type of return code.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

