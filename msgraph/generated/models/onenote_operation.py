from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

onenote_operation_error = lazy_import('msgraph.generated.models.onenote_operation_error')
operation = lazy_import('msgraph.generated.models.operation')

class OnenoteOperation(operation.Operation):
    def __init__(self,) -> None:
        """
        Instantiates a new OnenoteOperation and sets the default values.
        """
        super().__init__()
        # The error returned by the operation.
        self._error: Optional[onenote_operation_error.OnenoteOperationError] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operation percent complete if the operation is still in running status.
        self._percent_complete: Optional[str] = None
        # The resource id.
        self._resource_id: Optional[str] = None
        # The resource URI for the object. For example, the resource URI for a copied page or section.
        self._resource_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenoteOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenoteOperation()
    
    @property
    def error(self,) -> Optional[onenote_operation_error.OnenoteOperationError]:
        """
        Gets the error property value. The error returned by the operation.
        Returns: Optional[onenote_operation_error.OnenoteOperationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[onenote_operation_error.OnenoteOperationError] = None) -> None:
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
            "error": lambda n : setattr(self, 'error', n.get_object_value(onenote_operation_error.OnenoteOperationError)),
            "percent_complete": lambda n : setattr(self, 'percent_complete', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resource_location": lambda n : setattr(self, 'resource_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def percent_complete(self,) -> Optional[str]:
        """
        Gets the percentComplete property value. The operation percent complete if the operation is still in running status.
        Returns: Optional[str]
        """
        return self._percent_complete
    
    @percent_complete.setter
    def percent_complete(self,value: Optional[str] = None) -> None:
        """
        Sets the percentComplete property value. The operation percent complete if the operation is still in running status.
        Args:
            value: Value to set for the percentComplete property.
        """
        self._percent_complete = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. The resource id.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. The resource id.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    @property
    def resource_location(self,) -> Optional[str]:
        """
        Gets the resourceLocation property value. The resource URI for the object. For example, the resource URI for a copied page or section.
        Returns: Optional[str]
        """
        return self._resource_location
    
    @resource_location.setter
    def resource_location(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceLocation property value. The resource URI for the object. For example, the resource URI for a copied page or section.
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
        writer.write_str_value("percentComplete", self.percent_complete)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("resourceLocation", self.resource_location)
    

