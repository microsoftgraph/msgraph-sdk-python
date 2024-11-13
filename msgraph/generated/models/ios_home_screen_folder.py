from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_home_screen_folder_page import IosHomeScreenFolderPage
    from .ios_home_screen_item import IosHomeScreenItem

from .ios_home_screen_item import IosHomeScreenItem

@dataclass
class IosHomeScreenFolder(IosHomeScreenItem, Parsable):
    """
    A folder containing pages of apps and web clips on the Home Screen.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosHomeScreenFolder"
    # Pages of Home Screen Layout Icons which must be applications or web clips. This collection can contain a maximum of 500 elements.
    pages: Optional[List[IosHomeScreenFolderPage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosHomeScreenFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosHomeScreenFolder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosHomeScreenFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_home_screen_folder_page import IosHomeScreenFolderPage
        from .ios_home_screen_item import IosHomeScreenItem

        from .ios_home_screen_folder_page import IosHomeScreenFolderPage
        from .ios_home_screen_item import IosHomeScreenItem

        fields: Dict[str, Callable[[Any], None]] = {
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(IosHomeScreenFolderPage)),
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
        from .ios_home_screen_folder_page import IosHomeScreenFolderPage
        from .ios_home_screen_item import IosHomeScreenItem

        writer.write_collection_of_object_values("pages", self.pages)
    

