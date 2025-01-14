from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
    from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
    from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidWorkProfileGeneralDeviceConfiguration(DeviceConfiguration, Parsable):
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
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidWorkProfileGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidWorkProfileGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
        from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
        from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
        from .device_configuration import DeviceConfiguration

        from .android_work_profile_cross_profile_data_sharing_type import AndroidWorkProfileCrossProfileDataSharingType
        from .android_work_profile_default_app_permission_policy_type import AndroidWorkProfileDefaultAppPermissionPolicyType
        from .android_work_profile_required_password_type import AndroidWorkProfileRequiredPasswordType
        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "passwordBlockFingerprintUnlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "passwordBlockTrustAgents": lambda n : setattr(self, 'password_block_trust_agents', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidWorkProfileRequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "securityRequireVerifyApps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "workProfileBlockAddingAccounts": lambda n : setattr(self, 'work_profile_block_adding_accounts', n.get_bool_value()),
            "workProfileBlockCamera": lambda n : setattr(self, 'work_profile_block_camera', n.get_bool_value()),
            "workProfileBlockCrossProfileCallerId": lambda n : setattr(self, 'work_profile_block_cross_profile_caller_id', n.get_bool_value()),
            "workProfileBlockCrossProfileContactsSearch": lambda n : setattr(self, 'work_profile_block_cross_profile_contacts_search', n.get_bool_value()),
            "workProfileBlockCrossProfileCopyPaste": lambda n : setattr(self, 'work_profile_block_cross_profile_copy_paste', n.get_bool_value()),
            "workProfileBlockNotificationsWhileDeviceLocked": lambda n : setattr(self, 'work_profile_block_notifications_while_device_locked', n.get_bool_value()),
            "workProfileBlockScreenCapture": lambda n : setattr(self, 'work_profile_block_screen_capture', n.get_bool_value()),
            "workProfileBluetoothEnableContactSharing": lambda n : setattr(self, 'work_profile_bluetooth_enable_contact_sharing', n.get_bool_value()),
            "workProfileDataSharingType": lambda n : setattr(self, 'work_profile_data_sharing_type', n.get_enum_value(AndroidWorkProfileCrossProfileDataSharingType)),
            "workProfileDefaultAppPermissionPolicy": lambda n : setattr(self, 'work_profile_default_app_permission_policy', n.get_enum_value(AndroidWorkProfileDefaultAppPermissionPolicyType)),
            "workProfilePasswordBlockFingerprintUnlock": lambda n : setattr(self, 'work_profile_password_block_fingerprint_unlock', n.get_bool_value()),
            "workProfilePasswordBlockTrustAgents": lambda n : setattr(self, 'work_profile_password_block_trust_agents', n.get_bool_value()),
            "workProfilePasswordExpirationDays": lambda n : setattr(self, 'work_profile_password_expiration_days', n.get_int_value()),
            "workProfilePasswordMinLetterCharacters": lambda n : setattr(self, 'work_profile_password_min_letter_characters', n.get_int_value()),
            "workProfilePasswordMinLowerCaseCharacters": lambda n : setattr(self, 'work_profile_password_min_lower_case_characters', n.get_int_value()),
            "workProfilePasswordMinNonLetterCharacters": lambda n : setattr(self, 'work_profile_password_min_non_letter_characters', n.get_int_value()),
            "workProfilePasswordMinNumericCharacters": lambda n : setattr(self, 'work_profile_password_min_numeric_characters', n.get_int_value()),
            "workProfilePasswordMinSymbolCharacters": lambda n : setattr(self, 'work_profile_password_min_symbol_characters', n.get_int_value()),
            "workProfilePasswordMinUpperCaseCharacters": lambda n : setattr(self, 'work_profile_password_min_upper_case_characters', n.get_int_value()),
            "workProfilePasswordMinimumLength": lambda n : setattr(self, 'work_profile_password_minimum_length', n.get_int_value()),
            "workProfilePasswordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'work_profile_password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "workProfilePasswordPreviousPasswordBlockCount": lambda n : setattr(self, 'work_profile_password_previous_password_block_count', n.get_int_value()),
            "workProfilePasswordRequiredType": lambda n : setattr(self, 'work_profile_password_required_type', n.get_enum_value(AndroidWorkProfileRequiredPasswordType)),
            "workProfilePasswordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'work_profile_password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "workProfileRequirePassword": lambda n : setattr(self, 'work_profile_require_password', n.get_bool_value()),
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
        writer.write_bool_value("passwordBlockFingerprintUnlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("passwordBlockTrustAgents", self.password_block_trust_agents)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("securityRequireVerifyApps", self.security_require_verify_apps)
        writer.write_bool_value("workProfileBlockAddingAccounts", self.work_profile_block_adding_accounts)
        writer.write_bool_value("workProfileBlockCamera", self.work_profile_block_camera)
        writer.write_bool_value("workProfileBlockCrossProfileCallerId", self.work_profile_block_cross_profile_caller_id)
        writer.write_bool_value("workProfileBlockCrossProfileContactsSearch", self.work_profile_block_cross_profile_contacts_search)
        writer.write_bool_value("workProfileBlockCrossProfileCopyPaste", self.work_profile_block_cross_profile_copy_paste)
        writer.write_bool_value("workProfileBlockNotificationsWhileDeviceLocked", self.work_profile_block_notifications_while_device_locked)
        writer.write_bool_value("workProfileBlockScreenCapture", self.work_profile_block_screen_capture)
        writer.write_bool_value("workProfileBluetoothEnableContactSharing", self.work_profile_bluetooth_enable_contact_sharing)
        writer.write_enum_value("workProfileDataSharingType", self.work_profile_data_sharing_type)
        writer.write_enum_value("workProfileDefaultAppPermissionPolicy", self.work_profile_default_app_permission_policy)
        writer.write_bool_value("workProfilePasswordBlockFingerprintUnlock", self.work_profile_password_block_fingerprint_unlock)
        writer.write_bool_value("workProfilePasswordBlockTrustAgents", self.work_profile_password_block_trust_agents)
        writer.write_int_value("workProfilePasswordExpirationDays", self.work_profile_password_expiration_days)
        writer.write_int_value("workProfilePasswordMinLetterCharacters", self.work_profile_password_min_letter_characters)
        writer.write_int_value("workProfilePasswordMinLowerCaseCharacters", self.work_profile_password_min_lower_case_characters)
        writer.write_int_value("workProfilePasswordMinNonLetterCharacters", self.work_profile_password_min_non_letter_characters)
        writer.write_int_value("workProfilePasswordMinNumericCharacters", self.work_profile_password_min_numeric_characters)
        writer.write_int_value("workProfilePasswordMinSymbolCharacters", self.work_profile_password_min_symbol_characters)
        writer.write_int_value("workProfilePasswordMinUpperCaseCharacters", self.work_profile_password_min_upper_case_characters)
        writer.write_int_value("workProfilePasswordMinimumLength", self.work_profile_password_minimum_length)
        writer.write_int_value("workProfilePasswordMinutesOfInactivityBeforeScreenTimeout", self.work_profile_password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("workProfilePasswordPreviousPasswordBlockCount", self.work_profile_password_previous_password_block_count)
        writer.write_enum_value("workProfilePasswordRequiredType", self.work_profile_password_required_type)
        writer.write_int_value("workProfilePasswordSignInFailureCountBeforeFactoryReset", self.work_profile_password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("workProfileRequirePassword", self.work_profile_require_password)
    

