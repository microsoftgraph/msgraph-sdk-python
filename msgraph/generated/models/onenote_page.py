from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

notebook = lazy_import('msgraph.generated.models.notebook')
onenote_entity_schema_object_model = lazy_import('msgraph.generated.models.onenote_entity_schema_object_model')
onenote_section = lazy_import('msgraph.generated.models.onenote_section')
page_links = lazy_import('msgraph.generated.models.page_links')

class OnenotePage(onenote_entity_schema_object_model.OnenoteEntitySchemaObjectModel):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new onenotePage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onenotePage"
        # The page's HTML content.
        self._content: Optional[bytes] = None
        # The URL for the page's HTML content.  Read-only.
        self._content_url: Optional[str] = None
        # The unique identifier of the application that created the page. Read-only.
        self._created_by_app_id: Optional[str] = None
        # The date and time when the page was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The indentation level of the page. Read-only.
        self._level: Optional[int] = None
        # Links for opening the page. The oneNoteClientURL link opens the page in the OneNote native client if it 's installed. The oneNoteWebUrl link opens the page in OneNote on the web. Read-only.
        self._links: Optional[page_links.PageLinks] = None
        # The order of the page within its parent section. Read-only.
        self._order: Optional[int] = None
        # The notebook that contains the page.  Read-only.
        self._parent_notebook: Optional[notebook.Notebook] = None
        # The section that contains the page. Read-only.
        self._parent_section: Optional[onenote_section.OnenoteSection] = None
        # The title of the page.
        self._title: Optional[str] = None
        # The userTags property
        self._user_tags: Optional[List[str]] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The page's HTML content.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The page's HTML content.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def content_url(self,) -> Optional[str]:
        """
        Gets the contentUrl property value. The URL for the page's HTML content.  Read-only.
        Returns: Optional[str]
        """
        return self._content_url
    
    @content_url.setter
    def content_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentUrl property value. The URL for the page's HTML content.  Read-only.
        Args:
            value: Value to set for the contentUrl property.
        """
        self._content_url = value
    
    @property
    def created_by_app_id(self,) -> Optional[str]:
        """
        Gets the createdByAppId property value. The unique identifier of the application that created the page. Read-only.
        Returns: Optional[str]
        """
        return self._created_by_app_id
    
    @created_by_app_id.setter
    def created_by_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByAppId property value. The unique identifier of the application that created the page. Read-only.
        Args:
            value: Value to set for the createdByAppId property.
        """
        self._created_by_app_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenotePage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenotePage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "content_url": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "created_by_app_id": lambda n : setattr(self, 'created_by_app_id', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "level": lambda n : setattr(self, 'level', n.get_int_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(page_links.PageLinks)),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "parent_notebook": lambda n : setattr(self, 'parent_notebook', n.get_object_value(notebook.Notebook)),
            "parent_section": lambda n : setattr(self, 'parent_section', n.get_object_value(onenote_section.OnenoteSection)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "user_tags": lambda n : setattr(self, 'user_tags', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the page was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the page was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def level(self,) -> Optional[int]:
        """
        Gets the level property value. The indentation level of the page. Read-only.
        Returns: Optional[int]
        """
        return self._level
    
    @level.setter
    def level(self,value: Optional[int] = None) -> None:
        """
        Sets the level property value. The indentation level of the page. Read-only.
        Args:
            value: Value to set for the level property.
        """
        self._level = value
    
    @property
    def links(self,) -> Optional[page_links.PageLinks]:
        """
        Gets the links property value. Links for opening the page. The oneNoteClientURL link opens the page in the OneNote native client if it 's installed. The oneNoteWebUrl link opens the page in OneNote on the web. Read-only.
        Returns: Optional[page_links.PageLinks]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[page_links.PageLinks] = None) -> None:
        """
        Sets the links property value. Links for opening the page. The oneNoteClientURL link opens the page in the OneNote native client if it 's installed. The oneNoteWebUrl link opens the page in OneNote on the web. Read-only.
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
    @property
    def order(self,) -> Optional[int]:
        """
        Gets the order property value. The order of the page within its parent section. Read-only.
        Returns: Optional[int]
        """
        return self._order
    
    @order.setter
    def order(self,value: Optional[int] = None) -> None:
        """
        Sets the order property value. The order of the page within its parent section. Read-only.
        Args:
            value: Value to set for the order property.
        """
        self._order = value
    
    @property
    def parent_notebook(self,) -> Optional[notebook.Notebook]:
        """
        Gets the parentNotebook property value. The notebook that contains the page.  Read-only.
        Returns: Optional[notebook.Notebook]
        """
        return self._parent_notebook
    
    @parent_notebook.setter
    def parent_notebook(self,value: Optional[notebook.Notebook] = None) -> None:
        """
        Sets the parentNotebook property value. The notebook that contains the page.  Read-only.
        Args:
            value: Value to set for the parentNotebook property.
        """
        self._parent_notebook = value
    
    @property
    def parent_section(self,) -> Optional[onenote_section.OnenoteSection]:
        """
        Gets the parentSection property value. The section that contains the page. Read-only.
        Returns: Optional[onenote_section.OnenoteSection]
        """
        return self._parent_section
    
    @parent_section.setter
    def parent_section(self,value: Optional[onenote_section.OnenoteSection] = None) -> None:
        """
        Sets the parentSection property value. The section that contains the page. Read-only.
        Args:
            value: Value to set for the parentSection property.
        """
        self._parent_section = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("content", self.content)
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
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of the page.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of the page.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def user_tags(self,) -> Optional[List[str]]:
        """
        Gets the userTags property value. The userTags property
        Returns: Optional[List[str]]
        """
        return self._user_tags
    
    @user_tags.setter
    def user_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the userTags property value. The userTags property
        Args:
            value: Value to set for the userTags property.
        """
        self._user_tags = value
    

