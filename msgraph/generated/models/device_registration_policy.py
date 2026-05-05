from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_a_d_join_policy import AzureADJoinPolicy
    from .azure_a_d_registration_policy import AzureADRegistrationPolicy
    from .entity import Entity
    from .local_admin_password_settings import LocalAdminPasswordSettings
    from .multi_factor_auth_configuration import MultiFactorAuthConfiguration

from .entity import Entity

@dataclass
class DeviceRegistrationPolicy(Entity, Parsable):
    # Specifies the authorization policy for controlling registration of new devices using Microsoft Entra join within your organization. Required. For more information, see What is a device identity?.
    azure_a_d_join: Optional[AzureADJoinPolicy] = None
    # Specifies the authorization policy for controlling registration of new devices using Microsoft Entra registered within your organization. Required. For more information, see What is a device identity?.
    azure_a_d_registration: Optional[AzureADRegistrationPolicy] = None
    # The description of the device registration policy. Always set to Tenant-wide policy that manages intial provisioning controls using quota restrictions, additional authentication and authorization checks. Read-only.
    description: Optional[str] = None
    # The name of the device registration policy. Always set to Device Registration Policy. Read-only.
    display_name: Optional[str] = None
    # Specifies the setting for Local Admin Password Solution (LAPS) within your organization.
    local_admin_password: Optional[LocalAdminPasswordSettings] = None
    # The multiFactorAuthConfiguration property
    multi_factor_auth_configuration: Optional[MultiFactorAuthConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the maximum number of devices that a user can have within your organization before blocking new device registrations. The default value is set to 50. If this property isn't specified during the policy update operation, it's automatically reset to 0 to indicate that users aren't allowed to join any devices.
    user_device_quota: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceRegistrationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceRegistrationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceRegistrationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .azure_a_d_join_policy import AzureADJoinPolicy
        from .azure_a_d_registration_policy import AzureADRegistrationPolicy
        from .entity import Entity
        from .local_admin_password_settings import LocalAdminPasswordSettings
        from .multi_factor_auth_configuration import MultiFactorAuthConfiguration

        from .azure_a_d_join_policy import AzureADJoinPolicy
        from .azure_a_d_registration_policy import AzureADRegistrationPolicy
        from .entity import Entity
        from .local_admin_password_settings import LocalAdminPasswordSettings
        from .multi_factor_auth_configuration import MultiFactorAuthConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "azureADJoin": lambda n : setattr(self, 'azure_a_d_join', n.get_object_value(AzureADJoinPolicy)),
            "azureADRegistration": lambda n : setattr(self, 'azure_a_d_registration', n.get_object_value(AzureADRegistrationPolicy)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "localAdminPassword": lambda n : setattr(self, 'local_admin_password', n.get_object_value(LocalAdminPasswordSettings)),
            "multiFactorAuthConfiguration": lambda n : setattr(self, 'multi_factor_auth_configuration', n.get_enum_value(MultiFactorAuthConfiguration)),
            "userDeviceQuota": lambda n : setattr(self, 'user_device_quota', n.get_int_value()),
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
        writer.write_object_value("azureADJoin", self.azure_a_d_join)
        writer.write_object_value("azureADRegistration", self.azure_a_d_registration)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("localAdminPassword", self.local_admin_password)
        writer.write_enum_value("multiFactorAuthConfiguration", self.multi_factor_auth_configuration)
        writer.write_int_value("userDeviceQuota", self.user_device_quota)
    

