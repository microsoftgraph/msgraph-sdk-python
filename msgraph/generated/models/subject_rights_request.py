from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authored_note import AuthoredNote
    from .data_subject import DataSubject
    from .data_subject_type import DataSubjectType
    from .entity import Entity
    from .identity import Identity
    from .identity_set import IdentitySet
    from .subject_rights_request_detail import SubjectRightsRequestDetail
    from .subject_rights_request_history import SubjectRightsRequestHistory
    from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
    from .subject_rights_request_status import SubjectRightsRequestStatus
    from .subject_rights_request_type import SubjectRightsRequestType
    from .team import Team

from .entity import Entity

@dataclass
class SubjectRightsRequest(Entity):
    # Identity that the request is assigned to.
    assigned_to: Optional[Identity] = None
    # The date and time when the request was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    closed_date_time: Optional[datetime.datetime] = None
    # Identity information for the entity that created the request.
    created_by: Optional[IdentitySet] = None
    # The date and time when the request was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Information about the data subject.
    data_subject: Optional[DataSubject] = None
    # The type of the data subject. Possible values are: customer, currentEmployee, formerEmployee, prospectiveEmployee, student, teacher, faculty, other, unknownFutureValue.
    data_subject_type: Optional[DataSubjectType] = None
    # Description for the request.
    description: Optional[str] = None
    # The name of the request.
    display_name: Optional[str] = None
    # Collection of history change events.
    history: Optional[List[SubjectRightsRequestHistory]] = None
    # Insight about the request.
    insight: Optional[SubjectRightsRequestDetail] = None
    # The date and time when the request is internally due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    internal_due_date_time: Optional[datetime.datetime] = None
    # Identity information for the entity that last modified the request.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the request was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # List of notes associcated with the request.
    notes: Optional[List[AuthoredNote]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of regulations that this request will fulfill.
    regulations: Optional[List[str]] = None
    # Information about the different stages for the request.
    stages: Optional[List[SubjectRightsRequestStageDetail]] = None
    # The status of the request.. Possible values are: active, closed, unknownFutureValue.
    status: Optional[SubjectRightsRequestStatus] = None
    # Information about the Microsoft Teams team that was created for the request.
    team: Optional[Team] = None
    # The type of the request. Possible values are: export, delete,  access, tagForAction, unknownFutureValue.
    type: Optional[SubjectRightsRequestType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authored_note import AuthoredNote
        from .data_subject import DataSubject
        from .data_subject_type import DataSubjectType
        from .entity import Entity
        from .identity import Identity
        from .identity_set import IdentitySet
        from .subject_rights_request_detail import SubjectRightsRequestDetail
        from .subject_rights_request_history import SubjectRightsRequestHistory
        from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
        from .subject_rights_request_status import SubjectRightsRequestStatus
        from .subject_rights_request_type import SubjectRightsRequestType
        from .team import Team

        from .authored_note import AuthoredNote
        from .data_subject import DataSubject
        from .data_subject_type import DataSubjectType
        from .entity import Entity
        from .identity import Identity
        from .identity_set import IdentitySet
        from .subject_rights_request_detail import SubjectRightsRequestDetail
        from .subject_rights_request_history import SubjectRightsRequestHistory
        from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
        from .subject_rights_request_status import SubjectRightsRequestStatus
        from .subject_rights_request_type import SubjectRightsRequestType
        from .team import Team

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(Identity)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dataSubject": lambda n : setattr(self, 'data_subject', n.get_object_value(DataSubject)),
            "dataSubjectType": lambda n : setattr(self, 'data_subject_type', n.get_enum_value(DataSubjectType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(SubjectRightsRequestHistory)),
            "insight": lambda n : setattr(self, 'insight', n.get_object_value(SubjectRightsRequestDetail)),
            "internalDueDateTime": lambda n : setattr(self, 'internal_due_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_object_values(AuthoredNote)),
            "regulations": lambda n : setattr(self, 'regulations', n.get_collection_of_primitive_values(str)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(SubjectRightsRequestStageDetail)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SubjectRightsRequestStatus)),
            "team": lambda n : setattr(self, 'team', n.get_object_value(Team)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(SubjectRightsRequestType)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_datetime_value()("closedDateTime", self.closed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value()("createdDateTime", self.created_date_time)
        writer.write_object_value("dataSubject", self.data_subject)
        writer.write_enum_value("dataSubjectType", self.data_subject_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_object_value("insight", self.insight)
        writer.write_datetime_value()("internalDueDateTime", self.internal_due_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value()("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("notes", self.notes)
        writer.write_collection_of_primitive_values("regulations", self.regulations)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("team", self.team)
        writer.write_enum_value("type", self.type)
    

