from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_source import DataSource
    from .source_type import SourceType

from .data_source import DataSource

@dataclass
class UserSource(DataSource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.userSource"
    # Email address of the user's mailbox.
    email: Optional[str] = None
    # Specifies which sources are included in this group. The possible values are: mailbox, site.
    included_sources: Optional[SourceType] = None
    # The URL of the user's OneDrive for Business site. Read-only.
    site_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .data_source import DataSource
        from .source_type import SourceType

        from .data_source import DataSource
        from .source_type import SourceType

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "includedSources": lambda n : setattr(self, 'included_sources', n.get_collection_of_enum_values(SourceType)),
            "siteWebUrl": lambda n : setattr(self, 'site_web_url', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_enum_value("includedSources", self.included_sources)
        writer.write_str_value("siteWebUrl", self.site_web_url)
    

