from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.date_time_time_zone import DateTimeTimeZone

@dataclass
class GetStaffAvailabilityPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The staffIds property
    staff_ids: Optional[List[str]] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetStaffAvailabilityPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetStaffAvailabilityPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetStaffAvailabilityPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.date_time_time_zone import DateTimeTimeZone

        from .....models.date_time_time_zone import DateTimeTimeZone

        fields: Dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "staffIds": lambda n : setattr(self, 'staff_ids', n.get_collection_of_primitive_values(str)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
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
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_primitive_values("staffIds", self.staff_ids)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

