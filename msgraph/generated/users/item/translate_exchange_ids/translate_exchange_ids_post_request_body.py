from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.exchange_id_format import ExchangeIdFormat

@dataclass
class TranslateExchangeIdsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The InputIds property
    input_ids: Optional[List[str]] = None
    # The SourceIdType property
    source_id_type: Optional[ExchangeIdFormat] = None
    # The TargetIdType property
    target_id_type: Optional[ExchangeIdFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TranslateExchangeIdsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TranslateExchangeIdsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TranslateExchangeIdsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.exchange_id_format import ExchangeIdFormat

        from ....models.exchange_id_format import ExchangeIdFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "InputIds": lambda n : setattr(self, 'input_ids', n.get_collection_of_primitive_values(str)),
            "SourceIdType": lambda n : setattr(self, 'source_id_type', n.get_enum_value(ExchangeIdFormat)),
            "TargetIdType": lambda n : setattr(self, 'target_id_type', n.get_enum_value(ExchangeIdFormat)),
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
        from ....models.exchange_id_format import ExchangeIdFormat

        writer.write_collection_of_primitive_values("InputIds", self.input_ids)
        writer.write_enum_value("SourceIdType", self.source_id_type)
        writer.write_enum_value("TargetIdType", self.target_id_type)
        writer.write_additional_data_value(self.additional_data)
    

