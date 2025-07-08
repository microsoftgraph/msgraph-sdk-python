from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classifcation_error_base import ClassifcationErrorBase
    from .processing_error import ProcessingError

from .classifcation_error_base import ClassifcationErrorBase

@dataclass
class ClassificationError(ClassifcationErrorBase, Parsable):
    # A collection of more specific errors contributing to the overall error.
    details: Optional[list[ClassifcationErrorBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClassificationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClassificationError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.processingError".casefold():
            from .processing_error import ProcessingError

            return ProcessingError()
        return ClassificationError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classifcation_error_base import ClassifcationErrorBase
        from .processing_error import ProcessingError

        from .classifcation_error_base import ClassifcationErrorBase
        from .processing_error import ProcessingError

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(ClassifcationErrorBase)),
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
        writer.write_collection_of_object_values("details", self.details)
    

