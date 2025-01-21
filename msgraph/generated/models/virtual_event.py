from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .communications_identity_set import CommunicationsIdentitySet
    from .date_time_time_zone import DateTimeTimeZone
    from .entity import Entity
    from .item_body import ItemBody
    from .virtual_event_external_information import VirtualEventExternalInformation
    from .virtual_event_presenter import VirtualEventPresenter
    from .virtual_event_session import VirtualEventSession
    from .virtual_event_settings import VirtualEventSettings
    from .virtual_event_status import VirtualEventStatus
    from .virtual_event_townhall import VirtualEventTownhall
    from .virtual_event_webinar import VirtualEventWebinar

from .entity import Entity

@dataclass
class VirtualEvent(Entity, Parsable):
    # The identity information for the creator of the virtual event. Inherited from virtualEvent.
    created_by: Optional[CommunicationsIdentitySet] = None
    # A description of the virtual event.
    description: Optional[ItemBody] = None
    # The display name of the virtual event.
    display_name: Optional[str] = None
    # The end time of the virtual event. The timeZone property can be set to any of the time zones currently supported by Windows. For details on how to get all available time zones using PowerShell, see Get-TimeZone.
    end_date_time: Optional[DateTimeTimeZone] = None
    # The external information of a virtual event. Returned only for event organizers or coorganizers; otherwise, null.
    external_event_information: Optional[list[VirtualEventExternalInformation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The virtual event presenters.
    presenters: Optional[list[VirtualEventPresenter]] = None
    # The sessions for the virtual event.
    sessions: Optional[list[VirtualEventSession]] = None
    # The virtual event settings.
    settings: Optional[VirtualEventSettings] = None
    # Start time of the virtual event. The timeZone property can be set to any of the time zones currently supported by Windows. For details on how to get all available time zones using PowerShell, see Get-TimeZone.
    start_date_time: Optional[DateTimeTimeZone] = None
    # The status of the virtual event. The possible values are: draft, published, canceled, and unknownFutureValue.
    status: Optional[VirtualEventStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventTownhall".casefold():
            from .virtual_event_townhall import VirtualEventTownhall

            return VirtualEventTownhall()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinar".casefold():
            from .virtual_event_webinar import VirtualEventWebinar

            return VirtualEventWebinar()
        return VirtualEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .communications_identity_set import CommunicationsIdentitySet
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .item_body import ItemBody
        from .virtual_event_external_information import VirtualEventExternalInformation
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_settings import VirtualEventSettings
        from .virtual_event_status import VirtualEventStatus
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar

        from .communications_identity_set import CommunicationsIdentitySet
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .item_body import ItemBody
        from .virtual_event_external_information import VirtualEventExternalInformation
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_settings import VirtualEventSettings
        from .virtual_event_status import VirtualEventStatus
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(CommunicationsIdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_object_value(ItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "externalEventInformation": lambda n : setattr(self, 'external_event_information', n.get_collection_of_object_values(VirtualEventExternalInformation)),
            "presenters": lambda n : setattr(self, 'presenters', n.get_collection_of_object_values(VirtualEventPresenter)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(VirtualEventSession)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(VirtualEventSettings)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(VirtualEventStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("externalEventInformation", self.external_event_information)
        writer.write_collection_of_object_values("presenters", self.presenters)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    

