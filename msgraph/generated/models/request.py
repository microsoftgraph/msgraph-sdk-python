from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class Request(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def approval_id(self,) -> Optional[str]:
        """
        Gets the approvalId property value. The identifier of the approval of the request.
        Returns: Optional[str]
        """
        return self._approval_id
    
    @approval_id.setter
    def approval_id(self,value: Optional[str] = None) -> None:
        """
        Sets the approvalId property value. The identifier of the approval of the request.
        Args:
            value: Value to set for the approvalId property.
        """
        self._approval_id = value
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The request completion date time.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The request completion date time.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new request and sets the default values.
        """
        super().__init__()
        # The identifier of the approval of the request.
        self._approval_id: Optional[str] = None
        # The request completion date time.
        self._completed_date_time: Optional[datetime] = None
        # The principal that created the request.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The request creation date time.
        self._created_date_time: Optional[datetime] = None
        # Free text field to define any custom data for the request. Not used.
        self._custom_data: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
        self._status: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The principal that created the request.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The principal that created the request.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The request creation date time.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The request creation date time.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Request:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Request
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Request()
    
    @property
    def custom_data(self,) -> Optional[str]:
        """
        Gets the customData property value. Free text field to define any custom data for the request. Not used.
        Returns: Optional[str]
        """
        return self._custom_data
    
    @custom_data.setter
    def custom_data(self,value: Optional[str] = None) -> None:
        """
        Sets the customData property value. Free text field to define any custom data for the request. Not used.
        Args:
            value: Value to set for the customData property.
        """
        self._custom_data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approval_id": lambda n : setattr(self, 'approval_id', n.get_str_value()),
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custom_data": lambda n : setattr(self, 'custom_data', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("approvalId", self.approval_id)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("customData", self.custom_data)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

