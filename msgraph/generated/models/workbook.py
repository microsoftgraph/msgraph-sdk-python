from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_application, workbook_comment, workbook_functions, workbook_named_item, workbook_operation, workbook_table, workbook_worksheet

from . import entity

@dataclass
class Workbook(entity.Entity):
    # The application property
    application: Optional[workbook_application.WorkbookApplication] = None
    # The comments property
    comments: Optional[List[workbook_comment.WorkbookComment]] = None
    # The functions property
    functions: Optional[workbook_functions.WorkbookFunctions] = None
    # Represents a collection of workbooks scoped named items (named ranges and constants). Read-only.
    names: Optional[List[workbook_named_item.WorkbookNamedItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.
    operations: Optional[List[workbook_operation.WorkbookOperation]] = None
    # Represents a collection of tables associated with the workbook. Read-only.
    tables: Optional[List[workbook_table.WorkbookTable]] = None
    # Represents a collection of worksheets associated with the workbook. Read-only.
    worksheets: Optional[List[workbook_worksheet.WorkbookWorksheet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Workbook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Workbook
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Workbook()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_application, workbook_comment, workbook_functions, workbook_named_item, workbook_operation, workbook_table, workbook_worksheet

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(workbook_application.WorkbookApplication)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(workbook_comment.WorkbookComment)),
            "functions": lambda n : setattr(self, 'functions', n.get_object_value(workbook_functions.WorkbookFunctions)),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(workbook_named_item.WorkbookNamedItem)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(workbook_operation.WorkbookOperation)),
            "tables": lambda n : setattr(self, 'tables', n.get_collection_of_object_values(workbook_table.WorkbookTable)),
            "worksheets": lambda n : setattr(self, 'worksheets', n.get_collection_of_object_values(workbook_worksheet.WorkbookWorksheet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("application", self.application)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_object_value("functions", self.functions)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("tables", self.tables)
        writer.write_collection_of_object_values("worksheets", self.worksheets)
    

