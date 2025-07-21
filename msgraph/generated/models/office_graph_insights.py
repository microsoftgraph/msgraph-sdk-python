from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .item_insights import ItemInsights
    from .shared_insight import SharedInsight
    from .trending import Trending
    from .used_insight import UsedInsight

from .entity import Entity

@dataclass
class OfficeGraphInsights(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Calculated relationship that identifies documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for work or school and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.
    shared: Optional[list[SharedInsight]] = None
    # Calculated relationship that identifies documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for work or school and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.
    trending: Optional[list[Trending]] = None
    # Calculated relationship that identifies the latest documents viewed or modified by a user, including OneDrive for work or school and SharePoint documents, ranked by recency of use.
    used: Optional[list[UsedInsight]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OfficeGraphInsights:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OfficeGraphInsights
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemInsights".casefold():
            from .item_insights import ItemInsights

            return ItemInsights()
        return OfficeGraphInsights()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .item_insights import ItemInsights
        from .shared_insight import SharedInsight
        from .trending import Trending
        from .used_insight import UsedInsight

        from .entity import Entity
        from .item_insights import ItemInsights
        from .shared_insight import SharedInsight
        from .trending import Trending
        from .used_insight import UsedInsight

        fields: dict[str, Callable[[Any], None]] = {
            "shared": lambda n : setattr(self, 'shared', n.get_collection_of_object_values(SharedInsight)),
            "trending": lambda n : setattr(self, 'trending', n.get_collection_of_object_values(Trending)),
            "used": lambda n : setattr(self, 'used', n.get_collection_of_object_values(UsedInsight)),
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
        writer.write_collection_of_object_values("shared", self.shared)
        writer.write_collection_of_object_values("trending", self.trending)
        writer.write_collection_of_object_values("used", self.used)
    

