from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_dynamic_approval_stage import AccessPackageDynamicApprovalStage
    from .subject_set import SubjectSet

@dataclass
class AccessPackageApprovalStage(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The number of days that a request can be pending a response before it is automatically denied.
    duration_before_automatic_denial: Optional[datetime.timedelta] = None
    # If escalation is required, the time a request can be pending a response from a primary approver.
    duration_before_escalation: Optional[datetime.timedelta] = None
    # If escalation is enabled and the primary approvers do not respond before the escalation time, the escalationApprovers are the users who will be asked to approve requests.
    escalation_approvers: Optional[list[SubjectSet]] = None
    # The subjects, typically users, who are the fallback escalation approvers.
    fallback_escalation_approvers: Optional[list[SubjectSet]] = None
    # The subjects, typically users, who are the fallback primary approvers.
    fallback_primary_approvers: Optional[list[SubjectSet]] = None
    # Indicates whether the approver is required to provide a justification for approving a request.
    is_approver_justification_required: Optional[bool] = None
    # If true, then one or more escalationApprovers are configured in this approval stage.
    is_escalation_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The subjects, typically users, who will be asked to approve requests. A collection of singleUser, groupMembers, requestorManager, internalSponsors, externalSponsors, or targetUserSponsors.
    primary_approvers: Optional[list[SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageApprovalStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageApprovalStage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageDynamicApprovalStage".casefold():
            from .access_package_dynamic_approval_stage import AccessPackageDynamicApprovalStage

            return AccessPackageDynamicApprovalStage()
        return AccessPackageApprovalStage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_dynamic_approval_stage import AccessPackageDynamicApprovalStage
        from .subject_set import SubjectSet

        from .access_package_dynamic_approval_stage import AccessPackageDynamicApprovalStage
        from .subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "durationBeforeAutomaticDenial": lambda n : setattr(self, 'duration_before_automatic_denial', n.get_timedelta_value()),
            "durationBeforeEscalation": lambda n : setattr(self, 'duration_before_escalation', n.get_timedelta_value()),
            "escalationApprovers": lambda n : setattr(self, 'escalation_approvers', n.get_collection_of_object_values(SubjectSet)),
            "fallbackEscalationApprovers": lambda n : setattr(self, 'fallback_escalation_approvers', n.get_collection_of_object_values(SubjectSet)),
            "fallbackPrimaryApprovers": lambda n : setattr(self, 'fallback_primary_approvers', n.get_collection_of_object_values(SubjectSet)),
            "isApproverJustificationRequired": lambda n : setattr(self, 'is_approver_justification_required', n.get_bool_value()),
            "isEscalationEnabled": lambda n : setattr(self, 'is_escalation_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryApprovers": lambda n : setattr(self, 'primary_approvers', n.get_collection_of_object_values(SubjectSet)),
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
        writer.write_timedelta_value("durationBeforeAutomaticDenial", self.duration_before_automatic_denial)
        writer.write_timedelta_value("durationBeforeEscalation", self.duration_before_escalation)
        writer.write_collection_of_object_values("escalationApprovers", self.escalation_approvers)
        writer.write_collection_of_object_values("fallbackEscalationApprovers", self.fallback_escalation_approvers)
        writer.write_collection_of_object_values("fallbackPrimaryApprovers", self.fallback_primary_approvers)
        writer.write_bool_value("isApproverJustificationRequired", self.is_approver_justification_required)
        writer.write_bool_value("isEscalationEnabled", self.is_escalation_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("primaryApprovers", self.primary_approvers)
        writer.write_additional_data_value(self.additional_data)
    

