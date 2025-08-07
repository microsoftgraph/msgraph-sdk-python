from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .challenging_word import ChallengingWord
    from .entity import Entity

from .entity import Entity

@dataclass
class ReadingAssignmentSubmission(Entity, Parsable):
    # Accuracy score of the reading progress.
    accuracy_score: Optional[float] = None
    # Indicates whether the submission is an attempt by the student or a miscue edit done by the educator. The possible values are Attempt and EditMiscue.
    action: Optional[str] = None
    # ID of the assignment with which this submission is associated.
    assignment_id: Optional[str] = None
    # List of words that the student found challenging during the reading session.
    challenging_words: Optional[list[ChallengingWord]] = None
    # ID of the class this reading progress is associated with.
    class_id: Optional[str] = None
    # Insertions of the reading progress.
    insertions: Optional[int] = None
    # Mispronunciations of the reading progress.
    mispronunciations: Optional[int] = None
    # Number of exclamation marks missed in the reading passage.
    missed_exclamation_marks: Optional[int] = None
    # Number of periods missed in the reading passage.
    missed_periods: Optional[int] = None
    # Number of question marks missed in the reading passage.
    missed_question_marks: Optional[int] = None
    # Number of short words missed during the reading session.
    missed_shorts: Optional[int] = None
    # Score that reflects the student's use of intonation and expression. Lower scores indicate more monotone reading.
    monotone_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Omissions of the reading progress.
    omissions: Optional[int] = None
    # Number of times the student repeated words or phrases during the reading session.
    repetitions: Optional[int] = None
    # Number of times the student self-corrected their reading errors.
    self_corrections: Optional[int] = None
    # ID of the user this reading progress is associated with.
    student_id: Optional[str] = None
    # Date and time of the submission this reading progress is associated with. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    submission_date_time: Optional[datetime.datetime] = None
    # ID of the submission this reading progress is associated with.
    submission_id: Optional[str] = None
    # Number of unexpected pauses made during the reading session.
    unexpected_pauses: Optional[int] = None
    # Words count of the reading progress.
    word_count: Optional[int] = None
    # Words per minute of the reading progress.
    words_per_minute: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReadingAssignmentSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReadingAssignmentSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReadingAssignmentSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .challenging_word import ChallengingWord
        from .entity import Entity

        from .challenging_word import ChallengingWord
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accuracyScore": lambda n : setattr(self, 'accuracy_score', n.get_float_value()),
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "assignmentId": lambda n : setattr(self, 'assignment_id', n.get_str_value()),
            "challengingWords": lambda n : setattr(self, 'challenging_words', n.get_collection_of_object_values(ChallengingWord)),
            "classId": lambda n : setattr(self, 'class_id', n.get_str_value()),
            "insertions": lambda n : setattr(self, 'insertions', n.get_int_value()),
            "mispronunciations": lambda n : setattr(self, 'mispronunciations', n.get_int_value()),
            "missedExclamationMarks": lambda n : setattr(self, 'missed_exclamation_marks', n.get_int_value()),
            "missedPeriods": lambda n : setattr(self, 'missed_periods', n.get_int_value()),
            "missedQuestionMarks": lambda n : setattr(self, 'missed_question_marks', n.get_int_value()),
            "missedShorts": lambda n : setattr(self, 'missed_shorts', n.get_int_value()),
            "monotoneScore": lambda n : setattr(self, 'monotone_score', n.get_float_value()),
            "omissions": lambda n : setattr(self, 'omissions', n.get_int_value()),
            "repetitions": lambda n : setattr(self, 'repetitions', n.get_int_value()),
            "selfCorrections": lambda n : setattr(self, 'self_corrections', n.get_int_value()),
            "studentId": lambda n : setattr(self, 'student_id', n.get_str_value()),
            "submissionDateTime": lambda n : setattr(self, 'submission_date_time', n.get_datetime_value()),
            "submissionId": lambda n : setattr(self, 'submission_id', n.get_str_value()),
            "unexpectedPauses": lambda n : setattr(self, 'unexpected_pauses', n.get_int_value()),
            "wordCount": lambda n : setattr(self, 'word_count', n.get_int_value()),
            "wordsPerMinute": lambda n : setattr(self, 'words_per_minute', n.get_float_value()),
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
        writer.write_float_value("accuracyScore", self.accuracy_score)
        writer.write_str_value("action", self.action)
        writer.write_str_value("assignmentId", self.assignment_id)
        writer.write_collection_of_object_values("challengingWords", self.challenging_words)
        writer.write_str_value("classId", self.class_id)
        writer.write_int_value("insertions", self.insertions)
        writer.write_int_value("mispronunciations", self.mispronunciations)
        writer.write_int_value("missedExclamationMarks", self.missed_exclamation_marks)
        writer.write_int_value("missedPeriods", self.missed_periods)
        writer.write_int_value("missedQuestionMarks", self.missed_question_marks)
        writer.write_int_value("missedShorts", self.missed_shorts)
        writer.write_float_value("monotoneScore", self.monotone_score)
        writer.write_int_value("omissions", self.omissions)
        writer.write_int_value("repetitions", self.repetitions)
        writer.write_int_value("selfCorrections", self.self_corrections)
        writer.write_str_value("studentId", self.student_id)
        writer.write_datetime_value("submissionDateTime", self.submission_date_time)
        writer.write_str_value("submissionId", self.submission_id)
        writer.write_int_value("unexpectedPauses", self.unexpected_pauses)
        writer.write_int_value("wordCount", self.word_count)
        writer.write_float_value("wordsPerMinute", self.words_per_minute)
    

