from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..group import Group
    from .data_source import DataSource
    from .source_type import SourceType

from .data_source import DataSource

@dataclass
class UnifiedGroupSource(DataSource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.unifiedGroupSource"
    # The group property
    group: Optional[Group] = None
    # Specifies which sources are included in this group. The possible values are: mailbox, site.
    included_sources: Optional[SourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedGroupSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedGroupSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedGroupSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..group import Group
        from .data_source import DataSource
        from .source_type import SourceType

        from ..group import Group
        from .data_source import DataSource
        from .source_type import SourceType

        fields: dict[str, Callable[[Any], None]] = {
            "group": lambda n : setattr(self, 'group', n.get_object_value(Group)),
            "includedSources": lambda n : setattr(self, 'included_sources', n.get_collection_of_enum_values(SourceType)),
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
        writer.write_object_value("group", self.group)
        writer.write_enum_value("includedSources", self.included_sources)
    

