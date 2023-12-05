from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, TypeVar, Generic

from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton

from generated.models.entity import Entity

T = TypeVar('T', bound=Entity)


@dataclass
class BaseCollectionPaginationCountResponse(AdditionalDataHolder, BackedModel, Parsable, Generic[T]):
    # Stores the generic type so it can be used in the get_field_deserializers method
    entity: T = field(default=Entity)
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataCount property
    odata_count: Optional[int] = None
    # The OdataNextLink property
    odata_next_link: Optional[str] = None
    value: Optional[List[T]] = None

    
    @classmethod
    def create_from_discriminator_value(cls, parse_node: Optional[ParseNode] = None) -> BaseCollectionPaginationCountResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseCollectionPaginationCountResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return cls()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.count": lambda n : setattr(self, 'odata_count', n.get_int_value()),
            "@odata.nextLink": lambda n : setattr(self, 'odata_next_link', n.get_str_value()),
            "value": lambda n: setattr(self, 'value', n.get_collection_of_object_values(self.entity)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("@odata.count", self.odata_count)
        writer.write_str_value("@odata.nextLink", self.odata_next_link)
        writer.write_collection_of_object_values("value", self.value)
        writer.write_additional_data_value(self.additional_data)
