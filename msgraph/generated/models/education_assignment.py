from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_add_to_calendar_options = lazy_import('msgraph.generated.models.education_add_to_calendar_options')
education_added_student_action = lazy_import('msgraph.generated.models.education_added_student_action')
education_assignment_grade_type = lazy_import('msgraph.generated.models.education_assignment_grade_type')
education_assignment_recipient = lazy_import('msgraph.generated.models.education_assignment_recipient')
education_assignment_resource = lazy_import('msgraph.generated.models.education_assignment_resource')
education_assignment_status = lazy_import('msgraph.generated.models.education_assignment_status')
education_category = lazy_import('msgraph.generated.models.education_category')
education_item_body = lazy_import('msgraph.generated.models.education_item_body')
education_rubric = lazy_import('msgraph.generated.models.education_rubric')
education_submission = lazy_import('msgraph.generated.models.education_submission')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class EducationAssignment(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def added_student_action(self,) -> Optional[education_added_student_action.EducationAddedStudentAction]:
        """
        Gets the addedStudentAction property value. Optional field to control the assignment behavior for students who are added after the assignment is published. If not specified, defaults to none. Supported values are: none, assignIfOpen. For example, a teacher can use assignIfOpen to indicate that an assignment should be assigned to any new student who joins the class while the assignment is still open, and none to indicate that an assignment should not be assigned to new students.
        Returns: Optional[education_added_student_action.EducationAddedStudentAction]
        """
        return self._added_student_action
    
    @added_student_action.setter
    def added_student_action(self,value: Optional[education_added_student_action.EducationAddedStudentAction] = None) -> None:
        """
        Sets the addedStudentAction property value. Optional field to control the assignment behavior for students who are added after the assignment is published. If not specified, defaults to none. Supported values are: none, assignIfOpen. For example, a teacher can use assignIfOpen to indicate that an assignment should be assigned to any new student who joins the class while the assignment is still open, and none to indicate that an assignment should not be assigned to new students.
        Args:
            value: Value to set for the addedStudentAction property.
        """
        self._added_student_action = value
    
    @property
    def add_to_calendar_action(self,) -> Optional[education_add_to_calendar_options.EducationAddToCalendarOptions]:
        """
        Gets the addToCalendarAction property value. Optional field to control the assignment behavior  for adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        Returns: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions]
        """
        return self._add_to_calendar_action
    
    @add_to_calendar_action.setter
    def add_to_calendar_action(self,value: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions] = None) -> None:
        """
        Sets the addToCalendarAction property value. Optional field to control the assignment behavior  for adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        Args:
            value: Value to set for the addToCalendarAction property.
        """
        self._add_to_calendar_action = value
    
    @property
    def allow_late_submissions(self,) -> Optional[bool]:
        """
        Gets the allowLateSubmissions property value. Identifies whether students can submit after the due date. If this property isn't specified during create, it defaults to true.
        Returns: Optional[bool]
        """
        return self._allow_late_submissions
    
    @allow_late_submissions.setter
    def allow_late_submissions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowLateSubmissions property value. Identifies whether students can submit after the due date. If this property isn't specified during create, it defaults to true.
        Args:
            value: Value to set for the allowLateSubmissions property.
        """
        self._allow_late_submissions = value
    
    @property
    def allow_students_to_add_resources_to_submission(self,) -> Optional[bool]:
        """
        Gets the allowStudentsToAddResourcesToSubmission property value. Identifies whether students can add their own resources to a submission or if they can only modify resources added by the teacher.
        Returns: Optional[bool]
        """
        return self._allow_students_to_add_resources_to_submission
    
    @allow_students_to_add_resources_to_submission.setter
    def allow_students_to_add_resources_to_submission(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowStudentsToAddResourcesToSubmission property value. Identifies whether students can add their own resources to a submission or if they can only modify resources added by the teacher.
        Args:
            value: Value to set for the allowStudentsToAddResourcesToSubmission property.
        """
        self._allow_students_to_add_resources_to_submission = value
    
    @property
    def assign_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignDateTime property value. The date when the assignment should become active.  If in the future, the assignment isn't shown to the student until this date.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._assign_date_time
    
    @assign_date_time.setter
    def assign_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignDateTime property value. The date when the assignment should become active.  If in the future, the assignment isn't shown to the student until this date.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the assignDateTime property.
        """
        self._assign_date_time = value
    
    @property
    def assigned_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignedDateTime property value. The moment that the assignment was published to students and the assignment shows up on the students timeline.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._assigned_date_time
    
    @assigned_date_time.setter
    def assigned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignedDateTime property value. The moment that the assignment was published to students and the assignment shows up on the students timeline.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the assignedDateTime property.
        """
        self._assigned_date_time = value
    
    @property
    def assign_to(self,) -> Optional[education_assignment_recipient.EducationAssignmentRecipient]:
        """
        Gets the assignTo property value. Which users, or whole class should receive a submission object once the assignment is published.
        Returns: Optional[education_assignment_recipient.EducationAssignmentRecipient]
        """
        return self._assign_to
    
    @assign_to.setter
    def assign_to(self,value: Optional[education_assignment_recipient.EducationAssignmentRecipient] = None) -> None:
        """
        Sets the assignTo property value. Which users, or whole class should receive a submission object once the assignment is published.
        Args:
            value: Value to set for the assignTo property.
        """
        self._assign_to = value
    
    @property
    def categories(self,) -> Optional[List[education_category.EducationCategory]]:
        """
        Gets the categories property value. When set, enables users to easily find assignments of a given type.  Read-only. Nullable.
        Returns: Optional[List[education_category.EducationCategory]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[education_category.EducationCategory]] = None) -> None:
        """
        Sets the categories property value. When set, enables users to easily find assignments of a given type.  Read-only. Nullable.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def class_id(self,) -> Optional[str]:
        """
        Gets the classId property value. Class which this assignment belongs.
        Returns: Optional[str]
        """
        return self._class_id
    
    @class_id.setter
    def class_id(self,value: Optional[str] = None) -> None:
        """
        Sets the classId property value. Class which this assignment belongs.
        Args:
            value: Value to set for the classId property.
        """
        self._class_id = value
    
    @property
    def close_date_time(self,) -> Optional[datetime]:
        """
        Gets the closeDateTime property value. Date when the assignment will be closed for submissions. This is an optional field that can be null if the assignment does not allowLateSubmissions or when the closeDateTime is the same as the dueDateTime. But if specified, then the closeDateTime must be greater than or equal to the dueDateTime. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._close_date_time
    
    @close_date_time.setter
    def close_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the closeDateTime property value. Date when the assignment will be closed for submissions. This is an optional field that can be null if the assignment does not allowLateSubmissions or when the closeDateTime is the same as the dueDateTime. But if specified, then the closeDateTime must be greater than or equal to the dueDateTime. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the closeDateTime property.
        """
        self._close_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationAssignment and sets the default values.
        """
        super().__init__()
        # Optional field to control the assignment behavior for students who are added after the assignment is published. If not specified, defaults to none. Supported values are: none, assignIfOpen. For example, a teacher can use assignIfOpen to indicate that an assignment should be assigned to any new student who joins the class while the assignment is still open, and none to indicate that an assignment should not be assigned to new students.
        self._added_student_action: Optional[education_added_student_action.EducationAddedStudentAction] = None
        # Optional field to control the assignment behavior  for adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: studentsOnly. The default value is none.
        self._add_to_calendar_action: Optional[education_add_to_calendar_options.EducationAddToCalendarOptions] = None
        # Identifies whether students can submit after the due date. If this property isn't specified during create, it defaults to true.
        self._allow_late_submissions: Optional[bool] = None
        # Identifies whether students can add their own resources to a submission or if they can only modify resources added by the teacher.
        self._allow_students_to_add_resources_to_submission: Optional[bool] = None
        # The date when the assignment should become active.  If in the future, the assignment isn't shown to the student until this date.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._assign_date_time: Optional[datetime] = None
        # The moment that the assignment was published to students and the assignment shows up on the students timeline.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._assigned_date_time: Optional[datetime] = None
        # Which users, or whole class should receive a submission object once the assignment is published.
        self._assign_to: Optional[education_assignment_recipient.EducationAssignmentRecipient] = None
        # When set, enables users to easily find assignments of a given type.  Read-only. Nullable.
        self._categories: Optional[List[education_category.EducationCategory]] = None
        # Class which this assignment belongs.
        self._class_id: Optional[str] = None
        # Date when the assignment will be closed for submissions. This is an optional field that can be null if the assignment does not allowLateSubmissions or when the closeDateTime is the same as the dueDateTime. But if specified, then the closeDateTime must be greater than or equal to the dueDateTime. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._close_date_time: Optional[datetime] = None
        # Who created the assignment.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Moment when the assignment was created.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # Name of the assignment.
        self._display_name: Optional[str] = None
        # Date when the students assignment is due.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._due_date_time: Optional[datetime] = None
        # Folder URL where all the feedback file resources for this assignment are stored.
        self._feedback_resources_folder_url: Optional[str] = None
        # How the assignment will be graded.
        self._grading: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None
        # Instructions for the assignment.  This along with the display name tell the student what to do.
        self._instructions: Optional[education_item_body.EducationItemBody] = None
        # Who last modified the assignment.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # Moment when the assignment was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_modified_date_time: Optional[datetime] = None
        # Optional field to specify the URL of the channel to post the assignment publish notification. If not specified or null, defaults to the General channel. This field only applies to assignments where the assignTo value is educationAssignmentClassRecipient. Updating the notificationChannelUrl isn't allowed after the assignment has been published.
        self._notification_channel_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Learning objects that are associated with this assignment.  Only teachers can modify this list. Nullable.
        self._resources: Optional[List[education_assignment_resource.EducationAssignmentResource]] = None
        # Folder URL where all the file resources for this assignment are stored.
        self._resources_folder_url: Optional[str] = None
        # When set, the grading rubric attached to this assignment.
        self._rubric: Optional[education_rubric.EducationRubric] = None
        # Status of the Assignment.  You can't PATCH this value.  Possible values are: draft, scheduled, published, assigned.
        self._status: Optional[education_assignment_status.EducationAssignmentStatus] = None
        # Once published, there is a submission object for each student representing their work and grade.  Read-only. Nullable.
        self._submissions: Optional[List[education_submission.EducationSubmission]] = None
        # The deep link URL for the given assignment.
        self._web_url: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Who created the assignment.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Who created the assignment.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Moment when the assignment was created.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Moment when the assignment was created.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignment()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the assignment.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the assignment.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def due_date_time(self,) -> Optional[datetime]:
        """
        Gets the dueDateTime property value. Date when the students assignment is due.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dueDateTime property value. Date when the students assignment is due.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the dueDateTime property.
        """
        self._due_date_time = value
    
    @property
    def feedback_resources_folder_url(self,) -> Optional[str]:
        """
        Gets the feedbackResourcesFolderUrl property value. Folder URL where all the feedback file resources for this assignment are stored.
        Returns: Optional[str]
        """
        return self._feedback_resources_folder_url
    
    @feedback_resources_folder_url.setter
    def feedback_resources_folder_url(self,value: Optional[str] = None) -> None:
        """
        Sets the feedbackResourcesFolderUrl property value. Folder URL where all the feedback file resources for this assignment are stored.
        Args:
            value: Value to set for the feedbackResourcesFolderUrl property.
        """
        self._feedback_resources_folder_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "added_student_action": lambda n : setattr(self, 'added_student_action', n.get_enum_value(education_added_student_action.EducationAddedStudentAction)),
            "add_to_calendar_action": lambda n : setattr(self, 'add_to_calendar_action', n.get_enum_value(education_add_to_calendar_options.EducationAddToCalendarOptions)),
            "allow_late_submissions": lambda n : setattr(self, 'allow_late_submissions', n.get_bool_value()),
            "allow_students_to_add_resources_to_submission": lambda n : setattr(self, 'allow_students_to_add_resources_to_submission', n.get_bool_value()),
            "assign_date_time": lambda n : setattr(self, 'assign_date_time', n.get_datetime_value()),
            "assigned_date_time": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "assign_to": lambda n : setattr(self, 'assign_to', n.get_object_value(education_assignment_recipient.EducationAssignmentRecipient)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(education_category.EducationCategory)),
            "class_id": lambda n : setattr(self, 'class_id', n.get_str_value()),
            "close_date_time": lambda n : setattr(self, 'close_date_time', n.get_datetime_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "due_date_time": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "feedback_resources_folder_url": lambda n : setattr(self, 'feedback_resources_folder_url', n.get_str_value()),
            "grading": lambda n : setattr(self, 'grading', n.get_object_value(education_assignment_grade_type.EducationAssignmentGradeType)),
            "instructions": lambda n : setattr(self, 'instructions', n.get_object_value(education_item_body.EducationItemBody)),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notification_channel_url": lambda n : setattr(self, 'notification_channel_url', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(education_assignment_resource.EducationAssignmentResource)),
            "resources_folder_url": lambda n : setattr(self, 'resources_folder_url', n.get_str_value()),
            "rubric": lambda n : setattr(self, 'rubric', n.get_object_value(education_rubric.EducationRubric)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(education_assignment_status.EducationAssignmentStatus)),
            "submissions": lambda n : setattr(self, 'submissions', n.get_collection_of_object_values(education_submission.EducationSubmission)),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grading(self,) -> Optional[education_assignment_grade_type.EducationAssignmentGradeType]:
        """
        Gets the grading property value. How the assignment will be graded.
        Returns: Optional[education_assignment_grade_type.EducationAssignmentGradeType]
        """
        return self._grading
    
    @grading.setter
    def grading(self,value: Optional[education_assignment_grade_type.EducationAssignmentGradeType] = None) -> None:
        """
        Sets the grading property value. How the assignment will be graded.
        Args:
            value: Value to set for the grading property.
        """
        self._grading = value
    
    @property
    def instructions(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the instructions property value. Instructions for the assignment.  This along with the display name tell the student what to do.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._instructions
    
    @instructions.setter
    def instructions(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the instructions property value. Instructions for the assignment.  This along with the display name tell the student what to do.
        Args:
            value: Value to set for the instructions property.
        """
        self._instructions = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Who last modified the assignment.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Who last modified the assignment.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Moment when the assignment was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Moment when the assignment was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def notification_channel_url(self,) -> Optional[str]:
        """
        Gets the notificationChannelUrl property value. Optional field to specify the URL of the channel to post the assignment publish notification. If not specified or null, defaults to the General channel. This field only applies to assignments where the assignTo value is educationAssignmentClassRecipient. Updating the notificationChannelUrl isn't allowed after the assignment has been published.
        Returns: Optional[str]
        """
        return self._notification_channel_url
    
    @notification_channel_url.setter
    def notification_channel_url(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationChannelUrl property value. Optional field to specify the URL of the channel to post the assignment publish notification. If not specified or null, defaults to the General channel. This field only applies to assignments where the assignTo value is educationAssignmentClassRecipient. Updating the notificationChannelUrl isn't allowed after the assignment has been published.
        Args:
            value: Value to set for the notificationChannelUrl property.
        """
        self._notification_channel_url = value
    
    @property
    def resources(self,) -> Optional[List[education_assignment_resource.EducationAssignmentResource]]:
        """
        Gets the resources property value. Learning objects that are associated with this assignment.  Only teachers can modify this list. Nullable.
        Returns: Optional[List[education_assignment_resource.EducationAssignmentResource]]
        """
        return self._resources
    
    @resources.setter
    def resources(self,value: Optional[List[education_assignment_resource.EducationAssignmentResource]] = None) -> None:
        """
        Sets the resources property value. Learning objects that are associated with this assignment.  Only teachers can modify this list. Nullable.
        Args:
            value: Value to set for the resources property.
        """
        self._resources = value
    
    @property
    def resources_folder_url(self,) -> Optional[str]:
        """
        Gets the resourcesFolderUrl property value. Folder URL where all the file resources for this assignment are stored.
        Returns: Optional[str]
        """
        return self._resources_folder_url
    
    @resources_folder_url.setter
    def resources_folder_url(self,value: Optional[str] = None) -> None:
        """
        Sets the resourcesFolderUrl property value. Folder URL where all the file resources for this assignment are stored.
        Args:
            value: Value to set for the resourcesFolderUrl property.
        """
        self._resources_folder_url = value
    
    @property
    def rubric(self,) -> Optional[education_rubric.EducationRubric]:
        """
        Gets the rubric property value. When set, the grading rubric attached to this assignment.
        Returns: Optional[education_rubric.EducationRubric]
        """
        return self._rubric
    
    @rubric.setter
    def rubric(self,value: Optional[education_rubric.EducationRubric] = None) -> None:
        """
        Sets the rubric property value. When set, the grading rubric attached to this assignment.
        Args:
            value: Value to set for the rubric property.
        """
        self._rubric = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("addedStudentAction", self.added_student_action)
        writer.write_enum_value("addToCalendarAction", self.add_to_calendar_action)
        writer.write_bool_value("allowLateSubmissions", self.allow_late_submissions)
        writer.write_bool_value("allowStudentsToAddResourcesToSubmission", self.allow_students_to_add_resources_to_submission)
        writer.write_object_value("assignTo", self.assign_to)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("classId", self.class_id)
        writer.write_datetime_value("closeDateTime", self.close_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_object_value("grading", self.grading)
        writer.write_object_value("instructions", self.instructions)
        writer.write_str_value("notificationChannelUrl", self.notification_channel_url)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_object_value("rubric", self.rubric)
        writer.write_collection_of_object_values("submissions", self.submissions)
    
    @property
    def status(self,) -> Optional[education_assignment_status.EducationAssignmentStatus]:
        """
        Gets the status property value. Status of the Assignment.  You can't PATCH this value.  Possible values are: draft, scheduled, published, assigned.
        Returns: Optional[education_assignment_status.EducationAssignmentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[education_assignment_status.EducationAssignmentStatus] = None) -> None:
        """
        Sets the status property value. Status of the Assignment.  You can't PATCH this value.  Possible values are: draft, scheduled, published, assigned.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def submissions(self,) -> Optional[List[education_submission.EducationSubmission]]:
        """
        Gets the submissions property value. Once published, there is a submission object for each student representing their work and grade.  Read-only. Nullable.
        Returns: Optional[List[education_submission.EducationSubmission]]
        """
        return self._submissions
    
    @submissions.setter
    def submissions(self,value: Optional[List[education_submission.EducationSubmission]] = None) -> None:
        """
        Sets the submissions property value. Once published, there is a submission object for each student representing their work and grade.  Read-only. Nullable.
        Args:
            value: Value to set for the submissions property.
        """
        self._submissions = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The deep link URL for the given assignment.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The deep link URL for the given assignment.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

