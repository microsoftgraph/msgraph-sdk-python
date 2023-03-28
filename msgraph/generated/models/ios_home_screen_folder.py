from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_home_screen_folder_page = lazy_import('msgraph.generated.models.ios_home_screen_folder_page')
ios_home_screen_item = lazy_import('msgraph.generated.models.ios_home_screen_item')

class IosHomeScreenFolder(ios_home_screen_item.IosHomeScreenItem):
    def __init__(self,) -> None:
        """
        Instantiates a new IosHomeScreenFolder and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosHomeScreenFolder"
        # Pages of Home Screen Layout Icons which must be applications or web clips. This collection can contain a maximum of 500 elements.
        self._pages: Optional[List[ios_home_screen_folder_page.IosHomeScreenFolderPage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosHomeScreenFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosHomeScreenFolder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosHomeScreenFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(ios_home_screen_folder_page.IosHomeScreenFolderPage)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def pages(self,) -> Optional[List[ios_home_screen_folder_page.IosHomeScreenFolderPage]]:
        """
        Gets the pages property value. Pages of Home Screen Layout Icons which must be applications or web clips. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_home_screen_folder_page.IosHomeScreenFolderPage]]
        """
        return self._pages
    
    @pages.setter
    def pages(self,value: Optional[List[ios_home_screen_folder_page.IosHomeScreenFolderPage]] = None) -> None:
        """
        Sets the pages property value. Pages of Home Screen Layout Icons which must be applications or web clips. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the pages property.
        """
        self._pages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("pages", self.pages)
    

