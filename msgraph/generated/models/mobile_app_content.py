from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, mobile_app_content_file, mobile_contained_app

from . import entity

@dataclass
class MobileAppContent(entity.Entity):
    """
    Contains content properties for a specific app version. Each mobileAppContent can have multiple mobileAppContentFile.
    """
    # The collection of contained apps in a MobileLobApp acting as a package.
    contained_apps: Optional[List[mobile_contained_app.MobileContainedApp]] = None
    # The list of files for this app content version.
    files: Optional[List[mobile_app_content_file.MobileAppContentFile]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MobileAppContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, mobile_app_content_file, mobile_contained_app

        from . import entity, mobile_app_content_file, mobile_contained_app

        fields: Dict[str, Callable[[Any], None]] = {
            "containedApps": lambda n : setattr(self, 'contained_apps', n.get_collection_of_object_values(mobile_contained_app.MobileContainedApp)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("containedApps", self.contained_apps)
        writer.write_collection_of_object_values("files", self.files)
    

