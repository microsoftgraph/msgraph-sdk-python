from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')
subject_rights_request_stage = lazy_import('msgraph.generated.models.subject_rights_request_stage')
subject_rights_request_stage_status = lazy_import('msgraph.generated.models.subject_rights_request_stage_status')

class SubjectRightsRequestHistory(AdditionalDataHolder, Parsable):
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
    def changed_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the changedBy property value. Identity of the user who changed the  subject rights request.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._changed_by
    
    @changed_by.setter
    def changed_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the changedBy property value. Identity of the user who changed the  subject rights request.
        Args:
            value: Value to set for the changedBy property.
        """
        self._changed_by = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new subjectRightsRequestHistory and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identity of the user who changed the  subject rights request.
        self._changed_by: Optional[identity_set.IdentitySet] = None
        # Data and time when the entity was changed.
        self._event_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The stage when the entity was changed. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
        self._stage: Optional[subject_rights_request_stage.SubjectRightsRequestStage] = None
        # The status of the stage when the entity was changed. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
        self._stage_status: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus] = None
        # Type of history.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequestHistory()
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. Data and time when the entity was changed.
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. Data and time when the entity was changed.
        Args:
            value: Value to set for the eventDateTime property.
        """
        self._event_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "changed_by": lambda n : setattr(self, 'changed_by', n.get_object_value(identity_set.IdentitySet)),
            "event_date_time": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(subject_rights_request_stage.SubjectRightsRequestStage)),
            "stage_status": lambda n : setattr(self, 'stage_status', n.get_enum_value(subject_rights_request_stage_status.SubjectRightsRequestStageStatus)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("changedBy", self.changed_by)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("stage", self.stage)
        writer.write_enum_value("stageStatus", self.stage_status)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def stage(self,) -> Optional[subject_rights_request_stage.SubjectRightsRequestStage]:
        """
        Gets the stage property value. The stage when the entity was changed. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
        Returns: Optional[subject_rights_request_stage.SubjectRightsRequestStage]
        """
        return self._stage
    
    @stage.setter
    def stage(self,value: Optional[subject_rights_request_stage.SubjectRightsRequestStage] = None) -> None:
        """
        Sets the stage property value. The stage when the entity was changed. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
        Args:
            value: Value to set for the stage property.
        """
        self._stage = value
    
    @property
    def stage_status(self,) -> Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus]:
        """
        Gets the stageStatus property value. The status of the stage when the entity was changed. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
        Returns: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus]
        """
        return self._stage_status
    
    @stage_status.setter
    def stage_status(self,value: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus] = None) -> None:
        """
        Sets the stageStatus property value. The status of the stage when the entity was changed. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
        Args:
            value: Value to set for the stageStatus property.
        """
        self._stage_status = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Type of history.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Type of history.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

