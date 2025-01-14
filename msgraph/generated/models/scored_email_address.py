from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .selection_likelihood_info import SelectionLikelihoodInfo

@dataclass
class ScoredEmailAddress(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The email address.
    address: Optional[str] = None
    # The itemId property
    item_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relevance score of the email address. A relevance score is used as a sort key, in relation to the other returned results. A higher relevance score value corresponds to a more relevant result. Relevance is determined by the user’s communication and collaboration patterns and business relationships.
    relevance_score: Optional[float] = None
    # The selectionLikelihood property
    selection_likelihood: Optional[SelectionLikelihoodInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScoredEmailAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScoredEmailAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScoredEmailAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .selection_likelihood_info import SelectionLikelihoodInfo

        from .selection_likelihood_info import SelectionLikelihoodInfo

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relevanceScore": lambda n : setattr(self, 'relevance_score', n.get_float_value()),
            "selectionLikelihood": lambda n : setattr(self, 'selection_likelihood', n.get_enum_value(SelectionLikelihoodInfo)),
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("relevanceScore", self.relevance_score)
        writer.write_enum_value("selectionLikelihood", self.selection_likelihood)
        writer.write_additional_data_value(self.additional_data)
    

