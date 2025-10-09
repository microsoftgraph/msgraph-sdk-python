from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .reading_assignment_submission import ReadingAssignmentSubmission
    from .reading_coach_passage import ReadingCoachPassage
    from .reflect_check_in_response import ReflectCheckInResponse
    from .speaker_assignment_submission import SpeakerAssignmentSubmission

from .entity import Entity

@dataclass
class ReportsRoot(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Details of submitted reading assignments.
    reading_assignment_submissions: Optional[list[ReadingAssignmentSubmission]] = None
    # Details of practiced Reading Coach passages.
    reading_coach_passages: Optional[list[ReadingCoachPassage]] = None
    # Details of check-in responses.
    reflect_check_in_responses: Optional[list[ReflectCheckInResponse]] = None
    # Details of submitted speaker assignments.
    speaker_assignment_submissions: Optional[list[SpeakerAssignmentSubmission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReportsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReportsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReportsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .reading_assignment_submission import ReadingAssignmentSubmission
        from .reading_coach_passage import ReadingCoachPassage
        from .reflect_check_in_response import ReflectCheckInResponse
        from .speaker_assignment_submission import SpeakerAssignmentSubmission

        from .entity import Entity
        from .reading_assignment_submission import ReadingAssignmentSubmission
        from .reading_coach_passage import ReadingCoachPassage
        from .reflect_check_in_response import ReflectCheckInResponse
        from .speaker_assignment_submission import SpeakerAssignmentSubmission

        fields: dict[str, Callable[[Any], None]] = {
            "readingAssignmentSubmissions": lambda n : setattr(self, 'reading_assignment_submissions', n.get_collection_of_object_values(ReadingAssignmentSubmission)),
            "readingCoachPassages": lambda n : setattr(self, 'reading_coach_passages', n.get_collection_of_object_values(ReadingCoachPassage)),
            "reflectCheckInResponses": lambda n : setattr(self, 'reflect_check_in_responses', n.get_collection_of_object_values(ReflectCheckInResponse)),
            "speakerAssignmentSubmissions": lambda n : setattr(self, 'speaker_assignment_submissions', n.get_collection_of_object_values(SpeakerAssignmentSubmission)),
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
        writer.write_collection_of_object_values("readingAssignmentSubmissions", self.reading_assignment_submissions)
        writer.write_collection_of_object_values("readingCoachPassages", self.reading_coach_passages)
        writer.write_collection_of_object_values("reflectCheckInResponses", self.reflect_check_in_responses)
        writer.write_collection_of_object_values("speakerAssignmentSubmissions", self.speaker_assignment_submissions)
    

