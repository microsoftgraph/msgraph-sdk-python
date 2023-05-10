from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import url_match_info, url_to_item_resolver_base

from . import url_to_item_resolver_base

class ItemIdResolver(url_to_item_resolver_base.UrlToItemResolverBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemIdResolver and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.externalConnectors.itemIdResolver"
        # Pattern that specifies how to form the ID of the external item that the URL represents. The named groups from the regular expression in urlPattern within the urlMatchInfo can be referenced by inserting the group name inside curly brackets.
        self._item_id: Optional[str] = None
        # Configurations to match and resolve URL.
        self._url_match_info: Optional[url_match_info.UrlMatchInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemIdResolver:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemIdResolver
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemIdResolver()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import url_match_info, url_to_item_resolver_base

        fields: Dict[str, Callable[[Any], None]] = {
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "urlMatchInfo": lambda n : setattr(self, 'url_match_info', n.get_object_value(url_match_info.UrlMatchInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def item_id(self,) -> Optional[str]:
        """
        Gets the itemId property value. Pattern that specifies how to form the ID of the external item that the URL represents. The named groups from the regular expression in urlPattern within the urlMatchInfo can be referenced by inserting the group name inside curly brackets.
        Returns: Optional[str]
        """
        return self._item_id
    
    @item_id.setter
    def item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the itemId property value. Pattern that specifies how to form the ID of the external item that the URL represents. The named groups from the regular expression in urlPattern within the urlMatchInfo can be referenced by inserting the group name inside curly brackets.
        Args:
            value: Value to set for the item_id property.
        """
        self._item_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("itemId", self.item_id)
        writer.write_object_value("urlMatchInfo", self.url_match_info)
    
    @property
    def url_match_info(self,) -> Optional[url_match_info.UrlMatchInfo]:
        """
        Gets the urlMatchInfo property value. Configurations to match and resolve URL.
        Returns: Optional[url_match_info.UrlMatchInfo]
        """
        return self._url_match_info
    
    @url_match_info.setter
    def url_match_info(self,value: Optional[url_match_info.UrlMatchInfo] = None) -> None:
        """
        Sets the urlMatchInfo property value. Configurations to match and resolve URL.
        Args:
            value: Value to set for the url_match_info property.
        """
        self._url_match_info = value
    

