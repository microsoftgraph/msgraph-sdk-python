from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .search.acronym import Acronym
    from .search.bookmark import Bookmark
    from .search.qna import Qna

from .entity import Entity

@dataclass
class SearchEntity(Entity, Parsable):
    # Administrative answer in Microsoft Search results to define common acronyms in an organization.
    acronyms: Optional[list[Acronym]] = None
    # Administrative answer in Microsoft Search results for common search queries in an organization.
    bookmarks: Optional[list[Bookmark]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Administrative answer in Microsoft Search results that provide answers for specific search keywords in an organization.
    qnas: Optional[list[Qna]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .search.acronym import Acronym
        from .search.bookmark import Bookmark
        from .search.qna import Qna

        from .entity import Entity
        from .search.acronym import Acronym
        from .search.bookmark import Bookmark
        from .search.qna import Qna

        fields: dict[str, Callable[[Any], None]] = {
            "acronyms": lambda n : setattr(self, 'acronyms', n.get_collection_of_object_values(Acronym)),
            "bookmarks": lambda n : setattr(self, 'bookmarks', n.get_collection_of_object_values(Bookmark)),
            "qnas": lambda n : setattr(self, 'qnas', n.get_collection_of_object_values(Qna)),
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
        writer.write_collection_of_object_values("acronyms", self.acronyms)
        writer.write_collection_of_object_values("bookmarks", self.bookmarks)
        writer.write_collection_of_object_values("qnas", self.qnas)
    

