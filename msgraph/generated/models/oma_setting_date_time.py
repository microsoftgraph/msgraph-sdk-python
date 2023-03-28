from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import oma_setting

from . import oma_setting

class OmaSettingDateTime(oma_setting.OmaSetting):
    def __init__(self,) -> None:
        """
        Instantiates a new OmaSettingDateTime and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.omaSettingDateTime"
        # Value.
        self._value: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSettingDateTime:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OmaSettingDateTime
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OmaSettingDateTime()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import oma_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("value", self.value)
    
    @property
    def value(self,) -> Optional[datetime]:
        """
        Gets the value property value. Value.
        Returns: Optional[datetime]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[datetime] = None) -> None:
        """
        Sets the value property value. Value.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

