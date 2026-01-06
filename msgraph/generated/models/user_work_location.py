from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .work_location_source import WorkLocationSource
    from .work_location_type import WorkLocationType

@dataclass
class UserWorkLocation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier of the place, if applicable.
    place_id: Optional[str] = None
    # The source property
    source: Optional[WorkLocationSource] = None
    # The workLocationType property
    work_location_type: Optional[WorkLocationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserWorkLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserWorkLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserWorkLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .work_location_source import WorkLocationSource
        from .work_location_type import WorkLocationType

        from .work_location_source import WorkLocationSource
        from .work_location_type import WorkLocationType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(WorkLocationSource)),
            "workLocationType": lambda n : setattr(self, 'work_location_type', n.get_enum_value(WorkLocationType)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("placeId", self.place_id)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("workLocationType", self.work_location_type)
        writer.write_additional_data_value(self.additional_data)
    

