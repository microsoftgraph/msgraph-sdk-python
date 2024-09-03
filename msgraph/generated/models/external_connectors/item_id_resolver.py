from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .url_match_info import UrlMatchInfo
    from .url_to_item_resolver_base import UrlToItemResolverBase

from .url_to_item_resolver_base import UrlToItemResolverBase

@dataclass
class ItemIdResolver(UrlToItemResolverBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalConnectors.itemIdResolver"
    # Pattern that specifies how to form the ID of the external item that the URL represents. The named groups from the regular expression in urlPattern within the urlMatchInfo can be referenced by inserting the group name inside curly brackets.
    item_id: Optional[str] = None
    # Configurations to match and resolve URL.
    url_match_info: Optional[UrlMatchInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemIdResolver:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemIdResolver
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemIdResolver()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .url_match_info import UrlMatchInfo
        from .url_to_item_resolver_base import UrlToItemResolverBase

        from .url_match_info import UrlMatchInfo
        from .url_to_item_resolver_base import UrlToItemResolverBase

        fields: Dict[str, Callable[[Any], None]] = {
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "urlMatchInfo": lambda n : setattr(self, 'url_match_info', n.get_object_value(UrlMatchInfo)),
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
        writer.write_str_value("itemId", self.item_id)
        writer.write_object_value("urlMatchInfo", self.url_match_info)
    

