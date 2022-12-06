from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_session_control = lazy_import('msgraph.generated.models.conditional_access_session_control')
persistent_browser_session_mode = lazy_import('msgraph.generated.models.persistent_browser_session_mode')

class PersistentBrowserSessionControl(conditional_access_session_control.ConditionalAccessSessionControl):
    def __init__(self,) -> None:
        """
        Instantiates a new PersistentBrowserSessionControl and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.persistentBrowserSessionControl"
        # Possible values are: always, never.
        self._mode: Optional[persistent_browser_session_mode.PersistentBrowserSessionMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PersistentBrowserSessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PersistentBrowserSessionControl
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PersistentBrowserSessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(persistent_browser_session_mode.PersistentBrowserSessionMode)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mode(self,) -> Optional[persistent_browser_session_mode.PersistentBrowserSessionMode]:
        """
        Gets the mode property value. Possible values are: always, never.
        Returns: Optional[persistent_browser_session_mode.PersistentBrowserSessionMode]
        """
        return self._mode
    
    @mode.setter
    def mode(self,value: Optional[persistent_browser_session_mode.PersistentBrowserSessionMode] = None) -> None:
        """
        Sets the mode property value. Possible values are: always, never.
        Args:
            value: Value to set for the mode property.
        """
        self._mode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("mode", self.mode)
    

