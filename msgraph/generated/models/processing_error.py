from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_error import ClassificationError
    from .content_processing_error_type import ContentProcessingErrorType

from .classification_error import ClassificationError

@dataclass
class ProcessingError(ClassificationError, Parsable):
    # The errorType property
    error_type: Optional[ContentProcessingErrorType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessingError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessingError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProcessingError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classification_error import ClassificationError
        from .content_processing_error_type import ContentProcessingErrorType

        from .classification_error import ClassificationError
        from .content_processing_error_type import ContentProcessingErrorType

        fields: dict[str, Callable[[Any], None]] = {
            "errorType": lambda n : setattr(self, 'error_type', n.get_enum_value(ContentProcessingErrorType)),
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
        writer.write_enum_value("errorType", self.error_type)
    

