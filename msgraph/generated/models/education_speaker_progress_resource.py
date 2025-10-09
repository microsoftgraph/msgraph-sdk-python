from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_ai_feedback_criteria import EducationAiFeedbackCriteria
    from .education_resource import EducationResource
    from .education_speaker_coach_settings import EducationSpeakerCoachSettings

from .education_resource import EducationResource

@dataclass
class EducationSpeakerProgressResource(EducationResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationSpeakerProgressResource"
    # The feedback types that students should receive from AI feedback. This property should only be provided if isAiFeedbackEnabled is true.
    ai_feedback_criteria: Optional[EducationAiFeedbackCriteria] = None
    # Indicates whether AI feedback is enabled for the student submissions.
    is_ai_feedback_enabled: Optional[bool] = None
    # Indicates whether video is required for the student recording.
    is_video_required: Optional[bool] = None
    # The maximum number of recording attempts available to the student. Specify 0 to set unlimited recording attempts.
    max_recording_attempts: Optional[int] = None
    # The title of the speaker progress resource visible to students.
    presentation_title: Optional[str] = None
    # The time limit is in minutes for the student recording.
    recording_time_limit_in_minutes: Optional[int] = None
    # Allows students to view their rehearsal report before the assignment is graded.
    show_rehearsal_report_to_student_before_media_upload: Optional[bool] = None
    # The feedback types that students should receive from the Speaker Coach.
    speaker_coach_settings: Optional[EducationSpeakerCoachSettings] = None
    # The spoken language for the student recording. For example, en-US.
    spoken_language_locale: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSpeakerProgressResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSpeakerProgressResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSpeakerProgressResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_ai_feedback_criteria import EducationAiFeedbackCriteria
        from .education_resource import EducationResource
        from .education_speaker_coach_settings import EducationSpeakerCoachSettings

        from .education_ai_feedback_criteria import EducationAiFeedbackCriteria
        from .education_resource import EducationResource
        from .education_speaker_coach_settings import EducationSpeakerCoachSettings

        fields: dict[str, Callable[[Any], None]] = {
            "aiFeedbackCriteria": lambda n : setattr(self, 'ai_feedback_criteria', n.get_object_value(EducationAiFeedbackCriteria)),
            "isAiFeedbackEnabled": lambda n : setattr(self, 'is_ai_feedback_enabled', n.get_bool_value()),
            "isVideoRequired": lambda n : setattr(self, 'is_video_required', n.get_bool_value()),
            "maxRecordingAttempts": lambda n : setattr(self, 'max_recording_attempts', n.get_int_value()),
            "presentationTitle": lambda n : setattr(self, 'presentation_title', n.get_str_value()),
            "recordingTimeLimitInMinutes": lambda n : setattr(self, 'recording_time_limit_in_minutes', n.get_int_value()),
            "showRehearsalReportToStudentBeforeMediaUpload": lambda n : setattr(self, 'show_rehearsal_report_to_student_before_media_upload', n.get_bool_value()),
            "speakerCoachSettings": lambda n : setattr(self, 'speaker_coach_settings', n.get_object_value(EducationSpeakerCoachSettings)),
            "spokenLanguageLocale": lambda n : setattr(self, 'spoken_language_locale', n.get_str_value()),
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
        writer.write_object_value("aiFeedbackCriteria", self.ai_feedback_criteria)
        writer.write_bool_value("isAiFeedbackEnabled", self.is_ai_feedback_enabled)
        writer.write_bool_value("isVideoRequired", self.is_video_required)
        writer.write_int_value("maxRecordingAttempts", self.max_recording_attempts)
        writer.write_str_value("presentationTitle", self.presentation_title)
        writer.write_int_value("recordingTimeLimitInMinutes", self.recording_time_limit_in_minutes)
        writer.write_bool_value("showRehearsalReportToStudentBeforeMediaUpload", self.show_rehearsal_report_to_student_before_media_upload)
        writer.write_object_value("speakerCoachSettings", self.speaker_coach_settings)
        writer.write_str_value("spokenLanguageLocale", self.spoken_language_locale)
    

