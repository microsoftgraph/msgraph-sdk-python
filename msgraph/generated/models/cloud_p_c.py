from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_provisioning_type import CloudPcProvisioningType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPC(Entity, Parsable):
    # The Microsoft Entra device ID for the Cloud PC, also known as the Azure Active Directory (Azure AD) device ID, that consists of 32 characters in a GUID format. Generated on a VM joined to Microsoft Entra ID. Read-only.
    aad_device_id: Optional[str] = None
    # The display name for the Cloud PC. Maximum length is 64 characters. Read-only. You can use the cloudPC: rename API to modify the Cloud PC name.
    display_name: Optional[str] = None
    # The date and time when the grace period ends and reprovisioning or deprovisioning happen. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    grace_period_end_date_time: Optional[datetime.datetime] = None
    # The name of the operating system image used for the Cloud PC. Maximum length is 50 characters. Only letters (A-Z, a-z), numbers (0-9), and special characters (-,,.) are allowed for this property. The property value can't begin or end with an underscore. Read-only.
    image_display_name: Optional[str] = None
    # The last modified date and time of the Cloud PC. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The Intune enrolled device ID for the Cloud PC that consists of 32 characters in a GUID format. The managedDeviceId property of Windows 365 Business Cloud PCs is always null as Windows 365 Business Cloud PCs aren't Intune-enrolled automatically by Windows 365. Read-only.
    managed_device_id: Optional[str] = None
    # The Intune enrolled device name for the Cloud PC. The managedDeviceName property of Windows 365 Business Cloud PCs is always null as Windows 365 Business Cloud PCs aren't Intune-enrolled automatically by Windows 365. Read-only.
    managed_device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The on-premises connection that applied during the provisioning of Cloud PCs. Read-only.
    on_premises_connection_name: Optional[str] = None
    # The provisioning policy ID for the Cloud PC that consists of 32 characters in a GUID format. A policy defines the type of Cloud PC the user wants to create. Read-only.
    provisioning_policy_id: Optional[str] = None
    # The provisioning policy that applied during the provisioning of Cloud PCs. Maximum length is 120 characters. Read-only.
    provisioning_policy_name: Optional[str] = None
    # The type of licenses to be used when provisioning Cloud PCs using this policy. The possible values are: dedicated, shared, unknownFutureValue. The default value is dedicated.
    provisioning_type: Optional[CloudPcProvisioningType] = None
    # The service plan ID for the Cloud PC that consists of 32 characters in a GUID format. For more information about service plans, see Product names and service plan identifiers for licensing. Read-only.
    service_plan_id: Optional[str] = None
    # The service plan name for the customer-facing Cloud PC entity. Read-only.
    service_plan_name: Optional[str] = None
    # The user principal name (UPN) of the user assigned to the Cloud PC. Maximum length is 113 characters. For more information on username policies, see Password policies and account restrictions in Microsoft Entra ID. Read-only.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPC:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPC
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPC()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .entity import Entity

        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "aadDeviceId": lambda n : setattr(self, 'aad_device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "gracePeriodEndDateTime": lambda n : setattr(self, 'grace_period_end_date_time', n.get_datetime_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "onPremisesConnectionName": lambda n : setattr(self, 'on_premises_connection_name', n.get_str_value()),
            "provisioningPolicyId": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "provisioningPolicyName": lambda n : setattr(self, 'provisioning_policy_name', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(CloudPcProvisioningType)),
            "servicePlanId": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
            "servicePlanName": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("aadDeviceId", self.aad_device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("gracePeriodEndDateTime", self.grace_period_end_date_time)
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("onPremisesConnectionName", self.on_premises_connection_name)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_str_value("provisioningPolicyName", self.provisioning_policy_name)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_str_value("servicePlanId", self.service_plan_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

