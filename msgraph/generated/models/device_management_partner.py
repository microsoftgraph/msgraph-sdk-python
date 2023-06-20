from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_partner_app_type, device_management_partner_assignment, device_management_partner_tenant_state, entity

from . import entity

@dataclass
class DeviceManagementPartner(entity.Entity):
    """
    Entity which represents a connection to device management partner.
    """
    # Partner display name
    display_name: Optional[str] = None
    # User groups that specifies whether enrollment is through partner.
    groups_requiring_partner_enrollment: Optional[List[device_management_partner_assignment.DeviceManagementPartnerAssignment]] = None
    # Whether device management partner is configured or not
    is_configured: Optional[bool] = None
    # Timestamp of last heartbeat after admin enabled option Connect to Device management Partner
    last_heartbeat_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Partner App Type.
    partner_app_type: Optional[device_management_partner_app_type.DeviceManagementPartnerAppType] = None
    # Partner state of this tenant.
    partner_state: Optional[device_management_partner_tenant_state.DeviceManagementPartnerTenantState] = None
    # Partner Single tenant App id
    single_tenant_app_id: Optional[str] = None
    # DateTime in UTC when PartnerDevices will be marked as NonCompliant
    when_partner_devices_will_be_marked_as_non_compliant_date_time: Optional[datetime] = None
    # DateTime in UTC when PartnerDevices will be removed
    when_partner_devices_will_be_removed_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementPartner
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementPartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_partner_app_type, device_management_partner_assignment, device_management_partner_tenant_state, entity

        from . import device_management_partner_app_type, device_management_partner_assignment, device_management_partner_tenant_state, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupsRequiringPartnerEnrollment": lambda n : setattr(self, 'groups_requiring_partner_enrollment', n.get_collection_of_object_values(device_management_partner_assignment.DeviceManagementPartnerAssignment)),
            "isConfigured": lambda n : setattr(self, 'is_configured', n.get_bool_value()),
            "lastHeartbeatDateTime": lambda n : setattr(self, 'last_heartbeat_date_time', n.get_datetime_value()),
            "partnerAppType": lambda n : setattr(self, 'partner_app_type', n.get_enum_value(device_management_partner_app_type.DeviceManagementPartnerAppType)),
            "partnerState": lambda n : setattr(self, 'partner_state', n.get_enum_value(device_management_partner_tenant_state.DeviceManagementPartnerTenantState)),
            "singleTenantAppId": lambda n : setattr(self, 'single_tenant_app_id', n.get_str_value()),
            "whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime": lambda n : setattr(self, 'when_partner_devices_will_be_marked_as_non_compliant_date_time', n.get_datetime_value()),
            "whenPartnerDevicesWillBeRemovedDateTime": lambda n : setattr(self, 'when_partner_devices_will_be_removed_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("groupsRequiringPartnerEnrollment", self.groups_requiring_partner_enrollment)
        writer.write_bool_value("isConfigured", self.is_configured)
        writer.write_datetime_value("lastHeartbeatDateTime", self.last_heartbeat_date_time)
        writer.write_enum_value("partnerAppType", self.partner_app_type)
        writer.write_enum_value("partnerState", self.partner_state)
        writer.write_str_value("singleTenantAppId", self.single_tenant_app_id)
        writer.write_datetime_value("whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime", self.when_partner_devices_will_be_marked_as_non_compliant_date_time)
        writer.write_datetime_value("whenPartnerDevicesWillBeRemovedDateTime", self.when_partner_devices_will_be_removed_date_time)
    

