from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
internet_site_security_level = lazy_import('msgraph.generated.models.internet_site_security_level')
required_password_type = lazy_import('msgraph.generated.models.required_password_type')
site_security_level = lazy_import('msgraph.generated.models.site_security_level')
windows_user_account_control_settings = lazy_import('msgraph.generated.models.windows_user_account_control_settings')

class Windows81GeneralConfiguration(device_configuration.DeviceConfiguration):
    @property
    def accounts_block_adding_non_microsoft_account_email(self,) -> Optional[bool]:
        """
        Gets the accountsBlockAddingNonMicrosoftAccountEmail property value. Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
        Returns: Optional[bool]
        """
        return self._accounts_block_adding_non_microsoft_account_email
    
    @accounts_block_adding_non_microsoft_account_email.setter
    def accounts_block_adding_non_microsoft_account_email(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountsBlockAddingNonMicrosoftAccountEmail property value. Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
        Args:
            value: Value to set for the accountsBlockAddingNonMicrosoftAccountEmail property.
        """
        self._accounts_block_adding_non_microsoft_account_email = value
    
    @property
    def apply_only_to_windows81(self,) -> Optional[bool]:
        """
        Gets the applyOnlyToWindows81 property value. Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        Returns: Optional[bool]
        """
        return self._apply_only_to_windows81
    
    @apply_only_to_windows81.setter
    def apply_only_to_windows81(self,value: Optional[bool] = None) -> None:
        """
        Sets the applyOnlyToWindows81 property value. Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        Args:
            value: Value to set for the applyOnlyToWindows81 property.
        """
        self._apply_only_to_windows81 = value
    
    @property
    def browser_block_autofill(self,) -> Optional[bool]:
        """
        Gets the browserBlockAutofill property value. Indicates whether or not to block auto fill.
        Returns: Optional[bool]
        """
        return self._browser_block_autofill
    
    @browser_block_autofill.setter
    def browser_block_autofill(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockAutofill property value. Indicates whether or not to block auto fill.
        Args:
            value: Value to set for the browserBlockAutofill property.
        """
        self._browser_block_autofill = value
    
    @property
    def browser_block_automatic_detection_of_intranet_sites(self,) -> Optional[bool]:
        """
        Gets the browserBlockAutomaticDetectionOfIntranetSites property value. Indicates whether or not to block automatic detection of Intranet sites.
        Returns: Optional[bool]
        """
        return self._browser_block_automatic_detection_of_intranet_sites
    
    @browser_block_automatic_detection_of_intranet_sites.setter
    def browser_block_automatic_detection_of_intranet_sites(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockAutomaticDetectionOfIntranetSites property value. Indicates whether or not to block automatic detection of Intranet sites.
        Args:
            value: Value to set for the browserBlockAutomaticDetectionOfIntranetSites property.
        """
        self._browser_block_automatic_detection_of_intranet_sites = value
    
    @property
    def browser_block_enterprise_mode_access(self,) -> Optional[bool]:
        """
        Gets the browserBlockEnterpriseModeAccess property value. Indicates whether or not to block enterprise mode access.
        Returns: Optional[bool]
        """
        return self._browser_block_enterprise_mode_access
    
    @browser_block_enterprise_mode_access.setter
    def browser_block_enterprise_mode_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockEnterpriseModeAccess property value. Indicates whether or not to block enterprise mode access.
        Args:
            value: Value to set for the browserBlockEnterpriseModeAccess property.
        """
        self._browser_block_enterprise_mode_access = value
    
    @property
    def browser_block_java_script(self,) -> Optional[bool]:
        """
        Gets the browserBlockJavaScript property value. Indicates whether or not to Block the user from using JavaScript.
        Returns: Optional[bool]
        """
        return self._browser_block_java_script
    
    @browser_block_java_script.setter
    def browser_block_java_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockJavaScript property value. Indicates whether or not to Block the user from using JavaScript.
        Args:
            value: Value to set for the browserBlockJavaScript property.
        """
        self._browser_block_java_script = value
    
    @property
    def browser_block_plugins(self,) -> Optional[bool]:
        """
        Gets the browserBlockPlugins property value. Indicates whether or not to block plug-ins.
        Returns: Optional[bool]
        """
        return self._browser_block_plugins
    
    @browser_block_plugins.setter
    def browser_block_plugins(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockPlugins property value. Indicates whether or not to block plug-ins.
        Args:
            value: Value to set for the browserBlockPlugins property.
        """
        self._browser_block_plugins = value
    
    @property
    def browser_block_popups(self,) -> Optional[bool]:
        """
        Gets the browserBlockPopups property value. Indicates whether or not to block popups.
        Returns: Optional[bool]
        """
        return self._browser_block_popups
    
    @browser_block_popups.setter
    def browser_block_popups(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockPopups property value. Indicates whether or not to block popups.
        Args:
            value: Value to set for the browserBlockPopups property.
        """
        self._browser_block_popups = value
    
    @property
    def browser_block_sending_do_not_track_header(self,) -> Optional[bool]:
        """
        Gets the browserBlockSendingDoNotTrackHeader property value. Indicates whether or not to Block the user from sending the do not track header.
        Returns: Optional[bool]
        """
        return self._browser_block_sending_do_not_track_header
    
    @browser_block_sending_do_not_track_header.setter
    def browser_block_sending_do_not_track_header(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockSendingDoNotTrackHeader property value. Indicates whether or not to Block the user from sending the do not track header.
        Args:
            value: Value to set for the browserBlockSendingDoNotTrackHeader property.
        """
        self._browser_block_sending_do_not_track_header = value
    
    @property
    def browser_block_single_word_entry_on_intranet_sites(self,) -> Optional[bool]:
        """
        Gets the browserBlockSingleWordEntryOnIntranetSites property value. Indicates whether or not to block a single word entry on Intranet sites.
        Returns: Optional[bool]
        """
        return self._browser_block_single_word_entry_on_intranet_sites
    
    @browser_block_single_word_entry_on_intranet_sites.setter
    def browser_block_single_word_entry_on_intranet_sites(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserBlockSingleWordEntryOnIntranetSites property value. Indicates whether or not to block a single word entry on Intranet sites.
        Args:
            value: Value to set for the browserBlockSingleWordEntryOnIntranetSites property.
        """
        self._browser_block_single_word_entry_on_intranet_sites = value
    
    @property
    def browser_enterprise_mode_site_list_location(self,) -> Optional[str]:
        """
        Gets the browserEnterpriseModeSiteListLocation property value. The enterprise mode site list location. Could be a local file, local network or http location.
        Returns: Optional[str]
        """
        return self._browser_enterprise_mode_site_list_location
    
    @browser_enterprise_mode_site_list_location.setter
    def browser_enterprise_mode_site_list_location(self,value: Optional[str] = None) -> None:
        """
        Sets the browserEnterpriseModeSiteListLocation property value. The enterprise mode site list location. Could be a local file, local network or http location.
        Args:
            value: Value to set for the browserEnterpriseModeSiteListLocation property.
        """
        self._browser_enterprise_mode_site_list_location = value
    
    @property
    def browser_internet_security_level(self,) -> Optional[internet_site_security_level.InternetSiteSecurityLevel]:
        """
        Gets the browserInternetSecurityLevel property value. Possible values for internet site security level.
        Returns: Optional[internet_site_security_level.InternetSiteSecurityLevel]
        """
        return self._browser_internet_security_level
    
    @browser_internet_security_level.setter
    def browser_internet_security_level(self,value: Optional[internet_site_security_level.InternetSiteSecurityLevel] = None) -> None:
        """
        Sets the browserInternetSecurityLevel property value. Possible values for internet site security level.
        Args:
            value: Value to set for the browserInternetSecurityLevel property.
        """
        self._browser_internet_security_level = value
    
    @property
    def browser_intranet_security_level(self,) -> Optional[site_security_level.SiteSecurityLevel]:
        """
        Gets the browserIntranetSecurityLevel property value. Possible values for site security level.
        Returns: Optional[site_security_level.SiteSecurityLevel]
        """
        return self._browser_intranet_security_level
    
    @browser_intranet_security_level.setter
    def browser_intranet_security_level(self,value: Optional[site_security_level.SiteSecurityLevel] = None) -> None:
        """
        Sets the browserIntranetSecurityLevel property value. Possible values for site security level.
        Args:
            value: Value to set for the browserIntranetSecurityLevel property.
        """
        self._browser_intranet_security_level = value
    
    @property
    def browser_logging_report_location(self,) -> Optional[str]:
        """
        Gets the browserLoggingReportLocation property value. The logging report location.
        Returns: Optional[str]
        """
        return self._browser_logging_report_location
    
    @browser_logging_report_location.setter
    def browser_logging_report_location(self,value: Optional[str] = None) -> None:
        """
        Sets the browserLoggingReportLocation property value. The logging report location.
        Args:
            value: Value to set for the browserLoggingReportLocation property.
        """
        self._browser_logging_report_location = value
    
    @property
    def browser_require_firewall(self,) -> Optional[bool]:
        """
        Gets the browserRequireFirewall property value. Indicates whether or not to require a firewall.
        Returns: Optional[bool]
        """
        return self._browser_require_firewall
    
    @browser_require_firewall.setter
    def browser_require_firewall(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserRequireFirewall property value. Indicates whether or not to require a firewall.
        Args:
            value: Value to set for the browserRequireFirewall property.
        """
        self._browser_require_firewall = value
    
    @property
    def browser_require_fraud_warning(self,) -> Optional[bool]:
        """
        Gets the browserRequireFraudWarning property value. Indicates whether or not to require fraud warning.
        Returns: Optional[bool]
        """
        return self._browser_require_fraud_warning
    
    @browser_require_fraud_warning.setter
    def browser_require_fraud_warning(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserRequireFraudWarning property value. Indicates whether or not to require fraud warning.
        Args:
            value: Value to set for the browserRequireFraudWarning property.
        """
        self._browser_require_fraud_warning = value
    
    @property
    def browser_require_high_security_for_restricted_sites(self,) -> Optional[bool]:
        """
        Gets the browserRequireHighSecurityForRestrictedSites property value. Indicates whether or not to require high security for restricted sites.
        Returns: Optional[bool]
        """
        return self._browser_require_high_security_for_restricted_sites
    
    @browser_require_high_security_for_restricted_sites.setter
    def browser_require_high_security_for_restricted_sites(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserRequireHighSecurityForRestrictedSites property value. Indicates whether or not to require high security for restricted sites.
        Args:
            value: Value to set for the browserRequireHighSecurityForRestrictedSites property.
        """
        self._browser_require_high_security_for_restricted_sites = value
    
    @property
    def browser_require_smart_screen(self,) -> Optional[bool]:
        """
        Gets the browserRequireSmartScreen property value. Indicates whether or not to require the user to use the smart screen filter.
        Returns: Optional[bool]
        """
        return self._browser_require_smart_screen
    
    @browser_require_smart_screen.setter
    def browser_require_smart_screen(self,value: Optional[bool] = None) -> None:
        """
        Sets the browserRequireSmartScreen property value. Indicates whether or not to require the user to use the smart screen filter.
        Args:
            value: Value to set for the browserRequireSmartScreen property.
        """
        self._browser_require_smart_screen = value
    
    @property
    def browser_trusted_sites_security_level(self,) -> Optional[site_security_level.SiteSecurityLevel]:
        """
        Gets the browserTrustedSitesSecurityLevel property value. Possible values for site security level.
        Returns: Optional[site_security_level.SiteSecurityLevel]
        """
        return self._browser_trusted_sites_security_level
    
    @browser_trusted_sites_security_level.setter
    def browser_trusted_sites_security_level(self,value: Optional[site_security_level.SiteSecurityLevel] = None) -> None:
        """
        Sets the browserTrustedSitesSecurityLevel property value. Possible values for site security level.
        Args:
            value: Value to set for the browserTrustedSitesSecurityLevel property.
        """
        self._browser_trusted_sites_security_level = value
    
    @property
    def cellular_block_data_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockDataRoaming property value. Indicates whether or not to block data roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_data_roaming
    
    @cellular_block_data_roaming.setter
    def cellular_block_data_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockDataRoaming property value. Indicates whether or not to block data roaming.
        Args:
            value: Value to set for the cellularBlockDataRoaming property.
        """
        self._cellular_block_data_roaming = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows81GeneralConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows81GeneralConfiguration"
        # Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
        self._accounts_block_adding_non_microsoft_account_email: Optional[bool] = None
        # Value indicating whether this policy only applies to Windows 8.1. This property is read-only.
        self._apply_only_to_windows81: Optional[bool] = None
        # Indicates whether or not to block auto fill.
        self._browser_block_autofill: Optional[bool] = None
        # Indicates whether or not to block automatic detection of Intranet sites.
        self._browser_block_automatic_detection_of_intranet_sites: Optional[bool] = None
        # Indicates whether or not to block enterprise mode access.
        self._browser_block_enterprise_mode_access: Optional[bool] = None
        # Indicates whether or not to Block the user from using JavaScript.
        self._browser_block_java_script: Optional[bool] = None
        # Indicates whether or not to block plug-ins.
        self._browser_block_plugins: Optional[bool] = None
        # Indicates whether or not to block popups.
        self._browser_block_popups: Optional[bool] = None
        # Indicates whether or not to Block the user from sending the do not track header.
        self._browser_block_sending_do_not_track_header: Optional[bool] = None
        # Indicates whether or not to block a single word entry on Intranet sites.
        self._browser_block_single_word_entry_on_intranet_sites: Optional[bool] = None
        # The enterprise mode site list location. Could be a local file, local network or http location.
        self._browser_enterprise_mode_site_list_location: Optional[str] = None
        # Possible values for internet site security level.
        self._browser_internet_security_level: Optional[internet_site_security_level.InternetSiteSecurityLevel] = None
        # Possible values for site security level.
        self._browser_intranet_security_level: Optional[site_security_level.SiteSecurityLevel] = None
        # The logging report location.
        self._browser_logging_report_location: Optional[str] = None
        # Indicates whether or not to require a firewall.
        self._browser_require_firewall: Optional[bool] = None
        # Indicates whether or not to require fraud warning.
        self._browser_require_fraud_warning: Optional[bool] = None
        # Indicates whether or not to require high security for restricted sites.
        self._browser_require_high_security_for_restricted_sites: Optional[bool] = None
        # Indicates whether or not to require the user to use the smart screen filter.
        self._browser_require_smart_screen: Optional[bool] = None
        # Possible values for site security level.
        self._browser_trusted_sites_security_level: Optional[site_security_level.SiteSecurityLevel] = None
        # Indicates whether or not to block data roaming.
        self._cellular_block_data_roaming: Optional[bool] = None
        # Indicates whether or not to block diagnostic data submission.
        self._diagnostics_block_data_submission: Optional[bool] = None
        # Indicates whether or not to Block the user from using a pictures password and pin.
        self._password_block_picture_password_and_pin: Optional[bool] = None
        # Password expiration in days.
        self._password_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._password_minimum_character_set_count: Optional[int] = None
        # The minimum password length.
        self._password_minimum_length: Optional[int] = None
        # The minutes of inactivity before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # The number of previous passwords to prevent re-use of. Valid values 0 to 24
        self._password_previous_password_block_count: Optional[int] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # The number of sign in failures before factory reset.
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # Indicates whether or not to require encryption on a mobile device.
        self._storage_require_device_encryption: Optional[bool] = None
        # Indicates whether or not to require automatic updates.
        self._updates_require_automatic_updates: Optional[bool] = None
        # Possible values for Windows user account control settings.
        self._user_account_control_settings: Optional[windows_user_account_control_settings.WindowsUserAccountControlSettings] = None
        # The work folders url.
        self._work_folders_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows81GeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows81GeneralConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows81GeneralConfiguration()
    
    @property
    def diagnostics_block_data_submission(self,) -> Optional[bool]:
        """
        Gets the diagnosticsBlockDataSubmission property value. Indicates whether or not to block diagnostic data submission.
        Returns: Optional[bool]
        """
        return self._diagnostics_block_data_submission
    
    @diagnostics_block_data_submission.setter
    def diagnostics_block_data_submission(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticsBlockDataSubmission property value. Indicates whether or not to block diagnostic data submission.
        Args:
            value: Value to set for the diagnosticsBlockDataSubmission property.
        """
        self._diagnostics_block_data_submission = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accounts_block_adding_non_microsoft_account_email": lambda n : setattr(self, 'accounts_block_adding_non_microsoft_account_email', n.get_bool_value()),
            "apply_only_to_windows81": lambda n : setattr(self, 'apply_only_to_windows81', n.get_bool_value()),
            "browser_block_autofill": lambda n : setattr(self, 'browser_block_autofill', n.get_bool_value()),
            "browser_block_automatic_detection_of_intranet_sites": lambda n : setattr(self, 'browser_block_automatic_detection_of_intranet_sites', n.get_bool_value()),
            "browser_block_enterprise_mode_access": lambda n : setattr(self, 'browser_block_enterprise_mode_access', n.get_bool_value()),
            "browser_block_java_script": lambda n : setattr(self, 'browser_block_java_script', n.get_bool_value()),
            "browser_block_plugins": lambda n : setattr(self, 'browser_block_plugins', n.get_bool_value()),
            "browser_block_popups": lambda n : setattr(self, 'browser_block_popups', n.get_bool_value()),
            "browser_block_sending_do_not_track_header": lambda n : setattr(self, 'browser_block_sending_do_not_track_header', n.get_bool_value()),
            "browser_block_single_word_entry_on_intranet_sites": lambda n : setattr(self, 'browser_block_single_word_entry_on_intranet_sites', n.get_bool_value()),
            "browser_enterprise_mode_site_list_location": lambda n : setattr(self, 'browser_enterprise_mode_site_list_location', n.get_str_value()),
            "browser_internet_security_level": lambda n : setattr(self, 'browser_internet_security_level', n.get_enum_value(internet_site_security_level.InternetSiteSecurityLevel)),
            "browser_intranet_security_level": lambda n : setattr(self, 'browser_intranet_security_level', n.get_enum_value(site_security_level.SiteSecurityLevel)),
            "browser_logging_report_location": lambda n : setattr(self, 'browser_logging_report_location', n.get_str_value()),
            "browser_require_firewall": lambda n : setattr(self, 'browser_require_firewall', n.get_bool_value()),
            "browser_require_fraud_warning": lambda n : setattr(self, 'browser_require_fraud_warning', n.get_bool_value()),
            "browser_require_high_security_for_restricted_sites": lambda n : setattr(self, 'browser_require_high_security_for_restricted_sites', n.get_bool_value()),
            "browser_require_smart_screen": lambda n : setattr(self, 'browser_require_smart_screen', n.get_bool_value()),
            "browser_trusted_sites_security_level": lambda n : setattr(self, 'browser_trusted_sites_security_level', n.get_enum_value(site_security_level.SiteSecurityLevel)),
            "cellular_block_data_roaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "diagnostics_block_data_submission": lambda n : setattr(self, 'diagnostics_block_data_submission', n.get_bool_value()),
            "password_block_picture_password_and_pin": lambda n : setattr(self, 'password_block_picture_password_and_pin', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_character_set_count": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "storage_require_device_encryption": lambda n : setattr(self, 'storage_require_device_encryption', n.get_bool_value()),
            "updates_require_automatic_updates": lambda n : setattr(self, 'updates_require_automatic_updates', n.get_bool_value()),
            "user_account_control_settings": lambda n : setattr(self, 'user_account_control_settings', n.get_enum_value(windows_user_account_control_settings.WindowsUserAccountControlSettings)),
            "work_folders_url": lambda n : setattr(self, 'work_folders_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def password_block_picture_password_and_pin(self,) -> Optional[bool]:
        """
        Gets the passwordBlockPicturePasswordAndPin property value. Indicates whether or not to Block the user from using a pictures password and pin.
        Returns: Optional[bool]
        """
        return self._password_block_picture_password_and_pin
    
    @password_block_picture_password_and_pin.setter
    def password_block_picture_password_and_pin(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockPicturePasswordAndPin property value. Indicates whether or not to Block the user from using a pictures password and pin.
        Args:
            value: Value to set for the passwordBlockPicturePasswordAndPin property.
        """
        self._password_block_picture_password_and_pin = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Password expiration in days.
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Password expiration in days.
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Args:
            value: Value to set for the passwordMinimumCharacterSetCount property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. The minimum password length.
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. The minimum password length.
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeScreenTimeout property value. The minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_screen_timeout
    
    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeScreenTimeout property value. The minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the passwordMinutesOfInactivityBeforeScreenTimeout property.
        """
        self._password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of. Valid values 0 to 24
        Args:
            value: Value to set for the passwordPreviousPasswordBlockCount property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the passwordRequiredType property.
        """
        self._password_required_type = value
    
    @property
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. The number of sign in failures before factory reset.
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. The number of sign in failures before factory reset.
        Args:
            value: Value to set for the passwordSignInFailureCountBeforeFactoryReset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def storage_require_device_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireDeviceEncryption property value. Indicates whether or not to require encryption on a mobile device.
        Returns: Optional[bool]
        """
        return self._storage_require_device_encryption
    
    @storage_require_device_encryption.setter
    def storage_require_device_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireDeviceEncryption property value. Indicates whether or not to require encryption on a mobile device.
        Args:
            value: Value to set for the storageRequireDeviceEncryption property.
        """
        self._storage_require_device_encryption = value
    
    @property
    def updates_require_automatic_updates(self,) -> Optional[bool]:
        """
        Gets the updatesRequireAutomaticUpdates property value. Indicates whether or not to require automatic updates.
        Returns: Optional[bool]
        """
        return self._updates_require_automatic_updates
    
    @updates_require_automatic_updates.setter
    def updates_require_automatic_updates(self,value: Optional[bool] = None) -> None:
        """
        Sets the updatesRequireAutomaticUpdates property value. Indicates whether or not to require automatic updates.
        Args:
            value: Value to set for the updatesRequireAutomaticUpdates property.
        """
        self._updates_require_automatic_updates = value
    
    @property
    def user_account_control_settings(self,) -> Optional[windows_user_account_control_settings.WindowsUserAccountControlSettings]:
        """
        Gets the userAccountControlSettings property value. Possible values for Windows user account control settings.
        Returns: Optional[windows_user_account_control_settings.WindowsUserAccountControlSettings]
        """
        return self._user_account_control_settings
    
    @user_account_control_settings.setter
    def user_account_control_settings(self,value: Optional[windows_user_account_control_settings.WindowsUserAccountControlSettings] = None) -> None:
        """
        Sets the userAccountControlSettings property value. Possible values for Windows user account control settings.
        Args:
            value: Value to set for the userAccountControlSettings property.
        """
        self._user_account_control_settings = value
    
    @property
    def work_folders_url(self,) -> Optional[str]:
        """
        Gets the workFoldersUrl property value. The work folders url.
        Returns: Optional[str]
        """
        return self._work_folders_url
    
    @work_folders_url.setter
    def work_folders_url(self,value: Optional[str] = None) -> None:
        """
        Sets the workFoldersUrl property value. The work folders url.
        Args:
            value: Value to set for the workFoldersUrl property.
        """
        self._work_folders_url = value
    

