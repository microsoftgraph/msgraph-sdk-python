from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_error import ClassificationError
    from .classification_inner_error import ClassificationInnerError
    from .processing_error import ProcessingError

@dataclass
class ClassifcationErrorBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A service-defined error code string.
    code: Optional[str] = None
    # Contains more specific, potentially internal error details.
    inner_error: Optional[ClassificationInnerError] = None
    # A human-readable representation of the error.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The target of the error (for example, the specific property or item causing the issue).
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClassifcationErrorBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClassifcationErrorBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.classificationError".casefold():
            from .classification_error import ClassificationError

            return ClassificationError()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.processingError".casefold():
            from .processing_error import ProcessingError

            return ProcessingError()
        return ClassifcationErrorBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classification_error import ClassificationError
        from .classification_inner_error import ClassificationInnerError
        from .processing_error import ProcessingError

        from .classification_error import ClassificationError
        from .classification_inner_error import ClassificationInnerError
        from .processing_error import ProcessingError

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "innerError": lambda n : setattr(self, 'inner_error', n.get_object_value(ClassificationInnerError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("code", self.code)
        writer.write_object_value("innerError", self.inner_error)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

