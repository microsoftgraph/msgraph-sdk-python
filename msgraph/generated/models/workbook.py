from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_application = lazy_import('msgraph.generated.models.workbook_application')
workbook_comment = lazy_import('msgraph.generated.models.workbook_comment')
workbook_functions = lazy_import('msgraph.generated.models.workbook_functions')
workbook_named_item = lazy_import('msgraph.generated.models.workbook_named_item')
workbook_operation = lazy_import('msgraph.generated.models.workbook_operation')
workbook_table = lazy_import('msgraph.generated.models.workbook_table')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')

class Workbook(entity.Entity):
    @property
    def application(self,) -> Optional[workbook_application.WorkbookApplication]:
        """
        Gets the application property value. The application property
        Returns: Optional[workbook_application.WorkbookApplication]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[workbook_application.WorkbookApplication] = None) -> None:
        """
        Sets the application property value. The application property
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    @property
    def comments(self,) -> Optional[List[workbook_comment.WorkbookComment]]:
        """
        Gets the comments property value. The comments property
        Returns: Optional[List[workbook_comment.WorkbookComment]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[workbook_comment.WorkbookComment]] = None) -> None:
        """
        Sets the comments property value. The comments property
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbook and sets the default values.
        """
        super().__init__()
        # The application property
        self._application: Optional[workbook_application.WorkbookApplication] = None
        # The comments property
        self._comments: Optional[List[workbook_comment.WorkbookComment]] = None
        # The functions property
        self._functions: Optional[workbook_functions.WorkbookFunctions] = None
        # Represents a collection of workbooks scoped named items (named ranges and constants). Read-only.
        self._names: Optional[List[workbook_named_item.WorkbookNamedItem]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.
        self._operations: Optional[List[workbook_operation.WorkbookOperation]] = None
        # Represents a collection of tables associated with the workbook. Read-only.
        self._tables: Optional[List[workbook_table.WorkbookTable]] = None
        # Represents a collection of worksheets associated with the workbook. Read-only.
        self._worksheets: Optional[List[workbook_worksheet.WorkbookWorksheet]] = None
    
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
    
    @property
    def functions(self,) -> Optional[workbook_functions.WorkbookFunctions]:
        """
        Gets the functions property value. The functions property
        Returns: Optional[workbook_functions.WorkbookFunctions]
        """
        return self._functions
    
    @functions.setter
    def functions(self,value: Optional[workbook_functions.WorkbookFunctions] = None) -> None:
        """
        Sets the functions property value. The functions property
        Args:
            value: Value to set for the functions property.
        """
        self._functions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
    
    @property
    def names(self,) -> Optional[List[workbook_named_item.WorkbookNamedItem]]:
        """
        Gets the names property value. Represents a collection of workbooks scoped named items (named ranges and constants). Read-only.
        Returns: Optional[List[workbook_named_item.WorkbookNamedItem]]
        """
        return self._names
    
    @names.setter
    def names(self,value: Optional[List[workbook_named_item.WorkbookNamedItem]] = None) -> None:
        """
        Sets the names property value. Represents a collection of workbooks scoped named items (named ranges and constants). Read-only.
        Args:
            value: Value to set for the names property.
        """
        self._names = value
    
    @property
    def operations(self,) -> Optional[List[workbook_operation.WorkbookOperation]]:
        """
        Gets the operations property value. The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.
        Returns: Optional[List[workbook_operation.WorkbookOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[workbook_operation.WorkbookOperation]] = None) -> None:
        """
        Sets the operations property value. The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
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
    
    @property
    def tables(self,) -> Optional[List[workbook_table.WorkbookTable]]:
        """
        Gets the tables property value. Represents a collection of tables associated with the workbook. Read-only.
        Returns: Optional[List[workbook_table.WorkbookTable]]
        """
        return self._tables
    
    @tables.setter
    def tables(self,value: Optional[List[workbook_table.WorkbookTable]] = None) -> None:
        """
        Sets the tables property value. Represents a collection of tables associated with the workbook. Read-only.
        Args:
            value: Value to set for the tables property.
        """
        self._tables = value
    
    @property
    def worksheets(self,) -> Optional[List[workbook_worksheet.WorkbookWorksheet]]:
        """
        Gets the worksheets property value. Represents a collection of worksheets associated with the workbook. Read-only.
        Returns: Optional[List[workbook_worksheet.WorkbookWorksheet]]
        """
        return self._worksheets
    
    @worksheets.setter
    def worksheets(self,value: Optional[List[workbook_worksheet.WorkbookWorksheet]] = None) -> None:
        """
        Sets the worksheets property value. Represents a collection of worksheets associated with the workbook. Read-only.
        Args:
            value: Value to set for the worksheets property.
        """
        self._worksheets = value
    

