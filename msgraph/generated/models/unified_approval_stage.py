from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class UnifiedApprovalStage(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def approval_stage_time_out_in_days(self,) -> Optional[int]:
        """
        Gets the approvalStageTimeOutInDays property value. The number of days that a request can be pending a response before it is automatically denied.
        Returns: Optional[int]
        """
        return self._approval_stage_time_out_in_days
    
    @approval_stage_time_out_in_days.setter
    def approval_stage_time_out_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the approvalStageTimeOutInDays property value. The number of days that a request can be pending a response before it is automatically denied.
        Args:
            value: Value to set for the approvalStageTimeOutInDays property.
        """
        self._approval_stage_time_out_in_days = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedApprovalStage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of days that a request can be pending a response before it is automatically denied.
        self._approval_stage_time_out_in_days: Optional[int] = None
        # The escalation approvers for this stage when the primary approvers don't respond.
        self._escalation_approvers: Optional[List[subject_set.SubjectSet]] = None
        # The time a request can be pending a response from a primary approver before it can be escalated to the escalation approvers.
        self._escalation_time_in_minutes: Optional[int] = None
        # Indicates whether the approver must provide justification for their reponse.
        self._is_approver_justification_required: Optional[bool] = None
        # Indicates whether escalation if enabled.
        self._is_escalation_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The primary approvers of this stage.
        self._primary_approvers: Optional[List[subject_set.SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedApprovalStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedApprovalStage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedApprovalStage()
    
    @property
    def escalation_approvers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the escalationApprovers property value. The escalation approvers for this stage when the primary approvers don't respond.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._escalation_approvers
    
    @escalation_approvers.setter
    def escalation_approvers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the escalationApprovers property value. The escalation approvers for this stage when the primary approvers don't respond.
        Args:
            value: Value to set for the escalationApprovers property.
        """
        self._escalation_approvers = value
    
    @property
    def escalation_time_in_minutes(self,) -> Optional[int]:
        """
        Gets the escalationTimeInMinutes property value. The time a request can be pending a response from a primary approver before it can be escalated to the escalation approvers.
        Returns: Optional[int]
        """
        return self._escalation_time_in_minutes
    
    @escalation_time_in_minutes.setter
    def escalation_time_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the escalationTimeInMinutes property value. The time a request can be pending a response from a primary approver before it can be escalated to the escalation approvers.
        Args:
            value: Value to set for the escalationTimeInMinutes property.
        """
        self._escalation_time_in_minutes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approval_stage_time_out_in_days": lambda n : setattr(self, 'approval_stage_time_out_in_days', n.get_int_value()),
            "escalation_approvers": lambda n : setattr(self, 'escalation_approvers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "escalation_time_in_minutes": lambda n : setattr(self, 'escalation_time_in_minutes', n.get_int_value()),
            "is_approver_justification_required": lambda n : setattr(self, 'is_approver_justification_required', n.get_bool_value()),
            "is_escalation_enabled": lambda n : setattr(self, 'is_escalation_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primary_approvers": lambda n : setattr(self, 'primary_approvers', n.get_collection_of_object_values(subject_set.SubjectSet)),
        }
        return fields
    
    @property
    def is_approver_justification_required(self,) -> Optional[bool]:
        """
        Gets the isApproverJustificationRequired property value. Indicates whether the approver must provide justification for their reponse.
        Returns: Optional[bool]
        """
        return self._is_approver_justification_required
    
    @is_approver_justification_required.setter
    def is_approver_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApproverJustificationRequired property value. Indicates whether the approver must provide justification for their reponse.
        Args:
            value: Value to set for the isApproverJustificationRequired property.
        """
        self._is_approver_justification_required = value
    
    @property
    def is_escalation_enabled(self,) -> Optional[bool]:
        """
        Gets the isEscalationEnabled property value. Indicates whether escalation if enabled.
        Returns: Optional[bool]
        """
        return self._is_escalation_enabled
    
    @is_escalation_enabled.setter
    def is_escalation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEscalationEnabled property value. Indicates whether escalation if enabled.
        Args:
            value: Value to set for the isEscalationEnabled property.
        """
        self._is_escalation_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def primary_approvers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the primaryApprovers property value. The primary approvers of this stage.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._primary_approvers
    
    @primary_approvers.setter
    def primary_approvers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the primaryApprovers property value. The primary approvers of this stage.
        Args:
            value: Value to set for the primaryApprovers property.
        """
        self._primary_approvers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("approvalStageTimeOutInDays", self.approval_stage_time_out_in_days)
        writer.write_collection_of_object_values("escalationApprovers", self.escalation_approvers)
        writer.write_int_value("escalationTimeInMinutes", self.escalation_time_in_minutes)
        writer.write_bool_value("isApproverJustificationRequired", self.is_approver_justification_required)
        writer.write_bool_value("isEscalationEnabled", self.is_escalation_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("primaryApprovers", self.primary_approvers)
        writer.write_additional_data_value(self.additional_data)
    

