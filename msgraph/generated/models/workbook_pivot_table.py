from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')

class WorkbookPivotTable(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new workbookPivotTable and sets the default values.
        """
        super().__init__()
        # Name of the PivotTable.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The worksheet containing the current PivotTable. Read-only.
        self._worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookPivotTable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookPivotTable
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookPivotTable()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the PivotTable.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the PivotTable.
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
        writer.write_str_value("name", self.name)
        writer.write_object_value("worksheet", self.worksheet)
    
    @property
    def worksheet(self,) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Gets the worksheet property value. The worksheet containing the current PivotTable. Read-only.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
        """
        return self._worksheet
    
    @worksheet.setter
    def worksheet(self,value: Optional[workbook_worksheet.WorkbookWorksheet] = None) -> None:
        """
        Sets the worksheet property value. The worksheet containing the current PivotTable. Read-only.
        Args:
            value: Value to set for the worksheet property.
        """
        self._worksheet = value
    

