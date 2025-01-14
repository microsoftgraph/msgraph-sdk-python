from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .learning_content import LearningContent
    from .learning_course_activity import LearningCourseActivity

from .entity import Entity

@dataclass
class LearningProvider(Entity, Parsable):
    # The display name that appears in Viva Learning. Required.
    display_name: Optional[str] = None
    # Indicates whether a provider can ingest learning course activity records. The default value is false. Set to true to make learningCourseActivities available for this provider.
    is_course_activity_sync_enabled: Optional[bool] = None
    # Learning catalog items for the provider.
    learning_contents: Optional[list[LearningContent]] = None
    # The learningCourseActivities property
    learning_course_activities: Optional[list[LearningCourseActivity]] = None
    # Authentication URL to access the courses for the provider. Optional.
    login_web_url: Optional[str] = None
    # The long logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
    long_logo_web_url_for_dark_theme: Optional[str] = None
    # The long logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
    long_logo_web_url_for_light_theme: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The square logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
    square_logo_web_url_for_dark_theme: Optional[str] = None
    # The square logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
    square_logo_web_url_for_light_theme: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LearningProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LearningProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LearningProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .learning_content import LearningContent
        from .learning_course_activity import LearningCourseActivity

        from .entity import Entity
        from .learning_content import LearningContent
        from .learning_course_activity import LearningCourseActivity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isCourseActivitySyncEnabled": lambda n : setattr(self, 'is_course_activity_sync_enabled', n.get_bool_value()),
            "learningContents": lambda n : setattr(self, 'learning_contents', n.get_collection_of_object_values(LearningContent)),
            "learningCourseActivities": lambda n : setattr(self, 'learning_course_activities', n.get_collection_of_object_values(LearningCourseActivity)),
            "loginWebUrl": lambda n : setattr(self, 'login_web_url', n.get_str_value()),
            "longLogoWebUrlForDarkTheme": lambda n : setattr(self, 'long_logo_web_url_for_dark_theme', n.get_str_value()),
            "longLogoWebUrlForLightTheme": lambda n : setattr(self, 'long_logo_web_url_for_light_theme', n.get_str_value()),
            "squareLogoWebUrlForDarkTheme": lambda n : setattr(self, 'square_logo_web_url_for_dark_theme', n.get_str_value()),
            "squareLogoWebUrlForLightTheme": lambda n : setattr(self, 'square_logo_web_url_for_light_theme', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isCourseActivitySyncEnabled", self.is_course_activity_sync_enabled)
        writer.write_collection_of_object_values("learningContents", self.learning_contents)
        writer.write_collection_of_object_values("learningCourseActivities", self.learning_course_activities)
        writer.write_str_value("loginWebUrl", self.login_web_url)
        writer.write_str_value("longLogoWebUrlForDarkTheme", self.long_logo_web_url_for_dark_theme)
        writer.write_str_value("longLogoWebUrlForLightTheme", self.long_logo_web_url_for_light_theme)
        writer.write_str_value("squareLogoWebUrlForDarkTheme", self.square_logo_web_url_for_dark_theme)
        writer.write_str_value("squareLogoWebUrlForLightTheme", self.square_logo_web_url_for_light_theme)
    

