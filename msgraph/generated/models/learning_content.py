from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class LearningContent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new learningContent and sets the default values.
        """
        super().__init__()
        # Keywords, topics, and other tags associated with the learning content. Optional.
        self._additional_tags: Optional[List[str]] = None
        # The content web URL for the learning content. Required.
        self._content_web_url: Optional[str] = None
        # The authors, creators, or contributors of the learning content. Optional.
        self._contributors: Optional[List[str]] = None
        # The date and time when the learning content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        self._created_date_time: Optional[datetime] = None
        # The description or summary for the learning content. Optional.
        self._description: Optional[str] = None
        # The duration of the learning content in seconds. The value is represented in ISO 8601 format for durations. Optional.
        self._duration: Optional[timedelta] = None
        # Unique external content ID for the learning content. Required.
        self._external_id: Optional[str] = None
        # The format of the learning content. For example, Course, Video, Book, Book Summary, Audiobook Summary. Optional.
        self._format: Optional[str] = None
        # Indicates whether the content is active or not. Inactive content doesn't show up in the UI. The default value is true. Optional.
        self._is_active: Optional[bool] = None
        # Indicates whether the learning content requires the user to sign-in on the learning provider platform or not. The default value is false. Optional.
        self._is_premium: Optional[bool] = None
        # Indicates whether the learning content is searchable or not. The default value is true. Optional.
        self._is_searchable: Optional[bool] = None
        # The language of the learning content, for example, en-us or fr-fr. Required.
        self._language_tag: Optional[str] = None
        # The date and time when the learning content was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        self._last_modified_date_time: Optional[datetime] = None
        # The number of pages of the learning content, for example, 9. Optional.
        self._number_of_pages: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The skills tags associated with the learning content. Optional.
        self._skill_tags: Optional[List[str]] = None
        # The source name of the learning content, such as LinkedIn Learning or Coursera. Optional.
        self._source_name: Optional[str] = None
        # The URL of learning content thumbnail image. Optional.
        self._thumbnail_web_url: Optional[str] = None
        # The title of the learning content. Required.
        self._title: Optional[str] = None
    
    @property
    def additional_tags(self,) -> Optional[List[str]]:
        """
        Gets the additionalTags property value. Keywords, topics, and other tags associated with the learning content. Optional.
        Returns: Optional[List[str]]
        """
        return self._additional_tags
    
    @additional_tags.setter
    def additional_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the additionalTags property value. Keywords, topics, and other tags associated with the learning content. Optional.
        Args:
            value: Value to set for the additional_tags property.
        """
        self._additional_tags = value
    
    @property
    def content_web_url(self,) -> Optional[str]:
        """
        Gets the contentWebUrl property value. The content web URL for the learning content. Required.
        Returns: Optional[str]
        """
        return self._content_web_url
    
    @content_web_url.setter
    def content_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentWebUrl property value. The content web URL for the learning content. Required.
        Args:
            value: Value to set for the content_web_url property.
        """
        self._content_web_url = value
    
    @property
    def contributors(self,) -> Optional[List[str]]:
        """
        Gets the contributors property value. The authors, creators, or contributors of the learning content. Optional.
        Returns: Optional[List[str]]
        """
        return self._contributors
    
    @contributors.setter
    def contributors(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contributors property value. The authors, creators, or contributors of the learning content. Optional.
        Args:
            value: Value to set for the contributors property.
        """
        self._contributors = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the learning content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the learning content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LearningContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LearningContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LearningContent()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description or summary for the learning content. Optional.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description or summary for the learning content. Optional.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def duration(self,) -> Optional[timedelta]:
        """
        Gets the duration property value. The duration of the learning content in seconds. The value is represented in ISO 8601 format for durations. Optional.
        Returns: Optional[timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the duration property value. The duration of the learning content in seconds. The value is represented in ISO 8601 format for durations. Optional.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. Unique external content ID for the learning content. Required.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. Unique external content ID for the learning content. Required.
        Args:
            value: Value to set for the external_id property.
        """
        self._external_id = value
    
    @property
    def format(self,) -> Optional[str]:
        """
        Gets the format property value. The format of the learning content. For example, Course, Video, Book, Book Summary, Audiobook Summary. Optional.
        Returns: Optional[str]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[str] = None) -> None:
        """
        Sets the format property value. The format of the learning content. For example, Course, Video, Book, Book Summary, Audiobook Summary. Optional.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
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
            "numberOfPages": lambda n : setattr(self, 'number_of_pages', n.get_int_value()),
            "skillTags": lambda n : setattr(self, 'skill_tags', n.get_collection_of_primitive_values(str)),
            "sourceName": lambda n : setattr(self, 'source_name', n.get_str_value()),
            "thumbnailWebUrl": lambda n : setattr(self, 'thumbnail_web_url', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the content is active or not. Inactive content doesn't show up in the UI. The default value is true. Optional.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the content is active or not. Inactive content doesn't show up in the UI. The default value is true. Optional.
        Args:
            value: Value to set for the is_active property.
        """
        self._is_active = value
    
    @property
    def is_premium(self,) -> Optional[bool]:
        """
        Gets the isPremium property value. Indicates whether the learning content requires the user to sign-in on the learning provider platform or not. The default value is false. Optional.
        Returns: Optional[bool]
        """
        return self._is_premium
    
    @is_premium.setter
    def is_premium(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPremium property value. Indicates whether the learning content requires the user to sign-in on the learning provider platform or not. The default value is false. Optional.
        Args:
            value: Value to set for the is_premium property.
        """
        self._is_premium = value
    
    @property
    def is_searchable(self,) -> Optional[bool]:
        """
        Gets the isSearchable property value. Indicates whether the learning content is searchable or not. The default value is true. Optional.
        Returns: Optional[bool]
        """
        return self._is_searchable
    
    @is_searchable.setter
    def is_searchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSearchable property value. Indicates whether the learning content is searchable or not. The default value is true. Optional.
        Args:
            value: Value to set for the is_searchable property.
        """
        self._is_searchable = value
    
    @property
    def language_tag(self,) -> Optional[str]:
        """
        Gets the languageTag property value. The language of the learning content, for example, en-us or fr-fr. Required.
        Returns: Optional[str]
        """
        return self._language_tag
    
    @language_tag.setter
    def language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the languageTag property value. The language of the learning content, for example, en-us or fr-fr. Required.
        Args:
            value: Value to set for the language_tag property.
        """
        self._language_tag = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the learning content was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the learning content was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Optional.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def number_of_pages(self,) -> Optional[int]:
        """
        Gets the numberOfPages property value. The number of pages of the learning content, for example, 9. Optional.
        Returns: Optional[int]
        """
        return self._number_of_pages
    
    @number_of_pages.setter
    def number_of_pages(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfPages property value. The number of pages of the learning content, for example, 9. Optional.
        Args:
            value: Value to set for the number_of_pages property.
        """
        self._number_of_pages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_int_value("numberOfPages", self.number_of_pages)
        writer.write_collection_of_primitive_values("skillTags", self.skill_tags)
        writer.write_str_value("sourceName", self.source_name)
        writer.write_str_value("thumbnailWebUrl", self.thumbnail_web_url)
        writer.write_str_value("title", self.title)
    
    @property
    def skill_tags(self,) -> Optional[List[str]]:
        """
        Gets the skillTags property value. The skills tags associated with the learning content. Optional.
        Returns: Optional[List[str]]
        """
        return self._skill_tags
    
    @skill_tags.setter
    def skill_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the skillTags property value. The skills tags associated with the learning content. Optional.
        Args:
            value: Value to set for the skill_tags property.
        """
        self._skill_tags = value
    
    @property
    def source_name(self,) -> Optional[str]:
        """
        Gets the sourceName property value. The source name of the learning content, such as LinkedIn Learning or Coursera. Optional.
        Returns: Optional[str]
        """
        return self._source_name
    
    @source_name.setter
    def source_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceName property value. The source name of the learning content, such as LinkedIn Learning or Coursera. Optional.
        Args:
            value: Value to set for the source_name property.
        """
        self._source_name = value
    
    @property
    def thumbnail_web_url(self,) -> Optional[str]:
        """
        Gets the thumbnailWebUrl property value. The URL of learning content thumbnail image. Optional.
        Returns: Optional[str]
        """
        return self._thumbnail_web_url
    
    @thumbnail_web_url.setter
    def thumbnail_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailWebUrl property value. The URL of learning content thumbnail image. Optional.
        Args:
            value: Value to set for the thumbnail_web_url property.
        """
        self._thumbnail_web_url = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of the learning content. Required.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of the learning content. Required.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

