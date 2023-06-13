from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import url_match_info, url_to_item_resolver_base

from . import url_to_item_resolver_base

@dataclass
class ItemIdResolver(url_to_item_resolver_base.UrlToItemResolverBase):
    odata_type = "#microsoft.graph.externalConnectors.itemIdResolver"
    # Pattern that specifies how to form the ID of the external item that the URL represents. The named groups from the regular expression in urlPattern within the urlMatchInfo can be referenced by inserting the group name inside curly brackets.
    item_id: Optional[str] = None
    # Configurations to match and resolve URL.
    url_match_info: Optional[url_match_info.UrlMatchInfo] = None
    
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
    

