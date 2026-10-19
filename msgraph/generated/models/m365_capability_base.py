from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_calendar_availability_basic import CrossTenantCalendarAvailabilityBasic
    from .cross_tenant_calendar_availability_limited_details import CrossTenantCalendarAvailabilityLimitedDetails
    from .cross_tenant_calendar_sharing_free_busy_detail import CrossTenantCalendarSharingFreeBusyDetail
    from .cross_tenant_calendar_sharing_free_busy_reviewer import CrossTenantCalendarSharingFreeBusyReviewer
    from .cross_tenant_calendar_sharing_free_busy_simple import CrossTenantCalendarSharingFreeBusySimple
    from .cross_tenant_mail_tips_all import CrossTenantMailTipsAll
    from .cross_tenant_mail_tips_limited import CrossTenantMailTipsLimited
    from .cross_tenant_migration import CrossTenantMigration
    from .cross_tenant_open_profile_card import CrossTenantOpenProfileCard
    from .cross_tenant_places_desk_booking import CrossTenantPlacesDeskBooking
    from .cross_tenant_places_room_booking import CrossTenantPlacesRoomBooking
    from .entity import Entity
    from .m365_capability_inbound_access import M365CapabilityInboundAccess

from .entity import Entity

@dataclass
class M365CapabilityBase(Entity, Parsable):
    # The inbound access settings for the capability.
    inbound_access: Optional[M365CapabilityInboundAccess] = None
    # The automatically updated last modified timestamp for the capability. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The name or identifier of the capability. Key.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> M365CapabilityBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: M365CapabilityBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantCalendarAvailabilityBasic".casefold():
            from .cross_tenant_calendar_availability_basic import CrossTenantCalendarAvailabilityBasic

            return CrossTenantCalendarAvailabilityBasic()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantCalendarAvailabilityLimitedDetails".casefold():
            from .cross_tenant_calendar_availability_limited_details import CrossTenantCalendarAvailabilityLimitedDetails

            return CrossTenantCalendarAvailabilityLimitedDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantCalendarSharingFreeBusyDetail".casefold():
            from .cross_tenant_calendar_sharing_free_busy_detail import CrossTenantCalendarSharingFreeBusyDetail

            return CrossTenantCalendarSharingFreeBusyDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantCalendarSharingFreeBusyReviewer".casefold():
            from .cross_tenant_calendar_sharing_free_busy_reviewer import CrossTenantCalendarSharingFreeBusyReviewer

            return CrossTenantCalendarSharingFreeBusyReviewer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantCalendarSharingFreeBusySimple".casefold():
            from .cross_tenant_calendar_sharing_free_busy_simple import CrossTenantCalendarSharingFreeBusySimple

            return CrossTenantCalendarSharingFreeBusySimple()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantMailTipsAll".casefold():
            from .cross_tenant_mail_tips_all import CrossTenantMailTipsAll

            return CrossTenantMailTipsAll()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantMailTipsLimited".casefold():
            from .cross_tenant_mail_tips_limited import CrossTenantMailTipsLimited

            return CrossTenantMailTipsLimited()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantMigration".casefold():
            from .cross_tenant_migration import CrossTenantMigration

            return CrossTenantMigration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantOpenProfileCard".casefold():
            from .cross_tenant_open_profile_card import CrossTenantOpenProfileCard

            return CrossTenantOpenProfileCard()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantPlacesDeskBooking".casefold():
            from .cross_tenant_places_desk_booking import CrossTenantPlacesDeskBooking

            return CrossTenantPlacesDeskBooking()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantPlacesRoomBooking".casefold():
            from .cross_tenant_places_room_booking import CrossTenantPlacesRoomBooking

            return CrossTenantPlacesRoomBooking()
        return M365CapabilityBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_calendar_availability_basic import CrossTenantCalendarAvailabilityBasic
        from .cross_tenant_calendar_availability_limited_details import CrossTenantCalendarAvailabilityLimitedDetails
        from .cross_tenant_calendar_sharing_free_busy_detail import CrossTenantCalendarSharingFreeBusyDetail
        from .cross_tenant_calendar_sharing_free_busy_reviewer import CrossTenantCalendarSharingFreeBusyReviewer
        from .cross_tenant_calendar_sharing_free_busy_simple import CrossTenantCalendarSharingFreeBusySimple
        from .cross_tenant_mail_tips_all import CrossTenantMailTipsAll
        from .cross_tenant_mail_tips_limited import CrossTenantMailTipsLimited
        from .cross_tenant_migration import CrossTenantMigration
        from .cross_tenant_open_profile_card import CrossTenantOpenProfileCard
        from .cross_tenant_places_desk_booking import CrossTenantPlacesDeskBooking
        from .cross_tenant_places_room_booking import CrossTenantPlacesRoomBooking
        from .entity import Entity
        from .m365_capability_inbound_access import M365CapabilityInboundAccess

        from .cross_tenant_calendar_availability_basic import CrossTenantCalendarAvailabilityBasic
        from .cross_tenant_calendar_availability_limited_details import CrossTenantCalendarAvailabilityLimitedDetails
        from .cross_tenant_calendar_sharing_free_busy_detail import CrossTenantCalendarSharingFreeBusyDetail
        from .cross_tenant_calendar_sharing_free_busy_reviewer import CrossTenantCalendarSharingFreeBusyReviewer
        from .cross_tenant_calendar_sharing_free_busy_simple import CrossTenantCalendarSharingFreeBusySimple
        from .cross_tenant_mail_tips_all import CrossTenantMailTipsAll
        from .cross_tenant_mail_tips_limited import CrossTenantMailTipsLimited
        from .cross_tenant_migration import CrossTenantMigration
        from .cross_tenant_open_profile_card import CrossTenantOpenProfileCard
        from .cross_tenant_places_desk_booking import CrossTenantPlacesDeskBooking
        from .cross_tenant_places_room_booking import CrossTenantPlacesRoomBooking
        from .entity import Entity
        from .m365_capability_inbound_access import M365CapabilityInboundAccess

        fields: dict[str, Callable[[Any], None]] = {
            "inboundAccess": lambda n : setattr(self, 'inbound_access', n.get_object_value(M365CapabilityInboundAccess)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_object_value("inboundAccess", self.inbound_access)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
    

