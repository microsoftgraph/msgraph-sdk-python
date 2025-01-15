from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organizational_branding_localization import OrganizationalBrandingLocalization
    from .organizational_branding_properties import OrganizationalBrandingProperties

from .organizational_branding_properties import OrganizationalBrandingProperties

@dataclass
class OrganizationalBranding(OrganizationalBrandingProperties, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.organizationalBranding"
    # Add different branding based on a locale.
    localizations: Optional[list[OrganizationalBrandingLocalization]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationalBranding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBranding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationalBranding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties

        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties

        fields: dict[str, Callable[[Any], None]] = {
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(OrganizationalBrandingLocalization)),
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
        writer.write_collection_of_object_values("localizations", self.localizations)
    

