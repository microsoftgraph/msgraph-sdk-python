from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class SpeakerAssignmentSubmission(Entity, Parsable):
    # ID of the assignment with which this submission is associated.
    assignment_id: Optional[str] = None
    # The average speaking pace of the student, measured in words per minute.
    average_words_per_minute_pace: Optional[int] = None
    # ID of the class this speaker progress is associated with.
    class_id: Optional[str] = None
    # The number of times the student was flagged by Speaker Coach for using a filler word.
    filler_words_occurrences_count: Optional[int] = None
    # The number of times the student was flagged by Speaker Coach for being either too close or too far away from the camera.
    incorrect_camera_distance_occurrences_count: Optional[int] = None
    # The length of the student submission in seconds.
    length_of_submission_in_seconds: Optional[float] = None
    # The number of times the student was flagged by Speaker Coach for losing eye contact with the camera.
    lost_eye_contact_occurrences_count: Optional[int] = None
    # The number of times the student was flagged by Speaker Coach for speaking in monotone.
    monotone_occurrences_count: Optional[int] = None
    # The number of times the student was flagged by Speaker Coach for using non-inclusive or sensitive language.
    non_inclusive_language_occurrences_count: Optional[int] = None
    # The number of times the student was flagged by Speaker Coach for obstructing the view of their face.
    obstructed_view_occurrences_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of times the student was flagged by Speaker Coach for using repetitive language.
    repetitive_language_occurrences_count: Optional[int] = None
    # ID of the user this speaker progress is associated with.
    student_id: Optional[str] = None
    # Date and time of the submission this speaker progress is associated with. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    submission_date_time: Optional[datetime.datetime] = None
    # ID of the submission this speaker progress is associated with.
    submission_id: Optional[str] = None
    # The filler words used most by the student.
    top_filler_words: Optional[list[str]] = None
    # The words mispronounced most by the student.
    top_mispronounced_words: Optional[list[str]] = None
    # The non-inclusive or sensitive words and phrases most used by the student.
    top_non_inclusive_words_and_phrases: Optional[list[str]] = None
    # The words and phrases most repeated by the student.
    top_repetitive_words_and_phrases: Optional[list[str]] = None
    # Total number of words spoken by the student in the submission.
    words_spoken_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpeakerAssignmentSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpeakerAssignmentSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpeakerAssignmentSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentId": lambda n : setattr(self, 'assignment_id', n.get_str_value()),
            "averageWordsPerMinutePace": lambda n : setattr(self, 'average_words_per_minute_pace', n.get_int_value()),
            "classId": lambda n : setattr(self, 'class_id', n.get_str_value()),
            "fillerWordsOccurrencesCount": lambda n : setattr(self, 'filler_words_occurrences_count', n.get_int_value()),
            "incorrectCameraDistanceOccurrencesCount": lambda n : setattr(self, 'incorrect_camera_distance_occurrences_count', n.get_int_value()),
            "lengthOfSubmissionInSeconds": lambda n : setattr(self, 'length_of_submission_in_seconds', n.get_float_value()),
            "lostEyeContactOccurrencesCount": lambda n : setattr(self, 'lost_eye_contact_occurrences_count', n.get_int_value()),
            "monotoneOccurrencesCount": lambda n : setattr(self, 'monotone_occurrences_count', n.get_int_value()),
            "nonInclusiveLanguageOccurrencesCount": lambda n : setattr(self, 'non_inclusive_language_occurrences_count', n.get_int_value()),
            "obstructedViewOccurrencesCount": lambda n : setattr(self, 'obstructed_view_occurrences_count', n.get_int_value()),
            "repetitiveLanguageOccurrencesCount": lambda n : setattr(self, 'repetitive_language_occurrences_count', n.get_int_value()),
            "studentId": lambda n : setattr(self, 'student_id', n.get_str_value()),
            "submissionDateTime": lambda n : setattr(self, 'submission_date_time', n.get_datetime_value()),
            "submissionId": lambda n : setattr(self, 'submission_id', n.get_str_value()),
            "topFillerWords": lambda n : setattr(self, 'top_filler_words', n.get_collection_of_primitive_values(str)),
            "topMispronouncedWords": lambda n : setattr(self, 'top_mispronounced_words', n.get_collection_of_primitive_values(str)),
            "topNonInclusiveWordsAndPhrases": lambda n : setattr(self, 'top_non_inclusive_words_and_phrases', n.get_collection_of_primitive_values(str)),
            "topRepetitiveWordsAndPhrases": lambda n : setattr(self, 'top_repetitive_words_and_phrases', n.get_collection_of_primitive_values(str)),
            "wordsSpokenCount": lambda n : setattr(self, 'words_spoken_count', n.get_int_value()),
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
        writer.write_str_value("assignmentId", self.assignment_id)
        writer.write_int_value("averageWordsPerMinutePace", self.average_words_per_minute_pace)
        writer.write_str_value("classId", self.class_id)
        writer.write_int_value("fillerWordsOccurrencesCount", self.filler_words_occurrences_count)
        writer.write_int_value("incorrectCameraDistanceOccurrencesCount", self.incorrect_camera_distance_occurrences_count)
        writer.write_float_value("lengthOfSubmissionInSeconds", self.length_of_submission_in_seconds)
        writer.write_int_value("lostEyeContactOccurrencesCount", self.lost_eye_contact_occurrences_count)
        writer.write_int_value("monotoneOccurrencesCount", self.monotone_occurrences_count)
        writer.write_int_value("nonInclusiveLanguageOccurrencesCount", self.non_inclusive_language_occurrences_count)
        writer.write_int_value("obstructedViewOccurrencesCount", self.obstructed_view_occurrences_count)
        writer.write_int_value("repetitiveLanguageOccurrencesCount", self.repetitive_language_occurrences_count)
        writer.write_str_value("studentId", self.student_id)
        writer.write_datetime_value("submissionDateTime", self.submission_date_time)
        writer.write_str_value("submissionId", self.submission_id)
        writer.write_collection_of_primitive_values("topFillerWords", self.top_filler_words)
        writer.write_collection_of_primitive_values("topMispronouncedWords", self.top_mispronounced_words)
        writer.write_collection_of_primitive_values("topNonInclusiveWordsAndPhrases", self.top_non_inclusive_words_and_phrases)
        writer.write_collection_of_primitive_values("topRepetitiveWordsAndPhrases", self.top_repetitive_words_and_phrases)
        writer.write_int_value("wordsSpokenCount", self.words_spoken_count)
    

