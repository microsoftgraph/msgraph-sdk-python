from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WindowsDefenderScanPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the windowsDefenderScan method.
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
        Instantiates a new windowsDefenderScanPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The quickScan property
        self._quick_scan: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderScanPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderScanPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDefenderScanPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "quick_scan": lambda n : setattr(self, 'quick_scan', n.get_bool_value()),
        }
        return fields
    
    @property
    def quick_scan(self,) -> Optional[bool]:
        """
        Gets the quickScan property value. The quickScan property
        Returns: Optional[bool]
        """
        return self._quick_scan
    
    @quick_scan.setter
    def quick_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the quickScan property value. The quickScan property
        Args:
            value: Value to set for the quickScan property.
        """
        self._quick_scan = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("quickScan", self.quick_scan)
        writer.write_additional_data_value(self.additional_data)
    

