from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .internet_site_security_level import InternetSiteSecurityLevel
    from .required_password_type import RequiredPasswordType
    from .site_security_level import SiteSecurityLevel
    from .windows_user_account_control_settings import WindowsUserAccountControlSettings

from .device_configuration import DeviceConfiguration

@dataclass
class Windows81GeneralConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the windows81GeneralConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows81GeneralConfiguration"
    # Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
    accounts_block_adding_non_microsoft_account_email: Optional[bool] = None
    # Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
    apply_only_to_windows81: Optional[bool] = None
    # Indicates whether or not to block auto fill.
    browser_block_autofill: Optional[bool] = None
    # Indicates whether or not to block automatic detection of Intranet sites.
    browser_block_automatic_detection_of_intranet_sites: Optional[bool] = None
    # Indicates whether or not to block enterprise mode access.
    browser_block_enterprise_mode_access: Optional[bool] = None
    # Indicates whether or not to Block the user from using JavaScript.
    browser_block_java_script: Optional[bool] = None
    # Indicates whether or not to block plug-ins.
    browser_block_plugins: Optional[bool] = None
    # Indicates whether or not to block popups.
    browser_block_popups: Optional[bool] = None
    # Indicates whether or not to Block the user from sending the do not track header.
    browser_block_sending_do_not_track_header: Optional[bool] = None
    # Indicates whether or not to block a single word entry on Intranet sites.
    browser_block_single_word_entry_on_intranet_sites: Optional[bool] = None
    # The enterprise mode site list location. Could be a local file, local network or http location.
    browser_enterprise_mode_site_list_location: Optional[str] = None
    # Possible values for internet site security level.
    browser_internet_security_level: Optional[InternetSiteSecurityLevel] = None
    # Possible values for site security level.
    browser_intranet_security_level: Optional[SiteSecurityLevel] = None
    # The logging report location.
    browser_logging_report_location: Optional[str] = None
    # Indicates whether or not to require a firewall.
    browser_require_firewall: Optional[bool] = None
    # Indicates whether or not to require fraud warning.
    browser_require_fraud_warning: Optional[bool] = None
    # Indicates whether or not to require high security for restricted sites.
    browser_require_high_security_for_restricted_sites: Optional[bool] = None
    # Indicates whether or not to require the user to use the smart screen filter.
    browser_require_smart_screen: Optional[bool] = None
    # Possible values for site security level.
    browser_trusted_sites_security_level: Optional[SiteSecurityLevel] = None
    # Indicates whether or not to block data roaming.
    cellular_block_data_roaming: Optional[bool] = None
    # Indicates whether or not to block diagnostic data submission.
    diagnostics_block_data_submission: Optional[bool] = None
    # Indicates whether or not to Block the user from using a pictures password and pin.
    password_block_picture_password_and_pin: Optional[bool] = None
    # Password expiration in days.
    password_expiration_days: Optional[int] = None
    # The number of character sets required in the password.
    password_minimum_character_set_count: Optional[int] = None
    # The minimum password length.
    password_minimum_length: Optional[int] = None
    # The minutes of inactivity before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # The number of previous passwords to prevent re-use of. Valid values 0 to 24
    password_previous_password_block_count: Optional[int] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # The number of sign in failures before factory reset.
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Indicates whether or not to require encryption on a mobile device.
    storage_require_device_encryption: Optional[bool] = None
    # Indicates whether or not to require automatic updates.
    updates_require_automatic_updates: Optional[bool] = None
    # Possible values for Windows user account control settings.
    user_account_control_settings: Optional[WindowsUserAccountControlSettings] = None
    # The work folders url.
    work_folders_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows81GeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows81GeneralConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows81GeneralConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .internet_site_security_level import InternetSiteSecurityLevel
        from .required_password_type import RequiredPasswordType
        from .site_security_level import SiteSecurityLevel
        from .windows_user_account_control_settings import WindowsUserAccountControlSettings

        from .device_configuration import DeviceConfiguration
        from .internet_site_security_level import InternetSiteSecurityLevel
        from .required_password_type import RequiredPasswordType
        from .site_security_level import SiteSecurityLevel
        from .windows_user_account_control_settings import WindowsUserAccountControlSettings

        fields: dict[str, Callable[[Any], None]] = {
            "accountsBlockAddingNonMicrosoftAccountEmail": lambda n : setattr(self, 'accounts_block_adding_non_microsoft_account_email', n.get_bool_value()),
            "applyOnlyToWindows81": lambda n : setattr(self, 'apply_only_to_windows81', n.get_bool_value()),
            "browserBlockAutofill": lambda n : setattr(self, 'browser_block_autofill', n.get_bool_value()),
            "browserBlockAutomaticDetectionOfIntranetSites": lambda n : setattr(self, 'browser_block_automatic_detection_of_intranet_sites', n.get_bool_value()),
            "browserBlockEnterpriseModeAccess": lambda n : setattr(self, 'browser_block_enterprise_mode_access', n.get_bool_value()),
            "browserBlockJavaScript": lambda n : setattr(self, 'browser_block_java_script', n.get_bool_value()),
            "browserBlockPlugins": lambda n : setattr(self, 'browser_block_plugins', n.get_bool_value()),
            "browserBlockPopups": lambda n : setattr(self, 'browser_block_popups', n.get_bool_value()),
            "browserBlockSendingDoNotTrackHeader": lambda n : setattr(self, 'browser_block_sending_do_not_track_header', n.get_bool_value()),
            "browserBlockSingleWordEntryOnIntranetSites": lambda n : setattr(self, 'browser_block_single_word_entry_on_intranet_sites', n.get_bool_value()),
            "browserEnterpriseModeSiteListLocation": lambda n : setattr(self, 'browser_enterprise_mode_site_list_location', n.get_str_value()),
            "browserInternetSecurityLevel": lambda n : setattr(self, 'browser_internet_security_level', n.get_enum_value(InternetSiteSecurityLevel)),
            "browserIntranetSecurityLevel": lambda n : setattr(self, 'browser_intranet_security_level', n.get_enum_value(SiteSecurityLevel)),
            "browserLoggingReportLocation": lambda n : setattr(self, 'browser_logging_report_location', n.get_str_value()),
            "browserRequireFirewall": lambda n : setattr(self, 'browser_require_firewall', n.get_bool_value()),
            "browserRequireFraudWarning": lambda n : setattr(self, 'browser_require_fraud_warning', n.get_bool_value()),
            "browserRequireHighSecurityForRestrictedSites": lambda n : setattr(self, 'browser_require_high_security_for_restricted_sites', n.get_bool_value()),
            "browserRequireSmartScreen": lambda n : setattr(self, 'browser_require_smart_screen', n.get_bool_value()),
            "browserTrustedSitesSecurityLevel": lambda n : setattr(self, 'browser_trusted_sites_security_level', n.get_enum_value(SiteSecurityLevel)),
            "cellularBlockDataRoaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "diagnosticsBlockDataSubmission": lambda n : setattr(self, 'diagnostics_block_data_submission', n.get_bool_value()),
            "passwordBlockPicturePasswordAndPin": lambda n : setattr(self, 'password_block_picture_password_and_pin', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "storageRequireDeviceEncryption": lambda n : setattr(self, 'storage_require_device_encryption', n.get_bool_value()),
            "updatesRequireAutomaticUpdates": lambda n : setattr(self, 'updates_require_automatic_updates', n.get_bool_value()),
            "userAccountControlSettings": lambda n : setattr(self, 'user_account_control_settings', n.get_enum_value(WindowsUserAccountControlSettings)),
            "workFoldersUrl": lambda n : setattr(self, 'work_folders_url', n.get_str_value()),
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
        writer.write_bool_value("accountsBlockAddingNonMicrosoftAccountEmail", self.accounts_block_adding_non_microsoft_account_email)
        writer.write_bool_value("browserBlockAutofill", self.browser_block_autofill)
        writer.write_bool_value("browserBlockAutomaticDetectionOfIntranetSites", self.browser_block_automatic_detection_of_intranet_sites)
        writer.write_bool_value("browserBlockEnterpriseModeAccess", self.browser_block_enterprise_mode_access)
        writer.write_bool_value("browserBlockJavaScript", self.browser_block_java_script)
        writer.write_bool_value("browserBlockPlugins", self.browser_block_plugins)
        writer.write_bool_value("browserBlockPopups", self.browser_block_popups)
        writer.write_bool_value("browserBlockSendingDoNotTrackHeader", self.browser_block_sending_do_not_track_header)
        writer.write_bool_value("browserBlockSingleWordEntryOnIntranetSites", self.browser_block_single_word_entry_on_intranet_sites)
        writer.write_str_value("browserEnterpriseModeSiteListLocation", self.browser_enterprise_mode_site_list_location)
        writer.write_enum_value("browserInternetSecurityLevel", self.browser_internet_security_level)
        writer.write_enum_value("browserIntranetSecurityLevel", self.browser_intranet_security_level)
        writer.write_str_value("browserLoggingReportLocation", self.browser_logging_report_location)
        writer.write_bool_value("browserRequireFirewall", self.browser_require_firewall)
        writer.write_bool_value("browserRequireFraudWarning", self.browser_require_fraud_warning)
        writer.write_bool_value("browserRequireHighSecurityForRestrictedSites", self.browser_require_high_security_for_restricted_sites)
        writer.write_bool_value("browserRequireSmartScreen", self.browser_require_smart_screen)
        writer.write_enum_value("browserTrustedSitesSecurityLevel", self.browser_trusted_sites_security_level)
        writer.write_bool_value("cellularBlockDataRoaming", self.cellular_block_data_roaming)
        writer.write_bool_value("diagnosticsBlockDataSubmission", self.diagnostics_block_data_submission)
        writer.write_bool_value("passwordBlockPicturePasswordAndPin", self.password_block_picture_password_and_pin)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("storageRequireDeviceEncryption", self.storage_require_device_encryption)
        writer.write_bool_value("updatesRequireAutomaticUpdates", self.updates_require_automatic_updates)
        writer.write_enum_value("userAccountControlSettings", self.user_account_control_settings)
        writer.write_str_value("workFoldersUrl", self.work_folders_url)
    

