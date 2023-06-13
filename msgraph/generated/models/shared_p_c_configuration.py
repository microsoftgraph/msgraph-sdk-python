from __future__ import annotations
from dataclasses import dataclass, field
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, shared_p_c_account_manager_policy, shared_p_c_allowed_account_type

from . import device_configuration

@dataclass
class SharedPCConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.sharedPCConfiguration"
    # Specifies how accounts are managed on a shared PC. Only applies when disableAccountManager is false.
    account_manager_policy: Optional[shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy] = None
    # Specifies whether local storage is allowed on a shared PC.
    allow_local_storage: Optional[bool] = None
    # Type of accounts that are allowed to share the PC.
    allowed_accounts: Optional[shared_p_c_allowed_account_type.SharedPCAllowedAccountType] = None
    # Disables the account manager for shared PC mode.
    disable_account_manager: Optional[bool] = None
    # Specifies whether the default shared PC education environment policies should be disabled. For Windows 10 RS2 and later, this policy will be applied without setting Enabled to true.
    disable_edu_policies: Optional[bool] = None
    # Specifies whether the default shared PC power policies should be disabled.
    disable_power_policies: Optional[bool] = None
    # Disables the requirement to sign in whenever the device wakes up from sleep mode.
    disable_sign_in_on_resume: Optional[bool] = None
    # Enables shared PC mode and applies the shared pc policies.
    enabled: Optional[bool] = None
    # Specifies the time in seconds that a device must sit idle before the PC goes to sleep. Setting this value to 0 prevents the sleep timeout from occurring.
    idle_time_before_sleep_in_seconds: Optional[int] = None
    # Specifies the display text for the account shown on the sign-in screen which launches the app specified by SetKioskAppUserModelId. Only applies when KioskAppUserModelId is set.
    kiosk_app_display_name: Optional[str] = None
    # Specifies the application user model ID of the app to use with assigned access.
    kiosk_app_user_model_id: Optional[str] = None
    # Specifies the daily start time of maintenance hour.
    maintenance_start_time: Optional[time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedPCConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedPCConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedPCConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, shared_p_c_account_manager_policy, shared_p_c_allowed_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accountManagerPolicy": lambda n : setattr(self, 'account_manager_policy', n.get_object_value(shared_p_c_account_manager_policy.SharedPCAccountManagerPolicy)),
            "allowedAccounts": lambda n : setattr(self, 'allowed_accounts', n.get_enum_value(shared_p_c_allowed_account_type.SharedPCAllowedAccountType)),
            "allowLocalStorage": lambda n : setattr(self, 'allow_local_storage', n.get_bool_value()),
            "disableAccountManager": lambda n : setattr(self, 'disable_account_manager', n.get_bool_value()),
            "disableEduPolicies": lambda n : setattr(self, 'disable_edu_policies', n.get_bool_value()),
            "disablePowerPolicies": lambda n : setattr(self, 'disable_power_policies', n.get_bool_value()),
            "disableSignInOnResume": lambda n : setattr(self, 'disable_sign_in_on_resume', n.get_bool_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "idleTimeBeforeSleepInSeconds": lambda n : setattr(self, 'idle_time_before_sleep_in_seconds', n.get_int_value()),
            "kioskAppDisplayName": lambda n : setattr(self, 'kiosk_app_display_name', n.get_str_value()),
            "kioskAppUserModelId": lambda n : setattr(self, 'kiosk_app_user_model_id', n.get_str_value()),
            "maintenanceStartTime": lambda n : setattr(self, 'maintenance_start_time', n.get_time_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accountManagerPolicy", self.account_manager_policy)
        writer.write_enum_value("allowedAccounts", self.allowed_accounts)
        writer.write_bool_value("allowLocalStorage", self.allow_local_storage)
        writer.write_bool_value("disableAccountManager", self.disable_account_manager)
        writer.write_bool_value("disableEduPolicies", self.disable_edu_policies)
        writer.write_bool_value("disablePowerPolicies", self.disable_power_policies)
        writer.write_bool_value("disableSignInOnResume", self.disable_sign_in_on_resume)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_int_value("idleTimeBeforeSleepInSeconds", self.idle_time_before_sleep_in_seconds)
        writer.write_str_value("kioskAppDisplayName", self.kiosk_app_display_name)
        writer.write_str_value("kioskAppUserModelId", self.kiosk_app_user_model_id)
        writer.write_time_value("maintenanceStartTime", self.maintenance_start_time)
    

