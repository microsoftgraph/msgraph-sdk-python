from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .oma_setting import OmaSetting

from .oma_setting import OmaSetting

@dataclass
class OmaSettingStringXml(OmaSetting, Parsable):
    """
    OMA Settings StringXML definition.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.omaSettingStringXml"
    # File name associated with the Value property (.xml).
    file_name: Optional[str] = None
    # Value. (UTF8 encoded byte array)
    value: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OmaSettingStringXml:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OmaSettingStringXml
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OmaSettingStringXml()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .oma_setting import OmaSetting

        from .oma_setting import OmaSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_bytes_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .oma_setting import OmaSetting

        writer.write_str_value("fileName", self.file_name)
        writer.write_bytes_value("value", self.value)
    

