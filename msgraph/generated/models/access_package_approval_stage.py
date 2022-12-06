from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class AccessPackageApprovalStage(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageApprovalStage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of days that a request can be pending a response before it is automatically denied.
        self._duration_before_automatic_denial: Optional[Timedelta] = None
        # If escalation is required, the time a request can be pending a response from a primary approver.
        self._duration_before_escalation: Optional[Timedelta] = None
        # If escalation is enabled and the primary approvers do not respond before the escalation time, the escalationApprovers are the users who will be asked to approve requests.
        self._escalation_approvers: Optional[List[subject_set.SubjectSet]] = None
        # The subjects, typically users, who are the fallback escalation approvers.
        self._fallback_escalation_approvers: Optional[List[subject_set.SubjectSet]] = None
        # The subjects, typically users, who are the fallback primary approvers.
        self._fallback_primary_approvers: Optional[List[subject_set.SubjectSet]] = None
        # Indicates whether the approver is required to provide a justification for approving a request.
        self._is_approver_justification_required: Optional[bool] = None
        # If true, then one or more escalationApprovers are configured in this approval stage.
        self._is_escalation_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The subjects, typically users, who will be asked to approve requests. A collection of singleUser, groupMembers, requestorManager, internalSponsors or externalSponsors.
        self._primary_approvers: Optional[List[subject_set.SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageApprovalStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageApprovalStage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageApprovalStage()
    
    @property
    def duration_before_automatic_denial(self,) -> Optional[Timedelta]:
        """
        Gets the durationBeforeAutomaticDenial property value. The number of days that a request can be pending a response before it is automatically denied.
        Returns: Optional[Timedelta]
        """
        return self._duration_before_automatic_denial
    
    @duration_before_automatic_denial.setter
    def duration_before_automatic_denial(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the durationBeforeAutomaticDenial property value. The number of days that a request can be pending a response before it is automatically denied.
        Args:
            value: Value to set for the durationBeforeAutomaticDenial property.
        """
        self._duration_before_automatic_denial = value
    
    @property
    def duration_before_escalation(self,) -> Optional[Timedelta]:
        """
        Gets the durationBeforeEscalation property value. If escalation is required, the time a request can be pending a response from a primary approver.
        Returns: Optional[Timedelta]
        """
        return self._duration_before_escalation
    
    @duration_before_escalation.setter
    def duration_before_escalation(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the durationBeforeEscalation property value. If escalation is required, the time a request can be pending a response from a primary approver.
        Args:
            value: Value to set for the durationBeforeEscalation property.
        """
        self._duration_before_escalation = value
    
    @property
    def escalation_approvers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the escalationApprovers property value. If escalation is enabled and the primary approvers do not respond before the escalation time, the escalationApprovers are the users who will be asked to approve requests.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._escalation_approvers
    
    @escalation_approvers.setter
    def escalation_approvers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the escalationApprovers property value. If escalation is enabled and the primary approvers do not respond before the escalation time, the escalationApprovers are the users who will be asked to approve requests.
        Args:
            value: Value to set for the escalationApprovers property.
        """
        self._escalation_approvers = value
    
    @property
    def fallback_escalation_approvers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the fallbackEscalationApprovers property value. The subjects, typically users, who are the fallback escalation approvers.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._fallback_escalation_approvers
    
    @fallback_escalation_approvers.setter
    def fallback_escalation_approvers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the fallbackEscalationApprovers property value. The subjects, typically users, who are the fallback escalation approvers.
        Args:
            value: Value to set for the fallbackEscalationApprovers property.
        """
        self._fallback_escalation_approvers = value
    
    @property
    def fallback_primary_approvers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the fallbackPrimaryApprovers property value. The subjects, typically users, who are the fallback primary approvers.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._fallback_primary_approvers
    
    @fallback_primary_approvers.setter
    def fallback_primary_approvers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the fallbackPrimaryApprovers property value. The subjects, typically users, who are the fallback primary approvers.
        Args:
            value: Value to set for the fallbackPrimaryApprovers property.
        """
        self._fallback_primary_approvers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "duration_before_automatic_denial": lambda n : setattr(self, 'duration_before_automatic_denial', n.get_object_value(Timedelta)),
            "duration_before_escalation": lambda n : setattr(self, 'duration_before_escalation', n.get_object_value(Timedelta)),
            "escalation_approvers": lambda n : setattr(self, 'escalation_approvers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "fallback_escalation_approvers": lambda n : setattr(self, 'fallback_escalation_approvers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "fallback_primary_approvers": lambda n : setattr(self, 'fallback_primary_approvers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "is_approver_justification_required": lambda n : setattr(self, 'is_approver_justification_required', n.get_bool_value()),
            "is_escalation_enabled": lambda n : setattr(self, 'is_escalation_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primary_approvers": lambda n : setattr(self, 'primary_approvers', n.get_collection_of_object_values(subject_set.SubjectSet)),
        }
        return fields
    
    @property
    def is_approver_justification_required(self,) -> Optional[bool]:
        """
        Gets the isApproverJustificationRequired property value. Indicates whether the approver is required to provide a justification for approving a request.
        Returns: Optional[bool]
        """
        return self._is_approver_justification_required
    
    @is_approver_justification_required.setter
    def is_approver_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApproverJustificationRequired property value. Indicates whether the approver is required to provide a justification for approving a request.
        Args:
            value: Value to set for the isApproverJustificationRequired property.
        """
        self._is_approver_justification_required = value
    
    @property
    def is_escalation_enabled(self,) -> Optional[bool]:
        """
        Gets the isEscalationEnabled property value. If true, then one or more escalationApprovers are configured in this approval stage.
        Returns: Optional[bool]
        """
        return self._is_escalation_enabled
    
    @is_escalation_enabled.setter
    def is_escalation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEscalationEnabled property value. If true, then one or more escalationApprovers are configured in this approval stage.
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
        Gets the primaryApprovers property value. The subjects, typically users, who will be asked to approve requests. A collection of singleUser, groupMembers, requestorManager, internalSponsors or externalSponsors.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._primary_approvers
    
    @primary_approvers.setter
    def primary_approvers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the primaryApprovers property value. The subjects, typically users, who will be asked to approve requests. A collection of singleUser, groupMembers, requestorManager, internalSponsors or externalSponsors.
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
        writer.write_object_value("durationBeforeAutomaticDenial", self.duration_before_automatic_denial)
        writer.write_object_value("durationBeforeEscalation", self.duration_before_escalation)
        writer.write_collection_of_object_values("escalationApprovers", self.escalation_approvers)
        writer.write_collection_of_object_values("fallbackEscalationApprovers", self.fallback_escalation_approvers)
        writer.write_collection_of_object_values("fallbackPrimaryApprovers", self.fallback_primary_approvers)
        writer.write_bool_value("isApproverJustificationRequired", self.is_approver_justification_required)
        writer.write_bool_value("isEscalationEnabled", self.is_escalation_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("primaryApprovers", self.primary_approvers)
        writer.write_additional_data_value(self.additional_data)
    

