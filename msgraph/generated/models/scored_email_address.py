from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import selection_likelihood_info

@dataclass
class ScoredEmailAddress(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The email address.
    address: Optional[str] = None
    # The itemId property
    item_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relevance score of the email address. A relevance score is used as a sort key, in relation to the other returned results. A higher relevance score value corresponds to a more relevant result. Relevance is determined by the user’s communication and collaboration patterns and business relationships.
    relevance_score: Optional[float] = None
    # The selectionLikelihood property
    selection_likelihood: Optional[selection_likelihood_info.SelectionLikelihoodInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScoredEmailAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScoredEmailAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScoredEmailAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import selection_likelihood_info

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relevanceScore": lambda n : setattr(self, 'relevance_score', n.get_float_value()),
            "selectionLikelihood": lambda n : setattr(self, 'selection_likelihood', n.get_enum_value(selection_likelihood_info.SelectionLikelihoodInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("address", self.address)
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("relevanceScore", self.relevance_score)
        writer.write_enum_value("selectionLikelihood", self.selection_likelihood)
        writer.write_additional_data_value(self.additional_data)
    

