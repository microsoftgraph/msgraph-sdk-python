from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
long_running_operation_status = lazy_import('msgraph.generated.models.long_running_operation_status')

class LongRunningOperation(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new longRunningOperation and sets the default values.
        """
        super().__init__()
        # The start time of the operation.
        self._created_date_time: Optional[datetime] = None
        # The time of the last action in the operation.
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # URI of the resource that the operation is performed on.
        self._resource_location: Optional[str] = None
        # The status of the operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
        self._status: Optional[long_running_operation_status.LongRunningOperationStatus] = None
        # Details about the status of the operation.
        self._status_detail: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The start time of the operation.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The start time of the operation.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LongRunningOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LongRunningOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LongRunningOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "resource_location": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(long_running_operation_status.LongRunningOperationStatus)),
            "status_detail": lambda n : setattr(self, 'status_detail', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The time of the last action in the operation.
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The time of the last action in the operation.
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def resource_location(self,) -> Optional[str]:
        """
        Gets the resourceLocation property value. URI of the resource that the operation is performed on.
        Returns: Optional[str]
        """
        return self._resource_location
    
    @resource_location.setter
    def resource_location(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceLocation property value. URI of the resource that the operation is performed on.
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusDetail", self.status_detail)
    
    @property
    def status(self,) -> Optional[long_running_operation_status.LongRunningOperationStatus]:
        """
        Gets the status property value. The status of the operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
        Returns: Optional[long_running_operation_status.LongRunningOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[long_running_operation_status.LongRunningOperationStatus] = None) -> None:
        """
        Sets the status property value. The status of the operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def status_detail(self,) -> Optional[str]:
        """
        Gets the statusDetail property value. Details about the status of the operation.
        Returns: Optional[str]
        """
        return self._status_detail
    
    @status_detail.setter
    def status_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the statusDetail property value. Details about the status of the operation.
        Args:
            value: Value to set for the statusDetail property.
        """
        self._status_detail = value
    

