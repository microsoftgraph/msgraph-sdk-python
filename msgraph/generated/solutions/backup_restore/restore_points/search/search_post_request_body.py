from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.artifact_query import ArtifactQuery
    from .....models.restore_point_preference import RestorePointPreference
    from .....models.restore_point_tags import RestorePointTags
    from .....models.time_period import TimePeriod

@dataclass
class SearchPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The artifactQuery property
    artifact_query: Optional[ArtifactQuery] = None
    # The protectionTimePeriod property
    protection_time_period: Optional[TimePeriod] = None
    # The protectionUnitIds property
    protection_unit_ids: Optional[List[str]] = None
    # The restorePointPreference property
    restore_point_preference: Optional[RestorePointPreference] = None
    # The tags property
    tags: Optional[RestorePointTags] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.artifact_query import ArtifactQuery
        from .....models.restore_point_preference import RestorePointPreference
        from .....models.restore_point_tags import RestorePointTags
        from .....models.time_period import TimePeriod

        from .....models.artifact_query import ArtifactQuery
        from .....models.restore_point_preference import RestorePointPreference
        from .....models.restore_point_tags import RestorePointTags
        from .....models.time_period import TimePeriod

        fields: Dict[str, Callable[[Any], None]] = {
            "artifactQuery": lambda n : setattr(self, 'artifact_query', n.get_object_value(ArtifactQuery)),
            "protectionTimePeriod": lambda n : setattr(self, 'protection_time_period', n.get_object_value(TimePeriod)),
            "protectionUnitIds": lambda n : setattr(self, 'protection_unit_ids', n.get_collection_of_primitive_values(str)),
            "restorePointPreference": lambda n : setattr(self, 'restore_point_preference', n.get_enum_value(RestorePointPreference)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_enum_values(RestorePointTags)),
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
        writer.write_object_value("artifactQuery", self.artifact_query)
        writer.write_object_value("protectionTimePeriod", self.protection_time_period)
        writer.write_collection_of_primitive_values("protectionUnitIds", self.protection_unit_ids)
        writer.write_enum_value("restorePointPreference", self.restore_point_preference)
        writer.write_enum_value("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

