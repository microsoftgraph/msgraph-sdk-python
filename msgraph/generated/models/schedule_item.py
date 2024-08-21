from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .free_busy_status import FreeBusyStatus

@dataclass
class ScheduleItem(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The date, time, and time zone that the corresponding event ends.
    end: Optional[DateTimeTimeZone] = None
    # The sensitivity of the corresponding event. True if the event is marked private, false otherwise. Optional.
    is_private: Optional[bool] = None
    # The location where the corresponding event is held or attended from. Optional.
    location: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date, time, and time zone that the corresponding event starts.
    start: Optional[DateTimeTimeZone] = None
    # The availability status of the user or resource during the corresponding event. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
    status: Optional[FreeBusyStatus] = None
    # The corresponding event's subject line. Optional.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduleItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScheduleItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .free_busy_status import FreeBusyStatus

        from .date_time_time_zone import DateTimeTimeZone
        from .free_busy_status import FreeBusyStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "end": lambda n : setattr(self, 'end', n.get_object_value(DateTimeTimeZone)),
            "isPrivate": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FreeBusyStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_object_value("end", self.end)
        writer.write_bool_value("isPrivate", self.is_private)
        writer.write_str_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("start", self.start)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    

