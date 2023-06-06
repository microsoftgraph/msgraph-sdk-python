from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_outcome, education_submission_recipient, education_submission_resource, education_submission_status, entity, identity_set

from . import entity

@dataclass
class EducationSubmission(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The outcomes property
    outcomes: Optional[List[education_outcome.EducationOutcome]] = None
    # User who moved the status of this submission to reassigned.
    reassigned_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the submission was reassigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    reassigned_date_time: Optional[datetime] = None
    # Who this submission is assigned to.
    recipient: Optional[education_submission_recipient.EducationSubmissionRecipient] = None
    # The resources property
    resources: Optional[List[education_submission_resource.EducationSubmissionResource]] = None
    # Folder where all file resources for this submission need to be stored.
    resources_folder_url: Optional[str] = None
    # User who moved the status of this submission to returned.
    returned_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the submission was returned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    returned_date_time: Optional[datetime] = None
    # Read-only. Possible values are: working, submitted, returned, and reassigned. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: reassigned.
    status: Optional[education_submission_status.EducationSubmissionStatus] = None
    # User who moved the resource into the submitted state.
    submitted_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the submission was moved into the submitted state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    submitted_date_time: Optional[datetime] = None
    # The submittedResources property
    submitted_resources: Optional[List[education_submission_resource.EducationSubmissionResource]] = None
    # User who moved the resource from submitted into the working state.
    unsubmitted_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the submission was moved from submitted into the working state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    unsubmitted_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSubmission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_outcome, education_submission_recipient, education_submission_resource, education_submission_status, entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "outcomes": lambda n : setattr(self, 'outcomes', n.get_collection_of_object_values(education_outcome.EducationOutcome)),
            "reassignedBy": lambda n : setattr(self, 'reassigned_by', n.get_object_value(identity_set.IdentitySet)),
            "reassignedDateTime": lambda n : setattr(self, 'reassigned_date_time', n.get_datetime_value()),
            "recipient": lambda n : setattr(self, 'recipient', n.get_object_value(education_submission_recipient.EducationSubmissionRecipient)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(education_submission_resource.EducationSubmissionResource)),
            "resourcesFolderUrl": lambda n : setattr(self, 'resources_folder_url', n.get_str_value()),
            "returnedBy": lambda n : setattr(self, 'returned_by', n.get_object_value(identity_set.IdentitySet)),
            "returnedDateTime": lambda n : setattr(self, 'returned_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(education_submission_status.EducationSubmissionStatus)),
            "submittedBy": lambda n : setattr(self, 'submitted_by', n.get_object_value(identity_set.IdentitySet)),
            "submittedDateTime": lambda n : setattr(self, 'submitted_date_time', n.get_datetime_value()),
            "submittedResources": lambda n : setattr(self, 'submitted_resources', n.get_collection_of_object_values(education_submission_resource.EducationSubmissionResource)),
            "unsubmittedBy": lambda n : setattr(self, 'unsubmitted_by', n.get_object_value(identity_set.IdentitySet)),
            "unsubmittedDateTime": lambda n : setattr(self, 'unsubmitted_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("outcomes", self.outcomes)
        writer.write_object_value("recipient", self.recipient)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("submittedResources", self.submitted_resources)
    

