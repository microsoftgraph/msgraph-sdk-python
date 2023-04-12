from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_site_list, entity

from . import entity

class InternetExplorerMode(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new internetExplorerMode and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of site lists to support Internet Explorer mode.
        self._site_lists: Optional[List[browser_site_list.BrowserSiteList]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InternetExplorerMode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InternetExplorerMode
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InternetExplorerMode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import browser_site_list, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "siteLists": lambda n : setattr(self, 'site_lists', n.get_collection_of_object_values(browser_site_list.BrowserSiteList)),
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
        writer.write_collection_of_object_values("siteLists", self.site_lists)
    
    @property
    def site_lists(self,) -> Optional[List[browser_site_list.BrowserSiteList]]:
        """
        Gets the siteLists property value. A collection of site lists to support Internet Explorer mode.
        Returns: Optional[List[browser_site_list.BrowserSiteList]]
        """
        return self._site_lists
    
    @site_lists.setter
    def site_lists(self,value: Optional[List[browser_site_list.BrowserSiteList]] = None) -> None:
        """
        Sets the siteLists property value. A collection of site lists to support Internet Explorer mode.
        Args:
            value: Value to set for the site_lists property.
        """
        self._site_lists = value
    

