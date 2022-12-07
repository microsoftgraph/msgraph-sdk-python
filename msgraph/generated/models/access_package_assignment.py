from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_assignment_policy = lazy_import('msgraph.generated.models.access_package_assignment_policy')
access_package_assignment_state = lazy_import('msgraph.generated.models.access_package_assignment_state')
access_package_subject = lazy_import('msgraph.generated.models.access_package_subject')
entitlement_management_schedule = lazy_import('msgraph.generated.models.entitlement_management_schedule')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageAssignment(entity.Entity):
    @property
    def access_package(self,) -> Optional[access_package.AccessPackage]:
        """
        Gets the accessPackage property value. Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        Returns: Optional[access_package.AccessPackage]
        """
        return self._access_package
    
    @access_package.setter
    def access_package(self,value: Optional[access_package.AccessPackage] = None) -> None:
        """
        Sets the accessPackage property value. Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        Args:
            value: Value to set for the accessPackage property.
        """
        self._access_package = value
    
    @property
    def assignment_policy(self,) -> Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]:
        """
        Gets the assignmentPolicy property value. Read-only. Supports $filter (eq) on the id property and $expand query parameters.
        Returns: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]
        """
        return self._assignment_policy
    
    @assignment_policy.setter
    def assignment_policy(self,value: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy] = None) -> None:
        """
        Sets the assignmentPolicy property value. Read-only. Supports $filter (eq) on the id property and $expand query parameters.
        Args:
            value: Value to set for the assignmentPolicy property.
        """
        self._assignment_policy = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignment and sets the default values.
        """
        super().__init__()
        # Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
        self._access_package: Optional[access_package.AccessPackage] = None
        # Read-only. Supports $filter (eq) on the id property and $expand query parameters.
        self._assignment_policy: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._expired_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # When the access assignment is to be in place. Read-only.
        self._schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
        # The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).
        self._state: Optional[access_package_assignment_state.AccessPackageAssignmentState] = None
        # More information about the assignment lifecycle.  Possible values include Delivering, Delivered, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered.  Read-only.
        self._status: Optional[str] = None
        # The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
        self._target: Optional[access_package_subject.AccessPackageSubject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignment()
    
    @property
    def expired_date_time(self,) -> Optional[datetime]:
        """
        Gets the expiredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._expired_date_time
    
    @expired_date_time.setter
    def expired_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the expiredDateTime property.
        """
        self._expired_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "assignment_policy": lambda n : setattr(self, 'assignment_policy', n.get_object_value(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "expired_date_time": lambda n : setattr(self, 'expired_date_time', n.get_datetime_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(access_package_assignment_state.AccessPackageAssignmentState)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(access_package_subject.AccessPackageSubject)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def schedule(self,) -> Optional[entitlement_management_schedule.EntitlementManagementSchedule]:
        """
        Gets the schedule property value. When the access assignment is to be in place. Read-only.
        Returns: Optional[entitlement_management_schedule.EntitlementManagementSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None) -> None:
        """
        Sets the schedule property value. When the access assignment is to be in place. Read-only.
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
        writer.write_object_value("assignmentPolicy", self.assignment_policy)
        writer.write_datetime_value("expiredDateTime", self.expired_date_time)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("status", self.status)
        writer.write_object_value("target", self.target)
    
    @property
    def state(self,) -> Optional[access_package_assignment_state.AccessPackageAssignmentState]:
        """
        Gets the state property value. The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).
        Returns: Optional[access_package_assignment_state.AccessPackageAssignmentState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[access_package_assignment_state.AccessPackageAssignmentState] = None) -> None:
        """
        Sets the state property value. The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. More information about the assignment lifecycle.  Possible values include Delivering, Delivered, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered.  Read-only.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. More information about the assignment lifecycle.  Possible values include Delivering, Delivered, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered.  Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def target(self,) -> Optional[access_package_subject.AccessPackageSubject]:
        """
        Gets the target property value. The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
        Returns: Optional[access_package_subject.AccessPackageSubject]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[access_package_subject.AccessPackageSubject] = None) -> None:
        """
        Sets the target property value. The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

