from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_answer, access_package_assignment, access_package_request_state, access_package_request_type, access_package_subject, entitlement_management_schedule, entity

from . import entity

@dataclass
class AccessPackageAssignmentRequest(entity.Entity):
    # The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.
    access_package: Optional[access_package.AccessPackage] = None
    # Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.
    answers: Optional[List[access_package_answer.AccessPackageAnswer]] = None
    # For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created.  For a requestType of userRemove, adminRemove or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.
    assignment: Optional[access_package_assignment.AccessPackageAssignment] = None
    # The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    completed_date_time: Optional[datetime] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter.
    created_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the request. The possible values are: notSpecified, userAdd, UserExtend, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. A request from the user themselves would have requestType of userAdd, userUpdate or userRemove. This property cannot be changed once set.
    request_type: Optional[access_package_request_type.AccessPackageRequestType] = None
    # The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
    requestor: Optional[access_package_subject.AccessPackageSubject] = None
    # The range of dates that access is to be assigned to the requestor. This property cannot be changed once set.
    schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
    # The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).
    state: Optional[access_package_request_state.AccessPackageRequestState] = None
    # More information on the request processing status. Read-only.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_answer, access_package_assignment, access_package_request_state, access_package_request_type, access_package_subject, entitlement_management_schedule, entity

        from . import access_package, access_package_answer, access_package_assignment, access_package_request_state, access_package_request_type, access_package_subject, entitlement_management_schedule, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "answers": lambda n : setattr(self, 'answers', n.get_collection_of_object_values(access_package_answer.AccessPackageAnswer)),
            "assignment": lambda n : setattr(self, 'assignment', n.get_object_value(access_package_assignment.AccessPackageAssignment)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_enum_value(access_package_request_type.AccessPackageRequestType)),
            "requestor": lambda n : setattr(self, 'requestor', n.get_object_value(access_package_subject.AccessPackageSubject)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(access_package_request_state.AccessPackageRequestState)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_collection_of_object_values("answers", self.answers)
        writer.write_object_value("assignment", self.assignment)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("requestType", self.request_type)
        writer.write_object_value("requestor", self.requestor)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("status", self.status)
    

