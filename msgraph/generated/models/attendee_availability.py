from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attendee_base import AttendeeBase
    from .free_busy_status import FreeBusyStatus

@dataclass
class AttendeeAvailability(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The email address and type of attendee - whether it's a person or a resource, and whether required or optional if it's a person.
    attendee: Optional[AttendeeBase] = None
    # The availability status of the attendee. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
    availability: Optional[FreeBusyStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttendeeAvailability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttendeeAvailability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttendeeAvailability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attendee_base import AttendeeBase
        from .free_busy_status import FreeBusyStatus

        from .attendee_base import AttendeeBase
        from .free_busy_status import FreeBusyStatus

        fields: dict[str, Callable[[Any], None]] = {
            "attendee": lambda n : setattr(self, 'attendee', n.get_object_value(AttendeeBase)),
            "availability": lambda n : setattr(self, 'availability', n.get_enum_value(FreeBusyStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("attendee", self.attendee)
        writer.write_enum_value("availability", self.availability)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

