from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security import additional_data_options, ediscovery_search

@dataclass
class AddToReviewSetPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The additionalDataOptions property
    additional_data_options: Optional[additional_data_options.AdditionalDataOptions] = None
    # The search property
    search: Optional[ediscovery_search.EdiscoverySearch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddToReviewSetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AddToReviewSetPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security import additional_data_options, ediscovery_search

        from ........models.security import additional_data_options, ediscovery_search

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalDataOptions": lambda n : setattr(self, 'additional_data_options', n.get_enum_value(additional_data_options.AdditionalDataOptions)),
            "search": lambda n : setattr(self, 'search', n.get_object_value(ediscovery_search.EdiscoverySearch)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("additionalDataOptions", self.additional_data_options)
        writer.write_object_value("search", self.search)
        writer.write_additional_data_value(self.additional_data)
    

