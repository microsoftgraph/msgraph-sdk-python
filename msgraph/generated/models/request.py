from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
    from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
    from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
    from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
    from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
    from .user_consent_request import UserConsentRequest

from .entity import Entity

@dataclass
class Request(Entity, Parsable):
    # The identifier of the approval of the request.
    approval_id: Optional[str] = None
    # The request completion date time.
    completed_date_time: Optional[datetime.datetime] = None
    # The principal that created the request.
    created_by: Optional[IdentitySet] = None
    # The request creation date time.
    created_date_time: Optional[datetime.datetime] = None
    # Free text field to define any custom data for the request. Not used.
    custom_data: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Request:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Request
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest".casefold():
            from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest

            return PrivilegedAccessGroupAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest".casefold():
            from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

            return PrivilegedAccessGroupEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessScheduleRequest".casefold():
            from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

            return PrivilegedAccessScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest".casefold():
            from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

            return UnifiedRoleAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest".casefold():
            from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

            return UnifiedRoleEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userConsentRequest".casefold():
            from .user_consent_request import UserConsentRequest

            return UserConsentRequest()
        return Request()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
        from .user_consent_request import UserConsentRequest

        from .entity import Entity
        from .identity_set import IdentitySet
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
        from .user_consent_request import UserConsentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "approvalId": lambda n : setattr(self, 'approval_id', n.get_str_value()),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customData": lambda n : setattr(self, 'custom_data', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("approvalId", self.approval_id)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("customData", self.custom_data)
        writer.write_str_value("status", self.status)
    

