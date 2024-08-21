from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .article_indicator import ArticleIndicator
    from .formatted_content import FormattedContent

from ..entity import Entity

@dataclass
class Article(Entity):
    # The body property
    body: Optional[FormattedContent] = None
    # The date and time when this article was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # URL of the header image for this article, used for display purposes.
    image_url: Optional[str] = None
    # Indicators related to this article.
    indicators: Optional[List[ArticleIndicator]] = None
    # Indicates whether this article is currently featured by Microsoft.
    is_featured: Optional[bool] = None
    # The most recent date and time when this article was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The summary property
    summary: Optional[FormattedContent] = None
    # Tags for this article, communicating keywords, or key concepts.
    tags: Optional[List[str]] = None
    # The title of this article.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Article:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Article
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Article()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .article_indicator import ArticleIndicator
        from .formatted_content import FormattedContent

        from ..entity import Entity
        from .article_indicator import ArticleIndicator
        from .formatted_content import FormattedContent

        fields: Dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_object_value(FormattedContent)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "indicators": lambda n : setattr(self, 'indicators', n.get_collection_of_object_values(ArticleIndicator)),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(FormattedContent)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_object_value("body", self.body)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_collection_of_object_values("indicators", self.indicators)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
    

