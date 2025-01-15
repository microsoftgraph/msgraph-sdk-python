from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RecommendedAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Web URL to the recommended action.
    action_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Potential improvement in the tenant security score from the recommended action.
    potential_score_impact: Optional[float] = None
    # Title of the recommended action.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecommendedAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecommendedAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecommendedAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionWebUrl": lambda n : setattr(self, 'action_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "potentialScoreImpact": lambda n : setattr(self, 'potential_score_impact', n.get_float_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("actionWebUrl", self.action_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("potentialScoreImpact", self.potential_score_impact)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

