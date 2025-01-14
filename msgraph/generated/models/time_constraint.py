from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_domain import ActivityDomain
    from .time_slot import TimeSlot

@dataclass
class TimeConstraint(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The nature of the activity, optional. The possible values are: work, personal, unrestricted, or unknown.
    activity_domain: Optional[ActivityDomain] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The timeSlots property
    time_slots: Optional[list[TimeSlot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeConstraint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeConstraint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_domain import ActivityDomain
        from .time_slot import TimeSlot

        from .activity_domain import ActivityDomain
        from .time_slot import TimeSlot

        fields: dict[str, Callable[[Any], None]] = {
            "activityDomain": lambda n : setattr(self, 'activity_domain', n.get_enum_value(ActivityDomain)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeSlots": lambda n : setattr(self, 'time_slots', n.get_collection_of_object_values(TimeSlot)),
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
        writer.write_enum_value("activityDomain", self.activity_domain)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("timeSlots", self.time_slots)
        writer.write_additional_data_value(self.additional_data)
    

