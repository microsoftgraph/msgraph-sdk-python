from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mobile_app_content_file = lazy_import('msgraph.generated.models.mobile_app_content_file')
mobile_contained_app = lazy_import('msgraph.generated.models.mobile_contained_app')

class MobileAppContent(entity.Entity):
    """
    Contains content properties for a specific app version. Each mobileAppContent can have multiple mobileAppContentFile.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppContent and sets the default values.
        """
        super().__init__()
        # The collection of contained apps in a MobileLobApp acting as a package.
        self._contained_apps: Optional[List[mobile_contained_app.MobileContainedApp]] = None
        # The list of files for this app content version.
        self._files: Optional[List[mobile_app_content_file.MobileAppContentFile]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def contained_apps(self,) -> Optional[List[mobile_contained_app.MobileContainedApp]]:
        """
        Gets the containedApps property value. The collection of contained apps in a MobileLobApp acting as a package.
        Returns: Optional[List[mobile_contained_app.MobileContainedApp]]
        """
        return self._contained_apps
    
    @contained_apps.setter
    def contained_apps(self,value: Optional[List[mobile_contained_app.MobileContainedApp]] = None) -> None:
        """
        Sets the containedApps property value. The collection of contained apps in a MobileLobApp acting as a package.
        Args:
            value: Value to set for the containedApps property.
        """
        self._contained_apps = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppContent()
    
    @property
    def files(self,) -> Optional[List[mobile_app_content_file.MobileAppContentFile]]:
        """
        Gets the files property value. The list of files for this app content version.
        Returns: Optional[List[mobile_app_content_file.MobileAppContentFile]]
        """
        return self._files
    
    @files.setter
    def files(self,value: Optional[List[mobile_app_content_file.MobileAppContentFile]] = None) -> None:
        """
        Sets the files property value. The list of files for this app content version.
        Args:
            value: Value to set for the files property.
        """
        self._files = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contained_apps": lambda n : setattr(self, 'contained_apps', n.get_collection_of_object_values(mobile_contained_app.MobileContainedApp)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(mobile_app_content_file.MobileAppContentFile)),
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
        writer.write_collection_of_object_values("containedApps", self.contained_apps)
        writer.write_collection_of_object_values("files", self.files)
    

