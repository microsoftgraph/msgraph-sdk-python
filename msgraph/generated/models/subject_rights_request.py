from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authored_note import AuthoredNote
    from .data_subject import DataSubject
    from .data_subject_type import DataSubjectType
    from .entity import Entity
    from .identity import Identity
    from .identity_set import IdentitySet
    from .subject_rights_request_detail import SubjectRightsRequestDetail
    from .subject_rights_request_history import SubjectRightsRequestHistory
    from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation
    from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation
    from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
    from .subject_rights_request_status import SubjectRightsRequestStatus
    from .subject_rights_request_type import SubjectRightsRequestType
    from .team import Team
    from .user import User

from .entity import Entity

@dataclass
class SubjectRightsRequest(Entity, Parsable):
    # Collection of users who can approve the request. Currently only supported for requests of type delete.
    approvers: Optional[list[User]] = None
    # Identity that the request is assigned to.
    assigned_to: Optional[Identity] = None
    # The date and time when the request was closed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    closed_date_time: Optional[datetime.datetime] = None
    # Collection of users who can collaborate on the request.
    collaborators: Optional[list[User]] = None
    # KQL based content query that should be used for search. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    content_query: Optional[str] = None
    # Identity information for the entity that created the request.
    created_by: Optional[IdentitySet] = None
    # The date and time when the request was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Information about the data subject.
    data_subject: Optional[DataSubject] = None
    # The type of the data subject. The possible values are: customer, currentEmployee, formerEmployee, prospectiveEmployee, student, teacher, faculty, other, unknownFutureValue.
    data_subject_type: Optional[DataSubjectType] = None
    # Description for the request.
    description: Optional[str] = None
    # The name of the request.
    display_name: Optional[str] = None
    # The external ID for the request that is immutable after creation and is used for tracking the request for the external system. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    external_id: Optional[str] = None
    # Collection of history change events.
    history: Optional[list[SubjectRightsRequestHistory]] = None
    # Include all versions of the documents. By default, the current copies of the documents are returned. If SharePoint sites have versioning enabled, including all versions includes the historical copies of the documents. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    include_all_versions: Optional[bool] = None
    # Include content authored by the data subject. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    include_authored_content: Optional[bool] = None
    # Insight about the request.
    insight: Optional[SubjectRightsRequestDetail] = None
    # The date and time when the request is internally due. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    internal_due_date_time: Optional[datetime.datetime] = None
    # Identity information for the entity that last modified the request.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the request was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The mailbox locations that should be searched. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    mailbox_locations: Optional[SubjectRightsRequestMailboxLocation] = None
    # List of notes associated with the request.
    notes: Optional[list[AuthoredNote]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Pause the request after estimate has finished. By default, the data estimate runs and then pauses, allowing you to preview results and then select the option to retrieve data in the UI. You can set this property to false if you want it to perform the estimate and then automatically begin with the retrieval of the content. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    pause_after_estimate: Optional[bool] = None
    # List of regulations that this request fulfill.
    regulations: Optional[list[str]] = None
    # The SharePoint and OneDrive site locations that should be searched. This property is defined only for APIs accessed using the /security query path and not the /privacy query path.
    site_locations: Optional[SubjectRightsRequestSiteLocation] = None
    # Information about the different stages for the request.
    stages: Optional[list[SubjectRightsRequestStageDetail]] = None
    # The status of the request. The possible values are: active, closed, unknownFutureValue.
    status: Optional[SubjectRightsRequestStatus] = None
    # Information about the Microsoft Teams team that was created for the request.
    team: Optional[Team] = None
    # The type of the request. The possible values are: export, delete, access, tagForAction, unknownFutureValue.
    type: Optional[SubjectRightsRequestType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectRightsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authored_note import AuthoredNote
        from .data_subject import DataSubject
        from .data_subject_type import DataSubjectType
        from .entity import Entity
        from .identity import Identity
        from .identity_set import IdentitySet
        from .subject_rights_request_detail import SubjectRightsRequestDetail
        from .subject_rights_request_history import SubjectRightsRequestHistory
        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation
        from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation
        from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
        from .subject_rights_request_status import SubjectRightsRequestStatus
        from .subject_rights_request_type import SubjectRightsRequestType
        from .team import Team
        from .user import User

        from .authored_note import AuthoredNote
        from .data_subject import DataSubject
        from .data_subject_type import DataSubjectType
        from .entity import Entity
        from .identity import Identity
        from .identity_set import IdentitySet
        from .subject_rights_request_detail import SubjectRightsRequestDetail
        from .subject_rights_request_history import SubjectRightsRequestHistory
        from .subject_rights_request_mailbox_location import SubjectRightsRequestMailboxLocation
        from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation
        from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
        from .subject_rights_request_status import SubjectRightsRequestStatus
        from .subject_rights_request_type import SubjectRightsRequestType
        from .team import Team
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "approvers": lambda n : setattr(self, 'approvers', n.get_collection_of_object_values(User)),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_object_value(Identity)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "collaborators": lambda n : setattr(self, 'collaborators', n.get_collection_of_object_values(User)),
            "contentQuery": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dataSubject": lambda n : setattr(self, 'data_subject', n.get_object_value(DataSubject)),
            "dataSubjectType": lambda n : setattr(self, 'data_subject_type', n.get_enum_value(DataSubjectType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(SubjectRightsRequestHistory)),
            "includeAllVersions": lambda n : setattr(self, 'include_all_versions', n.get_bool_value()),
            "includeAuthoredContent": lambda n : setattr(self, 'include_authored_content', n.get_bool_value()),
            "insight": lambda n : setattr(self, 'insight', n.get_object_value(SubjectRightsRequestDetail)),
            "internalDueDateTime": lambda n : setattr(self, 'internal_due_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "mailboxLocations": lambda n : setattr(self, 'mailbox_locations', n.get_object_value(SubjectRightsRequestMailboxLocation)),
            "notes": lambda n : setattr(self, 'notes', n.get_collection_of_object_values(AuthoredNote)),
            "pauseAfterEstimate": lambda n : setattr(self, 'pause_after_estimate', n.get_bool_value()),
            "regulations": lambda n : setattr(self, 'regulations', n.get_collection_of_primitive_values(str)),
            "siteLocations": lambda n : setattr(self, 'site_locations', n.get_object_value(SubjectRightsRequestSiteLocation)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("approvers", self.approvers)
        writer.write_object_value("assignedTo", self.assigned_to)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_collection_of_object_values("collaborators", self.collaborators)
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("dataSubject", self.data_subject)
        writer.write_enum_value("dataSubjectType", self.data_subject_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("includeAllVersions", self.include_all_versions)
        writer.write_bool_value("includeAuthoredContent", self.include_authored_content)
        writer.write_object_value("insight", self.insight)
        writer.write_datetime_value("internalDueDateTime", self.internal_due_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("mailboxLocations", self.mailbox_locations)
        writer.write_collection_of_object_values("notes", self.notes)
        writer.write_bool_value("pauseAfterEstimate", self.pause_after_estimate)
        writer.write_collection_of_primitive_values("regulations", self.regulations)
        writer.write_object_value("siteLocations", self.site_locations)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("team", self.team)
        writer.write_enum_value("type", self.type)
    

