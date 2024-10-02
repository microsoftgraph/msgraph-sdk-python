from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .free_busy_error import FreeBusyError
    from .schedule_item import ScheduleItem
    from .working_hours import WorkingHours

@dataclass
class ScheduleInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents a merged view of availability of all the items in scheduleItems. The view consists of time slots. Availability during each time slot is indicated with: 0= free or working elswhere, 1= tentative, 2= busy, 3= out of office.Note: Working elsewhere is set to 0 instead of 4 for backward compatibility. For details, see the Q&A and Exchange 2007 and Exchange 2010 do not use the WorkingElsewhere value.
    availability_view: Optional[str] = None
    # Error information from attempting to get the availability of the user, distribution list, or resource.
    error: Optional[FreeBusyError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An SMTP address of the user, distribution list, or resource, identifying an instance of scheduleInformation.
    schedule_id: Optional[str] = None
    # Contains the items that describe the availability of the user or resource.
    schedule_items: Optional[List[ScheduleItem]] = None
    # The days of the week and hours in a specific time zone that the user works. These are set as part of the user's mailboxSettings.
    working_hours: Optional[WorkingHours] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduleInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ScheduleInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .free_busy_error import FreeBusyError
        from .schedule_item import ScheduleItem
        from .working_hours import WorkingHours

        from .free_busy_error import FreeBusyError
        from .schedule_item import ScheduleItem
        from .working_hours import WorkingHours

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityView": lambda n : setattr(self, 'availability_view', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(FreeBusyError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduleId": lambda n : setattr(self, 'schedule_id', n.get_str_value()),
            "scheduleItems": lambda n : setattr(self, 'schedule_items', n.get_collection_of_object_values(ScheduleItem)),
            "workingHours": lambda n : setattr(self, 'working_hours', n.get_object_value(WorkingHours)),
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
        writer.write_str_value("availabilityView", self.availability_view)
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("scheduleId", self.schedule_id)
        writer.write_collection_of_object_values("scheduleItems", self.schedule_items)
        writer.write_object_value("workingHours", self.working_hours)
        writer.write_additional_data_value(self.additional_data)
    

