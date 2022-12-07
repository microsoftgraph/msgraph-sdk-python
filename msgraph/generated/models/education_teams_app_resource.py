from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_resource = lazy_import('msgraph.generated.models.education_resource')

class EducationTeamsAppResource(education_resource.EducationResource):
    @property
    def app_icon_web_url(self,) -> Optional[str]:
        """
        Gets the appIconWebUrl property value. The appIconWebUrl property
        Returns: Optional[str]
        """
        return self._app_icon_web_url
    
    @app_icon_web_url.setter
    def app_icon_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appIconWebUrl property value. The appIconWebUrl property
        Args:
            value: Value to set for the appIconWebUrl property.
        """
        self._app_icon_web_url = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The appId property
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The appId property
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EducationTeamsAppResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationTeamsAppResource"
        # The appIconWebUrl property
        self._app_icon_web_url: Optional[str] = None
        # The appId property
        self._app_id: Optional[str] = None
        # The teamsEmbeddedContentUrl property
        self._teams_embedded_content_url: Optional[str] = None
        # The webUrl property
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationTeamsAppResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationTeamsAppResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationTeamsAppResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_icon_web_url": lambda n : setattr(self, 'app_icon_web_url', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "teams_embedded_content_url": lambda n : setattr(self, 'teams_embedded_content_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appIconWebUrl", self.app_icon_web_url)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("teamsEmbeddedContentUrl", self.teams_embedded_content_url)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def teams_embedded_content_url(self,) -> Optional[str]:
        """
        Gets the teamsEmbeddedContentUrl property value. The teamsEmbeddedContentUrl property
        Returns: Optional[str]
        """
        return self._teams_embedded_content_url
    
    @teams_embedded_content_url.setter
    def teams_embedded_content_url(self,value: Optional[str] = None) -> None:
        """
        Sets the teamsEmbeddedContentUrl property value. The teamsEmbeddedContentUrl property
        Args:
            value: Value to set for the teamsEmbeddedContentUrl property.
        """
        self._teams_embedded_content_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The webUrl property
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The webUrl property
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

