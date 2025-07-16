from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_application import WorkbookApplication
    from .workbook_comment import WorkbookComment
    from .workbook_functions import WorkbookFunctions
    from .workbook_named_item import WorkbookNamedItem
    from .workbook_operation import WorkbookOperation
    from .workbook_table import WorkbookTable
    from .workbook_worksheet import WorkbookWorksheet

from .entity import Entity

@dataclass
class Workbook(Entity, Parsable):
    # The application property
    application: Optional[WorkbookApplication] = None
    # Represents a collection of comments in a workbook.
    comments: Optional[list[WorkbookComment]] = None
    # The functions property
    functions: Optional[WorkbookFunctions] = None
    # Represents a collection of workbooks scoped named items (named ranges and constants). Read-only.
    names: Optional[list[WorkbookNamedItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.
    operations: Optional[list[WorkbookOperation]] = None
    # Represents a collection of tables associated with the workbook. Read-only.
    tables: Optional[list[WorkbookTable]] = None
    # Represents a collection of worksheets associated with the workbook. Read-only.
    worksheets: Optional[list[WorkbookWorksheet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Workbook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Workbook
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Workbook()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_application import WorkbookApplication
        from .workbook_comment import WorkbookComment
        from .workbook_functions import WorkbookFunctions
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_operation import WorkbookOperation
        from .workbook_table import WorkbookTable
        from .workbook_worksheet import WorkbookWorksheet

        from .entity import Entity
        from .workbook_application import WorkbookApplication
        from .workbook_comment import WorkbookComment
        from .workbook_functions import WorkbookFunctions
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_operation import WorkbookOperation
        from .workbook_table import WorkbookTable
        from .workbook_worksheet import WorkbookWorksheet

        fields: dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(WorkbookApplication)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(WorkbookComment)),
            "functions": lambda n : setattr(self, 'functions', n.get_object_value(WorkbookFunctions)),
            "names": lambda n : setattr(self, 'names', n.get_collection_of_object_values(WorkbookNamedItem)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(WorkbookOperation)),
            "tables": lambda n : setattr(self, 'tables', n.get_collection_of_object_values(WorkbookTable)),
            "worksheets": lambda n : setattr(self, 'worksheets', n.get_collection_of_object_values(WorkbookWorksheet)),
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
        writer.write_object_value("application", self.application)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_object_value("functions", self.functions)
        writer.write_collection_of_object_values("names", self.names)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("tables", self.tables)
        writer.write_collection_of_object_values("worksheets", self.worksheets)
    

