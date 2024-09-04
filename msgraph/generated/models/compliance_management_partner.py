from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
    from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState
    from .entity import Entity

from .entity import Entity

@dataclass
class ComplianceManagementPartner(Entity):
    """
    Compliance management partner for all platforms
    """
    # User groups which enroll Android devices through partner.
    android_enrollment_assignments: Optional[List[ComplianceManagementPartnerAssignment]] = None
    # Partner onboarded for Android devices.
    android_onboarded: Optional[bool] = None
    # Partner display name
    display_name: Optional[str] = None
    # User groups which enroll ios devices through partner.
    ios_enrollment_assignments: Optional[List[ComplianceManagementPartnerAssignment]] = None
    # Partner onboarded for ios devices.
    ios_onboarded: Optional[bool] = None
    # Timestamp of last heartbeat after admin onboarded to the compliance management partner
    last_heartbeat_date_time: Optional[datetime.datetime] = None
    # User groups which enroll Mac devices through partner.
    mac_os_enrollment_assignments: Optional[List[ComplianceManagementPartnerAssignment]] = None
    # Partner onboarded for Mac devices.
    mac_os_onboarded: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Partner state of this tenant.
    partner_state: Optional[DeviceManagementPartnerTenantState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceManagementPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceManagementPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComplianceManagementPartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
        from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState
        from .entity import Entity

        from .compliance_management_partner_assignment import ComplianceManagementPartnerAssignment
        from .device_management_partner_tenant_state import DeviceManagementPartnerTenantState
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "androidEnrollmentAssignments": lambda n : setattr(self, 'android_enrollment_assignments', n.get_collection_of_object_values(ComplianceManagementPartnerAssignment)),
            "androidOnboarded": lambda n : setattr(self, 'android_onboarded', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "iosEnrollmentAssignments": lambda n : setattr(self, 'ios_enrollment_assignments', n.get_collection_of_object_values(ComplianceManagementPartnerAssignment)),
            "iosOnboarded": lambda n : setattr(self, 'ios_onboarded', n.get_bool_value()),
            "lastHeartbeatDateTime": lambda n : setattr(self, 'last_heartbeat_date_time', n.get_datetime_value()),
            "macOsEnrollmentAssignments": lambda n : setattr(self, 'mac_os_enrollment_assignments', n.get_collection_of_object_values(ComplianceManagementPartnerAssignment)),
            "macOsOnboarded": lambda n : setattr(self, 'mac_os_onboarded', n.get_bool_value()),
            "partnerState": lambda n : setattr(self, 'partner_state', n.get_enum_value(DeviceManagementPartnerTenantState)),
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
        writer.write_collection_of_object_values("androidEnrollmentAssignments", self.android_enrollment_assignments)
        writer.write_bool_value("androidOnboarded", self.android_onboarded)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("iosEnrollmentAssignments", self.ios_enrollment_assignments)
        writer.write_bool_value("iosOnboarded", self.ios_onboarded)
        writer.write_datetime_value("lastHeartbeatDateTime", self.last_heartbeat_date_time)
        writer.write_collection_of_object_values("macOsEnrollmentAssignments", self.mac_os_enrollment_assignments)
        writer.write_bool_value("macOsOnboarded", self.mac_os_onboarded)
        writer.write_enum_value("partnerState", self.partner_state)
    

