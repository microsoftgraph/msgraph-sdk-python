from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WorkbookWorksheetProtectionOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether the worksheet protection option to allow the use of the autofilter feature is enabled.
    allow_auto_filter: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow deleting columns is enabled.
    allow_delete_columns: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow deleting rows is enabled.
    allow_delete_rows: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow formatting cells is enabled.
    allow_format_cells: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow formatting columns is enabled.
    allow_format_columns: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow formatting rows is enabled.
    allow_format_rows: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow inserting columns is enabled.
    allow_insert_columns: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow inserting hyperlinks is enabled.
    allow_insert_hyperlinks: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow inserting rows is enabled.
    allow_insert_rows: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow the use of the pivot table feature is enabled.
    allow_pivot_tables: Optional[bool] = None
    # Indicates whether the worksheet protection option to allow the use of the sort feature is enabled.
    allow_sort: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookWorksheetProtectionOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheetProtectionOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookWorksheetProtectionOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowAutoFilter": lambda n : setattr(self, 'allow_auto_filter', n.get_bool_value()),
            "allowDeleteColumns": lambda n : setattr(self, 'allow_delete_columns', n.get_bool_value()),
            "allowDeleteRows": lambda n : setattr(self, 'allow_delete_rows', n.get_bool_value()),
            "allowFormatCells": lambda n : setattr(self, 'allow_format_cells', n.get_bool_value()),
            "allowFormatColumns": lambda n : setattr(self, 'allow_format_columns', n.get_bool_value()),
            "allowFormatRows": lambda n : setattr(self, 'allow_format_rows', n.get_bool_value()),
            "allowInsertColumns": lambda n : setattr(self, 'allow_insert_columns', n.get_bool_value()),
            "allowInsertHyperlinks": lambda n : setattr(self, 'allow_insert_hyperlinks', n.get_bool_value()),
            "allowInsertRows": lambda n : setattr(self, 'allow_insert_rows', n.get_bool_value()),
            "allowPivotTables": lambda n : setattr(self, 'allow_pivot_tables', n.get_bool_value()),
            "allowSort": lambda n : setattr(self, 'allow_sort', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

