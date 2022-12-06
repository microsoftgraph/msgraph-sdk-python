from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart = lazy_import('msgraph.generated.models.workbook_chart')
workbook_named_item = lazy_import('msgraph.generated.models.workbook_named_item')
workbook_pivot_table = lazy_import('msgraph.generated.models.workbook_pivot_table')
workbook_table = lazy_import('msgraph.generated.models.workbook_table')
workbook_worksheet_protection = lazy_import('msgraph.generated.models.workbook_worksheet_protection')

class WorkbookWorksheet(entity.Entity):
    @property
    def charts(self,) -> Optional[List[workbook_chart.WorkbookChart]]:
        """
        Gets the charts property value. Returns collection of charts that are part of the worksheet. Read-only.
        Returns: Optional[List[workbook_chart.WorkbookChart]]
        """
        return self._charts
    
    @charts.setter
    def charts(self,value: Optional[List[workbook_chart.WorkbookChart]] = None) -> None:
        """
        Sets the charts property value. Returns collection of charts that are part of the worksheet. Read-only.
        Args:
            value: Value to set for the charts property.
        """
        self._charts = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookWorksheet and sets the default values.
        """
        super().__init__()
        # Returns collection of charts that are part of the worksheet. Read-only.
        self._charts: Optional[List[workbook_chart.WorkbookChart]] = None
        # The display name of the worksheet.
        self._name: Optional[str] = None
        # Returns collection of names that are associated with the worksheet. Read-only.
        self._names: Optional[List[workbook_named_item.WorkbookNamedItem]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of PivotTables that are part of the worksheet.
        self._pivot_tables: Optional[List[workbook_pivot_table.WorkbookPivotTable]] = None
        # The zero-based position of the worksheet within the workbook.
        self._position: Optional[int] = None
        # Returns sheet protection object for a worksheet. Read-only.
        self._protection: Optional[workbook_worksheet_protection.WorkbookWorksheetProtection] = None
        # Collection of tables that are part of the worksheet. Read-only.
        self._tables: Optional[List[workbook_table.WorkbookTable]] = None
        # The Visibility of the worksheet. The possible values are: Visible, Hidden, VeryHidden.
        self._visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookWorksheet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookWorksheet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "charts": lambda n : setattr(self, 'charts', n.get_collection_of_object_values(workbook_chart.WorkbookChart)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(workbook_named_item.WorkbookNamedItem)),
            "pivot_tables": lambda n : setattr(self, 'pivot_tables', n.get_collection_of_object_values(workbook_pivot_table.WorkbookPivotTable)),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
            "protection": lambda n : setattr(self, 'protection', n.get_object_value(workbook_worksheet_protection.WorkbookWorksheetProtection)),
            "tables": lambda n : setattr(self, 'tables', n.get_collection_of_object_values(workbook_table.WorkbookTable)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The display name of the worksheet.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The display name of the worksheet.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def names(self,) -> Optional[List[workbook_named_item.WorkbookNamedItem]]:
        """
        Gets the names property value. Returns collection of names that are associated with the worksheet. Read-only.
        Returns: Optional[List[workbook_named_item.WorkbookNamedItem]]
        """
        return self._names
    
    @names.setter
    def names(self,value: Optional[List[workbook_named_item.WorkbookNamedItem]] = None) -> None:
        """
        Sets the names property value. Returns collection of names that are associated with the worksheet. Read-only.
        Args:
            value: Value to set for the names property.
        """
        self._names = value
    
    @property
    def pivot_tables(self,) -> Optional[List[workbook_pivot_table.WorkbookPivotTable]]:
        """
        Gets the pivotTables property value. Collection of PivotTables that are part of the worksheet.
        Returns: Optional[List[workbook_pivot_table.WorkbookPivotTable]]
        """
        return self._pivot_tables
    
    @pivot_tables.setter
    def pivot_tables(self,value: Optional[List[workbook_pivot_table.WorkbookPivotTable]] = None) -> None:
        """
        Sets the pivotTables property value. Collection of PivotTables that are part of the worksheet.
        Args:
            value: Value to set for the pivotTables property.
        """
        self._pivot_tables = value
    
    @property
    def position(self,) -> Optional[int]:
        """
        Gets the position property value. The zero-based position of the worksheet within the workbook.
        Returns: Optional[int]
        """
        return self._position
    
    @position.setter
    def position(self,value: Optional[int] = None) -> None:
        """
        Sets the position property value. The zero-based position of the worksheet within the workbook.
        Args:
            value: Value to set for the position property.
        """
        self._position = value
    
    @property
    def protection(self,) -> Optional[workbook_worksheet_protection.WorkbookWorksheetProtection]:
        """
        Gets the protection property value. Returns sheet protection object for a worksheet. Read-only.
        Returns: Optional[workbook_worksheet_protection.WorkbookWorksheetProtection]
        """
        return self._protection
    
    @protection.setter
    def protection(self,value: Optional[workbook_worksheet_protection.WorkbookWorksheetProtection] = None) -> None:
        """
        Sets the protection property value. Returns sheet protection object for a worksheet. Read-only.
        Args:
            value: Value to set for the protection property.
        """
        self._protection = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("charts", self.charts)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("pivotTables", self.pivot_tables)
        writer.write_int_value("position", self.position)
        writer.write_object_value("protection", self.protection)
        writer.write_collection_of_object_values("tables", self.tables)
        writer.write_str_value("visibility", self.visibility)
    
    @property
    def tables(self,) -> Optional[List[workbook_table.WorkbookTable]]:
        """
        Gets the tables property value. Collection of tables that are part of the worksheet. Read-only.
        Returns: Optional[List[workbook_table.WorkbookTable]]
        """
        return self._tables
    
    @tables.setter
    def tables(self,value: Optional[List[workbook_table.WorkbookTable]] = None) -> None:
        """
        Sets the tables property value. Collection of tables that are part of the worksheet. Read-only.
        Args:
            value: Value to set for the tables property.
        """
        self._tables = value
    
    @property
    def visibility(self,) -> Optional[str]:
        """
        Gets the visibility property value. The Visibility of the worksheet. The possible values are: Visible, Hidden, VeryHidden.
        Returns: Optional[str]
        """
        return self._visibility
    
    @visibility.setter
    def visibility(self,value: Optional[str] = None) -> None:
        """
        Sets the visibility property value. The Visibility of the worksheet. The possible values are: Visible, Hidden, VeryHidden.
        Args:
            value: Value to set for the visibility property.
        """
        self._visibility = value
    

