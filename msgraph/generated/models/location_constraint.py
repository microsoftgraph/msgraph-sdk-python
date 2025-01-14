from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location_constraint_item import LocationConstraintItem

@dataclass
class LocationConstraint(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The client requests the service to include in the response a meeting location for the meeting. If this is true and all the resources are busy, findMeetingTimes won't return any meeting time suggestions. If this is false and all the resources are busy, findMeetingTimes would still look for meeting times without locations.
    is_required: Optional[bool] = None
    # Constraint information for one or more locations that the client requests for the meeting.
    locations: Optional[list[LocationConstraintItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The client requests the service to suggest one or more meeting locations.
    suggest_location: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocationConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocationConstraint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LocationConstraint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .location_constraint_item import LocationConstraintItem

        from .location_constraint_item import LocationConstraintItem

        fields: dict[str, Callable[[Any], None]] = {
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(LocationConstraintItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "suggestLocation": lambda n : setattr(self, 'suggest_location', n.get_bool_value()),
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
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("suggestLocation", self.suggest_location)
        writer.write_additional_data_value(self.additional_data)
    

