from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .threat_assessment_result_type import ThreatAssessmentResultType

from .entity import Entity

@dataclass
class ThreatAssessmentResult(Entity, Parsable):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The result message for each threat assessment.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The threat assessment result type. The possible values are: checkPolicy, rescan.
    result_type: Optional[ThreatAssessmentResultType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatAssessmentResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatAssessmentResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThreatAssessmentResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .threat_assessment_result_type import ThreatAssessmentResultType

        from .entity import Entity
        from .threat_assessment_result_type import ThreatAssessmentResultType

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "resultType": lambda n : setattr(self, 'result_type', n.get_enum_value(ThreatAssessmentResultType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("message", self.message)
        writer.write_enum_value("resultType", self.result_type)
    

