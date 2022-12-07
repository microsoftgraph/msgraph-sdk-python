from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_policy_operation_status = lazy_import('msgraph.generated.models.data_policy_operation_status')
entity = lazy_import('msgraph.generated.models.entity')

class DataPolicyOperation(entity.Entity):
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Null until the operation completes.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Null until the operation completes.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DataPolicyOperation and sets the default values.
        """
        super().__init__()
        # Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Null until the operation completes.
        self._completed_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the progress of an operation.
        self._progress: Optional[float] = None
        # Possible values are: notStarted, running, complete, failed, unknownFutureValue.
        self._status: Optional[data_policy_operation_status.DataPolicyOperationStatus] = None
        # The URL location to where data is being exported for export requests.
        self._storage_location: Optional[str] = None
        # Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._submitted_date_time: Optional[datetime] = None
        # The id for the user on whom the operation is performed.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataPolicyOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataPolicyOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataPolicyOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(data_policy_operation_status.DataPolicyOperationStatus)),
            "storage_location": lambda n : setattr(self, 'storage_location', n.get_str_value()),
            "submitted_date_time": lambda n : setattr(self, 'submitted_date_time', n.get_datetime_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def progress(self,) -> Optional[float]:
        """
        Gets the progress property value. Specifies the progress of an operation.
        Returns: Optional[float]
        """
        return self._progress
    
    @progress.setter
    def progress(self,value: Optional[float] = None) -> None:
        """
        Sets the progress property value. Specifies the progress of an operation.
        Args:
            value: Value to set for the progress property.
        """
        self._progress = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_float_value("progress", self.progress)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("storageLocation", self.storage_location)
        writer.write_datetime_value("submittedDateTime", self.submitted_date_time)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def status(self,) -> Optional[data_policy_operation_status.DataPolicyOperationStatus]:
        """
        Gets the status property value. Possible values are: notStarted, running, complete, failed, unknownFutureValue.
        Returns: Optional[data_policy_operation_status.DataPolicyOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[data_policy_operation_status.DataPolicyOperationStatus] = None) -> None:
        """
        Sets the status property value. Possible values are: notStarted, running, complete, failed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def storage_location(self,) -> Optional[str]:
        """
        Gets the storageLocation property value. The URL location to where data is being exported for export requests.
        Returns: Optional[str]
        """
        return self._storage_location
    
    @storage_location.setter
    def storage_location(self,value: Optional[str] = None) -> None:
        """
        Sets the storageLocation property value. The URL location to where data is being exported for export requests.
        Args:
            value: Value to set for the storageLocation property.
        """
        self._storage_location = value
    
    @property
    def submitted_date_time(self,) -> Optional[datetime]:
        """
        Gets the submittedDateTime property value. Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._submitted_date_time
    
    @submitted_date_time.setter
    def submitted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the submittedDateTime property value. Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the submittedDateTime property.
        """
        self._submitted_date_time = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The id for the user on whom the operation is performed.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The id for the user on whom the operation is performed.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

