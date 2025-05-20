from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_question import AccessPackageQuestion
    from .entitlement_management_schedule import EntitlementManagementSchedule

@dataclass
class AccessPackageAssignmentRequestRequirements(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether the requestor is allowed to set a custom schedule.
    allow_custom_assignment_schedule: Optional[bool] = None
    # Indicates whether a request to add must be approved by an approver.
    is_approval_required_for_add: Optional[bool] = None
    # Indicates whether a request to update must be approved by an approver.
    is_approval_required_for_update: Optional[bool] = None
    # Indicates whether requestors must justify requesting access to an access package.
    is_requestor_justification_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The description of the policy that the user is trying to request access using.
    policy_description: Optional[str] = None
    # The display name of the policy that the user is trying to request access using.
    policy_display_name: Optional[str] = None
    # The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
    policy_id: Optional[str] = None
    # The questions property
    questions: Optional[list[AccessPackageQuestion]] = None
    # Schedule restrictions enforced, if any.
    schedule: Optional[EntitlementManagementSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentRequestRequirements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestRequirements
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentRequestRequirements()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_question import AccessPackageQuestion
        from .entitlement_management_schedule import EntitlementManagementSchedule

        from .access_package_question import AccessPackageQuestion
        from .entitlement_management_schedule import EntitlementManagementSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "allowCustomAssignmentSchedule": lambda n : setattr(self, 'allow_custom_assignment_schedule', n.get_bool_value()),
            "isApprovalRequiredForAdd": lambda n : setattr(self, 'is_approval_required_for_add', n.get_bool_value()),
            "isApprovalRequiredForUpdate": lambda n : setattr(self, 'is_approval_required_for_update', n.get_bool_value()),
            "isRequestorJustificationRequired": lambda n : setattr(self, 'is_requestor_justification_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyDescription": lambda n : setattr(self, 'policy_description', n.get_str_value()),
            "policyDisplayName": lambda n : setattr(self, 'policy_display_name', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(AccessPackageQuestion)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(EntitlementManagementSchedule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allowCustomAssignmentSchedule", self.allow_custom_assignment_schedule)
        writer.write_bool_value("isApprovalRequiredForAdd", self.is_approval_required_for_add)
        writer.write_bool_value("isApprovalRequiredForUpdate", self.is_approval_required_for_update)
        writer.write_bool_value("isRequestorJustificationRequired", self.is_requestor_justification_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyDescription", self.policy_description)
        writer.write_str_value("policyDisplayName", self.policy_display_name)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

