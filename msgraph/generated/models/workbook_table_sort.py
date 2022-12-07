from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_sort_field = lazy_import('msgraph.generated.models.workbook_sort_field')

class WorkbookTableSort(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookTableSort and sets the default values.
        """
        super().__init__()
        # Represents the current conditions used to last sort the table. Read-only.
        self._fields: Optional[List[workbook_sort_field.WorkbookSortField]] = None
        # Represents whether the casing impacted the last sort of the table. Read-only.
        self._match_case: Optional[bool] = None
        # Represents Chinese character ordering method last used to sort the table. The possible values are: PinYin, StrokeCount. Read-only.
        self._method: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookTableSort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookTableSort
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookTableSort()
    
    @property
    def fields(self,) -> Optional[List[workbook_sort_field.WorkbookSortField]]:
        """
        Gets the fields property value. Represents the current conditions used to last sort the table. Read-only.
        Returns: Optional[List[workbook_sort_field.WorkbookSortField]]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[List[workbook_sort_field.WorkbookSortField]] = None) -> None:
        """
        Sets the fields property value. Represents the current conditions used to last sort the table. Read-only.
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(workbook_sort_field.WorkbookSortField)),
            "match_case": lambda n : setattr(self, 'match_case', n.get_bool_value()),
            "method": lambda n : setattr(self, 'method', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def match_case(self,) -> Optional[bool]:
        """
        Gets the matchCase property value. Represents whether the casing impacted the last sort of the table. Read-only.
        Returns: Optional[bool]
        """
        return self._match_case
    
    @match_case.setter
    def match_case(self,value: Optional[bool] = None) -> None:
        """
        Sets the matchCase property value. Represents whether the casing impacted the last sort of the table. Read-only.
        Args:
            value: Value to set for the matchCase property.
        """
        self._match_case = value
    
    @property
    def method(self,) -> Optional[str]:
        """
        Gets the method property value. Represents Chinese character ordering method last used to sort the table. The possible values are: PinYin, StrokeCount. Read-only.
        Returns: Optional[str]
        """
        return self._method
    
    @method.setter
    def method(self,value: Optional[str] = None) -> None:
        """
        Sets the method property value. Represents Chinese character ordering method last used to sort the table. The possible values are: PinYin, StrokeCount. Read-only.
        Args:
            value: Value to set for the method property.
        """
        self._method = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_bool_value("matchCase", self.match_case)
        writer.write_str_value("method", self.method)
    

