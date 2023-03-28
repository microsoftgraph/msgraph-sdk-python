from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_partner_app_type, device_management_partner_assignment, device_management_partner_tenant_state, entity

from . import entity

class DeviceManagementPartner(entity.Entity):
    """
    Entity which represents a connection to device management partner.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementPartner and sets the default values.
        """
        super().__init__()
        # Partner display name
        self._display_name: Optional[str] = None
        # User groups that specifies whether enrollment is through partner.
        self._groups_requiring_partner_enrollment: Optional[List[device_management_partner_assignment.DeviceManagementPartnerAssignment]] = None
        # Whether device management partner is configured or not
        self._is_configured: Optional[bool] = None
        # Timestamp of last heartbeat after admin enabled option Connect to Device management Partner
        self._last_heartbeat_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Partner App Type.
        self._partner_app_type: Optional[device_management_partner_app_type.DeviceManagementPartnerAppType] = None
        # Partner state of this tenant.
        self._partner_state: Optional[device_management_partner_tenant_state.DeviceManagementPartnerTenantState] = None
        # Partner Single tenant App id
        self._single_tenant_app_id: Optional[str] = None
        # DateTime in UTC when PartnerDevices will be marked as NonCompliant
        self._when_partner_devices_will_be_marked_as_non_compliant_date_time: Optional[datetime] = None
        # DateTime in UTC when PartnerDevices will be removed
        self._when_partner_devices_will_be_removed_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementPartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementPartner()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Partner display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Partner display name
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def groups_requiring_partner_enrollment(self,) -> Optional[List[device_management_partner_assignment.DeviceManagementPartnerAssignment]]:
        """
        Gets the groupsRequiringPartnerEnrollment property value. User groups that specifies whether enrollment is through partner.
        Returns: Optional[List[device_management_partner_assignment.DeviceManagementPartnerAssignment]]
        """
        return self._groups_requiring_partner_enrollment
    
    @groups_requiring_partner_enrollment.setter
    def groups_requiring_partner_enrollment(self,value: Optional[List[device_management_partner_assignment.DeviceManagementPartnerAssignment]] = None) -> None:
        """
        Sets the groupsRequiringPartnerEnrollment property value. User groups that specifies whether enrollment is through partner.
        Args:
            value: Value to set for the groups_requiring_partner_enrollment property.
        """
        self._groups_requiring_partner_enrollment = value
    
    @property
    def is_configured(self,) -> Optional[bool]:
        """
        Gets the isConfigured property value. Whether device management partner is configured or not
        Returns: Optional[bool]
        """
        return self._is_configured
    
    @is_configured.setter
    def is_configured(self,value: Optional[bool] = None) -> None:
        """
        Sets the isConfigured property value. Whether device management partner is configured or not
        Args:
            value: Value to set for the is_configured property.
        """
        self._is_configured = value
    
    @property
    def last_heartbeat_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastHeartbeatDateTime property value. Timestamp of last heartbeat after admin enabled option Connect to Device management Partner
        Returns: Optional[datetime]
        """
        return self._last_heartbeat_date_time
    
    @last_heartbeat_date_time.setter
    def last_heartbeat_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastHeartbeatDateTime property value. Timestamp of last heartbeat after admin enabled option Connect to Device management Partner
        Args:
            value: Value to set for the last_heartbeat_date_time property.
        """
        self._last_heartbeat_date_time = value
    
    @property
    def partner_app_type(self,) -> Optional[device_management_partner_app_type.DeviceManagementPartnerAppType]:
        """
        Gets the partnerAppType property value. Partner App Type.
        Returns: Optional[device_management_partner_app_type.DeviceManagementPartnerAppType]
        """
        return self._partner_app_type
    
    @partner_app_type.setter
    def partner_app_type(self,value: Optional[device_management_partner_app_type.DeviceManagementPartnerAppType] = None) -> None:
        """
        Sets the partnerAppType property value. Partner App Type.
        Args:
            value: Value to set for the partner_app_type property.
        """
        self._partner_app_type = value
    
    @property
    def partner_state(self,) -> Optional[device_management_partner_tenant_state.DeviceManagementPartnerTenantState]:
        """
        Gets the partnerState property value. Partner state of this tenant.
        Returns: Optional[device_management_partner_tenant_state.DeviceManagementPartnerTenantState]
        """
        return self._partner_state
    
    @partner_state.setter
    def partner_state(self,value: Optional[device_management_partner_tenant_state.DeviceManagementPartnerTenantState] = None) -> None:
        """
        Sets the partnerState property value. Partner state of this tenant.
        Args:
            value: Value to set for the partner_state property.
        """
        self._partner_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def single_tenant_app_id(self,) -> Optional[str]:
        """
        Gets the singleTenantAppId property value. Partner Single tenant App id
        Returns: Optional[str]
        """
        return self._single_tenant_app_id
    
    @single_tenant_app_id.setter
    def single_tenant_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the singleTenantAppId property value. Partner Single tenant App id
        Args:
            value: Value to set for the single_tenant_app_id property.
        """
        self._single_tenant_app_id = value
    
    @property
    def when_partner_devices_will_be_marked_as_non_compliant_date_time(self,) -> Optional[datetime]:
        """
        Gets the whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime property value. DateTime in UTC when PartnerDevices will be marked as NonCompliant
        Returns: Optional[datetime]
        """
        return self._when_partner_devices_will_be_marked_as_non_compliant_date_time
    
    @when_partner_devices_will_be_marked_as_non_compliant_date_time.setter
    def when_partner_devices_will_be_marked_as_non_compliant_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime property value. DateTime in UTC when PartnerDevices will be marked as NonCompliant
        Args:
            value: Value to set for the when_partner_devices_will_be_marked_as_non_compliant_date_time property.
        """
        self._when_partner_devices_will_be_marked_as_non_compliant_date_time = value
    
    @property
    def when_partner_devices_will_be_removed_date_time(self,) -> Optional[datetime]:
        """
        Gets the whenPartnerDevicesWillBeRemovedDateTime property value. DateTime in UTC when PartnerDevices will be removed
        Returns: Optional[datetime]
        """
        return self._when_partner_devices_will_be_removed_date_time
    
    @when_partner_devices_will_be_removed_date_time.setter
    def when_partner_devices_will_be_removed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the whenPartnerDevicesWillBeRemovedDateTime property value. DateTime in UTC when PartnerDevices will be removed
        Args:
            value: Value to set for the when_partner_devices_will_be_removed_date_time property.
        """
        self._when_partner_devices_will_be_removed_date_time = value
    

