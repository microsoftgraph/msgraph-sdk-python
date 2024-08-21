from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .inference_classification_override import InferenceClassificationOverride

from .entity import Entity

@dataclass
class InferenceClassification(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.
    overrides: Optional[List[InferenceClassificationOverride]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InferenceClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceClassification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InferenceClassification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .inference_classification_override import InferenceClassificationOverride

        from .entity import Entity
        from .inference_classification_override import InferenceClassificationOverride

        fields: Dict[str, Callable[[Any], None]] = {
            "overrides": lambda n : setattr(self, 'overrides', n.get_collection_of_object_values(InferenceClassificationOverride)),
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
        writer.write_collection_of_object_values("overrides", self.overrides)
    

