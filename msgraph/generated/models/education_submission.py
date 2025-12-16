from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_outcome import EducationOutcome
    from .education_submission_recipient import EducationSubmissionRecipient
    from .education_submission_resource import EducationSubmissionResource
    from .education_submission_status import EducationSubmissionStatus
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class EducationSubmission(Entity, Parsable):
    # The unique identifier for the assignment with which this submission is associated. A submission is always associated with one and only one assignment.
    assignment_id: Optional[str] = None
    # The user that marked the submission as excused.
    excused_by: Optional[IdentitySet] = None
    # The time that the submission was excused. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    excused_date_time: Optional[datetime.datetime] = None
    # The identities of those who modified the submission.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time the submission was modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outcomes property
    outcomes: Optional[list[EducationOutcome]] = None
    # User who moved the status of this submission to reassigned.
    reassigned_by: Optional[IdentitySet] = None
    # Moment in time when the submission was reassigned. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    reassigned_date_time: Optional[datetime.datetime] = None
    # Who this submission is assigned to.
    recipient: Optional[EducationSubmissionRecipient] = None
    # The resources property
    resources: Optional[list[EducationSubmissionResource]] = None
    # Folder where all file resources for this submission need to be stored.
    resources_folder_url: Optional[str] = None
    # User who moved the status of this submission to returned.
    returned_by: Optional[IdentitySet] = None
    # Moment in time when the submission was returned. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    returned_date_time: Optional[datetime.datetime] = None
    # Read-only. The possible values are: excused, reassigned, returned, submitted and working. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: excused and reassigned.
    status: Optional[EducationSubmissionStatus] = None
    # User who moved the resource into the submitted state.
    submitted_by: Optional[IdentitySet] = None
    # Moment in time when the submission was moved into the submitted state. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    submitted_date_time: Optional[datetime.datetime] = None
    # The submittedResources property
    submitted_resources: Optional[list[EducationSubmissionResource]] = None
    # User who moved the resource from submitted into the working state.
    unsubmitted_by: Optional[IdentitySet] = None
    # Moment in time when the submission was moved from submitted into the working state. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    unsubmitted_date_time: Optional[datetime.datetime] = None
    # The deep link URL for the given submission.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_outcome import EducationOutcome
        from .education_submission_recipient import EducationSubmissionRecipient
        from .education_submission_resource import EducationSubmissionResource
        from .education_submission_status import EducationSubmissionStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        from .education_outcome import EducationOutcome
        from .education_submission_recipient import EducationSubmissionRecipient
        from .education_submission_resource import EducationSubmissionResource
        from .education_submission_status import EducationSubmissionStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentId": lambda n : setattr(self, 'assignment_id', n.get_str_value()),
            "excusedBy": lambda n : setattr(self, 'excused_by', n.get_object_value(IdentitySet)),
            "excusedDateTime": lambda n : setattr(self, 'excused_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "outcomes": lambda n : setattr(self, 'outcomes', n.get_collection_of_object_values(EducationOutcome)),
            "reassignedBy": lambda n : setattr(self, 'reassigned_by', n.get_object_value(IdentitySet)),
            "reassignedDateTime": lambda n : setattr(self, 'reassigned_date_time', n.get_datetime_value()),
            "recipient": lambda n : setattr(self, 'recipient', n.get_object_value(EducationSubmissionRecipient)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(EducationSubmissionResource)),
            "resourcesFolderUrl": lambda n : setattr(self, 'resources_folder_url', n.get_str_value()),
            "returnedBy": lambda n : setattr(self, 'returned_by', n.get_object_value(IdentitySet)),
            "returnedDateTime": lambda n : setattr(self, 'returned_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(EducationSubmissionStatus)),
            "submittedBy": lambda n : setattr(self, 'submitted_by', n.get_object_value(IdentitySet)),
            "submittedDateTime": lambda n : setattr(self, 'submitted_date_time', n.get_datetime_value()),
            "submittedResources": lambda n : setattr(self, 'submitted_resources', n.get_collection_of_object_values(EducationSubmissionResource)),
            "unsubmittedBy": lambda n : setattr(self, 'unsubmitted_by', n.get_object_value(IdentitySet)),
            "unsubmittedDateTime": lambda n : setattr(self, 'unsubmitted_date_time', n.get_datetime_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("outcomes", self.outcomes)
        writer.write_object_value("recipient", self.recipient)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("submittedResources", self.submitted_resources)
    

