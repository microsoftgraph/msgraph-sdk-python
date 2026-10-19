from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.access_review_instance_decision_item_apply_result import AccessReviewInstanceDecisionItemApplyResult

@dataclass
class BatchApplyCustomDataProvidedResourceDecisionsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The applyDescription property
    apply_description: Optional[str] = None
    # The applyResult property
    apply_result: Optional[AccessReviewInstanceDecisionItemApplyResult] = None
    # The customDataProvidedResourceId property
    custom_data_provided_resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchApplyCustomDataProvidedResourceDecisionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchApplyCustomDataProvidedResourceDecisionsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchApplyCustomDataProvidedResourceDecisionsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.access_review_instance_decision_item_apply_result import AccessReviewInstanceDecisionItemApplyResult

        from ........models.access_review_instance_decision_item_apply_result import AccessReviewInstanceDecisionItemApplyResult

        fields: dict[str, Callable[[Any], None]] = {
            "applyDescription": lambda n : setattr(self, 'apply_description', n.get_str_value()),
            "applyResult": lambda n : setattr(self, 'apply_result', n.get_enum_value(AccessReviewInstanceDecisionItemApplyResult)),
            "customDataProvidedResourceId": lambda n : setattr(self, 'custom_data_provided_resource_id', n.get_str_value()),
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
        writer.write_str_value("applyDescription", self.apply_description)
        writer.write_enum_value("applyResult", self.apply_result)
        writer.write_str_value("customDataProvidedResourceId", self.custom_data_provided_resource_id)
        writer.write_additional_data_value(self.additional_data)
    

