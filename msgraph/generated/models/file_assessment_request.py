from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import threat_assessment_request

from . import threat_assessment_request

@dataclass
class FileAssessmentRequest(threat_assessment_request.ThreatAssessmentRequest):
    odata_type = "#microsoft.graph.fileAssessmentRequest"
    # Base64 encoded file content. The file content cannot fetch back because it isn't stored.
    content_data: Optional[str] = None
    # The file name.
    file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileAssessmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileAssessmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import threat_assessment_request

        fields: Dict[str, Callable[[Any], None]] = {
            "contentData": lambda n : setattr(self, 'content_data', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("contentData", self.content_data)
        writer.write_str_value("fileName", self.file_name)
    

