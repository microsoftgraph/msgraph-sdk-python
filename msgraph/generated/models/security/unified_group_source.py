from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_source, source_type
    from .. import group

from . import data_source

@dataclass
class UnifiedGroupSource(data_source.DataSource):
    odata_type = "#microsoft.graph.security.unifiedGroupSource"
    # The group property
    group: Optional[group.Group] = None
    # Specifies which sources are included in this group. Possible values are: mailbox, site.
    included_sources: Optional[source_type.SourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedGroupSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedGroupSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedGroupSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_source, source_type
        from .. import group

        from . import data_source, source_type
        from .. import group

        fields: Dict[str, Callable[[Any], None]] = {
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "includedSources": lambda n : setattr(self, 'included_sources', n.get_enum_value(source_type.SourceType)),
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
        writer.write_object_value("group", self.group)
        writer.write_enum_value("includedSources", self.included_sources)
    

