from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
shift_availability = lazy_import('msgraph.generated.models.shift_availability')

class ShiftPreferences(change_tracked_entity.ChangeTrackedEntity):
    @property
    def availability(self,) -> Optional[List[shift_availability.ShiftAvailability]]:
        """
        Gets the availability property value. Availability of the user to be scheduled for work and its recurrence pattern.
        Returns: Optional[List[shift_availability.ShiftAvailability]]
        """
        return self._availability
    
    @availability.setter
    def availability(self,value: Optional[List[shift_availability.ShiftAvailability]] = None) -> None:
        """
        Sets the availability property value. Availability of the user to be scheduled for work and its recurrence pattern.
        Args:
            value: Value to set for the availability property.
        """
        self._availability = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ShiftPreferences and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.shiftPreferences"
        # Availability of the user to be scheduled for work and its recurrence pattern.
        self._availability: Optional[List[shift_availability.ShiftAvailability]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ShiftPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ShiftPreferences
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ShiftPreferences()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "availability": lambda n : setattr(self, 'availability', n.get_collection_of_object_values(shift_availability.ShiftAvailability)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("availability", self.availability)
    

