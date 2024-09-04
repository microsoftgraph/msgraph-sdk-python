from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .m365_apps_installation_options import M365AppsInstallationOptions

from .entity import Entity

@dataclass
class AdminMicrosoft365Apps(Entity):
    # A container for tenant-level settings for Microsoft 365 applications.
    installation_options: Optional[M365AppsInstallationOptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminMicrosoft365Apps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminMicrosoft365Apps
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminMicrosoft365Apps()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .m365_apps_installation_options import M365AppsInstallationOptions

        from .entity import Entity
        from .m365_apps_installation_options import M365AppsInstallationOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "installationOptions": lambda n : setattr(self, 'installation_options', n.get_object_value(M365AppsInstallationOptions)),
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
        writer.write_object_value("installationOptions", self.installation_options)
    

