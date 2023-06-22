from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, subject_rights_request_stage, subject_rights_request_stage_status

@dataclass
class SubjectRightsRequestHistory(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Identity of the user who changed the  subject rights request.
    changed_by: Optional[identity_set.IdentitySet] = None
    # Data and time when the entity was changed.
    event_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The stage when the entity was changed. Possible values are: contentRetrieval, contentReview, generateReport, contentDeletion, caseResolved, unknownFutureValue.
    stage: Optional[subject_rights_request_stage.SubjectRightsRequestStage] = None
    # The status of the stage when the entity was changed. Possible values are: notStarted, current, completed, failed, unknownFutureValue.
    stage_status: Optional[subject_rights_request_stage_status.SubjectRightsRequestStageStatus] = None
    # Type of history.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestHistory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, subject_rights_request_stage, subject_rights_request_stage_status

        from . import identity_set, subject_rights_request_stage, subject_rights_request_stage_status

        fields: Dict[str, Callable[[Any], None]] = {
            "changedBy": lambda n : setattr(self, 'changed_by', n.get_object_value(identity_set.IdentitySet)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(subject_rights_request_stage.SubjectRightsRequestStage)),
            "stageStatus": lambda n : setattr(self, 'stage_status', n.get_enum_value(subject_rights_request_stage_status.SubjectRightsRequestStageStatus)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("changedBy", self.changed_by)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("stage", self.stage)
        writer.write_enum_value("stageStatus", self.stage_status)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

