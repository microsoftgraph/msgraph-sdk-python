from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security.statistics_options import StatisticsOptions

@dataclass
class EstimateStatisticsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The statisticsOptions property
    statistics_options: Optional[StatisticsOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EstimateStatisticsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EstimateStatisticsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EstimateStatisticsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security.statistics_options import StatisticsOptions

        from ........models.security.statistics_options import StatisticsOptions

        fields: dict[str, Callable[[Any], None]] = {
            "statisticsOptions": lambda n : setattr(self, 'statistics_options', n.get_collection_of_enum_values(StatisticsOptions)),
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
        writer.write_enum_value("statisticsOptions", self.statistics_options)
        writer.write_additional_data_value(self.additional_data)
    

