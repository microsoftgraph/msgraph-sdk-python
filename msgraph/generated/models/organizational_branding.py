from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

organizational_branding_localization = lazy_import('msgraph.generated.models.organizational_branding_localization')
organizational_branding_properties = lazy_import('msgraph.generated.models.organizational_branding_properties')

class OrganizationalBranding(organizational_branding_properties.OrganizationalBrandingProperties):
    def __init__(self,) -> None:
        """
        Instantiates a new OrganizationalBranding and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.organizationalBranding"
        # Add different branding based on a locale.
        self._localizations: Optional[List[organizational_branding_localization.OrganizationalBrandingLocalization]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizationalBranding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBranding
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OrganizationalBranding()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(organizational_branding_localization.OrganizationalBrandingLocalization)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def localizations(self,) -> Optional[List[organizational_branding_localization.OrganizationalBrandingLocalization]]:
        """
        Gets the localizations property value. Add different branding based on a locale.
        Returns: Optional[List[organizational_branding_localization.OrganizationalBrandingLocalization]]
        """
        return self._localizations
    
    @localizations.setter
    def localizations(self,value: Optional[List[organizational_branding_localization.OrganizationalBrandingLocalization]] = None) -> None:
        """
        Sets the localizations property value. Add different branding based on a locale.
        Args:
            value: Value to set for the localizations property.
        """
        self._localizations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("localizations", self.localizations)
    

