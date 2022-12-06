from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group = lazy_import('msgraph.generated.models.group')
data_source = lazy_import('msgraph.generated.models.security.data_source')
source_type = lazy_import('msgraph.generated.models.security.source_type')

class UnifiedGroupSource(data_source.DataSource):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedGroupSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.unifiedGroupSource"
        # The group property
        self._group: Optional[group.Group] = None
        # Specifies which sources are included in this group. Possible values are: mailbox, site.
        self._included_sources: Optional[source_type.SourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedGroupSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedGroupSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedGroupSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "included_sources": lambda n : setattr(self, 'included_sources', n.get_enum_value(source_type.SourceType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[group.Group]:
        """
        Gets the group property value. The group property
        Returns: Optional[group.Group]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the group property value. The group property
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def included_sources(self,) -> Optional[source_type.SourceType]:
        """
        Gets the includedSources property value. Specifies which sources are included in this group. Possible values are: mailbox, site.
        Returns: Optional[source_type.SourceType]
        """
        return self._included_sources
    
    @included_sources.setter
    def included_sources(self,value: Optional[source_type.SourceType] = None) -> None:
        """
        Sets the includedSources property value. Specifies which sources are included in this group. Possible values are: mailbox, site.
        Args:
            value: Value to set for the includedSources property.
        """
        self._included_sources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("group", self.group)
        writer.write_enum_value("includedSources", self.included_sources)
    

