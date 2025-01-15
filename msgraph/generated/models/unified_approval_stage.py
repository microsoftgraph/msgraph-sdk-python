from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_set import SubjectSet

@dataclass
class UnifiedApprovalStage(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The number of days that a request can be pending a response before it is automatically denied.
    approval_stage_time_out_in_days: Optional[int] = None
    # The escalation approvers for this stage when the primary approvers don't respond.
    escalation_approvers: Optional[list[SubjectSet]] = None
    # The time a request can be pending a response from a primary approver before it can be escalated to the escalation approvers.
    escalation_time_in_minutes: Optional[int] = None
    # Indicates whether the approver must provide justification for their reponse.
    is_approver_justification_required: Optional[bool] = None
    # Indicates whether escalation if enabled.
    is_escalation_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The primary approvers of this stage.
    primary_approvers: Optional[list[SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedApprovalStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedApprovalStage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedApprovalStage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .subject_set import SubjectSet

        from .subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "approvalStageTimeOutInDays": lambda n : setattr(self, 'approval_stage_time_out_in_days', n.get_int_value()),
            "escalationApprovers": lambda n : setattr(self, 'escalation_approvers', n.get_collection_of_object_values(SubjectSet)),
            "escalationTimeInMinutes": lambda n : setattr(self, 'escalation_time_in_minutes', n.get_int_value()),
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
        writer.write_int_value("approvalStageTimeOutInDays", self.approval_stage_time_out_in_days)
        writer.write_collection_of_object_values("escalationApprovers", self.escalation_approvers)
        writer.write_int_value("escalationTimeInMinutes", self.escalation_time_in_minutes)
        writer.write_bool_value("isApproverJustificationRequired", self.is_approver_justification_required)
        writer.write_bool_value("isEscalationEnabled", self.is_escalation_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("primaryApprovers", self.primary_approvers)
        writer.write_additional_data_value(self.additional_data)
    

