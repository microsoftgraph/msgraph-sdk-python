from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .level import Level

from .entity import Entity

@dataclass
class LearningContent(Entity, Parsable):
    # Keywords, topics, and other tags associated with the learning content. Optional.
    additional_tags: Optional[list[str]] = None
    # The content web URL for the learning content. Required.
    content_web_url: Optional[str] = None
    # The authors, creators, or contributors of the learning content. Optional.
    contributors: Optional[list[str]] = None
    # The date and time when the learning content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
    created_date_time: Optional[datetime.datetime] = None
    # The description or summary for the learning content. Optional.
    description: Optional[str] = None
    # The duration of the learning content in seconds. The value is represented in ISO 8601 format for durations. Optional.
    duration: Optional[datetime.timedelta] = None
    # Unique external content ID for the learning content. Required.
    external_id: Optional[str] = None
    # The format of the learning content. For example, Course, Video, Book, Book Summary, Audiobook Summary. Optional.
    format: Optional[str] = None
    # Indicates whether the content is active or not. Inactive content doesn't show up in the UI. The default value is true. Optional.
    is_active: Optional[bool] = None
    # Indicates whether the learning content requires the user to sign-in on the learning provider platform or not. The default value is false. Optional.
    is_premium: Optional[bool] = None
    # Indicates whether the learning content is searchable or not. The default value is true. Optional.
    is_searchable: Optional[bool] = None
    # The language of the learning content, for example, en-us or fr-fr. Required.
    language_tag: Optional[str] = None
    # The date and time when the learning content was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The difficulty level of the learning content. The possible values are: Beginner, Intermediate, Advanced, unknownFutureValue. Optional.
    level: Optional[Level] = None
    # The number of pages of the learning content, for example, 9. Optional.
    number_of_pages: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The skills tags associated with the learning content. Optional.
    skill_tags: Optional[list[str]] = None
    # The source name of the learning content, such as LinkedIn Learning or Coursera. Optional.
    source_name: Optional[str] = None
    # The URL of learning content thumbnail image. Optional.
    thumbnail_web_url: Optional[str] = None
    # The title of the learning content. Required.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LearningContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LearningContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LearningContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .level import Level

        from .entity import Entity
        from .level import Level

        fields: dict[str, Callable[[Any], None]] = {
            "additionalTags": lambda n : setattr(self, 'additional_tags', n.get_collection_of_primitive_values(str)),
            "contentWebUrl": lambda n : setattr(self, 'content_web_url', n.get_str_value()),
            "contributors": lambda n : setattr(self, 'contributors', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "isPremium": lambda n : setattr(self, 'is_premium', n.get_bool_value()),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "level": lambda n : setattr(self, 'level', n.get_enum_value(Level)),
            "numberOfPages": lambda n : setattr(self, 'number_of_pages', n.get_int_value()),
            "skillTags": lambda n : setattr(self, 'skill_tags', n.get_collection_of_primitive_values(str)),
            "sourceName": lambda n : setattr(self, 'source_name', n.get_str_value()),
            "thumbnailWebUrl": lambda n : setattr(self, 'thumbnail_web_url', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("additionalTags", self.additional_tags)
        writer.write_str_value("contentWebUrl", self.content_web_url)
        writer.write_collection_of_primitive_values("contributors", self.contributors)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_timedelta_value("duration", self.duration)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("format", self.format)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_bool_value("isPremium", self.is_premium)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("level", self.level)
        writer.write_int_value("numberOfPages", self.number_of_pages)
        writer.write_collection_of_primitive_values("skillTags", self.skill_tags)
        writer.write_str_value("sourceName", self.source_name)
        writer.write_str_value("thumbnailWebUrl", self.thumbnail_web_url)
        writer.write_str_value("title", self.title)
    

