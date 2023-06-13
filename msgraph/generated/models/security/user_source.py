from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_source, source_type

from . import data_source

@dataclass
class UserSource(data_source.DataSource):
    odata_type = "#microsoft.graph.security.userSource"
    # Email address of the user's mailbox.
    email: Optional[str] = None
    # Specifies which sources are included in this group. Possible values are: mailbox, site.
    included_sources: Optional[source_type.SourceType] = None
    # The URL of the user's OneDrive for Business site. Read-only.
    site_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_source, source_type

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "includedSources": lambda n : setattr(self, 'included_sources', n.get_enum_value(source_type.SourceType)),
            "siteWebUrl": lambda n : setattr(self, 'site_web_url', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_enum_value("includedSources", self.included_sources)
        writer.write_str_value("siteWebUrl", self.site_web_url)
    

