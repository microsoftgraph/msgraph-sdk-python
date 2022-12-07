from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
json = lazy_import('msgraph.generated.models.json')
workbook_filter = lazy_import('msgraph.generated.models.workbook_filter')

class WorkbookTableColumn(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new workbookTableColumn and sets the default values.
        """
        super().__init__()
        # Retrieve the filter applied to the column. Read-only.
        self._filter: Optional[workbook_filter.WorkbookFilter] = None
        # Returns the index number of the column within the columns collection of the table. Zero-indexed. Read-only.
        self._index: Optional[int] = None
        # Returns the name of the table column.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        self._values: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookTableColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookTableColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookTableColumn()
    
    @property
    def filter(self,) -> Optional[workbook_filter.WorkbookFilter]:
        """
        Gets the filter property value. Retrieve the filter applied to the column. Read-only.
        Returns: Optional[workbook_filter.WorkbookFilter]
        """
        return self._filter
    
    @filter.setter
    def filter(self,value: Optional[workbook_filter.WorkbookFilter] = None) -> None:
        """
        Sets the filter property value. Retrieve the filter applied to the column. Read-only.
        Args:
            value: Value to set for the filter property.
        """
        self._filter = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(workbook_filter.WorkbookFilter)),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def index(self,) -> Optional[int]:
        """
        Gets the index property value. Returns the index number of the column within the columns collection of the table. Zero-indexed. Read-only.
        Returns: Optional[int]
        """
        return self._index
    
    @index.setter
    def index(self,value: Optional[int] = None) -> None:
        """
        Sets the index property value. Returns the index number of the column within the columns collection of the table. Zero-indexed. Read-only.
        Args:
            value: Value to set for the index property.
        """
        self._index = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Returns the name of the table column.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Returns the name of the table column.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("filter", self.filter)
        writer.write_int_value("index", self.index)
        writer.write_str_value("name", self.name)
        writer.write_object_value("values", self.values)
    
    @property
    def values(self,) -> Optional[json.Json]:
        """
        Gets the values property value. Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. Represents the raw values of the specified range. The data returned could be of type string, number, or a boolean. Cell that contain an error will return the error string.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

