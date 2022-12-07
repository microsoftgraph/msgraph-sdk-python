from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_management_partner_assignment = lazy_import('msgraph.generated.models.compliance_management_partner_assignment')
device_management_partner_tenant_state = lazy_import('msgraph.generated.models.device_management_partner_tenant_state')
entity = lazy_import('msgraph.generated.models.entity')

class ComplianceManagementPartner(entity.Entity):
    """
    Compliance management partner for all platforms
    """
    @property
    def android_enrollment_assignments(self,) -> Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]]:
        """
        Gets the androidEnrollmentAssignments property value. User groups which enroll Android devices through partner.
        Returns: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]]
        """
        return self._android_enrollment_assignments
    
    @android_enrollment_assignments.setter
    def android_enrollment_assignments(self,value: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]] = None) -> None:
        """
        Sets the androidEnrollmentAssignments property value. User groups which enroll Android devices through partner.
        Args:
            value: Value to set for the androidEnrollmentAssignments property.
        """
        self._android_enrollment_assignments = value
    
    @property
    def android_onboarded(self,) -> Optional[bool]:
        """
        Gets the androidOnboarded property value. Partner onboarded for Android devices.
        Returns: Optional[bool]
        """
        return self._android_onboarded
    
    @android_onboarded.setter
    def android_onboarded(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidOnboarded property value. Partner onboarded for Android devices.
        Args:
            value: Value to set for the androidOnboarded property.
        """
        self._android_onboarded = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new complianceManagementPartner and sets the default values.
        """
        super().__init__()
        # User groups which enroll Android devices through partner.
        self._android_enrollment_assignments: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]] = None
        # Partner onboarded for Android devices.
        self._android_onboarded: Optional[bool] = None
        # Partner display name
        self._display_name: Optional[str] = None
        # User groups which enroll ios devices through partner.
        self._ios_enrollment_assignments: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]] = None
        # Partner onboarded for ios devices.
        self._ios_onboarded: Optional[bool] = None
        # Timestamp of last heartbeat after admin onboarded to the compliance management partner
        self._last_heartbeat_date_time: Optional[datetime] = None
        # User groups which enroll Mac devices through partner.
        self._mac_os_enrollment_assignments: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]] = None
        # Partner onboarded for Mac devices.
        self._mac_os_onboarded: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Partner state of this tenant.
        self._partner_state: Optional[device_management_partner_tenant_state.DeviceManagementPartnerTenantState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComplianceManagementPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceManagementPartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ComplianceManagementPartner()
    
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
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_enrollment_assignments": lambda n : setattr(self, 'android_enrollment_assignments', n.get_collection_of_object_values(compliance_management_partner_assignment.ComplianceManagementPartnerAssignment)),
            "android_onboarded": lambda n : setattr(self, 'android_onboarded', n.get_bool_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ios_enrollment_assignments": lambda n : setattr(self, 'ios_enrollment_assignments', n.get_collection_of_object_values(compliance_management_partner_assignment.ComplianceManagementPartnerAssignment)),
            "ios_onboarded": lambda n : setattr(self, 'ios_onboarded', n.get_bool_value()),
            "last_heartbeat_date_time": lambda n : setattr(self, 'last_heartbeat_date_time', n.get_datetime_value()),
            "mac_os_enrollment_assignments": lambda n : setattr(self, 'mac_os_enrollment_assignments', n.get_collection_of_object_values(compliance_management_partner_assignment.ComplianceManagementPartnerAssignment)),
            "mac_os_onboarded": lambda n : setattr(self, 'mac_os_onboarded', n.get_bool_value()),
            "partner_state": lambda n : setattr(self, 'partner_state', n.get_enum_value(device_management_partner_tenant_state.DeviceManagementPartnerTenantState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ios_enrollment_assignments(self,) -> Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]]:
        """
        Gets the iosEnrollmentAssignments property value. User groups which enroll ios devices through partner.
        Returns: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]]
        """
        return self._ios_enrollment_assignments
    
    @ios_enrollment_assignments.setter
    def ios_enrollment_assignments(self,value: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]] = None) -> None:
        """
        Sets the iosEnrollmentAssignments property value. User groups which enroll ios devices through partner.
        Args:
            value: Value to set for the iosEnrollmentAssignments property.
        """
        self._ios_enrollment_assignments = value
    
    @property
    def ios_onboarded(self,) -> Optional[bool]:
        """
        Gets the iosOnboarded property value. Partner onboarded for ios devices.
        Returns: Optional[bool]
        """
        return self._ios_onboarded
    
    @ios_onboarded.setter
    def ios_onboarded(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosOnboarded property value. Partner onboarded for ios devices.
        Args:
            value: Value to set for the iosOnboarded property.
        """
        self._ios_onboarded = value
    
    @property
    def last_heartbeat_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastHeartbeatDateTime property value. Timestamp of last heartbeat after admin onboarded to the compliance management partner
        Returns: Optional[datetime]
        """
        return self._last_heartbeat_date_time
    
    @last_heartbeat_date_time.setter
    def last_heartbeat_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastHeartbeatDateTime property value. Timestamp of last heartbeat after admin onboarded to the compliance management partner
        Args:
            value: Value to set for the lastHeartbeatDateTime property.
        """
        self._last_heartbeat_date_time = value
    
    @property
    def mac_os_enrollment_assignments(self,) -> Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]]:
        """
        Gets the macOsEnrollmentAssignments property value. User groups which enroll Mac devices through partner.
        Returns: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]]
        """
        return self._mac_os_enrollment_assignments
    
    @mac_os_enrollment_assignments.setter
    def mac_os_enrollment_assignments(self,value: Optional[List[compliance_management_partner_assignment.ComplianceManagementPartnerAssignment]] = None) -> None:
        """
        Sets the macOsEnrollmentAssignments property value. User groups which enroll Mac devices through partner.
        Args:
            value: Value to set for the macOsEnrollmentAssignments property.
        """
        self._mac_os_enrollment_assignments = value
    
    @property
    def mac_os_onboarded(self,) -> Optional[bool]:
        """
        Gets the macOsOnboarded property value. Partner onboarded for Mac devices.
        Returns: Optional[bool]
        """
        return self._mac_os_onboarded
    
    @mac_os_onboarded.setter
    def mac_os_onboarded(self,value: Optional[bool] = None) -> None:
        """
        Sets the macOsOnboarded property value. Partner onboarded for Mac devices.
        Args:
            value: Value to set for the macOsOnboarded property.
        """
        self._mac_os_onboarded = value
    
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
            value: Value to set for the partnerState property.
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
        writer.write_collection_of_object_values("androidEnrollmentAssignments", self.android_enrollment_assignments)
        writer.write_bool_value("androidOnboarded", self.android_onboarded)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("iosEnrollmentAssignments", self.ios_enrollment_assignments)
        writer.write_bool_value("iosOnboarded", self.ios_onboarded)
        writer.write_datetime_value("lastHeartbeatDateTime", self.last_heartbeat_date_time)
        writer.write_collection_of_object_values("macOsEnrollmentAssignments", self.mac_os_enrollment_assignments)
        writer.write_bool_value("macOsOnboarded", self.mac_os_onboarded)
        writer.write_enum_value("partnerState", self.partner_state)
    

