from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_outcome = lazy_import('msgraph.generated.models.education_outcome')
education_submission_recipient = lazy_import('msgraph.generated.models.education_submission_recipient')
education_submission_resource = lazy_import('msgraph.generated.models.education_submission_resource')
education_submission_status = lazy_import('msgraph.generated.models.education_submission_status')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class EducationSubmission(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new educationSubmission and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The outcomes property
        self._outcomes: Optional[List[education_outcome.EducationOutcome]] = None
        # User who moved the status of this submission to reassigned.
        self._reassigned_by: Optional[identity_set.IdentitySet] = None
        # Moment in time when the submission was reassigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._reassigned_date_time: Optional[datetime] = None
        # Who this submission is assigned to.
        self._recipient: Optional[education_submission_recipient.EducationSubmissionRecipient] = None
        # The resources property
        self._resources: Optional[List[education_submission_resource.EducationSubmissionResource]] = None
        # Folder where all file resources for this submission need to be stored.
        self._resources_folder_url: Optional[str] = None
        # User who moved the status of this submission to returned.
        self._returned_by: Optional[identity_set.IdentitySet] = None
        # Moment in time when the submission was returned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._returned_date_time: Optional[datetime] = None
        # Read-only. Possible values are: working, submitted, released, returned, and reassigned. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: reassigned.
        self._status: Optional[education_submission_status.EducationSubmissionStatus] = None
        # User who moved the resource into the submitted state.
        self._submitted_by: Optional[identity_set.IdentitySet] = None
        # Moment in time when the submission was moved into the submitted state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._submitted_date_time: Optional[datetime] = None
        # The submittedResources property
        self._submitted_resources: Optional[List[education_submission_resource.EducationSubmissionResource]] = None
        # User who moved the resource from submitted into the working state.
        self._unsubmitted_by: Optional[identity_set.IdentitySet] = None
        # Moment in time when the submission was moved from submitted into the working state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._unsubmitted_date_time: Optional[datetime] = None
    
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
        fields = {
            "outcomes": lambda n : setattr(self, 'outcomes', n.get_collection_of_object_values(education_outcome.EducationOutcome)),
            "reassigned_by": lambda n : setattr(self, 'reassigned_by', n.get_object_value(identity_set.IdentitySet)),
            "reassigned_date_time": lambda n : setattr(self, 'reassigned_date_time', n.get_datetime_value()),
            "recipient": lambda n : setattr(self, 'recipient', n.get_object_value(education_submission_recipient.EducationSubmissionRecipient)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(education_submission_resource.EducationSubmissionResource)),
            "resources_folder_url": lambda n : setattr(self, 'resources_folder_url', n.get_str_value()),
            "returned_by": lambda n : setattr(self, 'returned_by', n.get_object_value(identity_set.IdentitySet)),
            "returned_date_time": lambda n : setattr(self, 'returned_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(education_submission_status.EducationSubmissionStatus)),
            "submitted_by": lambda n : setattr(self, 'submitted_by', n.get_object_value(identity_set.IdentitySet)),
            "submitted_date_time": lambda n : setattr(self, 'submitted_date_time', n.get_datetime_value()),
            "submitted_resources": lambda n : setattr(self, 'submitted_resources', n.get_collection_of_object_values(education_submission_resource.EducationSubmissionResource)),
            "unsubmitted_by": lambda n : setattr(self, 'unsubmitted_by', n.get_object_value(identity_set.IdentitySet)),
            "unsubmitted_date_time": lambda n : setattr(self, 'unsubmitted_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def outcomes(self,) -> Optional[List[education_outcome.EducationOutcome]]:
        """
        Gets the outcomes property value. The outcomes property
        Returns: Optional[List[education_outcome.EducationOutcome]]
        """
        return self._outcomes
    
    @outcomes.setter
    def outcomes(self,value: Optional[List[education_outcome.EducationOutcome]] = None) -> None:
        """
        Sets the outcomes property value. The outcomes property
        Args:
            value: Value to set for the outcomes property.
        """
        self._outcomes = value
    
    @property
    def reassigned_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the reassignedBy property value. User who moved the status of this submission to reassigned.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._reassigned_by
    
    @reassigned_by.setter
    def reassigned_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the reassignedBy property value. User who moved the status of this submission to reassigned.
        Args:
            value: Value to set for the reassignedBy property.
        """
        self._reassigned_by = value
    
    @property
    def reassigned_date_time(self,) -> Optional[datetime]:
        """
        Gets the reassignedDateTime property value. Moment in time when the submission was reassigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._reassigned_date_time
    
    @reassigned_date_time.setter
    def reassigned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reassignedDateTime property value. Moment in time when the submission was reassigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the reassignedDateTime property.
        """
        self._reassigned_date_time = value
    
    @property
    def recipient(self,) -> Optional[education_submission_recipient.EducationSubmissionRecipient]:
        """
        Gets the recipient property value. Who this submission is assigned to.
        Returns: Optional[education_submission_recipient.EducationSubmissionRecipient]
        """
        return self._recipient
    
    @recipient.setter
    def recipient(self,value: Optional[education_submission_recipient.EducationSubmissionRecipient] = None) -> None:
        """
        Sets the recipient property value. Who this submission is assigned to.
        Args:
            value: Value to set for the recipient property.
        """
        self._recipient = value
    
    @property
    def resources(self,) -> Optional[List[education_submission_resource.EducationSubmissionResource]]:
        """
        Gets the resources property value. The resources property
        Returns: Optional[List[education_submission_resource.EducationSubmissionResource]]
        """
        return self._resources
    
    @resources.setter
    def resources(self,value: Optional[List[education_submission_resource.EducationSubmissionResource]] = None) -> None:
        """
        Sets the resources property value. The resources property
        Args:
            value: Value to set for the resources property.
        """
        self._resources = value
    
    @property
    def resources_folder_url(self,) -> Optional[str]:
        """
        Gets the resourcesFolderUrl property value. Folder where all file resources for this submission need to be stored.
        Returns: Optional[str]
        """
        return self._resources_folder_url
    
    @resources_folder_url.setter
    def resources_folder_url(self,value: Optional[str] = None) -> None:
        """
        Sets the resourcesFolderUrl property value. Folder where all file resources for this submission need to be stored.
        Args:
            value: Value to set for the resourcesFolderUrl property.
        """
        self._resources_folder_url = value
    
    @property
    def returned_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the returnedBy property value. User who moved the status of this submission to returned.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._returned_by
    
    @returned_by.setter
    def returned_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the returnedBy property value. User who moved the status of this submission to returned.
        Args:
            value: Value to set for the returnedBy property.
        """
        self._returned_by = value
    
    @property
    def returned_date_time(self,) -> Optional[datetime]:
        """
        Gets the returnedDateTime property value. Moment in time when the submission was returned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._returned_date_time
    
    @returned_date_time.setter
    def returned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the returnedDateTime property value. Moment in time when the submission was returned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the returnedDateTime property.
        """
        self._returned_date_time = value
    
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
    
    @property
    def status(self,) -> Optional[education_submission_status.EducationSubmissionStatus]:
        """
        Gets the status property value. Read-only. Possible values are: working, submitted, released, returned, and reassigned. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: reassigned.
        Returns: Optional[education_submission_status.EducationSubmissionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[education_submission_status.EducationSubmissionStatus] = None) -> None:
        """
        Sets the status property value. Read-only. Possible values are: working, submitted, released, returned, and reassigned. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: reassigned.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def submitted_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the submittedBy property value. User who moved the resource into the submitted state.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._submitted_by
    
    @submitted_by.setter
    def submitted_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the submittedBy property value. User who moved the resource into the submitted state.
        Args:
            value: Value to set for the submittedBy property.
        """
        self._submitted_by = value
    
    @property
    def submitted_date_time(self,) -> Optional[datetime]:
        """
        Gets the submittedDateTime property value. Moment in time when the submission was moved into the submitted state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._submitted_date_time
    
    @submitted_date_time.setter
    def submitted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the submittedDateTime property value. Moment in time when the submission was moved into the submitted state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the submittedDateTime property.
        """
        self._submitted_date_time = value
    
    @property
    def submitted_resources(self,) -> Optional[List[education_submission_resource.EducationSubmissionResource]]:
        """
        Gets the submittedResources property value. The submittedResources property
        Returns: Optional[List[education_submission_resource.EducationSubmissionResource]]
        """
        return self._submitted_resources
    
    @submitted_resources.setter
    def submitted_resources(self,value: Optional[List[education_submission_resource.EducationSubmissionResource]] = None) -> None:
        """
        Sets the submittedResources property value. The submittedResources property
        Args:
            value: Value to set for the submittedResources property.
        """
        self._submitted_resources = value
    
    @property
    def unsubmitted_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the unsubmittedBy property value. User who moved the resource from submitted into the working state.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._unsubmitted_by
    
    @unsubmitted_by.setter
    def unsubmitted_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the unsubmittedBy property value. User who moved the resource from submitted into the working state.
        Args:
            value: Value to set for the unsubmittedBy property.
        """
        self._unsubmitted_by = value
    
    @property
    def unsubmitted_date_time(self,) -> Optional[datetime]:
        """
        Gets the unsubmittedDateTime property value. Moment in time when the submission was moved from submitted into the working state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._unsubmitted_date_time
    
    @unsubmitted_date_time.setter
    def unsubmitted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the unsubmittedDateTime property value. Moment in time when the submission was moved from submitted into the working state. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the unsubmittedDateTime property.
        """
        self._unsubmitted_date_time = value
    

