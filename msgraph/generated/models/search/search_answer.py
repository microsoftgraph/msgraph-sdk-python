from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .acronym import Acronym
    from .bookmark import Bookmark
    from .identity_set import IdentitySet
    from .qna import Qna

from ..entity import Entity

@dataclass
class SearchAnswer(Entity, Parsable):
    # The search answer description that is shown on the search results page.
    description: Optional[str] = None
    # The search answer name that is displayed in search results.
    display_name: Optional[str] = None
    # Details of the user who created or last modified the search answer. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time when the search answer was created or last edited. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL link for the search answer. When users select this search answer from the search results, they are directed to the specified URL.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchAnswer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.acronym".casefold():
            from .acronym import Acronym

            return Acronym()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.bookmark".casefold():
            from .bookmark import Bookmark

            return Bookmark()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.qna".casefold():
            from .qna import Qna

            return Qna()
        return SearchAnswer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .acronym import Acronym
        from .bookmark import Bookmark
        from .identity_set import IdentitySet
        from .qna import Qna

        from ..entity import Entity
        from .acronym import Acronym
        from .bookmark import Bookmark
        from .identity_set import IdentitySet
        from .qna import Qna

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("webUrl", self.web_url)
    

