from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_source import DataSource
    from .data_source_container import DataSourceContainer
    from .ediscovery_index_operation import EdiscoveryIndexOperation

from .data_source_container import DataSourceContainer

@dataclass
class EdiscoveryNoncustodialDataSource(DataSourceContainer, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryNoncustodialDataSource"
    # User source or SharePoint site data source as noncustodial data source.
    data_source: Optional[DataSource] = None
    # Operation entity that represents the latest indexing for the noncustodial data source.
    last_index_operation: Optional[EdiscoveryIndexOperation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryNoncustodialDataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryNoncustodialDataSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryNoncustodialDataSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .data_source import DataSource
        from .data_source_container import DataSourceContainer
        from .ediscovery_index_operation import EdiscoveryIndexOperation

        from .data_source import DataSource
        from .data_source_container import DataSourceContainer
        from .ediscovery_index_operation import EdiscoveryIndexOperation

        fields: dict[str, Callable[[Any], None]] = {
            "dataSource": lambda n : setattr(self, 'data_source', n.get_object_value(DataSource)),
            "lastIndexOperation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(EdiscoveryIndexOperation)),
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
        writer.write_object_value("dataSource", self.data_source)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
    

