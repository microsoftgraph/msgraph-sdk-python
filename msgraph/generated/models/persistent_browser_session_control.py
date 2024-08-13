from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_session_control import ConditionalAccessSessionControl
    from .persistent_browser_session_mode import PersistentBrowserSessionMode

from .conditional_access_session_control import ConditionalAccessSessionControl

@dataclass
class PersistentBrowserSessionControl(ConditionalAccessSessionControl):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.persistentBrowserSessionControl"
    # Possible values are: always, never.
    mode: Optional[PersistentBrowserSessionMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PersistentBrowserSessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PersistentBrowserSessionControl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PersistentBrowserSessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_session_control import ConditionalAccessSessionControl
        from .persistent_browser_session_mode import PersistentBrowserSessionMode

        from .conditional_access_session_control import ConditionalAccessSessionControl
        from .persistent_browser_session_mode import PersistentBrowserSessionMode

        fields: Dict[str, Callable[[Any], None]] = {
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(PersistentBrowserSessionMode)),
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
        writer.write_enum_value("mode", self.mode)
    

