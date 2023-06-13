from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authored_note, data_subject, data_subject_type, entity, identity, identity_set, subject_rights_request_detail, subject_rights_request_history, subject_rights_request_stage_detail, subject_rights_request_status, subject_rights_request_type, team

from . import entity

@dataclass
class SubjectRightsRequest(entity.Entity):
    # Identity that the request is assigned to.
    assigned_to: Optional[identity.Identity] = None
    # The date and time when the request was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    closed_date_time: Optional[datetime] = None
    # Identity information for the entity that created the request.
    created_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the request was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # Information about the data subject.
    data_subject: Optional[data_subject.DataSubject] = None
    # The type of the data subject. Possible values are: customer, currentEmployee, formerEmployee, prospectiveEmployee, student, teacher, faculty, other, unknownFutureValue.
    data_subject_type: Optional[data_subject_type.DataSubjectType] = None
    # Description for the request.
    description: Optional[str] = None
    # The name of the request.
    display_name: Optional[str] = None
    # Collection of history change events.
    history: Optional[List[subject_rights_request_history.SubjectRightsRequestHistory]] = None
    # Insight about the request.
    insight: Optional[subject_rights_request_detail.SubjectRightsRequestDetail] = None
    # The date and time when the request is internally due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    internal_due_date_time: Optional[datetime] = None
    # Identity information for the entity that last modified the request.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the request was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime] = None
    # List of notes associcated with the request.
    notes: Optional[List[authored_note.AuthoredNote]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of regulations that this request will fulfill.
    regulations: Optional[List[str]] = None
    # Information about the different stages for the request.
    stages: Optional[List[subject_rights_request_stage_detail.SubjectRightsRequestStageDetail]] = None
    # The status of the request.. Possible values are: active, closed, unknownFutureValue.
    status: Optional[subject_rights_request_status.SubjectRightsRequestStatus] = None
    # Information about the Microsoft Teams team that was created for the request.
    team: Optional[team.Team] = None
    # The type of the request. Possible values are: export, delete,  access, tagForAction, unknownFutureValue.
    type: Optional[subject_rights_request_type.SubjectRightsRequestType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authored_note, data_subject, data_subject_type, entity, identity, identity_set, subject_rights_request_detail, subject_rights_request_history, subject_rights_request_stage_detail, subject_rights_request_status, subject_rights_request_type, team

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(identity.Identity)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dataSubject": lambda n : setattr(self, 'data_subject', n.get_object_value(data_subject.DataSubject)),
            "dataSubjectType": lambda n : setattr(self, 'data_subject_type', n.get_enum_value(data_subject_type.DataSubjectType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(subject_rights_request_history.SubjectRightsRequestHistory)),
            "insight": lambda n : setattr(self, 'insight', n.get_object_value(subject_rights_request_detail.SubjectRightsRequestDetail)),
            "internalDueDateTime": lambda n : setattr(self, 'internal_due_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_object_values(authored_note.AuthoredNote)),
            "regulations": lambda n : setattr(self, 'regulations', n.get_collection_of_primitive_values(str)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(subject_rights_request_stage_detail.SubjectRightsRequestStageDetail)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(subject_rights_request_status.SubjectRightsRequestStatus)),
            "team": lambda n : setattr(self, 'team', n.get_object_value(team.Team)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(subject_rights_request_type.SubjectRightsRequestType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("dataSubject", self.data_subject)
        writer.write_enum_value("dataSubjectType", self.data_subject_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_object_value("insight", self.insight)
        writer.write_datetime_value("internalDueDateTime", self.internal_due_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("notes", self.notes)
        writer.write_collection_of_primitive_values("regulations", self.regulations)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("team", self.team)
        writer.write_enum_value("type", self.type)
    

