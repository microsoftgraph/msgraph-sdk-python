from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_assignment = lazy_import('msgraph.generated.models.access_package_assignment')
access_package_request_state = lazy_import('msgraph.generated.models.access_package_request_state')
access_package_request_type = lazy_import('msgraph.generated.models.access_package_request_type')
access_package_subject = lazy_import('msgraph.generated.models.access_package_subject')
entitlement_management_schedule = lazy_import('msgraph.generated.models.entitlement_management_schedule')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageAssignmentRequest(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def access_package(self,) -> Optional[access_package.AccessPackage]:
        """
        Gets the accessPackage property value. The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.
        Returns: Optional[access_package.AccessPackage]
        """
        return self._access_package
    
    @access_package.setter
    def access_package(self,value: Optional[access_package.AccessPackage] = None) -> None:
        """
        Sets the accessPackage property value. The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.
        Args:
            value: Value to set for the accessPackage property.
        """
        self._access_package = value
    
    @property
    def assignment(self,) -> Optional[access_package_assignment.AccessPackageAssignment]:
        """
        Gets the assignment property value. For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created.  For a requestType of userRemove, adminRemove or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.
        Returns: Optional[access_package_assignment.AccessPackageAssignment]
        """
        return self._assignment
    
    @assignment.setter
    def assignment(self,value: Optional[access_package_assignment.AccessPackageAssignment] = None) -> None:
        """
        Sets the assignment property value. For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created.  For a requestType of userRemove, adminRemove or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.
        Args:
            value: Value to set for the assignment property.
        """
        self._assignment = value
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentRequest and sets the default values.
        """
        super().__init__()
        # The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.
        self._access_package: Optional[access_package.AccessPackage] = None
        # For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created.  For a requestType of userRemove, adminRemove or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.
        self._assignment: Optional[access_package_assignment.AccessPackageAssignment] = None
        # The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._completed_date_time: Optional[datetime] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
        self._requestor: Optional[access_package_subject.AccessPackageSubject] = None
        # The type of the request. The possible values are: notSpecified, userAdd, UserExtend, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. A request from the user themselves would have requestType of userAdd, userUpdate or userRemove. This property cannot be changed once set.
        self._request_type: Optional[access_package_request_type.AccessPackageRequestType] = None
        # The range of dates that access is to be assigned to the requestor. This property cannot be changed once set.
        self._schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
        # The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).
        self._state: Optional[access_package_request_state.AccessPackageRequestState] = None
        # More information on the request processing status. Read-only.
        self._status: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "assignment": lambda n : setattr(self, 'assignment', n.get_object_value(access_package_assignment.AccessPackageAssignment)),
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "requestor": lambda n : setattr(self, 'requestor', n.get_object_value(access_package_subject.AccessPackageSubject)),
            "request_type": lambda n : setattr(self, 'request_type', n.get_enum_value(access_package_request_type.AccessPackageRequestType)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(access_package_request_state.AccessPackageRequestState)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def requestor(self,) -> Optional[access_package_subject.AccessPackageSubject]:
        """
        Gets the requestor property value. The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
        Returns: Optional[access_package_subject.AccessPackageSubject]
        """
        return self._requestor
    
    @requestor.setter
    def requestor(self,value: Optional[access_package_subject.AccessPackageSubject] = None) -> None:
        """
        Sets the requestor property value. The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the requestor property.
        """
        self._requestor = value
    
    @property
    def request_type(self,) -> Optional[access_package_request_type.AccessPackageRequestType]:
        """
        Gets the requestType property value. The type of the request. The possible values are: notSpecified, userAdd, UserExtend, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. A request from the user themselves would have requestType of userAdd, userUpdate or userRemove. This property cannot be changed once set.
        Returns: Optional[access_package_request_type.AccessPackageRequestType]
        """
        return self._request_type
    
    @request_type.setter
    def request_type(self,value: Optional[access_package_request_type.AccessPackageRequestType] = None) -> None:
        """
        Sets the requestType property value. The type of the request. The possible values are: notSpecified, userAdd, UserExtend, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. A request from the user themselves would have requestType of userAdd, userUpdate or userRemove. This property cannot be changed once set.
        Args:
            value: Value to set for the requestType property.
        """
        self._request_type = value
    
    @property
    def schedule(self,) -> Optional[entitlement_management_schedule.EntitlementManagementSchedule]:
        """
        Gets the schedule property value. The range of dates that access is to be assigned to the requestor. This property cannot be changed once set.
        Returns: Optional[entitlement_management_schedule.EntitlementManagementSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None) -> None:
        """
        Sets the schedule property value. The range of dates that access is to be assigned to the requestor. This property cannot be changed once set.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_object_value("assignment", self.assignment)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("requestor", self.requestor)
        writer.write_enum_value("requestType", self.request_type)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("status", self.status)
    
    @property
    def state(self,) -> Optional[access_package_request_state.AccessPackageRequestState]:
        """
        Gets the state property value. The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).
        Returns: Optional[access_package_request_state.AccessPackageRequestState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[access_package_request_state.AccessPackageRequestState] = None) -> None:
        """
        Sets the state property value. The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. More information on the request processing status. Read-only.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. More information on the request processing status. Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

