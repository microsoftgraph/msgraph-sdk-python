from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .reading_coach_story_type import ReadingCoachStoryType

from .entity import Entity

@dataclass
class ReadingCoachPassage(Entity, Parsable):
    # Indicates if the reading passage was completed.
    is_reading_completed: Optional[bool] = None
    # The language of the reading passage.
    language_tag: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of challenging words for the student that they can practice further.
    practice_words: Optional[list[str]] = None
    # The date and time when the Reading Coach passage was practiced. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    practiced_at_date_time: Optional[datetime.datetime] = None
    # The storyType property
    story_type: Optional[ReadingCoachStoryType] = None
    # ID of the student that practiced the reading passage.
    student_id: Optional[str] = None
    # The time the student spent reading in seconds.
    time_spent_reading_in_seconds: Optional[float] = None
    # The percentage of words that the student read correctly.
    words_accuracy_percentage: Optional[float] = None
    # The rate the student read at in words per minute.
    words_per_minute: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReadingCoachPassage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReadingCoachPassage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReadingCoachPassage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .reading_coach_story_type import ReadingCoachStoryType

        from .entity import Entity
        from .reading_coach_story_type import ReadingCoachStoryType

        fields: dict[str, Callable[[Any], None]] = {
            "isReadingCompleted": lambda n : setattr(self, 'is_reading_completed', n.get_bool_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "practiceWords": lambda n : setattr(self, 'practice_words', n.get_collection_of_primitive_values(str)),
            "practicedAtDateTime": lambda n : setattr(self, 'practiced_at_date_time', n.get_datetime_value()),
            "storyType": lambda n : setattr(self, 'story_type', n.get_enum_value(ReadingCoachStoryType)),
            "studentId": lambda n : setattr(self, 'student_id', n.get_str_value()),
            "timeSpentReadingInSeconds": lambda n : setattr(self, 'time_spent_reading_in_seconds', n.get_float_value()),
            "wordsAccuracyPercentage": lambda n : setattr(self, 'words_accuracy_percentage', n.get_float_value()),
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
        writer.write_bool_value("isReadingCompleted", self.is_reading_completed)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_collection_of_primitive_values("practiceWords", self.practice_words)
        writer.write_datetime_value("practicedAtDateTime", self.practiced_at_date_time)
        writer.write_enum_value("storyType", self.story_type)
        writer.write_str_value("studentId", self.student_id)
        writer.write_float_value("timeSpentReadingInSeconds", self.time_spent_reading_in_seconds)
        writer.write_float_value("wordsAccuracyPercentage", self.words_accuracy_percentage)
        writer.write_float_value("wordsPerMinute", self.words_per_minute)
    

