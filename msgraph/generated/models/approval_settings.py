from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

unified_approval_stage = lazy_import('msgraph.generated.models.unified_approval_stage')

class ApprovalSettings(AdditionalDataHolder, Parsable):
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
    def approval_mode(self,) -> Optional[str]:
        """
        Gets the approvalMode property value. One of SingleStage, Serial, Parallel, NoApproval (default). NoApproval is used when isApprovalRequired is false.
        Returns: Optional[str]
        """
        return self._approval_mode
    
    @approval_mode.setter
    def approval_mode(self,value: Optional[str] = None) -> None:
        """
        Sets the approvalMode property value. One of SingleStage, Serial, Parallel, NoApproval (default). NoApproval is used when isApprovalRequired is false.
        Args:
            value: Value to set for the approvalMode property.
        """
        self._approval_mode = value
    
    @property
    def approval_stages(self,) -> Optional[List[unified_approval_stage.UnifiedApprovalStage]]:
        """
        Gets the approvalStages property value. If approval is required, the one or two elements of this collection define each of the stages of approval. An empty array if no approval is required.
        Returns: Optional[List[unified_approval_stage.UnifiedApprovalStage]]
        """
        return self._approval_stages
    
    @approval_stages.setter
    def approval_stages(self,value: Optional[List[unified_approval_stage.UnifiedApprovalStage]] = None) -> None:
        """
        Sets the approvalStages property value. If approval is required, the one or two elements of this collection define each of the stages of approval. An empty array if no approval is required.
        Args:
            value: Value to set for the approvalStages property.
        """
        self._approval_stages = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new approvalSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # One of SingleStage, Serial, Parallel, NoApproval (default). NoApproval is used when isApprovalRequired is false.
        self._approval_mode: Optional[str] = None
        # If approval is required, the one or two elements of this collection define each of the stages of approval. An empty array if no approval is required.
        self._approval_stages: Optional[List[unified_approval_stage.UnifiedApprovalStage]] = None
        # Indicates whether approval is required for requests in this policy.
        self._is_approval_required: Optional[bool] = None
        # Indicates whether approval is required for a user to extend their assignment.
        self._is_approval_required_for_extension: Optional[bool] = None
        # Indicates whether the requestor is required to supply a justification in their request.
        self._is_requestor_justification_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApprovalSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApprovalSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approval_mode": lambda n : setattr(self, 'approval_mode', n.get_str_value()),
            "approval_stages": lambda n : setattr(self, 'approval_stages', n.get_collection_of_object_values(unified_approval_stage.UnifiedApprovalStage)),
            "is_approval_required": lambda n : setattr(self, 'is_approval_required', n.get_bool_value()),
            "is_approval_required_for_extension": lambda n : setattr(self, 'is_approval_required_for_extension', n.get_bool_value()),
            "is_requestor_justification_required": lambda n : setattr(self, 'is_requestor_justification_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_approval_required(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequired property value. Indicates whether approval is required for requests in this policy.
        Returns: Optional[bool]
        """
        return self._is_approval_required
    
    @is_approval_required.setter
    def is_approval_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequired property value. Indicates whether approval is required for requests in this policy.
        Args:
            value: Value to set for the isApprovalRequired property.
        """
        self._is_approval_required = value
    
    @property
    def is_approval_required_for_extension(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequiredForExtension property value. Indicates whether approval is required for a user to extend their assignment.
        Returns: Optional[bool]
        """
        return self._is_approval_required_for_extension
    
    @is_approval_required_for_extension.setter
    def is_approval_required_for_extension(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequiredForExtension property value. Indicates whether approval is required for a user to extend their assignment.
        Args:
            value: Value to set for the isApprovalRequiredForExtension property.
        """
        self._is_approval_required_for_extension = value
    
    @property
    def is_requestor_justification_required(self,) -> Optional[bool]:
        """
        Gets the isRequestorJustificationRequired property value. Indicates whether the requestor is required to supply a justification in their request.
        Returns: Optional[bool]
        """
        return self._is_requestor_justification_required
    
    @is_requestor_justification_required.setter
    def is_requestor_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequestorJustificationRequired property value. Indicates whether the requestor is required to supply a justification in their request.
        Args:
            value: Value to set for the isRequestorJustificationRequired property.
        """
        self._is_requestor_justification_required = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("approvalMode", self.approval_mode)
        writer.write_collection_of_object_values("approvalStages", self.approval_stages)
        writer.write_bool_value("isApprovalRequired", self.is_approval_required)
        writer.write_bool_value("isApprovalRequiredForExtension", self.is_approval_required_for_extension)
        writer.write_bool_value("isRequestorJustificationRequired", self.is_requestor_justification_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

