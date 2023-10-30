from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
    from .defender_detected_malware_actions import DefenderDetectedMalwareActions
    from .defender_monitor_file_activity import DefenderMonitorFileActivity
    from .defender_prompt_for_sample_submission import DefenderPromptForSampleSubmission
    from .defender_scan_type import DefenderScanType
    from .device_configuration import DeviceConfiguration
    from .diagnostic_data_submission_mode import DiagnosticDataSubmissionMode
    from .edge_cookie_policy import EdgeCookiePolicy
    from .edge_search_engine_base import EdgeSearchEngineBase
    from .required_password_type import RequiredPasswordType
    from .safe_search_filter_type import SafeSearchFilterType
    from .state_management_setting import StateManagementSetting
    from .visibility_setting import VisibilitySetting
    from .weekly_schedule import WeeklySchedule
    from .windows10_network_proxy_server import Windows10NetworkProxyServer
    from .windows_spotlight_enablement_settings import WindowsSpotlightEnablementSettings
    from .windows_start_menu_app_list_visibility_type import WindowsStartMenuAppListVisibilityType
    from .windows_start_menu_mode_type import WindowsStartMenuModeType

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10GeneralConfiguration(DeviceConfiguration):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the windows10GeneralConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10GeneralConfiguration"
    # Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
    accounts_block_adding_non_microsoft_account_email: Optional[bool] = None
    # Indicates whether or not to block the user from selecting an AntiTheft mode preference (Windows 10 Mobile only).
    anti_theft_mode_blocked: Optional[bool] = None
    # State Management Setting.
    apps_allow_trusted_apps_sideloading: Optional[StateManagementSetting] = None
    # Indicates whether or not to disable the launch of all apps from Windows Store that came pre-installed or were downloaded.
    apps_block_windows_store_originated_apps: Optional[bool] = None
    # Specify a list of allowed Bluetooth services and profiles in hex formatted strings.
    bluetooth_allowed_services: Optional[List[str]] = None
    # Whether or not to Block the user from using bluetooth advertising.
    bluetooth_block_advertising: Optional[bool] = None
    # Whether or not to Block the user from using bluetooth discoverable mode.
    bluetooth_block_discoverable_mode: Optional[bool] = None
    # Whether or not to block specific bundled Bluetooth peripherals to automatically pair with the host device.
    bluetooth_block_pre_pairing: Optional[bool] = None
    # Whether or not to Block the user from using bluetooth.
    bluetooth_blocked: Optional[bool] = None
    # Whether or not to Block the user from accessing the camera of the device.
    camera_blocked: Optional[bool] = None
    # Whether or not to Block the user from using data over cellular while roaming.
    cellular_block_data_when_roaming: Optional[bool] = None
    # Whether or not to Block the user from using VPN over cellular.
    cellular_block_vpn: Optional[bool] = None
    # Whether or not to Block the user from using VPN when roaming over cellular.
    cellular_block_vpn_when_roaming: Optional[bool] = None
    # Whether or not to Block the user from doing manual root certificate installation.
    certificates_block_manual_root_certificate_installation: Optional[bool] = None
    # Whether or not to block Connected Devices Service which enables discovery and connection to other devices, remote messaging, remote app sessions and other cross-device experiences.
    connected_devices_service_blocked: Optional[bool] = None
    # Whether or not to Block the user from using copy paste.
    copy_paste_blocked: Optional[bool] = None
    # Whether or not to Block the user from using Cortana.
    cortana_blocked: Optional[bool] = None
    # Whether or not to block end user access to Defender.
    defender_block_end_user_access: Optional[bool] = None
    # Possible values of Cloud Block Level
    defender_cloud_block_level: Optional[DefenderCloudBlockLevelType] = None
    # Number of days before deleting quarantined malware. Valid values 0 to 90
    defender_days_before_deleting_quarantined_malware: Optional[int] = None
    # Gets or sets Defender’s actions to take on detected Malware per threat level.
    defender_detected_malware_actions: Optional[DefenderDetectedMalwareActions] = None
    # File extensions to exclude from scans and real time protection.
    defender_file_extensions_to_exclude: Optional[List[str]] = None
    # Files and folder to exclude from scans and real time protection.
    defender_files_and_folders_to_exclude: Optional[List[str]] = None
    # Possible values for monitoring file activity.
    defender_monitor_file_activity: Optional[DefenderMonitorFileActivity] = None
    # Processes to exclude from scans and real time protection.
    defender_processes_to_exclude: Optional[List[str]] = None
    # Possible values for prompting user for samples submission.
    defender_prompt_for_sample_submission: Optional[DefenderPromptForSampleSubmission] = None
    # Indicates whether or not to require behavior monitoring.
    defender_require_behavior_monitoring: Optional[bool] = None
    # Indicates whether or not to require cloud protection.
    defender_require_cloud_protection: Optional[bool] = None
    # Indicates whether or not to require network inspection system.
    defender_require_network_inspection_system: Optional[bool] = None
    # Indicates whether or not to require real time monitoring.
    defender_require_real_time_monitoring: Optional[bool] = None
    # Indicates whether or not to scan archive files.
    defender_scan_archive_files: Optional[bool] = None
    # Indicates whether or not to scan downloads.
    defender_scan_downloads: Optional[bool] = None
    # Indicates whether or not to scan incoming mail messages.
    defender_scan_incoming_mail: Optional[bool] = None
    # Indicates whether or not to scan mapped network drives during full scan.
    defender_scan_mapped_network_drives_during_full_scan: Optional[bool] = None
    # Max CPU usage percentage during scan. Valid values 0 to 100
    defender_scan_max_cpu: Optional[int] = None
    # Indicates whether or not to scan files opened from a network folder.
    defender_scan_network_files: Optional[bool] = None
    # Indicates whether or not to scan removable drives during full scan.
    defender_scan_removable_drives_during_full_scan: Optional[bool] = None
    # Indicates whether or not to scan scripts loaded in Internet Explorer browser.
    defender_scan_scripts_loaded_in_internet_explorer: Optional[bool] = None
    # Possible values for system scan type.
    defender_scan_type: Optional[DefenderScanType] = None
    # The time to perform a daily quick scan.
    defender_scheduled_quick_scan_time: Optional[datetime.time] = None
    # The defender time for the system scan.
    defender_scheduled_scan_time: Optional[datetime.time] = None
    # The signature update interval in hours. Specify 0 not to check. Valid values 0 to 24
    defender_signature_update_interval_in_hours: Optional[int] = None
    # Possible values for a weekly schedule.
    defender_system_scan_schedule: Optional[WeeklySchedule] = None
    # State Management Setting.
    developer_unlock_setting: Optional[StateManagementSetting] = None
    # Indicates whether or not to Block the user from resetting their phone.
    device_management_block_factory_reset_on_mobile: Optional[bool] = None
    # Indicates whether or not to Block the user from doing manual un-enrollment from device management.
    device_management_block_manual_unenroll: Optional[bool] = None
    # Allow the device to send diagnostic and usage telemetry data, such as Watson.
    diagnostics_data_submission_mode: Optional[DiagnosticDataSubmissionMode] = None
    # Allow users to change Start pages on Edge. Use the EdgeHomepageUrls to specify the Start pages that the user would see by default when they open Edge.
    edge_allow_start_pages_modification: Optional[bool] = None
    # Indicates whether or not to prevent access to about flags on Edge browser.
    edge_block_access_to_about_flags: Optional[bool] = None
    # Block the address bar dropdown functionality in Microsoft Edge. Disable this settings to minimize network connections from Microsoft Edge to Microsoft services.
    edge_block_address_bar_dropdown: Optional[bool] = None
    # Indicates whether or not to block auto fill.
    edge_block_autofill: Optional[bool] = None
    # Block Microsoft compatibility list in Microsoft Edge. This list from Microsoft helps Edge properly display sites with known compatibility issues.
    edge_block_compatibility_list: Optional[bool] = None
    # Indicates whether or not to block developer tools in the Edge browser.
    edge_block_developer_tools: Optional[bool] = None
    # Indicates whether or not to block extensions in the Edge browser.
    edge_block_extensions: Optional[bool] = None
    # Indicates whether or not to block InPrivate browsing on corporate networks, in the Edge browser.
    edge_block_in_private_browsing: Optional[bool] = None
    # Indicates whether or not to Block the user from using JavaScript.
    edge_block_java_script: Optional[bool] = None
    # Block the collection of information by Microsoft for live tile creation when users pin a site to Start from Microsoft Edge.
    edge_block_live_tile_data_collection: Optional[bool] = None
    # Indicates whether or not to Block password manager.
    edge_block_password_manager: Optional[bool] = None
    # Indicates whether or not to block popups.
    edge_block_popups: Optional[bool] = None
    # Indicates whether or not to block the user from using the search suggestions in the address bar.
    edge_block_search_suggestions: Optional[bool] = None
    # Indicates whether or not to Block the user from sending the do not track header.
    edge_block_sending_do_not_track_header: Optional[bool] = None
    # Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer. Note: the name of this property is misleading; the property is obsolete, use EdgeSendIntranetTrafficToInternetExplorer instead.
    edge_block_sending_intranet_traffic_to_internet_explorer: Optional[bool] = None
    # Indicates whether or not to Block the user from using the Edge browser.
    edge_blocked: Optional[bool] = None
    # Clear browsing data on exiting Microsoft Edge.
    edge_clear_browsing_data_on_exit: Optional[bool] = None
    # Possible values to specify which cookies are allowed in Microsoft Edge.
    edge_cookie_policy: Optional[EdgeCookiePolicy] = None
    # Block the Microsoft web page that opens on the first use of Microsoft Edge. This policy allows enterprises, like those enrolled in zero emissions configurations, to block this page.
    edge_disable_first_run_page: Optional[bool] = None
    # Indicates the enterprise mode site list location. Could be a local file, local network or http location.
    edge_enterprise_mode_site_list_location: Optional[str] = None
    # The first run URL for when Edge browser is opened for the first time.
    edge_first_run_url: Optional[str] = None
    # The list of URLs for homepages shodwn on MDM-enrolled devices on Edge browser.
    edge_homepage_urls: Optional[List[str]] = None
    # Indicates whether or not to Require the user to use the smart screen filter.
    edge_require_smart_screen: Optional[bool] = None
    # Allows IT admins to set a default search engine for MDM-Controlled devices. Users can override this and change their default search engine provided the AllowSearchEngineCustomization policy is not set.
    edge_search_engine: Optional[EdgeSearchEngineBase] = None
    # Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer.
    edge_send_intranet_traffic_to_internet_explorer: Optional[bool] = None
    # Enable favorites sync between Internet Explorer and Microsoft Edge. Additions, deletions, modifications and order changes to favorites are shared between browsers.
    edge_sync_favorites_with_internet_explorer: Optional[bool] = None
    # Endpoint for discovering cloud printers.
    enterprise_cloud_print_discovery_end_point: Optional[str] = None
    # Maximum number of printers that should be queried from a discovery endpoint. This is a mobile only setting. Valid values 1 to 65535
    enterprise_cloud_print_discovery_max_limit: Optional[int] = None
    # OAuth resource URI for printer discovery service as configured in Azure portal.
    enterprise_cloud_print_mopria_discovery_resource_identifier: Optional[str] = None
    # Authentication endpoint for acquiring OAuth tokens.
    enterprise_cloud_print_o_auth_authority: Optional[str] = None
    # GUID of a client application authorized to retrieve OAuth tokens from the OAuth Authority.
    enterprise_cloud_print_o_auth_client_identifier: Optional[str] = None
    # OAuth resource URI for print service as configured in the Azure portal.
    enterprise_cloud_print_resource_identifier: Optional[str] = None
    # Indicates whether or not to enable device discovery UX.
    experience_block_device_discovery: Optional[bool] = None
    # Indicates whether or not to allow the error dialog from displaying if no SIM card is detected.
    experience_block_error_dialog_when_no_s_i_m: Optional[bool] = None
    # Indicates whether or not to enable task switching on the device.
    experience_block_task_switcher: Optional[bool] = None
    # Indicates whether or not to block DVR and broadcasting.
    game_dvr_blocked: Optional[bool] = None
    # Indicates whether or not to Block the user from using internet sharing.
    internet_sharing_blocked: Optional[bool] = None
    # Indicates whether or not to Block the user from location services.
    location_services_blocked: Optional[bool] = None
    # Specify whether to show a user-configurable setting to control the screen timeout while on the lock screen of Windows 10 Mobile devices. If this policy is set to Allow, the value set by lockScreenTimeoutInSeconds is ignored.
    lock_screen_allow_timeout_configuration: Optional[bool] = None
    # Indicates whether or not to block action center notifications over lock screen.
    lock_screen_block_action_center_notifications: Optional[bool] = None
    # Indicates whether or not the user can interact with Cortana using speech while the system is locked.
    lock_screen_block_cortana: Optional[bool] = None
    # Indicates whether to allow toast notifications above the device lock screen.
    lock_screen_block_toast_notifications: Optional[bool] = None
    # Set the duration (in seconds) from the screen locking to the screen turning off for Windows 10 Mobile devices. Supported values are 11-1800. Valid values 11 to 1800
    lock_screen_timeout_in_seconds: Optional[int] = None
    # Disables the ability to quickly switch between users that are logged on simultaneously without logging off.
    logon_block_fast_user_switching: Optional[bool] = None
    # Indicates whether or not to Block Microsoft account settings sync.
    microsoft_account_block_settings_sync: Optional[bool] = None
    # Indicates whether or not to Block a Microsoft account.
    microsoft_account_blocked: Optional[bool] = None
    # If set, proxy settings will be applied to all processes and accounts in the device. Otherwise, it will be applied to the user account that’s enrolled into MDM.
    network_proxy_apply_settings_device_wide: Optional[bool] = None
    # Address to the proxy auto-config (PAC) script you want to use.
    network_proxy_automatic_configuration_url: Optional[str] = None
    # Disable automatic detection of settings. If enabled, the system will try to find the path to a proxy auto-config (PAC) script.
    network_proxy_disable_auto_detect: Optional[bool] = None
    # Specifies manual proxy server settings.
    network_proxy_server: Optional[Windows10NetworkProxyServer] = None
    # Indicates whether or not to Block the user from using near field communication.
    nfc_blocked: Optional[bool] = None
    # Gets or sets a value allowing IT admins to prevent apps and features from working with files on OneDrive.
    one_drive_disable_file_sync: Optional[bool] = None
    # Specify whether PINs or passwords such as '1111' or '1234' are allowed. For Windows 10 desktops, it also controls the use of picture passwords.
    password_block_simple: Optional[bool] = None
    # The password expiration in days. Valid values 0 to 730
    password_expiration_days: Optional[int] = None
    # The number of character sets required in the password.
    password_minimum_character_set_count: Optional[int] = None
    # The minimum password length. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # The minutes of inactivity before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # The number of previous passwords to prevent reuse of. Valid values 0 to 50
    password_previous_password_block_count: Optional[int] = None
    # Indicates whether or not to require a password upon resuming from an idle state.
    password_require_when_resume_from_idle_state: Optional[bool] = None
    # Indicates whether or not to require the user to have a password.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # The number of sign in failures before factory reset. Valid values 0 to 999
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # A http or https Url to a jpg, jpeg or png image that needs to be downloaded and used as the Desktop Image or a file Url to a local image on the file system that needs to used as the Desktop Image.
    personalization_desktop_image_url: Optional[str] = None
    # A http or https Url to a jpg, jpeg or png image that neeeds to be downloaded and used as the Lock Screen Image or a file Url to a local image on the file system that needs to be used as the Lock Screen Image.
    personalization_lock_screen_image_url: Optional[str] = None
    # State Management Setting.
    privacy_advertising_id: Optional[StateManagementSetting] = None
    # Indicates whether or not to allow the automatic acceptance of the pairing and privacy user consent dialog when launching apps.
    privacy_auto_accept_pairing_and_consent_prompts: Optional[bool] = None
    # Indicates whether or not to block the usage of cloud based speech services for Cortana, Dictation, or Store applications.
    privacy_block_input_personalization: Optional[bool] = None
    # Indicates whether or not to Block the user from reset protection mode.
    reset_protection_mode_blocked: Optional[bool] = None
    # Specifies what level of safe search (filtering adult content) is required
    safe_search_filter: Optional[SafeSearchFilterType] = None
    # Indicates whether or not to Block the user from taking Screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Specifies if search can use diacritics.
    search_block_diacritics: Optional[bool] = None
    # Specifies whether to use automatic language detection when indexing content and properties.
    search_disable_auto_language_detection: Optional[bool] = None
    # Indicates whether or not to disable the search indexer backoff feature.
    search_disable_indexer_backoff: Optional[bool] = None
    # Indicates whether or not to block indexing of WIP-protected items to prevent them from appearing in search results for Cortana or Explorer.
    search_disable_indexing_encrypted_items: Optional[bool] = None
    # Indicates whether or not to allow users to add locations on removable drives to libraries and to be indexed.
    search_disable_indexing_removable_drive: Optional[bool] = None
    # Specifies minimum amount of hard drive space on the same drive as the index location before indexing stops.
    search_enable_automatic_index_size_manangement: Optional[bool] = None
    # Indicates whether or not to block remote queries of this computer’s index.
    search_enable_remote_queries: Optional[bool] = None
    # Indicates whether or not to block access to Accounts in Settings app.
    settings_block_accounts_page: Optional[bool] = None
    # Indicates whether or not to block the user from installing provisioning packages.
    settings_block_add_provisioning_package: Optional[bool] = None
    # Indicates whether or not to block access to Apps in Settings app.
    settings_block_apps_page: Optional[bool] = None
    # Indicates whether or not to block the user from changing the language settings.
    settings_block_change_language: Optional[bool] = None
    # Indicates whether or not to block the user from changing power and sleep settings.
    settings_block_change_power_sleep: Optional[bool] = None
    # Indicates whether or not to block the user from changing the region settings.
    settings_block_change_region: Optional[bool] = None
    # Indicates whether or not to block the user from changing date and time settings.
    settings_block_change_system_time: Optional[bool] = None
    # Indicates whether or not to block access to Devices in Settings app.
    settings_block_devices_page: Optional[bool] = None
    # Indicates whether or not to block access to Ease of Access in Settings app.
    settings_block_ease_of_access_page: Optional[bool] = None
    # Indicates whether or not to block the user from editing the device name.
    settings_block_edit_device_name: Optional[bool] = None
    # Indicates whether or not to block access to Gaming in Settings app.
    settings_block_gaming_page: Optional[bool] = None
    # Indicates whether or not to block access to Network & Internet in Settings app.
    settings_block_network_internet_page: Optional[bool] = None
    # Indicates whether or not to block access to Personalization in Settings app.
    settings_block_personalization_page: Optional[bool] = None
    # Indicates whether or not to block access to Privacy in Settings app.
    settings_block_privacy_page: Optional[bool] = None
    # Indicates whether or not to block the runtime configuration agent from removing provisioning packages.
    settings_block_remove_provisioning_package: Optional[bool] = None
    # Indicates whether or not to block access to Settings app.
    settings_block_settings_app: Optional[bool] = None
    # Indicates whether or not to block access to System in Settings app.
    settings_block_system_page: Optional[bool] = None
    # Indicates whether or not to block access to Time & Language in Settings app.
    settings_block_time_language_page: Optional[bool] = None
    # Indicates whether or not to block access to Update & Security in Settings app.
    settings_block_update_security_page: Optional[bool] = None
    # Indicates whether or not to block multiple users of the same app to share data.
    shared_user_app_data_allowed: Optional[bool] = None
    # Indicates whether or not users can override SmartScreen Filter warnings about potentially malicious websites.
    smart_screen_block_prompt_override: Optional[bool] = None
    # Indicates whether or not users can override the SmartScreen Filter warnings about downloading unverified files
    smart_screen_block_prompt_override_for_files: Optional[bool] = None
    # This property will be deprecated in July 2019 and will be replaced by property SmartScreenAppInstallControl. Allows IT Admins to control whether users are allowed to install apps from places other than the Store.
    smart_screen_enable_app_install_control: Optional[bool] = None
    # Indicates whether or not to block the user from unpinning apps from taskbar.
    start_block_unpinning_apps_from_taskbar: Optional[bool] = None
    # Type of start menu app list visibility.
    start_menu_app_list_visibility: Optional[WindowsStartMenuAppListVisibilityType] = None
    # Enabling this policy hides the change account setting from appearing in the user tile in the start menu.
    start_menu_hide_change_account_settings: Optional[bool] = None
    # Enabling this policy hides the most used apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
    start_menu_hide_frequently_used_apps: Optional[bool] = None
    # Enabling this policy hides hibernate from appearing in the power button in the start menu.
    start_menu_hide_hibernate: Optional[bool] = None
    # Enabling this policy hides lock from appearing in the user tile in the start menu.
    start_menu_hide_lock: Optional[bool] = None
    # Enabling this policy hides the power button from appearing in the start menu.
    start_menu_hide_power_button: Optional[bool] = None
    # Enabling this policy hides recent jump lists from appearing on the start menu/taskbar and disables the corresponding toggle in the Settings app.
    start_menu_hide_recent_jump_lists: Optional[bool] = None
    # Enabling this policy hides recently added apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
    start_menu_hide_recently_added_apps: Optional[bool] = None
    # Enabling this policy hides 'Restart/Update and Restart' from appearing in the power button in the start menu.
    start_menu_hide_restart_options: Optional[bool] = None
    # Enabling this policy hides shut down/update and shut down from appearing in the power button in the start menu.
    start_menu_hide_shut_down: Optional[bool] = None
    # Enabling this policy hides sign out from appearing in the user tile in the start menu.
    start_menu_hide_sign_out: Optional[bool] = None
    # Enabling this policy hides sleep from appearing in the power button in the start menu.
    start_menu_hide_sleep: Optional[bool] = None
    # Enabling this policy hides switch account from appearing in the user tile in the start menu.
    start_menu_hide_switch_account: Optional[bool] = None
    # Enabling this policy hides the user tile from appearing in the start menu.
    start_menu_hide_user_tile: Optional[bool] = None
    # This policy setting allows you to import Edge assets to be used with startMenuLayoutXml policy. Start layout can contain secondary tile from Edge app which looks for Edge local asset file. Edge local asset would not exist and cause Edge secondary tile to appear empty in this case. This policy only gets applied when startMenuLayoutXml policy is modified. The value should be a UTF-8 Base64 encoded byte array.
    start_menu_layout_edge_assets_xml: Optional[bytes] = None
    # Allows admins to override the default Start menu layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in a UTF8 encoded byte array format.
    start_menu_layout_xml: Optional[bytes] = None
    # Type of display modes for the start menu.
    start_menu_mode: Optional[WindowsStartMenuModeType] = None
    # Generic visibility state.
    start_menu_pinned_folder_documents: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_downloads: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_file_explorer: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_home_group: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_music: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_network: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_personal_folder: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_pictures: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_settings: Optional[VisibilitySetting] = None
    # Generic visibility state.
    start_menu_pinned_folder_videos: Optional[VisibilitySetting] = None
    # Indicates whether or not to Block the user from using removable storage.
    storage_block_removable_storage: Optional[bool] = None
    # Indicating whether or not to require encryption on a mobile device.
    storage_require_mobile_device_encryption: Optional[bool] = None
    # Indicates whether application data is restricted to the system drive.
    storage_restrict_app_data_to_system_volume: Optional[bool] = None
    # Indicates whether the installation of applications is restricted to the system drive.
    storage_restrict_app_install_to_system_volume: Optional[bool] = None
    # Whether the device is required to connect to the network.
    tenant_lockdown_require_network_during_out_of_box_experience: Optional[bool] = None
    # Indicates whether or not to Block the user from USB connection.
    usb_blocked: Optional[bool] = None
    # Indicates whether or not to Block the user from voice recording.
    voice_recording_blocked: Optional[bool] = None
    # Indicates whether or not user's localhost IP address is displayed while making phone calls using the WebRTC
    web_rtc_block_localhost_ip_address: Optional[bool] = None
    # Indicating whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
    wi_fi_block_automatic_connect_hotspots: Optional[bool] = None
    # Indicates whether or not to Block the user from using Wi-Fi manual configuration.
    wi_fi_block_manual_configuration: Optional[bool] = None
    # Indicates whether or not to Block the user from using Wi-Fi.
    wi_fi_blocked: Optional[bool] = None
    # Specify how often devices scan for Wi-Fi networks. Supported values are 1-500, where 100 = default, and 500 = low frequency. Valid values 1 to 500
    wi_fi_scan_interval: Optional[int] = None
    # Allows IT admins to block experiences that are typically for consumers only, such as Start suggestions, Membership notifications, Post-OOBE app install and redirect tiles.
    windows_spotlight_block_consumer_specific_features: Optional[bool] = None
    # Block suggestions from Microsoft that show after each OS clean install, upgrade or in an on-going basis to introduce users to what is new or changed
    windows_spotlight_block_on_action_center: Optional[bool] = None
    # Block personalized content in Windows spotlight based on user’s device usage.
    windows_spotlight_block_tailored_experiences: Optional[bool] = None
    # Block third party content delivered via Windows Spotlight
    windows_spotlight_block_third_party_notifications: Optional[bool] = None
    # Block Windows Spotlight Windows welcome experience
    windows_spotlight_block_welcome_experience: Optional[bool] = None
    # Allows IT admins to turn off the popup of Windows Tips.
    windows_spotlight_block_windows_tips: Optional[bool] = None
    # Allows IT admins to turn off all Windows Spotlight features
    windows_spotlight_blocked: Optional[bool] = None
    # Allows IT admind to set a predefined default search engine for MDM-Controlled devices
    windows_spotlight_configure_on_lock_screen: Optional[WindowsSpotlightEnablementSettings] = None
    # Indicates whether or not to block automatic update of apps from Windows Store.
    windows_store_block_auto_update: Optional[bool] = None
    # Indicates whether or not to Block the user from using the Windows store.
    windows_store_blocked: Optional[bool] = None
    # Indicates whether or not to enable Private Store Only.
    windows_store_enable_private_store_only: Optional[bool] = None
    # Indicates whether or not to allow other devices from discovering this PC for projection.
    wireless_display_block_projection_to_this_device: Optional[bool] = None
    # Indicates whether or not to allow user input from wireless display receiver.
    wireless_display_block_user_input_from_receiver: Optional[bool] = None
    # Indicates whether or not to require a PIN for new devices to initiate pairing.
    wireless_display_require_pin_for_pairing: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10GeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10GeneralConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10GeneralConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
        from .defender_detected_malware_actions import DefenderDetectedMalwareActions
        from .defender_monitor_file_activity import DefenderMonitorFileActivity
        from .defender_prompt_for_sample_submission import DefenderPromptForSampleSubmission
        from .defender_scan_type import DefenderScanType
        from .device_configuration import DeviceConfiguration
        from .diagnostic_data_submission_mode import DiagnosticDataSubmissionMode
        from .edge_cookie_policy import EdgeCookiePolicy
        from .edge_search_engine_base import EdgeSearchEngineBase
        from .required_password_type import RequiredPasswordType
        from .safe_search_filter_type import SafeSearchFilterType
        from .state_management_setting import StateManagementSetting
        from .visibility_setting import VisibilitySetting
        from .weekly_schedule import WeeklySchedule
        from .windows10_network_proxy_server import Windows10NetworkProxyServer
        from .windows_spotlight_enablement_settings import WindowsSpotlightEnablementSettings
        from .windows_start_menu_app_list_visibility_type import WindowsStartMenuAppListVisibilityType
        from .windows_start_menu_mode_type import WindowsStartMenuModeType

        from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
        from .defender_detected_malware_actions import DefenderDetectedMalwareActions
        from .defender_monitor_file_activity import DefenderMonitorFileActivity
        from .defender_prompt_for_sample_submission import DefenderPromptForSampleSubmission
        from .defender_scan_type import DefenderScanType
        from .device_configuration import DeviceConfiguration
        from .diagnostic_data_submission_mode import DiagnosticDataSubmissionMode
        from .edge_cookie_policy import EdgeCookiePolicy
        from .edge_search_engine_base import EdgeSearchEngineBase
        from .required_password_type import RequiredPasswordType
        from .safe_search_filter_type import SafeSearchFilterType
        from .state_management_setting import StateManagementSetting
        from .visibility_setting import VisibilitySetting
        from .weekly_schedule import WeeklySchedule
        from .windows10_network_proxy_server import Windows10NetworkProxyServer
        from .windows_spotlight_enablement_settings import WindowsSpotlightEnablementSettings
        from .windows_start_menu_app_list_visibility_type import WindowsStartMenuAppListVisibilityType
        from .windows_start_menu_mode_type import WindowsStartMenuModeType

        fields: Dict[str, Callable[[Any], None]] = {
            "accounts_block_adding_non_microsoft_account_email": lambda n : setattr(self, 'accounts_block_adding_non_microsoft_account_email', n.get_bool_value()),
            "anti_theft_mode_blocked": lambda n : setattr(self, 'anti_theft_mode_blocked', n.get_bool_value()),
            "apps_allow_trusted_apps_sideloading": lambda n : setattr(self, 'apps_allow_trusted_apps_sideloading', n.get_enum_value(StateManagementSetting)),
            "apps_block_windows_store_originated_apps": lambda n : setattr(self, 'apps_block_windows_store_originated_apps', n.get_bool_value()),
            "bluetooth_allowed_services": lambda n : setattr(self, 'bluetooth_allowed_services', n.get_collection_of_primitive_values(str)),
            "bluetooth_block_advertising": lambda n : setattr(self, 'bluetooth_block_advertising', n.get_bool_value()),
            "bluetooth_block_discoverable_mode": lambda n : setattr(self, 'bluetooth_block_discoverable_mode', n.get_bool_value()),
            "bluetooth_block_pre_pairing": lambda n : setattr(self, 'bluetooth_block_pre_pairing', n.get_bool_value()),
            "bluetooth_blocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_data_when_roaming": lambda n : setattr(self, 'cellular_block_data_when_roaming', n.get_bool_value()),
            "cellular_block_vpn": lambda n : setattr(self, 'cellular_block_vpn', n.get_bool_value()),
            "cellular_block_vpn_when_roaming": lambda n : setattr(self, 'cellular_block_vpn_when_roaming', n.get_bool_value()),
            "certificates_block_manual_root_certificate_installation": lambda n : setattr(self, 'certificates_block_manual_root_certificate_installation', n.get_bool_value()),
            "connected_devices_service_blocked": lambda n : setattr(self, 'connected_devices_service_blocked', n.get_bool_value()),
            "copy_paste_blocked": lambda n : setattr(self, 'copy_paste_blocked', n.get_bool_value()),
            "cortana_blocked": lambda n : setattr(self, 'cortana_blocked', n.get_bool_value()),
            "defender_block_end_user_access": lambda n : setattr(self, 'defender_block_end_user_access', n.get_bool_value()),
            "defender_cloud_block_level": lambda n : setattr(self, 'defender_cloud_block_level', n.get_enum_value(DefenderCloudBlockLevelType)),
            "defender_days_before_deleting_quarantined_malware": lambda n : setattr(self, 'defender_days_before_deleting_quarantined_malware', n.get_int_value()),
            "defender_detected_malware_actions": lambda n : setattr(self, 'defender_detected_malware_actions', n.get_object_value(DefenderDetectedMalwareActions)),
            "defender_file_extensions_to_exclude": lambda n : setattr(self, 'defender_file_extensions_to_exclude', n.get_collection_of_primitive_values(str)),
            "defender_files_and_folders_to_exclude": lambda n : setattr(self, 'defender_files_and_folders_to_exclude', n.get_collection_of_primitive_values(str)),
            "defender_monitor_file_activity": lambda n : setattr(self, 'defender_monitor_file_activity', n.get_enum_value(DefenderMonitorFileActivity)),
            "defender_processes_to_exclude": lambda n : setattr(self, 'defender_processes_to_exclude', n.get_collection_of_primitive_values(str)),
            "defender_prompt_for_sample_submission": lambda n : setattr(self, 'defender_prompt_for_sample_submission', n.get_enum_value(DefenderPromptForSampleSubmission)),
            "defender_require_behavior_monitoring": lambda n : setattr(self, 'defender_require_behavior_monitoring', n.get_bool_value()),
            "defender_require_cloud_protection": lambda n : setattr(self, 'defender_require_cloud_protection', n.get_bool_value()),
            "defender_require_network_inspection_system": lambda n : setattr(self, 'defender_require_network_inspection_system', n.get_bool_value()),
            "defender_require_real_time_monitoring": lambda n : setattr(self, 'defender_require_real_time_monitoring', n.get_bool_value()),
            "defender_scan_archive_files": lambda n : setattr(self, 'defender_scan_archive_files', n.get_bool_value()),
            "defender_scan_downloads": lambda n : setattr(self, 'defender_scan_downloads', n.get_bool_value()),
            "defender_scan_incoming_mail": lambda n : setattr(self, 'defender_scan_incoming_mail', n.get_bool_value()),
            "defender_scan_mapped_network_drives_during_full_scan": lambda n : setattr(self, 'defender_scan_mapped_network_drives_during_full_scan', n.get_bool_value()),
            "defender_scan_max_cpu": lambda n : setattr(self, 'defender_scan_max_cpu', n.get_int_value()),
            "defender_scan_network_files": lambda n : setattr(self, 'defender_scan_network_files', n.get_bool_value()),
            "defender_scan_removable_drives_during_full_scan": lambda n : setattr(self, 'defender_scan_removable_drives_during_full_scan', n.get_bool_value()),
            "defender_scan_scripts_loaded_in_internet_explorer": lambda n : setattr(self, 'defender_scan_scripts_loaded_in_internet_explorer', n.get_bool_value()),
            "defender_scan_type": lambda n : setattr(self, 'defender_scan_type', n.get_enum_value(DefenderScanType)),
            "defender_scheduled_quick_scan_time": lambda n : setattr(self, 'defender_scheduled_quick_scan_time', n.get_time_value()),
            "defender_scheduled_scan_time": lambda n : setattr(self, 'defender_scheduled_scan_time', n.get_time_value()),
            "defender_signature_update_interval_in_hours": lambda n : setattr(self, 'defender_signature_update_interval_in_hours', n.get_int_value()),
            "defender_system_scan_schedule": lambda n : setattr(self, 'defender_system_scan_schedule', n.get_enum_value(WeeklySchedule)),
            "developer_unlock_setting": lambda n : setattr(self, 'developer_unlock_setting', n.get_enum_value(StateManagementSetting)),
            "device_management_block_factory_reset_on_mobile": lambda n : setattr(self, 'device_management_block_factory_reset_on_mobile', n.get_bool_value()),
            "device_management_block_manual_unenroll": lambda n : setattr(self, 'device_management_block_manual_unenroll', n.get_bool_value()),
            "diagnostics_data_submission_mode": lambda n : setattr(self, 'diagnostics_data_submission_mode', n.get_enum_value(DiagnosticDataSubmissionMode)),
            "edge_allow_start_pages_modification": lambda n : setattr(self, 'edge_allow_start_pages_modification', n.get_bool_value()),
            "edge_block_access_to_about_flags": lambda n : setattr(self, 'edge_block_access_to_about_flags', n.get_bool_value()),
            "edge_block_address_bar_dropdown": lambda n : setattr(self, 'edge_block_address_bar_dropdown', n.get_bool_value()),
            "edge_block_autofill": lambda n : setattr(self, 'edge_block_autofill', n.get_bool_value()),
            "edge_block_compatibility_list": lambda n : setattr(self, 'edge_block_compatibility_list', n.get_bool_value()),
            "edge_block_developer_tools": lambda n : setattr(self, 'edge_block_developer_tools', n.get_bool_value()),
            "edge_block_extensions": lambda n : setattr(self, 'edge_block_extensions', n.get_bool_value()),
            "edge_block_in_private_browsing": lambda n : setattr(self, 'edge_block_in_private_browsing', n.get_bool_value()),
            "edge_block_java_script": lambda n : setattr(self, 'edge_block_java_script', n.get_bool_value()),
            "edge_block_live_tile_data_collection": lambda n : setattr(self, 'edge_block_live_tile_data_collection', n.get_bool_value()),
            "edge_block_password_manager": lambda n : setattr(self, 'edge_block_password_manager', n.get_bool_value()),
            "edge_block_popups": lambda n : setattr(self, 'edge_block_popups', n.get_bool_value()),
            "edge_block_search_suggestions": lambda n : setattr(self, 'edge_block_search_suggestions', n.get_bool_value()),
            "edge_block_sending_do_not_track_header": lambda n : setattr(self, 'edge_block_sending_do_not_track_header', n.get_bool_value()),
            "edge_block_sending_intranet_traffic_to_internet_explorer": lambda n : setattr(self, 'edge_block_sending_intranet_traffic_to_internet_explorer', n.get_bool_value()),
            "edge_blocked": lambda n : setattr(self, 'edge_blocked', n.get_bool_value()),
            "edge_clear_browsing_data_on_exit": lambda n : setattr(self, 'edge_clear_browsing_data_on_exit', n.get_bool_value()),
            "edge_cookie_policy": lambda n : setattr(self, 'edge_cookie_policy', n.get_enum_value(EdgeCookiePolicy)),
            "edge_disable_first_run_page": lambda n : setattr(self, 'edge_disable_first_run_page', n.get_bool_value()),
            "edge_enterprise_mode_site_list_location": lambda n : setattr(self, 'edge_enterprise_mode_site_list_location', n.get_str_value()),
            "edge_first_run_url": lambda n : setattr(self, 'edge_first_run_url', n.get_str_value()),
            "edge_homepage_urls": lambda n : setattr(self, 'edge_homepage_urls', n.get_collection_of_primitive_values(str)),
            "edge_require_smart_screen": lambda n : setattr(self, 'edge_require_smart_screen', n.get_bool_value()),
            "edge_search_engine": lambda n : setattr(self, 'edge_search_engine', n.get_object_value(EdgeSearchEngineBase)),
            "edge_send_intranet_traffic_to_internet_explorer": lambda n : setattr(self, 'edge_send_intranet_traffic_to_internet_explorer', n.get_bool_value()),
            "edge_sync_favorites_with_internet_explorer": lambda n : setattr(self, 'edge_sync_favorites_with_internet_explorer', n.get_bool_value()),
            "enterprise_cloud_print_discovery_end_point": lambda n : setattr(self, 'enterprise_cloud_print_discovery_end_point', n.get_str_value()),
            "enterprise_cloud_print_discovery_max_limit": lambda n : setattr(self, 'enterprise_cloud_print_discovery_max_limit', n.get_int_value()),
            "enterprise_cloud_print_mopria_discovery_resource_identifier": lambda n : setattr(self, 'enterprise_cloud_print_mopria_discovery_resource_identifier', n.get_str_value()),
            "enterprise_cloud_print_o_auth_authority": lambda n : setattr(self, 'enterprise_cloud_print_o_auth_authority', n.get_str_value()),
            "enterprise_cloud_print_o_auth_client_identifier": lambda n : setattr(self, 'enterprise_cloud_print_o_auth_client_identifier', n.get_str_value()),
            "enterprise_cloud_print_resource_identifier": lambda n : setattr(self, 'enterprise_cloud_print_resource_identifier', n.get_str_value()),
            "experience_block_device_discovery": lambda n : setattr(self, 'experience_block_device_discovery', n.get_bool_value()),
            "experience_block_error_dialog_when_no_s_i_m": lambda n : setattr(self, 'experience_block_error_dialog_when_no_s_i_m', n.get_bool_value()),
            "experience_block_task_switcher": lambda n : setattr(self, 'experience_block_task_switcher', n.get_bool_value()),
            "game_dvr_blocked": lambda n : setattr(self, 'game_dvr_blocked', n.get_bool_value()),
            "internet_sharing_blocked": lambda n : setattr(self, 'internet_sharing_blocked', n.get_bool_value()),
            "location_services_blocked": lambda n : setattr(self, 'location_services_blocked', n.get_bool_value()),
            "lock_screen_allow_timeout_configuration": lambda n : setattr(self, 'lock_screen_allow_timeout_configuration', n.get_bool_value()),
            "lock_screen_block_action_center_notifications": lambda n : setattr(self, 'lock_screen_block_action_center_notifications', n.get_bool_value()),
            "lock_screen_block_cortana": lambda n : setattr(self, 'lock_screen_block_cortana', n.get_bool_value()),
            "lock_screen_block_toast_notifications": lambda n : setattr(self, 'lock_screen_block_toast_notifications', n.get_bool_value()),
            "lock_screen_timeout_in_seconds": lambda n : setattr(self, 'lock_screen_timeout_in_seconds', n.get_int_value()),
            "logon_block_fast_user_switching": lambda n : setattr(self, 'logon_block_fast_user_switching', n.get_bool_value()),
            "microsoft_account_block_settings_sync": lambda n : setattr(self, 'microsoft_account_block_settings_sync', n.get_bool_value()),
            "microsoft_account_blocked": lambda n : setattr(self, 'microsoft_account_blocked', n.get_bool_value()),
            "network_proxy_apply_settings_device_wide": lambda n : setattr(self, 'network_proxy_apply_settings_device_wide', n.get_bool_value()),
            "network_proxy_automatic_configuration_url": lambda n : setattr(self, 'network_proxy_automatic_configuration_url', n.get_str_value()),
            "network_proxy_disable_auto_detect": lambda n : setattr(self, 'network_proxy_disable_auto_detect', n.get_bool_value()),
            "network_proxy_server": lambda n : setattr(self, 'network_proxy_server', n.get_object_value(Windows10NetworkProxyServer)),
            "nfc_blocked": lambda n : setattr(self, 'nfc_blocked', n.get_bool_value()),
            "one_drive_disable_file_sync": lambda n : setattr(self, 'one_drive_disable_file_sync', n.get_bool_value()),
            "password_block_simple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_character_set_count": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_require_when_resume_from_idle_state": lambda n : setattr(self, 'password_require_when_resume_from_idle_state', n.get_bool_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "personalization_desktop_image_url": lambda n : setattr(self, 'personalization_desktop_image_url', n.get_str_value()),
            "personalization_lock_screen_image_url": lambda n : setattr(self, 'personalization_lock_screen_image_url', n.get_str_value()),
            "privacy_advertising_id": lambda n : setattr(self, 'privacy_advertising_id', n.get_enum_value(StateManagementSetting)),
            "privacy_auto_accept_pairing_and_consent_prompts": lambda n : setattr(self, 'privacy_auto_accept_pairing_and_consent_prompts', n.get_bool_value()),
            "privacy_block_input_personalization": lambda n : setattr(self, 'privacy_block_input_personalization', n.get_bool_value()),
            "reset_protection_mode_blocked": lambda n : setattr(self, 'reset_protection_mode_blocked', n.get_bool_value()),
            "safe_search_filter": lambda n : setattr(self, 'safe_search_filter', n.get_enum_value(SafeSearchFilterType)),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "search_block_diacritics": lambda n : setattr(self, 'search_block_diacritics', n.get_bool_value()),
            "search_disable_auto_language_detection": lambda n : setattr(self, 'search_disable_auto_language_detection', n.get_bool_value()),
            "search_disable_indexer_backoff": lambda n : setattr(self, 'search_disable_indexer_backoff', n.get_bool_value()),
            "search_disable_indexing_encrypted_items": lambda n : setattr(self, 'search_disable_indexing_encrypted_items', n.get_bool_value()),
            "search_disable_indexing_removable_drive": lambda n : setattr(self, 'search_disable_indexing_removable_drive', n.get_bool_value()),
            "search_enable_automatic_index_size_manangement": lambda n : setattr(self, 'search_enable_automatic_index_size_manangement', n.get_bool_value()),
            "search_enable_remote_queries": lambda n : setattr(self, 'search_enable_remote_queries', n.get_bool_value()),
            "settings_block_accounts_page": lambda n : setattr(self, 'settings_block_accounts_page', n.get_bool_value()),
            "settings_block_add_provisioning_package": lambda n : setattr(self, 'settings_block_add_provisioning_package', n.get_bool_value()),
            "settings_block_apps_page": lambda n : setattr(self, 'settings_block_apps_page', n.get_bool_value()),
            "settings_block_change_language": lambda n : setattr(self, 'settings_block_change_language', n.get_bool_value()),
            "settings_block_change_power_sleep": lambda n : setattr(self, 'settings_block_change_power_sleep', n.get_bool_value()),
            "settings_block_change_region": lambda n : setattr(self, 'settings_block_change_region', n.get_bool_value()),
            "settings_block_change_system_time": lambda n : setattr(self, 'settings_block_change_system_time', n.get_bool_value()),
            "settings_block_devices_page": lambda n : setattr(self, 'settings_block_devices_page', n.get_bool_value()),
            "settings_block_ease_of_access_page": lambda n : setattr(self, 'settings_block_ease_of_access_page', n.get_bool_value()),
            "settings_block_edit_device_name": lambda n : setattr(self, 'settings_block_edit_device_name', n.get_bool_value()),
            "settings_block_gaming_page": lambda n : setattr(self, 'settings_block_gaming_page', n.get_bool_value()),
            "settings_block_network_internet_page": lambda n : setattr(self, 'settings_block_network_internet_page', n.get_bool_value()),
            "settings_block_personalization_page": lambda n : setattr(self, 'settings_block_personalization_page', n.get_bool_value()),
            "settings_block_privacy_page": lambda n : setattr(self, 'settings_block_privacy_page', n.get_bool_value()),
            "settings_block_remove_provisioning_package": lambda n : setattr(self, 'settings_block_remove_provisioning_package', n.get_bool_value()),
            "settings_block_settings_app": lambda n : setattr(self, 'settings_block_settings_app', n.get_bool_value()),
            "settings_block_system_page": lambda n : setattr(self, 'settings_block_system_page', n.get_bool_value()),
            "settings_block_time_language_page": lambda n : setattr(self, 'settings_block_time_language_page', n.get_bool_value()),
            "settings_block_update_security_page": lambda n : setattr(self, 'settings_block_update_security_page', n.get_bool_value()),
            "shared_user_app_data_allowed": lambda n : setattr(self, 'shared_user_app_data_allowed', n.get_bool_value()),
            "smart_screen_block_prompt_override": lambda n : setattr(self, 'smart_screen_block_prompt_override', n.get_bool_value()),
            "smart_screen_block_prompt_override_for_files": lambda n : setattr(self, 'smart_screen_block_prompt_override_for_files', n.get_bool_value()),
            "smart_screen_enable_app_install_control": lambda n : setattr(self, 'smart_screen_enable_app_install_control', n.get_bool_value()),
            "start_block_unpinning_apps_from_taskbar": lambda n : setattr(self, 'start_block_unpinning_apps_from_taskbar', n.get_bool_value()),
            "start_menu_app_list_visibility": lambda n : setattr(self, 'start_menu_app_list_visibility', n.get_collection_of_enum_values(WindowsStartMenuAppListVisibilityType)),
            "start_menu_hide_change_account_settings": lambda n : setattr(self, 'start_menu_hide_change_account_settings', n.get_bool_value()),
            "start_menu_hide_frequently_used_apps": lambda n : setattr(self, 'start_menu_hide_frequently_used_apps', n.get_bool_value()),
            "start_menu_hide_hibernate": lambda n : setattr(self, 'start_menu_hide_hibernate', n.get_bool_value()),
            "start_menu_hide_lock": lambda n : setattr(self, 'start_menu_hide_lock', n.get_bool_value()),
            "start_menu_hide_power_button": lambda n : setattr(self, 'start_menu_hide_power_button', n.get_bool_value()),
            "start_menu_hide_recent_jump_lists": lambda n : setattr(self, 'start_menu_hide_recent_jump_lists', n.get_bool_value()),
            "start_menu_hide_recently_added_apps": lambda n : setattr(self, 'start_menu_hide_recently_added_apps', n.get_bool_value()),
            "start_menu_hide_restart_options": lambda n : setattr(self, 'start_menu_hide_restart_options', n.get_bool_value()),
            "start_menu_hide_shut_down": lambda n : setattr(self, 'start_menu_hide_shut_down', n.get_bool_value()),
            "start_menu_hide_sign_out": lambda n : setattr(self, 'start_menu_hide_sign_out', n.get_bool_value()),
            "start_menu_hide_sleep": lambda n : setattr(self, 'start_menu_hide_sleep', n.get_bool_value()),
            "start_menu_hide_switch_account": lambda n : setattr(self, 'start_menu_hide_switch_account', n.get_bool_value()),
            "start_menu_hide_user_tile": lambda n : setattr(self, 'start_menu_hide_user_tile', n.get_bool_value()),
            "start_menu_layout_edge_assets_xml": lambda n : setattr(self, 'start_menu_layout_edge_assets_xml', n.get_bytes_value()),
            "start_menu_layout_xml": lambda n : setattr(self, 'start_menu_layout_xml', n.get_bytes_value()),
            "start_menu_mode": lambda n : setattr(self, 'start_menu_mode', n.get_enum_value(WindowsStartMenuModeType)),
            "start_menu_pinned_folder_documents": lambda n : setattr(self, 'start_menu_pinned_folder_documents', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_downloads": lambda n : setattr(self, 'start_menu_pinned_folder_downloads', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_file_explorer": lambda n : setattr(self, 'start_menu_pinned_folder_file_explorer', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_home_group": lambda n : setattr(self, 'start_menu_pinned_folder_home_group', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_music": lambda n : setattr(self, 'start_menu_pinned_folder_music', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_network": lambda n : setattr(self, 'start_menu_pinned_folder_network', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_personal_folder": lambda n : setattr(self, 'start_menu_pinned_folder_personal_folder', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_pictures": lambda n : setattr(self, 'start_menu_pinned_folder_pictures', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_settings": lambda n : setattr(self, 'start_menu_pinned_folder_settings', n.get_enum_value(VisibilitySetting)),
            "start_menu_pinned_folder_videos": lambda n : setattr(self, 'start_menu_pinned_folder_videos', n.get_enum_value(VisibilitySetting)),
            "storage_block_removable_storage": lambda n : setattr(self, 'storage_block_removable_storage', n.get_bool_value()),
            "storage_require_mobile_device_encryption": lambda n : setattr(self, 'storage_require_mobile_device_encryption', n.get_bool_value()),
            "storage_restrict_app_data_to_system_volume": lambda n : setattr(self, 'storage_restrict_app_data_to_system_volume', n.get_bool_value()),
            "storage_restrict_app_install_to_system_volume": lambda n : setattr(self, 'storage_restrict_app_install_to_system_volume', n.get_bool_value()),
            "tenant_lockdown_require_network_during_out_of_box_experience": lambda n : setattr(self, 'tenant_lockdown_require_network_during_out_of_box_experience', n.get_bool_value()),
            "usb_blocked": lambda n : setattr(self, 'usb_blocked', n.get_bool_value()),
            "voice_recording_blocked": lambda n : setattr(self, 'voice_recording_blocked', n.get_bool_value()),
            "web_rtc_block_localhost_ip_address": lambda n : setattr(self, 'web_rtc_block_localhost_ip_address', n.get_bool_value()),
            "wi_fi_block_automatic_connect_hotspots": lambda n : setattr(self, 'wi_fi_block_automatic_connect_hotspots', n.get_bool_value()),
            "wi_fi_block_manual_configuration": lambda n : setattr(self, 'wi_fi_block_manual_configuration', n.get_bool_value()),
            "wi_fi_blocked": lambda n : setattr(self, 'wi_fi_blocked', n.get_bool_value()),
            "wi_fi_scan_interval": lambda n : setattr(self, 'wi_fi_scan_interval', n.get_int_value()),
            "windows_spotlight_block_consumer_specific_features": lambda n : setattr(self, 'windows_spotlight_block_consumer_specific_features', n.get_bool_value()),
            "windows_spotlight_block_on_action_center": lambda n : setattr(self, 'windows_spotlight_block_on_action_center', n.get_bool_value()),
            "windows_spotlight_block_tailored_experiences": lambda n : setattr(self, 'windows_spotlight_block_tailored_experiences', n.get_bool_value()),
            "windows_spotlight_block_third_party_notifications": lambda n : setattr(self, 'windows_spotlight_block_third_party_notifications', n.get_bool_value()),
            "windows_spotlight_block_welcome_experience": lambda n : setattr(self, 'windows_spotlight_block_welcome_experience', n.get_bool_value()),
            "windows_spotlight_block_windows_tips": lambda n : setattr(self, 'windows_spotlight_block_windows_tips', n.get_bool_value()),
            "windows_spotlight_blocked": lambda n : setattr(self, 'windows_spotlight_blocked', n.get_bool_value()),
            "windows_spotlight_configure_on_lock_screen": lambda n : setattr(self, 'windows_spotlight_configure_on_lock_screen', n.get_enum_value(WindowsSpotlightEnablementSettings)),
            "windows_store_block_auto_update": lambda n : setattr(self, 'windows_store_block_auto_update', n.get_bool_value()),
            "windows_store_blocked": lambda n : setattr(self, 'windows_store_blocked', n.get_bool_value()),
            "windows_store_enable_private_store_only": lambda n : setattr(self, 'windows_store_enable_private_store_only', n.get_bool_value()),
            "wireless_display_block_projection_to_this_device": lambda n : setattr(self, 'wireless_display_block_projection_to_this_device', n.get_bool_value()),
            "wireless_display_block_user_input_from_receiver": lambda n : setattr(self, 'wireless_display_block_user_input_from_receiver', n.get_bool_value()),
            "wireless_display_require_pin_for_pairing": lambda n : setattr(self, 'wireless_display_require_pin_for_pairing', n.get_bool_value()),
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
        writer.write_bool_value("accounts_block_adding_non_microsoft_account_email", self.accounts_block_adding_non_microsoft_account_email)
        writer.write_bool_value("anti_theft_mode_blocked", self.anti_theft_mode_blocked)
        writer.write_enum_value("apps_allow_trusted_apps_sideloading", self.apps_allow_trusted_apps_sideloading)
        writer.write_bool_value("apps_block_windows_store_originated_apps", self.apps_block_windows_store_originated_apps)
        writer.write_collection_of_primitive_values("bluetooth_allowed_services", self.bluetooth_allowed_services)
        writer.write_bool_value("bluetooth_block_advertising", self.bluetooth_block_advertising)
        writer.write_bool_value("bluetooth_block_discoverable_mode", self.bluetooth_block_discoverable_mode)
        writer.write_bool_value("bluetooth_block_pre_pairing", self.bluetooth_block_pre_pairing)
        writer.write_bool_value("bluetooth_blocked", self.bluetooth_blocked)
        writer.write_bool_value("camera_blocked", self.camera_blocked)
        writer.write_bool_value("cellular_block_data_when_roaming", self.cellular_block_data_when_roaming)
        writer.write_bool_value("cellular_block_vpn", self.cellular_block_vpn)
        writer.write_bool_value("cellular_block_vpn_when_roaming", self.cellular_block_vpn_when_roaming)
        writer.write_bool_value("certificates_block_manual_root_certificate_installation", self.certificates_block_manual_root_certificate_installation)
        writer.write_bool_value("connected_devices_service_blocked", self.connected_devices_service_blocked)
        writer.write_bool_value("copy_paste_blocked", self.copy_paste_blocked)
        writer.write_bool_value("cortana_blocked", self.cortana_blocked)
        writer.write_bool_value("defender_block_end_user_access", self.defender_block_end_user_access)
        writer.write_enum_value("defender_cloud_block_level", self.defender_cloud_block_level)
        writer.write_int_value("defender_days_before_deleting_quarantined_malware", self.defender_days_before_deleting_quarantined_malware)
        writer.write_object_value("defender_detected_malware_actions", self.defender_detected_malware_actions)
        writer.write_collection_of_primitive_values("defender_file_extensions_to_exclude", self.defender_file_extensions_to_exclude)
        writer.write_collection_of_primitive_values("defender_files_and_folders_to_exclude", self.defender_files_and_folders_to_exclude)
        writer.write_enum_value("defender_monitor_file_activity", self.defender_monitor_file_activity)
        writer.write_collection_of_primitive_values("defender_processes_to_exclude", self.defender_processes_to_exclude)
        writer.write_enum_value("defender_prompt_for_sample_submission", self.defender_prompt_for_sample_submission)
        writer.write_bool_value("defender_require_behavior_monitoring", self.defender_require_behavior_monitoring)
        writer.write_bool_value("defender_require_cloud_protection", self.defender_require_cloud_protection)
        writer.write_bool_value("defender_require_network_inspection_system", self.defender_require_network_inspection_system)
        writer.write_bool_value("defender_require_real_time_monitoring", self.defender_require_real_time_monitoring)
        writer.write_bool_value("defender_scan_archive_files", self.defender_scan_archive_files)
        writer.write_bool_value("defender_scan_downloads", self.defender_scan_downloads)
        writer.write_bool_value("defender_scan_incoming_mail", self.defender_scan_incoming_mail)
        writer.write_bool_value("defender_scan_mapped_network_drives_during_full_scan", self.defender_scan_mapped_network_drives_during_full_scan)
        writer.write_int_value("defender_scan_max_cpu", self.defender_scan_max_cpu)
        writer.write_bool_value("defender_scan_network_files", self.defender_scan_network_files)
        writer.write_bool_value("defender_scan_removable_drives_during_full_scan", self.defender_scan_removable_drives_during_full_scan)
        writer.write_bool_value("defender_scan_scripts_loaded_in_internet_explorer", self.defender_scan_scripts_loaded_in_internet_explorer)
        writer.write_enum_value("defender_scan_type", self.defender_scan_type)
        writer.write_time_value("defender_scheduled_quick_scan_time", self.defender_scheduled_quick_scan_time)
        writer.write_time_value("defender_scheduled_scan_time", self.defender_scheduled_scan_time)
        writer.write_int_value("defender_signature_update_interval_in_hours", self.defender_signature_update_interval_in_hours)
        writer.write_enum_value("defender_system_scan_schedule", self.defender_system_scan_schedule)
        writer.write_enum_value("developer_unlock_setting", self.developer_unlock_setting)
        writer.write_bool_value("device_management_block_factory_reset_on_mobile", self.device_management_block_factory_reset_on_mobile)
        writer.write_bool_value("device_management_block_manual_unenroll", self.device_management_block_manual_unenroll)
        writer.write_enum_value("diagnostics_data_submission_mode", self.diagnostics_data_submission_mode)
        writer.write_bool_value("edge_allow_start_pages_modification", self.edge_allow_start_pages_modification)
        writer.write_bool_value("edge_block_access_to_about_flags", self.edge_block_access_to_about_flags)
        writer.write_bool_value("edge_block_address_bar_dropdown", self.edge_block_address_bar_dropdown)
        writer.write_bool_value("edge_block_autofill", self.edge_block_autofill)
        writer.write_bool_value("edge_block_compatibility_list", self.edge_block_compatibility_list)
        writer.write_bool_value("edge_block_developer_tools", self.edge_block_developer_tools)
        writer.write_bool_value("edge_block_extensions", self.edge_block_extensions)
        writer.write_bool_value("edge_block_in_private_browsing", self.edge_block_in_private_browsing)
        writer.write_bool_value("edge_block_java_script", self.edge_block_java_script)
        writer.write_bool_value("edge_block_live_tile_data_collection", self.edge_block_live_tile_data_collection)
        writer.write_bool_value("edge_block_password_manager", self.edge_block_password_manager)
        writer.write_bool_value("edge_block_popups", self.edge_block_popups)
        writer.write_bool_value("edge_block_search_suggestions", self.edge_block_search_suggestions)
        writer.write_bool_value("edge_block_sending_do_not_track_header", self.edge_block_sending_do_not_track_header)
        writer.write_bool_value("edge_block_sending_intranet_traffic_to_internet_explorer", self.edge_block_sending_intranet_traffic_to_internet_explorer)
        writer.write_bool_value("edge_blocked", self.edge_blocked)
        writer.write_bool_value("edge_clear_browsing_data_on_exit", self.edge_clear_browsing_data_on_exit)
        writer.write_enum_value("edge_cookie_policy", self.edge_cookie_policy)
        writer.write_bool_value("edge_disable_first_run_page", self.edge_disable_first_run_page)
        writer.write_str_value("edge_enterprise_mode_site_list_location", self.edge_enterprise_mode_site_list_location)
        writer.write_str_value("edge_first_run_url", self.edge_first_run_url)
        writer.write_collection_of_primitive_values("edge_homepage_urls", self.edge_homepage_urls)
        writer.write_bool_value("edge_require_smart_screen", self.edge_require_smart_screen)
        writer.write_object_value("edge_search_engine", self.edge_search_engine)
        writer.write_bool_value("edge_send_intranet_traffic_to_internet_explorer", self.edge_send_intranet_traffic_to_internet_explorer)
        writer.write_bool_value("edge_sync_favorites_with_internet_explorer", self.edge_sync_favorites_with_internet_explorer)
        writer.write_str_value("enterprise_cloud_print_discovery_end_point", self.enterprise_cloud_print_discovery_end_point)
        writer.write_int_value("enterprise_cloud_print_discovery_max_limit", self.enterprise_cloud_print_discovery_max_limit)
        writer.write_str_value("enterprise_cloud_print_mopria_discovery_resource_identifier", self.enterprise_cloud_print_mopria_discovery_resource_identifier)
        writer.write_str_value("enterprise_cloud_print_o_auth_authority", self.enterprise_cloud_print_o_auth_authority)
        writer.write_str_value("enterprise_cloud_print_o_auth_client_identifier", self.enterprise_cloud_print_o_auth_client_identifier)
        writer.write_str_value("enterprise_cloud_print_resource_identifier", self.enterprise_cloud_print_resource_identifier)
        writer.write_bool_value("experience_block_device_discovery", self.experience_block_device_discovery)
        writer.write_bool_value("experience_block_error_dialog_when_no_s_i_m", self.experience_block_error_dialog_when_no_s_i_m)
        writer.write_bool_value("experience_block_task_switcher", self.experience_block_task_switcher)
        writer.write_bool_value("game_dvr_blocked", self.game_dvr_blocked)
        writer.write_bool_value("internet_sharing_blocked", self.internet_sharing_blocked)
        writer.write_bool_value("location_services_blocked", self.location_services_blocked)
        writer.write_bool_value("lock_screen_allow_timeout_configuration", self.lock_screen_allow_timeout_configuration)
        writer.write_bool_value("lock_screen_block_action_center_notifications", self.lock_screen_block_action_center_notifications)
        writer.write_bool_value("lock_screen_block_cortana", self.lock_screen_block_cortana)
        writer.write_bool_value("lock_screen_block_toast_notifications", self.lock_screen_block_toast_notifications)
        writer.write_int_value("lock_screen_timeout_in_seconds", self.lock_screen_timeout_in_seconds)
        writer.write_bool_value("logon_block_fast_user_switching", self.logon_block_fast_user_switching)
        writer.write_bool_value("microsoft_account_block_settings_sync", self.microsoft_account_block_settings_sync)
        writer.write_bool_value("microsoft_account_blocked", self.microsoft_account_blocked)
        writer.write_bool_value("network_proxy_apply_settings_device_wide", self.network_proxy_apply_settings_device_wide)
        writer.write_str_value("network_proxy_automatic_configuration_url", self.network_proxy_automatic_configuration_url)
        writer.write_bool_value("network_proxy_disable_auto_detect", self.network_proxy_disable_auto_detect)
        writer.write_object_value("network_proxy_server", self.network_proxy_server)
        writer.write_bool_value("nfc_blocked", self.nfc_blocked)
        writer.write_bool_value("one_drive_disable_file_sync", self.one_drive_disable_file_sync)
        writer.write_bool_value("password_block_simple", self.password_block_simple)
        writer.write_int_value("password_expiration_days", self.password_expiration_days)
        writer.write_int_value("password_minimum_character_set_count", self.password_minimum_character_set_count)
        writer.write_int_value("password_minimum_length", self.password_minimum_length)
        writer.write_int_value("password_minutes_of_inactivity_before_screen_timeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("password_previous_password_block_count", self.password_previous_password_block_count)
        writer.write_bool_value("password_require_when_resume_from_idle_state", self.password_require_when_resume_from_idle_state)
        writer.write_bool_value("password_required", self.password_required)
        writer.write_enum_value("password_required_type", self.password_required_type)
        writer.write_int_value("password_sign_in_failure_count_before_factory_reset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_str_value("personalization_desktop_image_url", self.personalization_desktop_image_url)
        writer.write_str_value("personalization_lock_screen_image_url", self.personalization_lock_screen_image_url)
        writer.write_enum_value("privacy_advertising_id", self.privacy_advertising_id)
        writer.write_bool_value("privacy_auto_accept_pairing_and_consent_prompts", self.privacy_auto_accept_pairing_and_consent_prompts)
        writer.write_bool_value("privacy_block_input_personalization", self.privacy_block_input_personalization)
        writer.write_bool_value("reset_protection_mode_blocked", self.reset_protection_mode_blocked)
        writer.write_enum_value("safe_search_filter", self.safe_search_filter)
        writer.write_bool_value("screen_capture_blocked", self.screen_capture_blocked)
        writer.write_bool_value("search_block_diacritics", self.search_block_diacritics)
        writer.write_bool_value("search_disable_auto_language_detection", self.search_disable_auto_language_detection)
        writer.write_bool_value("search_disable_indexer_backoff", self.search_disable_indexer_backoff)
        writer.write_bool_value("search_disable_indexing_encrypted_items", self.search_disable_indexing_encrypted_items)
        writer.write_bool_value("search_disable_indexing_removable_drive", self.search_disable_indexing_removable_drive)
        writer.write_bool_value("search_enable_automatic_index_size_manangement", self.search_enable_automatic_index_size_manangement)
        writer.write_bool_value("search_enable_remote_queries", self.search_enable_remote_queries)
        writer.write_bool_value("settings_block_accounts_page", self.settings_block_accounts_page)
        writer.write_bool_value("settings_block_add_provisioning_package", self.settings_block_add_provisioning_package)
        writer.write_bool_value("settings_block_apps_page", self.settings_block_apps_page)
        writer.write_bool_value("settings_block_change_language", self.settings_block_change_language)
        writer.write_bool_value("settings_block_change_power_sleep", self.settings_block_change_power_sleep)
        writer.write_bool_value("settings_block_change_region", self.settings_block_change_region)
        writer.write_bool_value("settings_block_change_system_time", self.settings_block_change_system_time)
        writer.write_bool_value("settings_block_devices_page", self.settings_block_devices_page)
        writer.write_bool_value("settings_block_ease_of_access_page", self.settings_block_ease_of_access_page)
        writer.write_bool_value("settings_block_edit_device_name", self.settings_block_edit_device_name)
        writer.write_bool_value("settings_block_gaming_page", self.settings_block_gaming_page)
        writer.write_bool_value("settings_block_network_internet_page", self.settings_block_network_internet_page)
        writer.write_bool_value("settings_block_personalization_page", self.settings_block_personalization_page)
        writer.write_bool_value("settings_block_privacy_page", self.settings_block_privacy_page)
        writer.write_bool_value("settings_block_remove_provisioning_package", self.settings_block_remove_provisioning_package)
        writer.write_bool_value("settings_block_settings_app", self.settings_block_settings_app)
        writer.write_bool_value("settings_block_system_page", self.settings_block_system_page)
        writer.write_bool_value("settings_block_time_language_page", self.settings_block_time_language_page)
        writer.write_bool_value("settings_block_update_security_page", self.settings_block_update_security_page)
        writer.write_bool_value("shared_user_app_data_allowed", self.shared_user_app_data_allowed)
        writer.write_bool_value("smart_screen_block_prompt_override", self.smart_screen_block_prompt_override)
        writer.write_bool_value("smart_screen_block_prompt_override_for_files", self.smart_screen_block_prompt_override_for_files)
        writer.write_bool_value("smart_screen_enable_app_install_control", self.smart_screen_enable_app_install_control)
        writer.write_bool_value("start_block_unpinning_apps_from_taskbar", self.start_block_unpinning_apps_from_taskbar)
        writer.write_enum_value("start_menu_app_list_visibility", self.start_menu_app_list_visibility)
        writer.write_bool_value("start_menu_hide_change_account_settings", self.start_menu_hide_change_account_settings)
        writer.write_bool_value("start_menu_hide_frequently_used_apps", self.start_menu_hide_frequently_used_apps)
        writer.write_bool_value("start_menu_hide_hibernate", self.start_menu_hide_hibernate)
        writer.write_bool_value("start_menu_hide_lock", self.start_menu_hide_lock)
        writer.write_bool_value("start_menu_hide_power_button", self.start_menu_hide_power_button)
        writer.write_bool_value("start_menu_hide_recent_jump_lists", self.start_menu_hide_recent_jump_lists)
        writer.write_bool_value("start_menu_hide_recently_added_apps", self.start_menu_hide_recently_added_apps)
        writer.write_bool_value("start_menu_hide_restart_options", self.start_menu_hide_restart_options)
        writer.write_bool_value("start_menu_hide_shut_down", self.start_menu_hide_shut_down)
        writer.write_bool_value("start_menu_hide_sign_out", self.start_menu_hide_sign_out)
        writer.write_bool_value("start_menu_hide_sleep", self.start_menu_hide_sleep)
        writer.write_bool_value("start_menu_hide_switch_account", self.start_menu_hide_switch_account)
        writer.write_bool_value("start_menu_hide_user_tile", self.start_menu_hide_user_tile)
        writer.write_bytes_value("start_menu_layout_edge_assets_xml", self.start_menu_layout_edge_assets_xml)
        writer.write_bytes_value("start_menu_layout_xml", self.start_menu_layout_xml)
        writer.write_enum_value("start_menu_mode", self.start_menu_mode)
        writer.write_enum_value("start_menu_pinned_folder_documents", self.start_menu_pinned_folder_documents)
        writer.write_enum_value("start_menu_pinned_folder_downloads", self.start_menu_pinned_folder_downloads)
        writer.write_enum_value("start_menu_pinned_folder_file_explorer", self.start_menu_pinned_folder_file_explorer)
        writer.write_enum_value("start_menu_pinned_folder_home_group", self.start_menu_pinned_folder_home_group)
        writer.write_enum_value("start_menu_pinned_folder_music", self.start_menu_pinned_folder_music)
        writer.write_enum_value("start_menu_pinned_folder_network", self.start_menu_pinned_folder_network)
        writer.write_enum_value("start_menu_pinned_folder_personal_folder", self.start_menu_pinned_folder_personal_folder)
        writer.write_enum_value("start_menu_pinned_folder_pictures", self.start_menu_pinned_folder_pictures)
        writer.write_enum_value("start_menu_pinned_folder_settings", self.start_menu_pinned_folder_settings)
        writer.write_enum_value("start_menu_pinned_folder_videos", self.start_menu_pinned_folder_videos)
        writer.write_bool_value("storage_block_removable_storage", self.storage_block_removable_storage)
        writer.write_bool_value("storage_require_mobile_device_encryption", self.storage_require_mobile_device_encryption)
        writer.write_bool_value("storage_restrict_app_data_to_system_volume", self.storage_restrict_app_data_to_system_volume)
        writer.write_bool_value("storage_restrict_app_install_to_system_volume", self.storage_restrict_app_install_to_system_volume)
        writer.write_bool_value("tenant_lockdown_require_network_during_out_of_box_experience", self.tenant_lockdown_require_network_during_out_of_box_experience)
        writer.write_bool_value("usb_blocked", self.usb_blocked)
        writer.write_bool_value("voice_recording_blocked", self.voice_recording_blocked)
        writer.write_bool_value("web_rtc_block_localhost_ip_address", self.web_rtc_block_localhost_ip_address)
        writer.write_bool_value("wi_fi_block_automatic_connect_hotspots", self.wi_fi_block_automatic_connect_hotspots)
        writer.write_bool_value("wi_fi_block_manual_configuration", self.wi_fi_block_manual_configuration)
        writer.write_bool_value("wi_fi_blocked", self.wi_fi_blocked)
        writer.write_int_value("wi_fi_scan_interval", self.wi_fi_scan_interval)
        writer.write_bool_value("windows_spotlight_block_consumer_specific_features", self.windows_spotlight_block_consumer_specific_features)
        writer.write_bool_value("windows_spotlight_block_on_action_center", self.windows_spotlight_block_on_action_center)
        writer.write_bool_value("windows_spotlight_block_tailored_experiences", self.windows_spotlight_block_tailored_experiences)
        writer.write_bool_value("windows_spotlight_block_third_party_notifications", self.windows_spotlight_block_third_party_notifications)
        writer.write_bool_value("windows_spotlight_block_welcome_experience", self.windows_spotlight_block_welcome_experience)
        writer.write_bool_value("windows_spotlight_block_windows_tips", self.windows_spotlight_block_windows_tips)
        writer.write_bool_value("windows_spotlight_blocked", self.windows_spotlight_blocked)
        writer.write_enum_value("windows_spotlight_configure_on_lock_screen", self.windows_spotlight_configure_on_lock_screen)
        writer.write_bool_value("windows_store_block_auto_update", self.windows_store_block_auto_update)
        writer.write_bool_value("windows_store_blocked", self.windows_store_blocked)
        writer.write_bool_value("windows_store_enable_private_store_only", self.windows_store_enable_private_store_only)
        writer.write_bool_value("wireless_display_block_projection_to_this_device", self.wireless_display_block_projection_to_this_device)
        writer.write_bool_value("wireless_display_block_user_input_from_receiver", self.wireless_display_block_user_input_from_receiver)
        writer.write_bool_value("wireless_display_require_pin_for_pairing", self.wireless_display_require_pin_for_pairing)
    

