from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
learning_content = lazy_import('msgraph.generated.models.learning_content')

class LearningProvider(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new learningProvider and sets the default values.
        """
        super().__init__()
        # The display name that appears in Viva Learning. Required.
        self._display_name: Optional[str] = None
        # Learning catalog items for the provider.
        self._learning_contents: Optional[List[learning_content.LearningContent]] = None
        # Authentication URL to access the courses for the provider. Optional.
        self._login_web_url: Optional[str] = None
        # The long logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        self._long_logo_web_url_for_dark_theme: Optional[str] = None
        # The long logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        self._long_logo_web_url_for_light_theme: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The square logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        self._square_logo_web_url_for_dark_theme: Optional[str] = None
        # The square logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        self._square_logo_web_url_for_light_theme: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LearningProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LearningProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LearningProvider()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name that appears in Viva Learning. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name that appears in Viva Learning. Required.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "learningContents": lambda n : setattr(self, 'learning_contents', n.get_collection_of_object_values(learning_content.LearningContent)),
            "loginWebUrl": lambda n : setattr(self, 'login_web_url', n.get_str_value()),
            "longLogoWebUrlForDarkTheme": lambda n : setattr(self, 'long_logo_web_url_for_dark_theme', n.get_str_value()),
            "longLogoWebUrlForLightTheme": lambda n : setattr(self, 'long_logo_web_url_for_light_theme', n.get_str_value()),
            "squareLogoWebUrlForDarkTheme": lambda n : setattr(self, 'square_logo_web_url_for_dark_theme', n.get_str_value()),
            "squareLogoWebUrlForLightTheme": lambda n : setattr(self, 'square_logo_web_url_for_light_theme', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def learning_contents(self,) -> Optional[List[learning_content.LearningContent]]:
        """
        Gets the learningContents property value. Learning catalog items for the provider.
        Returns: Optional[List[learning_content.LearningContent]]
        """
        return self._learning_contents
    
    @learning_contents.setter
    def learning_contents(self,value: Optional[List[learning_content.LearningContent]] = None) -> None:
        """
        Sets the learningContents property value. Learning catalog items for the provider.
        Args:
            value: Value to set for the learning_contents property.
        """
        self._learning_contents = value
    
    @property
    def login_web_url(self,) -> Optional[str]:
        """
        Gets the loginWebUrl property value. Authentication URL to access the courses for the provider. Optional.
        Returns: Optional[str]
        """
        return self._login_web_url
    
    @login_web_url.setter
    def login_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the loginWebUrl property value. Authentication URL to access the courses for the provider. Optional.
        Args:
            value: Value to set for the login_web_url property.
        """
        self._login_web_url = value
    
    @property
    def long_logo_web_url_for_dark_theme(self,) -> Optional[str]:
        """
        Gets the longLogoWebUrlForDarkTheme property value. The long logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Returns: Optional[str]
        """
        return self._long_logo_web_url_for_dark_theme
    
    @long_logo_web_url_for_dark_theme.setter
    def long_logo_web_url_for_dark_theme(self,value: Optional[str] = None) -> None:
        """
        Sets the longLogoWebUrlForDarkTheme property value. The long logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Args:
            value: Value to set for the long_logo_web_url_for_dark_theme property.
        """
        self._long_logo_web_url_for_dark_theme = value
    
    @property
    def long_logo_web_url_for_light_theme(self,) -> Optional[str]:
        """
        Gets the longLogoWebUrlForLightTheme property value. The long logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Returns: Optional[str]
        """
        return self._long_logo_web_url_for_light_theme
    
    @long_logo_web_url_for_light_theme.setter
    def long_logo_web_url_for_light_theme(self,value: Optional[str] = None) -> None:
        """
        Sets the longLogoWebUrlForLightTheme property value. The long logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Args:
            value: Value to set for the long_logo_web_url_for_light_theme property.
        """
        self._long_logo_web_url_for_light_theme = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("learningContents", self.learning_contents)
        writer.write_str_value("loginWebUrl", self.login_web_url)
        writer.write_str_value("longLogoWebUrlForDarkTheme", self.long_logo_web_url_for_dark_theme)
        writer.write_str_value("longLogoWebUrlForLightTheme", self.long_logo_web_url_for_light_theme)
        writer.write_str_value("squareLogoWebUrlForDarkTheme", self.square_logo_web_url_for_dark_theme)
        writer.write_str_value("squareLogoWebUrlForLightTheme", self.square_logo_web_url_for_light_theme)
    
    @property
    def square_logo_web_url_for_dark_theme(self,) -> Optional[str]:
        """
        Gets the squareLogoWebUrlForDarkTheme property value. The square logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Returns: Optional[str]
        """
        return self._square_logo_web_url_for_dark_theme
    
    @square_logo_web_url_for_dark_theme.setter
    def square_logo_web_url_for_dark_theme(self,value: Optional[str] = None) -> None:
        """
        Sets the squareLogoWebUrlForDarkTheme property value. The square logo URL for the dark mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Args:
            value: Value to set for the square_logo_web_url_for_dark_theme property.
        """
        self._square_logo_web_url_for_dark_theme = value
    
    @property
    def square_logo_web_url_for_light_theme(self,) -> Optional[str]:
        """
        Gets the squareLogoWebUrlForLightTheme property value. The square logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Returns: Optional[str]
        """
        return self._square_logo_web_url_for_light_theme
    
    @square_logo_web_url_for_light_theme.setter
    def square_logo_web_url_for_light_theme(self,value: Optional[str] = None) -> None:
        """
        Sets the squareLogoWebUrlForLightTheme property value. The square logo URL for the light mode that needs to be a publicly accessible image. This image would be saved to the blob storage of Viva Learning for rendering within the Viva Learning app. Required.
        Args:
            value: Value to set for the square_logo_web_url_for_light_theme property.
        """
        self._square_logo_web_url_for_light_theme = value
    

