from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_operation_error = lazy_import('msgraph.generated.models.workbook_operation_error')
workbook_operation_status = lazy_import('msgraph.generated.models.workbook_operation_status')

class WorkbookOperation(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new workbookOperation and sets the default values.
        """
        super().__init__()
        # The error returned by the operation.
        self._error: Optional[workbook_operation_error.WorkbookOperationError] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resource URI for the result.
        self._resource_location: Optional[str] = None
        # The status property
        self._status: Optional[workbook_operation_status.WorkbookOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookOperation()
    
    @property
    def error(self,) -> Optional[workbook_operation_error.WorkbookOperationError]:
        """
        Gets the error property value. The error returned by the operation.
        Returns: Optional[workbook_operation_error.WorkbookOperationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[workbook_operation_error.WorkbookOperationError] = None) -> None:
        """
        Sets the error property value. The error returned by the operation.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(workbook_operation_error.WorkbookOperationError)),
            "resource_location": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(workbook_operation_status.WorkbookOperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_location(self,) -> Optional[str]:
        """
        Gets the resourceLocation property value. The resource URI for the result.
        Returns: Optional[str]
        """
        return self._resource_location
    
    @resource_location.setter
    def resource_location(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceLocation property value. The resource URI for the result.
        Args:
            value: Value to set for the resourceLocation property.
        """
        self._resource_location = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("error", self.error)
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[workbook_operation_status.WorkbookOperationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[workbook_operation_status.WorkbookOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[workbook_operation_status.WorkbookOperationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

