from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_action_result

from . import device_action_result

class WindowsDefenderScanActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsDefenderScanActionResult and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Scan type either full scan or quick scan
        self._scan_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderScanActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderScanActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDefenderScanActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_action_result

        fields: Dict[str, Callable[[Any], None]] = {
            "scanType": lambda n : setattr(self, 'scan_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def scan_type(self,) -> Optional[str]:
        """
        Gets the scanType property value. Scan type either full scan or quick scan
        Returns: Optional[str]
        """
        return self._scan_type
    
    @scan_type.setter
    def scan_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scanType property value. Scan type either full scan or quick scan
        Args:
            value: Value to set for the scan_type property.
        """
        self._scan_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("scanType", self.scan_type)
    

