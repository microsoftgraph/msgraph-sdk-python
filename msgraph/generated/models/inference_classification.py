from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
inference_classification_override = lazy_import('msgraph.generated.models.inference_classification_override')

class InferenceClassification(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new inferenceClassification and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.
        self._overrides: Optional[List[inference_classification_override.InferenceClassificationOverride]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InferenceClassification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InferenceClassification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "overrides": lambda n : setattr(self, 'overrides', n.get_collection_of_object_values(inference_classification_override.InferenceClassificationOverride)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def overrides(self,) -> Optional[List[inference_classification_override.InferenceClassificationOverride]]:
        """
        Gets the overrides property value. A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.
        Returns: Optional[List[inference_classification_override.InferenceClassificationOverride]]
        """
        return self._overrides
    
    @overrides.setter
    def overrides(self,value: Optional[List[inference_classification_override.InferenceClassificationOverride]] = None) -> None:
        """
        Sets the overrides property value. A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.
        Args:
            value: Value to set for the overrides property.
        """
        self._overrides = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("overrides", self.overrides)
    

