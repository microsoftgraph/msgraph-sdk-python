from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .profile_source_localization import ProfileSourceLocalization

from .entity import Entity

@dataclass
class ProfileSource(Entity, Parsable):
    # Name of the profile source intended to inform users about the profile source name.
    display_name: Optional[str] = None
    # Type of the profile source.
    kind: Optional[str] = None
    # Alternative localized labels specified by an administrator.
    localizations: Optional[list[ProfileSourceLocalization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Profile source identifier used as an alternate key.
    source_id: Optional[str] = None
    # Web URL of the profile source that directs users to the page view of the profile data.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .profile_source_localization import ProfileSourceLocalization

        from .entity import Entity
        from .profile_source_localization import ProfileSourceLocalization

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(ProfileSourceLocalization)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("kind", self.kind)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("webUrl", self.web_url)
    

