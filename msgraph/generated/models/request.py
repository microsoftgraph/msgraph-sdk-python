from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, unified_role_assignment_schedule_request, unified_role_eligibility_schedule_request, user_consent_request

from . import entity

@dataclass
class Request(entity.Entity):
    # The identifier of the approval of the request.
    approval_id: Optional[str] = None
    # The request completion date time.
    completed_date_time: Optional[datetime] = None
    # The principal that created the request.
    created_by: Optional[identity_set.IdentitySet] = None
    # The request creation date time.
    created_date_time: Optional[datetime] = None
    # Free text field to define any custom data for the request. Not used.
    custom_data: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
    status: Optional[str] = None
    
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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest":
                from . import unified_role_assignment_schedule_request

                return unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest()
            if mapping_value == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest":
                from . import unified_role_eligibility_schedule_request

                return unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest()
            if mapping_value == "#microsoft.graph.userConsentRequest":
                from . import user_consent_request

                return user_consent_request.UserConsentRequest()
        return Request()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, unified_role_assignment_schedule_request, unified_role_eligibility_schedule_request, user_consent_request

        fields: Dict[str, Callable[[Any], None]] = {
            "approvalId": lambda n : setattr(self, 'approval_id', n.get_str_value()),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
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
    

