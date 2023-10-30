from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
    from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
    from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidWorkProfileGeneralDeviceConfiguration(DeviceConfiguration):
    """
    Android Work Profile general device configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration"
    # Indicates whether or not to block fingerprint unlock.
    password_block_fingerprint_unlock: Optional[bool] = None
    # Indicates whether or not to block Smart Lock and other trust agents.
    password_block_trust_agents: Optional[bool] = None
    # Number of days before the password expires. Valid values 1 to 365
    password_expiration_days: Optional[int] = None
    # Minimum length of passwords. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous passwords to block. Valid values 0 to 24
    password_previous_password_block_count: Optional[int] = None
    # Android Work Profile required password type.
    password_required_type: Optional[AndroidWorkProfileRequiredPasswordType] = None
    # Number of sign in failures allowed before factory reset. Valid values 1 to 16
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Require the Android Verify apps feature is turned on.
    security_require_verify_apps: Optional[bool] = None
    # Block users from adding/removing accounts in work profile.
    work_profile_block_adding_accounts: Optional[bool] = None
    # Block work profile camera.
    work_profile_block_camera: Optional[bool] = None
    # Block display work profile caller ID in personal profile.
    work_profile_block_cross_profile_caller_id: Optional[bool] = None
    # Block work profile contacts availability in personal profile.
    work_profile_block_cross_profile_contacts_search: Optional[bool] = None
    # Boolean that indicates if the setting disallow cross profile copy/paste is enabled.
    work_profile_block_cross_profile_copy_paste: Optional[bool] = None
    # Indicates whether or not to block notifications while device locked.
    work_profile_block_notifications_while_device_locked: Optional[bool] = None
    # Block screen capture in work profile.
    work_profile_block_screen_capture: Optional[bool] = None
    # Allow bluetooth devices to access enterprise contacts.
    work_profile_bluetooth_enable_contact_sharing: Optional[bool] = None
    # Android Work Profile cross profile data sharing type.
    work_profile_data_sharing_type: Optional[AndroidWorkProfileCrossProfileDataSharingType] = None
    # Android Work Profile default app permission policy type.
    work_profile_default_app_permission_policy: Optional[AndroidWorkProfileDefaultAppPermissionPolicyType] = None
    # Indicates whether or not to block fingerprint unlock for work profile.
    work_profile_password_block_fingerprint_unlock: Optional[bool] = None
    # Indicates whether or not to block Smart Lock and other trust agents for work profile.
    work_profile_password_block_trust_agents: Optional[bool] = None
    # Number of days before the work profile password expires. Valid values 1 to 365
    work_profile_password_expiration_days: Optional[int] = None
    # Minimum # of letter characters required in work profile password. Valid values 1 to 10
    work_profile_password_min_letter_characters: Optional[int] = None
    # Minimum # of lower-case characters required in work profile password. Valid values 1 to 10
    work_profile_password_min_lower_case_characters: Optional[int] = None
    # Minimum # of non-letter characters required in work profile password. Valid values 1 to 10
    work_profile_password_min_non_letter_characters: Optional[int] = None
    # Minimum # of numeric characters required in work profile password. Valid values 1 to 10
    work_profile_password_min_numeric_characters: Optional[int] = None
    # Minimum # of symbols required in work profile password. Valid values 1 to 10
    work_profile_password_min_symbol_characters: Optional[int] = None
    # Minimum # of upper-case characters required in work profile password. Valid values 1 to 10
    work_profile_password_min_upper_case_characters: Optional[int] = None
    # Minimum length of work profile password. Valid values 4 to 16
    work_profile_password_minimum_length: Optional[int] = None
    # Minutes of inactivity before the screen times out.
    work_profile_password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous work profile passwords to block. Valid values 0 to 24
    work_profile_password_previous_password_block_count: Optional[int] = None
    # Android Work Profile required password type.
    work_profile_password_required_type: Optional[AndroidWorkProfileRequiredPasswordType] = None
    # Number of sign in failures allowed before work profile is removed and all corporate data deleted. Valid values 1 to 16
    work_profile_password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Password is required or not for work profile
    work_profile_require_password: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileGeneralDeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidWorkProfileGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
        from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
        from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
        from .device_configuration import DeviceConfiguration

        from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
        from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
        from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "password_block_fingerprint_unlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "password_block_trust_agents": lambda n : setattr(self, 'password_block_trust_agents', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidWorkProfileRequiredPasswordType)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "security_require_verify_apps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "work_profile_block_adding_accounts": lambda n : setattr(self, 'work_profile_block_adding_accounts', n.get_bool_value()),
            "work_profile_block_camera": lambda n : setattr(self, 'work_profile_block_camera', n.get_bool_value()),
            "work_profile_block_cross_profile_caller_id": lambda n : setattr(self, 'work_profile_block_cross_profile_caller_id', n.get_bool_value()),
            "work_profile_block_cross_profile_contacts_search": lambda n : setattr(self, 'work_profile_block_cross_profile_contacts_search', n.get_bool_value()),
            "work_profile_block_cross_profile_copy_paste": lambda n : setattr(self, 'work_profile_block_cross_profile_copy_paste', n.get_bool_value()),
            "work_profile_block_notifications_while_device_locked": lambda n : setattr(self, 'work_profile_block_notifications_while_device_locked', n.get_bool_value()),
            "work_profile_block_screen_capture": lambda n : setattr(self, 'work_profile_block_screen_capture', n.get_bool_value()),
            "work_profile_bluetooth_enable_contact_sharing": lambda n : setattr(self, 'work_profile_bluetooth_enable_contact_sharing', n.get_bool_value()),
            "work_profile_data_sharing_type": lambda n : setattr(self, 'work_profile_data_sharing_type', n.get_enum_value(AndroidWorkProfileCrossProfileDataSharingType)),
            "work_profile_default_app_permission_policy": lambda n : setattr(self, 'work_profile_default_app_permission_policy', n.get_enum_value(AndroidWorkProfileDefaultAppPermissionPolicyType)),
            "work_profile_password_block_fingerprint_unlock": lambda n : setattr(self, 'work_profile_password_block_fingerprint_unlock', n.get_bool_value()),
            "work_profile_password_block_trust_agents": lambda n : setattr(self, 'work_profile_password_block_trust_agents', n.get_bool_value()),
            "work_profile_password_expiration_days": lambda n : setattr(self, 'work_profile_password_expiration_days', n.get_int_value()),
            "work_profile_password_min_letter_characters": lambda n : setattr(self, 'work_profile_password_min_letter_characters', n.get_int_value()),
            "work_profile_password_min_lower_case_characters": lambda n : setattr(self, 'work_profile_password_min_lower_case_characters', n.get_int_value()),
            "work_profile_password_min_non_letter_characters": lambda n : setattr(self, 'work_profile_password_min_non_letter_characters', n.get_int_value()),
            "work_profile_password_min_numeric_characters": lambda n : setattr(self, 'work_profile_password_min_numeric_characters', n.get_int_value()),
            "work_profile_password_min_symbol_characters": lambda n : setattr(self, 'work_profile_password_min_symbol_characters', n.get_int_value()),
            "work_profile_password_min_upper_case_characters": lambda n : setattr(self, 'work_profile_password_min_upper_case_characters', n.get_int_value()),
            "work_profile_password_minimum_length": lambda n : setattr(self, 'work_profile_password_minimum_length', n.get_int_value()),
            "work_profile_password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'work_profile_password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "work_profile_password_previous_password_block_count": lambda n : setattr(self, 'work_profile_password_previous_password_block_count', n.get_int_value()),
            "work_profile_password_required_type": lambda n : setattr(self, 'work_profile_password_required_type', n.get_enum_value(AndroidWorkProfileRequiredPasswordType)),
            "work_profile_password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'work_profile_password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "work_profile_require_password": lambda n : setattr(self, 'work_profile_require_password', n.get_bool_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("password_block_fingerprint_unlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("password_block_trust_agents", self.password_block_trust_agents)
        writer.write_int_value("password_expiration_days", self.password_expiration_days)
        writer.write_int_value("password_minimum_length", self.password_minimum_length)
        writer.write_int_value("password_minutes_of_inactivity_before_screen_timeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("password_previous_password_block_count", self.password_previous_password_block_count)
        writer.write_enum_value("password_required_type", self.password_required_type)
        writer.write_int_value("password_sign_in_failure_count_before_factory_reset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("security_require_verify_apps", self.security_require_verify_apps)
        writer.write_bool_value("work_profile_block_adding_accounts", self.work_profile_block_adding_accounts)
        writer.write_bool_value("work_profile_block_camera", self.work_profile_block_camera)
        writer.write_bool_value("work_profile_block_cross_profile_caller_id", self.work_profile_block_cross_profile_caller_id)
        writer.write_bool_value("work_profile_block_cross_profile_contacts_search", self.work_profile_block_cross_profile_contacts_search)
        writer.write_bool_value("work_profile_block_cross_profile_copy_paste", self.work_profile_block_cross_profile_copy_paste)
        writer.write_bool_value("work_profile_block_notifications_while_device_locked", self.work_profile_block_notifications_while_device_locked)
        writer.write_bool_value("work_profile_block_screen_capture", self.work_profile_block_screen_capture)
        writer.write_bool_value("work_profile_bluetooth_enable_contact_sharing", self.work_profile_bluetooth_enable_contact_sharing)
        writer.write_enum_value("work_profile_data_sharing_type", self.work_profile_data_sharing_type)
        writer.write_enum_value("work_profile_default_app_permission_policy", self.work_profile_default_app_permission_policy)
        writer.write_bool_value("work_profile_password_block_fingerprint_unlock", self.work_profile_password_block_fingerprint_unlock)
        writer.write_bool_value("work_profile_password_block_trust_agents", self.work_profile_password_block_trust_agents)
        writer.write_int_value("work_profile_password_expiration_days", self.work_profile_password_expiration_days)
        writer.write_int_value("work_profile_password_min_letter_characters", self.work_profile_password_min_letter_characters)
        writer.write_int_value("work_profile_password_min_lower_case_characters", self.work_profile_password_min_lower_case_characters)
        writer.write_int_value("work_profile_password_min_non_letter_characters", self.work_profile_password_min_non_letter_characters)
        writer.write_int_value("work_profile_password_min_numeric_characters", self.work_profile_password_min_numeric_characters)
        writer.write_int_value("work_profile_password_min_symbol_characters", self.work_profile_password_min_symbol_characters)
        writer.write_int_value("work_profile_password_min_upper_case_characters", self.work_profile_password_min_upper_case_characters)
        writer.write_int_value("work_profile_password_minimum_length", self.work_profile_password_minimum_length)
        writer.write_int_value("work_profile_password_minutes_of_inactivity_before_screen_timeout", self.work_profile_password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("work_profile_password_previous_password_block_count", self.work_profile_password_previous_password_block_count)
        writer.write_enum_value("work_profile_password_required_type", self.work_profile_password_required_type)
        writer.write_int_value("work_profile_password_sign_in_failure_count_before_factory_reset", self.work_profile_password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("work_profile_require_password", self.work_profile_require_password)
    

