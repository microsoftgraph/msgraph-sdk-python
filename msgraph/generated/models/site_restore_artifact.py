from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restore_artifact_base import RestoreArtifactBase

from .restore_artifact_base import RestoreArtifactBase

@dataclass
class SiteRestoreArtifact(RestoreArtifactBase):
    # The OdataType property
    odata_type: Optional[str] = None
    # The new site identifier if the value of the destinationType property is new, and the existing site ID if the value is inPlace.
    restored_site_id: Optional[str] = None
    # The name of the restored site.
    restored_site_name: Optional[str] = None
    # The web URL of the restored site.
    restored_site_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SiteRestoreArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SiteRestoreArtifact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SiteRestoreArtifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .restore_artifact_base import RestoreArtifactBase

        from .restore_artifact_base import RestoreArtifactBase

        fields: Dict[str, Callable[[Any], None]] = {
            "restoredSiteId": lambda n : setattr(self, 'restored_site_id', n.get_str_value()),
            "restoredSiteName": lambda n : setattr(self, 'restored_site_name', n.get_str_value()),
            "restoredSiteWebUrl": lambda n : setattr(self, 'restored_site_web_url', n.get_str_value()),
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
        writer.write_str_value("restoredSiteId", self.restored_site_id)
    

