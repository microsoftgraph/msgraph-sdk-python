from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

threat_assessment_request = lazy_import('msgraph.generated.models.threat_assessment_request')

class FileAssessmentRequest(threat_assessment_request.ThreatAssessmentRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new FileAssessmentRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.fileAssessmentRequest"
        # Base64 encoded file content. The file content cannot fetch back because it isn't stored.
        self._content_data: Optional[str] = None
        # The file name.
        self._file_name: Optional[str] = None
    
    @property
    def content_data(self,) -> Optional[str]:
        """
        Gets the contentData property value. Base64 encoded file content. The file content cannot fetch back because it isn't stored.
        Returns: Optional[str]
        """
        return self._content_data
    
    @content_data.setter
    def content_data(self,value: Optional[str] = None) -> None:
        """
        Sets the contentData property value. Base64 encoded file content. The file content cannot fetch back because it isn't stored.
        Args:
            value: Value to set for the contentData property.
        """
        self._content_data = value
    
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
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The file name.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The file name.
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_data": lambda n : setattr(self, 'content_data', n.get_str_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
    

