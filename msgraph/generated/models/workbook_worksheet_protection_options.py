from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WorkbookWorksheetProtectionOptions(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allow_auto_filter(self,) -> Optional[bool]:
        """
        Gets the allowAutoFilter property value. Represents the worksheet protection option of allowing using auto filter feature.
        Returns: Optional[bool]
        """
        return self._allow_auto_filter
    
    @allow_auto_filter.setter
    def allow_auto_filter(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAutoFilter property value. Represents the worksheet protection option of allowing using auto filter feature.
        Args:
            value: Value to set for the allowAutoFilter property.
        """
        self._allow_auto_filter = value
    
    @property
    def allow_delete_columns(self,) -> Optional[bool]:
        """
        Gets the allowDeleteColumns property value. Represents the worksheet protection option of allowing deleting columns.
        Returns: Optional[bool]
        """
        return self._allow_delete_columns
    
    @allow_delete_columns.setter
    def allow_delete_columns(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeleteColumns property value. Represents the worksheet protection option of allowing deleting columns.
        Args:
            value: Value to set for the allowDeleteColumns property.
        """
        self._allow_delete_columns = value
    
    @property
    def allow_delete_rows(self,) -> Optional[bool]:
        """
        Gets the allowDeleteRows property value. Represents the worksheet protection option of allowing deleting rows.
        Returns: Optional[bool]
        """
        return self._allow_delete_rows
    
    @allow_delete_rows.setter
    def allow_delete_rows(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeleteRows property value. Represents the worksheet protection option of allowing deleting rows.
        Args:
            value: Value to set for the allowDeleteRows property.
        """
        self._allow_delete_rows = value
    
    @property
    def allow_format_cells(self,) -> Optional[bool]:
        """
        Gets the allowFormatCells property value. Represents the worksheet protection option of allowing formatting cells.
        Returns: Optional[bool]
        """
        return self._allow_format_cells
    
    @allow_format_cells.setter
    def allow_format_cells(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowFormatCells property value. Represents the worksheet protection option of allowing formatting cells.
        Args:
            value: Value to set for the allowFormatCells property.
        """
        self._allow_format_cells = value
    
    @property
    def allow_format_columns(self,) -> Optional[bool]:
        """
        Gets the allowFormatColumns property value. Represents the worksheet protection option of allowing formatting columns.
        Returns: Optional[bool]
        """
        return self._allow_format_columns
    
    @allow_format_columns.setter
    def allow_format_columns(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowFormatColumns property value. Represents the worksheet protection option of allowing formatting columns.
        Args:
            value: Value to set for the allowFormatColumns property.
        """
        self._allow_format_columns = value
    
    @property
    def allow_format_rows(self,) -> Optional[bool]:
        """
        Gets the allowFormatRows property value. Represents the worksheet protection option of allowing formatting rows.
        Returns: Optional[bool]
        """
        return self._allow_format_rows
    
    @allow_format_rows.setter
    def allow_format_rows(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowFormatRows property value. Represents the worksheet protection option of allowing formatting rows.
        Args:
            value: Value to set for the allowFormatRows property.
        """
        self._allow_format_rows = value
    
    @property
    def allow_insert_columns(self,) -> Optional[bool]:
        """
        Gets the allowInsertColumns property value. Represents the worksheet protection option of allowing inserting columns.
        Returns: Optional[bool]
        """
        return self._allow_insert_columns
    
    @allow_insert_columns.setter
    def allow_insert_columns(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowInsertColumns property value. Represents the worksheet protection option of allowing inserting columns.
        Args:
            value: Value to set for the allowInsertColumns property.
        """
        self._allow_insert_columns = value
    
    @property
    def allow_insert_hyperlinks(self,) -> Optional[bool]:
        """
        Gets the allowInsertHyperlinks property value. Represents the worksheet protection option of allowing inserting hyperlinks.
        Returns: Optional[bool]
        """
        return self._allow_insert_hyperlinks
    
    @allow_insert_hyperlinks.setter
    def allow_insert_hyperlinks(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowInsertHyperlinks property value. Represents the worksheet protection option of allowing inserting hyperlinks.
        Args:
            value: Value to set for the allowInsertHyperlinks property.
        """
        self._allow_insert_hyperlinks = value
    
    @property
    def allow_insert_rows(self,) -> Optional[bool]:
        """
        Gets the allowInsertRows property value. Represents the worksheet protection option of allowing inserting rows.
        Returns: Optional[bool]
        """
        return self._allow_insert_rows
    
    @allow_insert_rows.setter
    def allow_insert_rows(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowInsertRows property value. Represents the worksheet protection option of allowing inserting rows.
        Args:
            value: Value to set for the allowInsertRows property.
        """
        self._allow_insert_rows = value
    
    @property
    def allow_pivot_tables(self,) -> Optional[bool]:
        """
        Gets the allowPivotTables property value. Represents the worksheet protection option of allowing using pivot table feature.
        Returns: Optional[bool]
        """
        return self._allow_pivot_tables
    
    @allow_pivot_tables.setter
    def allow_pivot_tables(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPivotTables property value. Represents the worksheet protection option of allowing using pivot table feature.
        Args:
            value: Value to set for the allowPivotTables property.
        """
        self._allow_pivot_tables = value
    
    @property
    def allow_sort(self,) -> Optional[bool]:
        """
        Gets the allowSort property value. Represents the worksheet protection option of allowing using sort feature.
        Returns: Optional[bool]
        """
        return self._allow_sort
    
    @allow_sort.setter
    def allow_sort(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowSort property value. Represents the worksheet protection option of allowing using sort feature.
        Args:
            value: Value to set for the allowSort property.
        """
        self._allow_sort = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookWorksheetProtectionOptions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents the worksheet protection option of allowing using auto filter feature.
        self._allow_auto_filter: Optional[bool] = None
        # Represents the worksheet protection option of allowing deleting columns.
        self._allow_delete_columns: Optional[bool] = None
        # Represents the worksheet protection option of allowing deleting rows.
        self._allow_delete_rows: Optional[bool] = None
        # Represents the worksheet protection option of allowing formatting cells.
        self._allow_format_cells: Optional[bool] = None
        # Represents the worksheet protection option of allowing formatting columns.
        self._allow_format_columns: Optional[bool] = None
        # Represents the worksheet protection option of allowing formatting rows.
        self._allow_format_rows: Optional[bool] = None
        # Represents the worksheet protection option of allowing inserting columns.
        self._allow_insert_columns: Optional[bool] = None
        # Represents the worksheet protection option of allowing inserting hyperlinks.
        self._allow_insert_hyperlinks: Optional[bool] = None
        # Represents the worksheet protection option of allowing inserting rows.
        self._allow_insert_rows: Optional[bool] = None
        # Represents the worksheet protection option of allowing using pivot table feature.
        self._allow_pivot_tables: Optional[bool] = None
        # Represents the worksheet protection option of allowing using sort feature.
        self._allow_sort: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookWorksheetProtectionOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheetProtectionOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookWorksheetProtectionOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_auto_filter": lambda n : setattr(self, 'allow_auto_filter', n.get_bool_value()),
            "allow_delete_columns": lambda n : setattr(self, 'allow_delete_columns', n.get_bool_value()),
            "allow_delete_rows": lambda n : setattr(self, 'allow_delete_rows', n.get_bool_value()),
            "allow_format_cells": lambda n : setattr(self, 'allow_format_cells', n.get_bool_value()),
            "allow_format_columns": lambda n : setattr(self, 'allow_format_columns', n.get_bool_value()),
            "allow_format_rows": lambda n : setattr(self, 'allow_format_rows', n.get_bool_value()),
            "allow_insert_columns": lambda n : setattr(self, 'allow_insert_columns', n.get_bool_value()),
            "allow_insert_hyperlinks": lambda n : setattr(self, 'allow_insert_hyperlinks', n.get_bool_value()),
            "allow_insert_rows": lambda n : setattr(self, 'allow_insert_rows', n.get_bool_value()),
            "allow_pivot_tables": lambda n : setattr(self, 'allow_pivot_tables', n.get_bool_value()),
            "allow_sort": lambda n : setattr(self, 'allow_sort', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowAutoFilter", self.allow_auto_filter)
        writer.write_bool_value("allowDeleteColumns", self.allow_delete_columns)
        writer.write_bool_value("allowDeleteRows", self.allow_delete_rows)
        writer.write_bool_value("allowFormatCells", self.allow_format_cells)
        writer.write_bool_value("allowFormatColumns", self.allow_format_columns)
        writer.write_bool_value("allowFormatRows", self.allow_format_rows)
        writer.write_bool_value("allowInsertColumns", self.allow_insert_columns)
        writer.write_bool_value("allowInsertHyperlinks", self.allow_insert_hyperlinks)
        writer.write_bool_value("allowInsertRows", self.allow_insert_rows)
        writer.write_bool_value("allowPivotTables", self.allow_pivot_tables)
        writer.write_bool_value("allowSort", self.allow_sort)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

