from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_question, entitlement_management_schedule

@dataclass
class AccessPackageAssignmentRequestRequirements(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates whether the requestor is allowed to set a custom schedule.
    allow_custom_assignment_schedule: Optional[bool] = None
    # Indicates whether a request to add must be approved by an approver.
    is_approval_required_for_add: Optional[bool] = None
    # Indicates whether a request to update must be approved by an approver.
    is_approval_required_for_update: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The description of the policy that the user is trying to request access using.
    policy_description: Optional[str] = None
    # The display name of the policy that the user is trying to request access using.
    policy_display_name: Optional[str] = None
    # The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
    policy_id: Optional[str] = None
    # The questions property
    questions: Optional[List[access_package_question.AccessPackageQuestion]] = None
    # Schedule restrictions enforced, if any.
    schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequestRequirements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestRequirements
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequestRequirements()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_question, entitlement_management_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "allowCustomAssignmentSchedule": lambda n : setattr(self, 'allow_custom_assignment_schedule', n.get_bool_value()),
            "isApprovalRequiredForAdd": lambda n : setattr(self, 'is_approval_required_for_add', n.get_bool_value()),
            "isApprovalRequiredForUpdate": lambda n : setattr(self, 'is_approval_required_for_update', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyDescription": lambda n : setattr(self, 'policy_description', n.get_str_value()),
            "policyDisplayName": lambda n : setattr(self, 'policy_display_name', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(access_package_question.AccessPackageQuestion)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowCustomAssignmentSchedule", self.allow_custom_assignment_schedule)
        writer.write_bool_value("isApprovalRequiredForAdd", self.is_approval_required_for_add)
        writer.write_bool_value("isApprovalRequiredForUpdate", self.is_approval_required_for_update)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyDescription", self.policy_description)
        writer.write_str_value("policyDisplayName", self.policy_display_name)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

