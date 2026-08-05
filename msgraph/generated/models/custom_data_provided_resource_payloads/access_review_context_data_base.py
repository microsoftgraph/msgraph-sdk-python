from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_context_data import AccessReviewContextData
    from .apply_decision_context_data import ApplyDecisionContextData
    from .data import Data

from .data import Data

@dataclass
class AccessReviewContextDataBase(Data, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customDataProvidedResourcePayloads.accessReviewContextDataBase"
    # The unique identifier of the access review definition that this data is associated with.
    review_definition_id: Optional[str] = None
    # The unique identifier of the access review instance that this data is associated with.
    review_instance_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewContextDataBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewContextDataBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customDataProvidedResourcePayloads.accessReviewContextData".casefold():
            from .access_review_context_data import AccessReviewContextData

            return AccessReviewContextData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customDataProvidedResourcePayloads.applyDecisionContextData".casefold():
            from .apply_decision_context_data import ApplyDecisionContextData

            return ApplyDecisionContextData()
        return AccessReviewContextDataBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_context_data import AccessReviewContextData
        from .apply_decision_context_data import ApplyDecisionContextData
        from .data import Data

        from .access_review_context_data import AccessReviewContextData
        from .apply_decision_context_data import ApplyDecisionContextData
        from .data import Data

        fields: dict[str, Callable[[Any], None]] = {
            "reviewDefinitionId": lambda n : setattr(self, 'review_definition_id', n.get_str_value()),
            "reviewInstanceId": lambda n : setattr(self, 'review_instance_id', n.get_str_value()),
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
        writer.write_str_value("reviewDefinitionId", self.review_definition_id)
        writer.write_str_value("reviewInstanceId", self.review_instance_id)
    

