from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

location = lazy_import('msgraph.generated.models.location')

class LocationConstraintItem(location.Location):
    def __init__(self,) -> None:
        """
        Instantiates a new LocationConstraintItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.locationConstraintItem"
        # If set to true and the specified resource is busy, findMeetingTimes looks for another resource that is free. If set to false and the specified resource is busy, findMeetingTimes returns the resource best ranked in the user's cache without checking if it's free. Default is true.
        self._resolve_availability: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocationConstraintItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocationConstraintItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LocationConstraintItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "resolve_availability": lambda n : setattr(self, 'resolve_availability', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resolve_availability(self,) -> Optional[bool]:
        """
        Gets the resolveAvailability property value. If set to true and the specified resource is busy, findMeetingTimes looks for another resource that is free. If set to false and the specified resource is busy, findMeetingTimes returns the resource best ranked in the user's cache without checking if it's free. Default is true.
        Returns: Optional[bool]
        """
        return self._resolve_availability
    
    @resolve_availability.setter
    def resolve_availability(self,value: Optional[bool] = None) -> None:
        """
        Sets the resolveAvailability property value. If set to true and the specified resource is busy, findMeetingTimes looks for another resource that is free. If set to false and the specified resource is busy, findMeetingTimes returns the resource best ranked in the user's cache without checking if it's free. Default is true.
        Args:
            value: Value to set for the resolveAvailability property.
        """
        self._resolve_availability = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("resolveAvailability", self.resolve_availability)
    

