from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
operation_status = lazy_import('msgraph.generated.models.operation_status')
result_info = lazy_import('msgraph.generated.models.result_info')

class CommsOperation(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def client_context(self,) -> Optional[str]:
        """
        Gets the clientContext property value. Unique Client Context string. Max limit is 256 chars.
        Returns: Optional[str]
        """
        return self._client_context
    
    @client_context.setter
    def client_context(self,value: Optional[str] = None) -> None:
        """
        Sets the clientContext property value. Unique Client Context string. Max limit is 256 chars.
        Args:
            value: Value to set for the clientContext property.
        """
        self._client_context = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new commsOperation and sets the default values.
        """
        super().__init__()
        # Unique Client Context string. Max limit is 256 chars.
        self._client_context: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The result information. Read-only.
        self._result_info: Optional[result_info.ResultInfo] = None
        # The status property
        self._status: Optional[operation_status.OperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommsOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommsOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_context": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "result_info": lambda n : setattr(self, 'result_info', n.get_object_value(result_info.ResultInfo)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(operation_status.OperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def result_info(self,) -> Optional[result_info.ResultInfo]:
        """
        Gets the resultInfo property value. The result information. Read-only.
        Returns: Optional[result_info.ResultInfo]
        """
        return self._result_info
    
    @result_info.setter
    def result_info(self,value: Optional[result_info.ResultInfo] = None) -> None:
        """
        Sets the resultInfo property value. The result information. Read-only.
        Args:
            value: Value to set for the resultInfo property.
        """
        self._result_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("clientContext", self.client_context)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[operation_status.OperationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[operation_status.OperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[operation_status.OperationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

