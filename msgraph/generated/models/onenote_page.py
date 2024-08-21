from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notebook import Notebook
    from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
    from .onenote_section import OnenoteSection
    from .page_links import PageLinks

from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel

@dataclass
class OnenotePage(OnenoteEntitySchemaObjectModel):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onenotePage"
    # The page's HTML content.
    content: Optional[bytes] = None
    # The URL for the page's HTML content.  Read-only.
    content_url: Optional[str] = None
    # The unique identifier of the application that created the page. Read-only.
    created_by_app_id: Optional[str] = None
    # The date and time when the page was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The indentation level of the page. Read-only.
    level: Optional[int] = None
    # Links for opening the page. The oneNoteClientURL link opens the page in the OneNote native client if it 's installed. The oneNoteWebUrl link opens the page in OneNote on the web. Read-only.
    links: Optional[PageLinks] = None
    # The order of the page within its parent section. Read-only.
    order: Optional[int] = None
    # The notebook that contains the page.  Read-only.
    parent_notebook: Optional[Notebook] = None
    # The section that contains the page. Read-only.
    parent_section: Optional[OnenoteSection] = None
    # The title of the page.
    title: Optional[str] = None
    # The userTags property
    user_tags: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenotePage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnenotePage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .notebook import Notebook
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_section import OnenoteSection
        from .page_links import PageLinks

        from .notebook import Notebook
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_section import OnenoteSection
        from .page_links import PageLinks

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "createdByAppId": lambda n : setattr(self, 'created_by_app_id', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "level": lambda n : setattr(self, 'level', n.get_int_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(PageLinks)),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "parentNotebook": lambda n : setattr(self, 'parent_notebook', n.get_object_value(Notebook)),
            "parentSection": lambda n : setattr(self, 'parent_section', n.get_object_value(OnenoteSection)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "userTags": lambda n : setattr(self, 'user_tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_bytes_value("content", self.content)
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_str_value("createdByAppId", self.created_by_app_id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("level", self.level)
        writer.write_object_value("links", self.links)
        writer.write_int_value("order", self.order)
        writer.write_object_value("parentNotebook", self.parent_notebook)
        writer.write_object_value("parentSection", self.parent_section)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_primitive_values("userTags", self.user_tags)
    

