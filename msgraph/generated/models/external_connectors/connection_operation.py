from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import connection_operation_status
from .. import entity, public_error

class ConnectionOperation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ConnectionOperation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.externalConnectors.connectionOperation"
        # If status is failed, provides more information about the error that caused the failure.
        self._error: Optional[public_error.PublicError] = None
        # Indicates the status of the asynchronous operation. Possible values are: unspecified, inprogress, completed, failed, unknownFutureValue.
        self._status: Optional[connection_operation_status.ConnectionOperationStatus] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectionOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectionOperation
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return ConnectionOperation()

    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. If status is failed, provides more information about the error that caused the failure.
        Returns: Optional[public_error.PublicError]
        """
        return self._error

    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. If status is failed, provides more information about the error that caused the failure.
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
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(connection_operation_status.ConnectionOperationStatus)),
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("error", self.error)
        writer.write_enum_value("status", self.status)

    @property
    def status(self,) -> Optional[connection_operation_status.ConnectionOperationStatus]:
        """
        Gets the status property value. Indicates the status of the asynchronous operation. Possible values are: unspecified, inprogress, completed, failed, unknownFutureValue.
        Returns: Optional[connection_operation_status.ConnectionOperationStatus]
        """
        return self._status

    @status.setter
    def status(self,value: Optional[connection_operation_status.ConnectionOperationStatus] = None) -> None:
        """
        Sets the status property value. Indicates the status of the asynchronous operation. Possible values are: unspecified, inprogress, completed, failed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value


