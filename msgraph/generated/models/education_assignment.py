from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_added_student_action import EducationAddedStudentAction
    from .education_add_to_calendar_options import EducationAddToCalendarOptions
    from .education_assignment_grade_type import EducationAssignmentGradeType
    from .education_assignment_recipient import EducationAssignmentRecipient
    from .education_assignment_resource import EducationAssignmentResource
    from .education_assignment_status import EducationAssignmentStatus
    from .education_category import EducationCategory
    from .education_grading_category import EducationGradingCategory
    from .education_grading_scheme import EducationGradingScheme
    from .education_item_body import EducationItemBody
    from .education_rubric import EducationRubric
    from .education_submission import EducationSubmission
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class EducationAssignment(Entity, Parsable):
    # Optional field to control the assignment behavior  for adding assignments to students' and teachers' calendars when the assignment is published. The possible values are: none, studentsAndPublisher, studentsAndTeamOwners, unknownFutureValue, and studentsOnly. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: studentsOnly. The default value is none.
    add_to_calendar_action: Optional[EducationAddToCalendarOptions] = None
    # Optional field to control the assignment behavior for students who are added after the assignment is published. If not specified, defaults to none. Supported values are: none, assignIfOpen. For example, a teacher can use assignIfOpen to indicate that an assignment should be assigned to any new student who joins the class while the assignment is still open, and none to indicate that an assignment shouldn't be assigned to new students.
    added_student_action: Optional[EducationAddedStudentAction] = None
    # Identifies whether students can submit after the due date. If this property isn't specified during create, it defaults to true.
    allow_late_submissions: Optional[bool] = None
    # Identifies whether students can add their own resources to a submission or if they can only modify resources added by the teacher.
    allow_students_to_add_resources_to_submission: Optional[bool] = None
    # The date when the assignment should become active. If in the future, the assignment isn't shown to the student until this date. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    assign_date_time: Optional[datetime.datetime] = None
    # Which users, or whole class should receive a submission object once the assignment is published.
    assign_to: Optional[EducationAssignmentRecipient] = None
    # The moment that the assignment was published to students and the assignment shows up on the students timeline. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    assigned_date_time: Optional[datetime.datetime] = None
    # When set, enables users to easily find assignments of a given type. Read-only. Nullable.
    categories: Optional[list[EducationCategory]] = None
    # Class to which this assignment belongs.
    class_id: Optional[str] = None
    # Date when the assignment is closed for submissions. This is an optional field that can be null if the assignment doesn't allowLateSubmissions or when the closeDateTime is the same as the dueDateTime. But if specified, then the closeDateTime must be greater than or equal to the dueDateTime. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    close_date_time: Optional[datetime.datetime] = None
    # Who created the assignment.
    created_by: Optional[IdentitySet] = None
    # Moment when the assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Name of the assignment.
    display_name: Optional[str] = None
    # Date when the students assignment is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    due_date_time: Optional[datetime.datetime] = None
    # Folder URL where all the feedback file resources for this assignment are stored.
    feedback_resources_folder_url: Optional[str] = None
    # How the assignment will be graded.
    grading: Optional[EducationAssignmentGradeType] = None
    # When set, enables users to weight assignments differently when computing a class average grade.
    grading_category: Optional[EducationGradingCategory] = None
    # When set, enables users to configure custom string grades based on the percentage of total points earned on this assignment.
    grading_scheme: Optional[EducationGradingScheme] = None
    # Instructions for the assignment. The instructions and the display name tell the student what to do.
    instructions: Optional[EducationItemBody] = None
    # Specifies the language in which UI notifications for the assignment are displayed. If languageTag isn't provided, the default language is en-US. Optional.
    language_tag: Optional[str] = None
    # Who last modified the assignment.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time on which the assignment was modified. A student submission doesn't modify the assignment; only teachers can update assignments. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # The URL of the module from which to access the assignment.
    module_url: Optional[str] = None
    # Optional field to specify the URL of the channel to post the assignment publish notification. If not specified or null, defaults to the General channel. This field only applies to assignments where the assignTo value is educationAssignmentClassRecipient. Updating the notificationChannelUrl isn't allowed after the assignment is published.
    notification_channel_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Learning objects that are associated with this assignment. Only teachers can modify this list. Nullable.
    resources: Optional[list[EducationAssignmentResource]] = None
    # Folder URL where all the file resources for this assignment are stored.
    resources_folder_url: Optional[str] = None
    # When set, the grading rubric attached to this assignment.
    rubric: Optional[EducationRubric] = None
    # Status of the assignment.  You can't PATCH this value. The possible values are: draft, scheduled, published, assigned, unknownFutureValue, inactive. Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: inactive.
    status: Optional[EducationAssignmentStatus] = None
    # Once published, there's a submission object for each student representing their work and grade. Read-only. Nullable.
    submissions: Optional[list[EducationSubmission]] = None
    # The deep link URL for the given assignment.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_added_student_action import EducationAddedStudentAction
        from .education_add_to_calendar_options import EducationAddToCalendarOptions
        from .education_assignment_grade_type import EducationAssignmentGradeType
        from .education_assignment_recipient import EducationAssignmentRecipient
        from .education_assignment_resource import EducationAssignmentResource
        from .education_assignment_status import EducationAssignmentStatus
        from .education_category import EducationCategory
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .education_item_body import EducationItemBody
        from .education_rubric import EducationRubric
        from .education_submission import EducationSubmission
        from .entity import Entity
        from .identity_set import IdentitySet

        from .education_added_student_action import EducationAddedStudentAction
        from .education_add_to_calendar_options import EducationAddToCalendarOptions
        from .education_assignment_grade_type import EducationAssignmentGradeType
        from .education_assignment_recipient import EducationAssignmentRecipient
        from .education_assignment_resource import EducationAssignmentResource
        from .education_assignment_status import EducationAssignmentStatus
        from .education_category import EducationCategory
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .education_item_body import EducationItemBody
        from .education_rubric import EducationRubric
        from .education_submission import EducationSubmission
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "addToCalendarAction": lambda n : setattr(self, 'add_to_calendar_action', n.get_enum_value(EducationAddToCalendarOptions)),
            "addedStudentAction": lambda n : setattr(self, 'added_student_action', n.get_enum_value(EducationAddedStudentAction)),
            "allowLateSubmissions": lambda n : setattr(self, 'allow_late_submissions', n.get_bool_value()),
            "allowStudentsToAddResourcesToSubmission": lambda n : setattr(self, 'allow_students_to_add_resources_to_submission', n.get_bool_value()),
            "assignDateTime": lambda n : setattr(self, 'assign_date_time', n.get_datetime_value()),
            "assignTo": lambda n : setattr(self, 'assign_to', n.get_object_value(EducationAssignmentRecipient)),
            "assignedDateTime": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_object_values(EducationCategory)),
            "classId": lambda n : setattr(self, 'class_id', n.get_str_value()),
            "closeDateTime": lambda n : setattr(self, 'close_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "feedbackResourcesFolderUrl": lambda n : setattr(self, 'feedback_resources_folder_url', n.get_str_value()),
            "grading": lambda n : setattr(self, 'grading', n.get_object_value(EducationAssignmentGradeType)),
            "gradingCategory": lambda n : setattr(self, 'grading_category', n.get_object_value(EducationGradingCategory)),
            "gradingScheme": lambda n : setattr(self, 'grading_scheme', n.get_object_value(EducationGradingScheme)),
            "instructions": lambda n : setattr(self, 'instructions', n.get_object_value(EducationItemBody)),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "moduleUrl": lambda n : setattr(self, 'module_url', n.get_str_value()),
            "notificationChannelUrl": lambda n : setattr(self, 'notification_channel_url', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(EducationAssignmentResource)),
            "resourcesFolderUrl": lambda n : setattr(self, 'resources_folder_url', n.get_str_value()),
            "rubric": lambda n : setattr(self, 'rubric', n.get_object_value(EducationRubric)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(EducationAssignmentStatus)),
            "submissions": lambda n : setattr(self, 'submissions', n.get_collection_of_object_values(EducationSubmission)),
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
        writer.write_enum_value("addToCalendarAction", self.add_to_calendar_action)
        writer.write_enum_value("addedStudentAction", self.added_student_action)
        writer.write_bool_value("allowLateSubmissions", self.allow_late_submissions)
        writer.write_bool_value("allowStudentsToAddResourcesToSubmission", self.allow_students_to_add_resources_to_submission)
        writer.write_object_value("assignTo", self.assign_to)
        writer.write_collection_of_object_values("categories", self.categories)
        writer.write_str_value("classId", self.class_id)
        writer.write_datetime_value("closeDateTime", self.close_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_object_value("grading", self.grading)
        writer.write_object_value("gradingCategory", self.grading_category)
        writer.write_object_value("gradingScheme", self.grading_scheme)
        writer.write_object_value("instructions", self.instructions)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("moduleUrl", self.module_url)
        writer.write_str_value("notificationChannelUrl", self.notification_channel_url)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_object_value("rubric", self.rubric)
        writer.write_collection_of_object_values("submissions", self.submissions)
    

