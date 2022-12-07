from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_resource = lazy_import('msgraph.generated.models.education_resource')

class EducationWordResource(education_resource.EducationResource):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationWordResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationWordResource"
        # Location of the file on disk.
        self._file_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationWordResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationWordResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationWordResource()
    
    @property
    def file_url(self,) -> Optional[str]:
        """
        Gets the fileUrl property value. Location of the file on disk.
        Returns: Optional[str]
        """
        return self._file_url
    
    @file_url.setter
    def file_url(self,value: Optional[str] = None) -> None:
        """
        Sets the fileUrl property value. Location of the file on disk.
        Args:
            value: Value to set for the fileUrl property.
        """
        self._file_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_url": lambda n : setattr(self, 'file_url', n.get_str_value()),
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
        writer.write_str_value("fileUrl", self.file_url)
    

