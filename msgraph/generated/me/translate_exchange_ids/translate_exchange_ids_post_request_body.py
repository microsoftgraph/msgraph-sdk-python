from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import exchange_id_format

@dataclass
class TranslateExchangeIdsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The InputIds property
    input_ids: Optional[List[str]] = None
    # The SourceIdType property
    source_id_type: Optional[exchange_id_format.ExchangeIdFormat] = None
    # The TargetIdType property
    target_id_type: Optional[exchange_id_format.ExchangeIdFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TranslateExchangeIdsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TranslateExchangeIdsPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TranslateExchangeIdsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models import exchange_id_format

        from ...models import exchange_id_format

        fields: Dict[str, Callable[[Any], None]] = {
            "InputIds": lambda n : setattr(self, 'input_ids', n.get_collection_of_primitive_values(str)),
            "SourceIdType": lambda n : setattr(self, 'source_id_type', n.get_enum_value(exchange_id_format.ExchangeIdFormat)),
            "TargetIdType": lambda n : setattr(self, 'target_id_type', n.get_enum_value(exchange_id_format.ExchangeIdFormat)),
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
        writer.write_collection_of_primitive_values("InputIds", self.input_ids)
        writer.write_enum_value("SourceIdType", self.source_id_type)
        writer.write_enum_value("TargetIdType", self.target_id_type)
        writer.write_additional_data_value(self.additional_data)
    

