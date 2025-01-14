from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_resource import EducationResource

from .education_resource import EducationResource

@dataclass
class EducationExcelResource(EducationResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationExcelResource"
    # Pointer to the Excel file object.
    file_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationExcelResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationExcelResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationExcelResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_resource import EducationResource

        from .education_resource import EducationResource

        fields: dict[str, Callable[[Any], None]] = {
            "fileUrl": lambda n : setattr(self, 'file_url', n.get_str_value()),
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
        writer.write_str_value("fileUrl", self.file_url)
    

