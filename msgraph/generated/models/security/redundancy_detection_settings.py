from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RedundancyDetectionSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether email threading and near duplicate detection are enabled.
    is_enabled: Optional[bool] = None
    # Specifies the maximum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
    max_words: Optional[int] = None
    # Specifies the minimum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
    min_words: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the similarity level for documents to be put in the same near duplicate set. To learn more, see Document and email similarity threshold.
    similarity_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedundancyDetectionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedundancyDetectionSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedundancyDetectionSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "maxWords": lambda n : setattr(self, 'max_words', n.get_int_value()),
            "minWords": lambda n : setattr(self, 'min_words', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "similarityThreshold": lambda n : setattr(self, 'similarity_threshold', n.get_int_value()),
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("maxWords", self.max_words)
        writer.write_int_value("minWords", self.min_words)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("similarityThreshold", self.similarity_threshold)
        writer.write_additional_data_value(self.additional_data)
    

