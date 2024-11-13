from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_home_screen_item import IosHomeScreenItem

from .ios_home_screen_item import IosHomeScreenItem

@dataclass
class IosHomeScreenApp(IosHomeScreenItem, Parsable):
    """
    Represents an icon for an app on the Home Screen
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosHomeScreenApp"
    # BundleID of the app if isWebClip is false or the URL of a web clip if isWebClip is true.
    bundle_i_d: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosHomeScreenApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosHomeScreenApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosHomeScreenApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_home_screen_item import IosHomeScreenItem

        from .ios_home_screen_item import IosHomeScreenItem

        fields: Dict[str, Callable[[Any], None]] = {
            "bundleID": lambda n : setattr(self, 'bundle_i_d', n.get_str_value()),
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
        from .ios_home_screen_item import IosHomeScreenItem

        writer.write_str_value("bundleID", self.bundle_i_d)
    

