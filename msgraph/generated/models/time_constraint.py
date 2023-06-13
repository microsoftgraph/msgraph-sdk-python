from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_domain, time_slot

@dataclass
class TimeConstraint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The nature of the activity, optional. The possible values are: work, personal, unrestricted, or unknown.
    activity_domain: Optional[activity_domain.ActivityDomain] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The timeSlots property
    time_slots: Optional[List[time_slot.TimeSlot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_domain, time_slot

        fields: Dict[str, Callable[[Any], None]] = {
            "activityDomain": lambda n : setattr(self, 'activity_domain', n.get_enum_value(activity_domain.ActivityDomain)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeSlots": lambda n : setattr(self, 'time_slots', n.get_collection_of_object_values(time_slot.TimeSlot)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("activityDomain", self.activity_domain)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("timeSlots", self.time_slots)
        writer.write_additional_data_value(self.additional_data)
    

