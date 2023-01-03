from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_source = lazy_import('msgraph.generated.models.security.data_source')
data_source_container = lazy_import('msgraph.generated.models.security.data_source_container')
ediscovery_index_operation = lazy_import('msgraph.generated.models.security.ediscovery_index_operation')

class EdiscoveryNoncustodialDataSource(data_source_container.DataSourceContainer):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryNoncustodialDataSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryNoncustodialDataSource"
        # User source or SharePoint site data source as non-custodial data source.
        self._data_source: Optional[data_source.DataSource] = None
        # Operation entity that represents the latest indexing for the non-custodial data source.
        self._last_index_operation: Optional[ediscovery_index_operation.EdiscoveryIndexOperation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryNoncustodialDataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryNoncustodialDataSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryNoncustodialDataSource()
    
    @property
    def data_source(self,) -> Optional[data_source.DataSource]:
        """
        Gets the dataSource property value. User source or SharePoint site data source as non-custodial data source.
        Returns: Optional[data_source.DataSource]
        """
        return self._data_source
    
    @data_source.setter
    def data_source(self,value: Optional[data_source.DataSource] = None) -> None:
        """
        Sets the dataSource property value. User source or SharePoint site data source as non-custodial data source.
        Args:
            value: Value to set for the dataSource property.
        """
        self._data_source = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_source": lambda n : setattr(self, 'data_source', n.get_object_value(data_source.DataSource)),
            "last_index_operation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(ediscovery_index_operation.EdiscoveryIndexOperation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_index_operation(self,) -> Optional[ediscovery_index_operation.EdiscoveryIndexOperation]:
        """
        Gets the lastIndexOperation property value. Operation entity that represents the latest indexing for the non-custodial data source.
        Returns: Optional[ediscovery_index_operation.EdiscoveryIndexOperation]
        """
        return self._last_index_operation
    
    @last_index_operation.setter
    def last_index_operation(self,value: Optional[ediscovery_index_operation.EdiscoveryIndexOperation] = None) -> None:
        """
        Sets the lastIndexOperation property value. Operation entity that represents the latest indexing for the non-custodial data source.
        Args:
            value: Value to set for the lastIndexOperation property.
        """
        self._last_index_operation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("dataSource", self.data_source)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
    

