from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_access_assignment, delegated_admin_access_details, delegated_admin_relationship_customer_participant, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_relationship_status, entity

from . import entity

class DelegatedAdminRelationship(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DelegatedAdminRelationship and sets the default values.
        """
        super().__init__()
        # The access assignments associated with the delegated admin relationship.
        self._access_assignments: Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]] = None
        # The accessDetails property
        self._access_details: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None
        # The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only.
        self._activated_date_time: Optional[datetime] = None
        # The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Cannot be changed by the customer.
        self._customer: Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant] = None
        # The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner. This is set by the partner only when the relationship is in the created status and cannot be changed by the customer.
        self._display_name: Optional[str] = None
        # The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and cannot be changed by the customer.
        self._duration: Optional[timedelta] = None
        # The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only.
        self._end_date_time: Optional[datetime] = None
        # The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The long running operations associated with the delegated admin relationship.
        self._operations: Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]] = None
        # The requests associated with the delegated admin relationship.
        self._requests: Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]] = None
        # The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderBy.
        self._status: Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus] = None
    
    @property
    def access_assignments(self,) -> Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]]:
        """
        Gets the accessAssignments property value. The access assignments associated with the delegated admin relationship.
        Returns: Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]]
        """
        return self._access_assignments
    
    @access_assignments.setter
    def access_assignments(self,value: Optional[List[delegated_admin_access_assignment.DelegatedAdminAccessAssignment]] = None) -> None:
        """
        Sets the accessAssignments property value. The access assignments associated with the delegated admin relationship.
        Args:
            value: Value to set for the access_assignments property.
        """
        self._access_assignments = value
    
    @property
    def access_details(self,) -> Optional[delegated_admin_access_details.DelegatedAdminAccessDetails]:
        """
        Gets the accessDetails property value. The accessDetails property
        Returns: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails]
        """
        return self._access_details
    
    @access_details.setter
    def access_details(self,value: Optional[delegated_admin_access_details.DelegatedAdminAccessDetails] = None) -> None:
        """
        Sets the accessDetails property value. The accessDetails property
        Args:
            value: Value to set for the access_details property.
        """
        self._access_details = value
    
    @property
    def activated_date_time(self,) -> Optional[datetime]:
        """
        Gets the activatedDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only.
        Returns: Optional[datetime]
        """
        return self._activated_date_time
    
    @activated_date_time.setter
    def activated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activatedDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only.
        Args:
            value: Value to set for the activated_date_time property.
        """
        self._activated_date_time = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationship
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminRelationship()
    
    @property
    def customer(self,) -> Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant]:
        """
        Gets the customer property value. The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Cannot be changed by the customer.
        Returns: Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant]
        """
        return self._customer
    
    @customer.setter
    def customer(self,value: Optional[delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant] = None) -> None:
        """
        Sets the customer property value. The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Cannot be changed by the customer.
        Args:
            value: Value to set for the customer property.
        """
        self._customer = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner. This is set by the partner only when the relationship is in the created status and cannot be changed by the customer.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner. This is set by the partner only when the relationship is in the created status and cannot be changed by the customer.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def duration(self,) -> Optional[timedelta]:
        """
        Gets the duration property value. The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and cannot be changed by the customer.
        Returns: Optional[timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the duration property value. The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and cannot be changed by the customer.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only.
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_access_assignment, delegated_admin_access_details, delegated_admin_relationship_customer_participant, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_relationship_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessAssignments": lambda n : setattr(self, 'access_assignments', n.get_collection_of_object_values(delegated_admin_access_assignment.DelegatedAdminAccessAssignment)),
            "accessDetails": lambda n : setattr(self, 'access_details', n.get_object_value(delegated_admin_access_details.DelegatedAdminAccessDetails)),
            "activatedDateTime": lambda n : setattr(self, 'activated_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(delegated_admin_relationship_customer_participant.DelegatedAdminRelationshipCustomerParticipant)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation)),
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(delegated_admin_relationship_request.DelegatedAdminRelationshipRequest)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(delegated_admin_relationship_status.DelegatedAdminRelationshipStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def operations(self,) -> Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]]:
        """
        Gets the operations property value. The long running operations associated with the delegated admin relationship.
        Returns: Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation]] = None) -> None:
        """
        Sets the operations property value. The long running operations associated with the delegated admin relationship.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def requests(self,) -> Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]]:
        """
        Gets the requests property value. The requests associated with the delegated admin relationship.
        Returns: Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]]
        """
        return self._requests
    
    @requests.setter
    def requests(self,value: Optional[List[delegated_admin_relationship_request.DelegatedAdminRelationshipRequest]] = None) -> None:
        """
        Sets the requests property value. The requests associated with the delegated admin relationship.
        Args:
            value: Value to set for the requests property.
        """
        self._requests = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessAssignments", self.access_assignments)
        writer.write_object_value("accessDetails", self.access_details)
        writer.write_datetime_value("activatedDateTime", self.activated_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("customer", self.customer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_timedelta_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus]:
        """
        Gets the status property value. The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderBy.
        Returns: Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[delegated_admin_relationship_status.DelegatedAdminRelationshipStatus] = None) -> None:
        """
        Sets the status property value. The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderBy.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

