from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_metadata_dictionary import CustomMetadataDictionary
    from .process_content_metadata_base import ProcessContentMetadataBase

from .process_content_metadata_base import ProcessContentMetadataBase

@dataclass
class ProcessFileMetadata(ProcessContentMetadataBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.processFileMetadata"
    # A dictionary containing custom metadata associated with the file, potentially extracted by the calling application.
    custom_properties: Optional[CustomMetadataDictionary] = None
    # The unique identifier (for example, Entra User ID or UPN) of the owner of the file.
    owner_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessFileMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessFileMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProcessFileMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_metadata_dictionary import CustomMetadataDictionary
        from .process_content_metadata_base import ProcessContentMetadataBase

        from .custom_metadata_dictionary import CustomMetadataDictionary
        from .process_content_metadata_base import ProcessContentMetadataBase

        fields: dict[str, Callable[[Any], None]] = {
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(CustomMetadataDictionary)),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_str_value()),
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
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("ownerId", self.owner_id)
    

