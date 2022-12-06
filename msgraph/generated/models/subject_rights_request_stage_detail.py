from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

public_error = lazy_import('msgraph.generated.models.public_error')
subject_rights_request_stage = lazy_import('msgraph.generated.models.subject_rights_request_stage')
subject_rights_request_stage_status = lazy_import('msgraph.generated.models.subject_rights_request_stage_status')

class SubjectRightsRequestStageDetail(AdditionalDataHolder, Parsable):
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
        Instantiates a new subjectRightsRequestStageDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Describes the error, if any, for the current stage.
        self._error: Optional[public_error.PublicError] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The stage of the subject rights request. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
        self._stage: Optional[subject_rights_request_stage.SubjectRightsRequestStage] = None
        # Status of the current stage. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
        self._status: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestStageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestStageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequestStageDetail()
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. Describes the error, if any, for the current stage.
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. Describes the error, if any, for the current stage.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(subject_rights_request_stage.SubjectRightsRequestStage)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(subject_rights_request_stage_status.SubjectRightsRequestStageStatus)),
        }
        return fields
    
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
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("stage", self.stage)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def stage(self,) -> Optional[subject_rights_request_stage.SubjectRightsRequestStage]:
        """
        Gets the stage property value. The stage of the subject rights request. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
        Returns: Optional[subject_rights_request_stage.SubjectRightsRequestStage]
        """
        return self._stage
    
    @stage.setter
    def stage(self,value: Optional[subject_rights_request_stage.SubjectRightsRequestStage] = None) -> None:
        """
        Sets the stage property value. The stage of the subject rights request. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
        Args:
            value: Value to set for the stage property.
        """
        self._stage = value
    
    @property
    def status(self,) -> Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus]:
        """
        Gets the status property value. Status of the current stage. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
        Returns: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus] = None) -> None:
        """
        Sets the status property value. Status of the current stage. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

