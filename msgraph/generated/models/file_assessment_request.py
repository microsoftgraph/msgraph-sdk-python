from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .threat_assessment_request import ThreatAssessmentRequest

from .threat_assessment_request import ThreatAssessmentRequest

@dataclass
class FileAssessmentRequest(ThreatAssessmentRequest, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.fileAssessmentRequest"
    # Base64 encoded file content. The file content can't fetch back because it isn't stored.
    content_data: Optional[str] = None
    # The file name.
    file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileAssessmentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileAssessmentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .threat_assessment_request import ThreatAssessmentRequest

        from .threat_assessment_request import ThreatAssessmentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "contentData": lambda n : setattr(self, 'content_data', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
        writer.write_str_value("contentData", self.content_data)
        writer.write_str_value("fileName", self.file_name)
    

