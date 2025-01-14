from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .microsoft_edge_channel import MicrosoftEdgeChannel
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class WindowsMicrosoftEdgeApp(MobileApp, Parsable):
    """
    Contains properties and inherited properties for the Microsoft Edge app on Windows.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsMicrosoftEdgeApp"
    # The enum to specify the channels for Microsoft Edge apps.
    channel: Optional[MicrosoftEdgeChannel] = None
    # The language locale to use when the Edge app displays text to the user.
    display_language_locale: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsMicrosoftEdgeApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMicrosoftEdgeApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsMicrosoftEdgeApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .microsoft_edge_channel import MicrosoftEdgeChannel
        from .mobile_app import MobileApp

        from .microsoft_edge_channel import MicrosoftEdgeChannel
        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(MicrosoftEdgeChannel)),
            "displayLanguageLocale": lambda n : setattr(self, 'display_language_locale', n.get_str_value()),
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
        writer.write_enum_value("channel", self.channel)
        writer.write_str_value("displayLanguageLocale", self.display_language_locale)
    

