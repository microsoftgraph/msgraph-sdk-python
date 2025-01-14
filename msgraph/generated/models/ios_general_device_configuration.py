from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_list_item import AppListItem
    from .app_list_type import AppListType
    from .device_configuration import DeviceConfiguration
    from .ios_network_usage_rule import IosNetworkUsageRule
    from .media_content_rating_australia import MediaContentRatingAustralia
    from .media_content_rating_canada import MediaContentRatingCanada
    from .media_content_rating_france import MediaContentRatingFrance
    from .media_content_rating_germany import MediaContentRatingGermany
    from .media_content_rating_ireland import MediaContentRatingIreland
    from .media_content_rating_japan import MediaContentRatingJapan
    from .media_content_rating_new_zealand import MediaContentRatingNewZealand
    from .media_content_rating_united_kingdom import MediaContentRatingUnitedKingdom
    from .media_content_rating_united_states import MediaContentRatingUnitedStates
    from .rating_apps_type import RatingAppsType
    from .required_password_type import RequiredPasswordType
    from .web_browser_cookie_settings import WebBrowserCookieSettings

from .device_configuration import DeviceConfiguration

@dataclass
class IosGeneralDeviceConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the iosGeneralDeviceConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosGeneralDeviceConfiguration"
    # Indicates whether or not to allow account modification when the device is in supervised mode.
    account_block_modification: Optional[bool] = None
    # Indicates whether or not to allow activation lock when the device is in the supervised mode.
    activation_lock_allow_when_supervised: Optional[bool] = None
    # Indicates whether or not to allow AirDrop when the device is in supervised mode.
    air_drop_blocked: Optional[bool] = None
    # Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
    air_drop_force_unmanaged_drop_target: Optional[bool] = None
    # Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
    air_play_force_pairing_password_for_outgoing_requests: Optional[bool] = None
    # Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
    app_store_block_automatic_downloads: Optional[bool] = None
    # Indicates whether or not to block the user from making in app purchases.
    app_store_block_in_app_purchases: Optional[bool] = None
    # Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
    app_store_block_u_i_app_installation: Optional[bool] = None
    # Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
    app_store_blocked: Optional[bool] = None
    # Indicates whether or not to require a password when using the app store.
    app_store_require_password: Optional[bool] = None
    # Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
    apple_news_blocked: Optional[bool] = None
    # Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
    apple_watch_block_pairing: Optional[bool] = None
    # Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
    apple_watch_force_wrist_detection: Optional[bool] = None
    # Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
    apps_single_app_mode_list: Optional[list[AppListItem]] = None
    # List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
    apps_visibility_list: Optional[list[AppListItem]] = None
    # Possible values of the compliance app list.
    apps_visibility_list_type: Optional[AppListType] = None
    # Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
    bluetooth_block_modification: Optional[bool] = None
    # Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
    camera_blocked: Optional[bool] = None
    # Indicates whether or not to block data roaming.
    cellular_block_data_roaming: Optional[bool] = None
    # Indicates whether or not to block global background fetch while roaming.
    cellular_block_global_background_fetch_while_roaming: Optional[bool] = None
    # Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
    cellular_block_per_app_data_modification: Optional[bool] = None
    # Indicates whether or not to block Personal Hotspot.
    cellular_block_personal_hotspot: Optional[bool] = None
    # Indicates whether or not to block voice roaming.
    cellular_block_voice_roaming: Optional[bool] = None
    # Indicates whether or not to block untrusted TLS certificates.
    certificates_block_untrusted_tls_certificates: Optional[bool] = None
    # Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
    classroom_app_block_remote_screen_observation: Optional[bool] = None
    # Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
    classroom_app_force_unprompted_screen_observation: Optional[bool] = None
    # Possible values of the compliance app list.
    compliant_app_list_type: Optional[AppListType] = None
    # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
    compliant_apps_list: Optional[list[AppListItem]] = None
    # Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
    configuration_profile_block_changes: Optional[bool] = None
    # Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
    definition_lookup_blocked: Optional[bool] = None
    # Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
    device_block_enable_restrictions: Optional[bool] = None
    # Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
    device_block_erase_content_and_settings: Optional[bool] = None
    # Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
    device_block_name_modification: Optional[bool] = None
    # Indicates whether or not to block diagnostic data submission.
    diagnostic_data_block_submission: Optional[bool] = None
    # Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
    diagnostic_data_block_submission_modification: Optional[bool] = None
    # Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
    documents_block_managed_documents_in_unmanaged_apps: Optional[bool] = None
    # Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
    documents_block_unmanaged_documents_in_managed_apps: Optional[bool] = None
    # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
    email_in_domain_suffixes: Optional[list[str]] = None
    # Indicates whether or not to block the user from trusting an enterprise app.
    enterprise_app_block_trust: Optional[bool] = None
    # [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
    enterprise_app_block_trust_modification: Optional[bool] = None
    # Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
    face_time_blocked: Optional[bool] = None
    # Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
    find_my_friends_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
    game_center_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
    gaming_block_game_center_friends: Optional[bool] = None
    # Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
    gaming_block_multiplayer: Optional[bool] = None
    # indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
    host_pairing_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
    i_books_store_block_erotica: Optional[bool] = None
    # Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
    i_books_store_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
    i_cloud_block_activity_continuation: Optional[bool] = None
    # Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
    i_cloud_block_backup: Optional[bool] = None
    # Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
    i_cloud_block_document_sync: Optional[bool] = None
    # Indicates whether or not to block Managed Apps Cloud Sync.
    i_cloud_block_managed_apps_sync: Optional[bool] = None
    # Indicates whether or not to block iCloud Photo Library.
    i_cloud_block_photo_library: Optional[bool] = None
    # Indicates whether or not to block iCloud Photo Stream Sync.
    i_cloud_block_photo_stream_sync: Optional[bool] = None
    # Indicates whether or not to block Shared Photo Stream.
    i_cloud_block_shared_photo_stream: Optional[bool] = None
    # Indicates whether or not to require backups to iCloud be encrypted.
    i_cloud_require_encrypted_backup: Optional[bool] = None
    # Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
    i_tunes_block_explicit_content: Optional[bool] = None
    # Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
    i_tunes_block_music_service: Optional[bool] = None
    # Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
    i_tunes_block_radio: Optional[bool] = None
    # Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
    keyboard_block_auto_correct: Optional[bool] = None
    # Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
    keyboard_block_dictation: Optional[bool] = None
    # Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
    keyboard_block_predictive: Optional[bool] = None
    # Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
    keyboard_block_shortcuts: Optional[bool] = None
    # Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
    keyboard_block_spell_check: Optional[bool] = None
    # Indicates whether or not to allow assistive speak while in kiosk mode.
    kiosk_mode_allow_assistive_speak: Optional[bool] = None
    # Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
    kiosk_mode_allow_assistive_touch_settings: Optional[bool] = None
    # Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
    kiosk_mode_allow_auto_lock: Optional[bool] = None
    # Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
    kiosk_mode_allow_color_inversion_settings: Optional[bool] = None
    # Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
    kiosk_mode_allow_ringer_switch: Optional[bool] = None
    # Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
    kiosk_mode_allow_screen_rotation: Optional[bool] = None
    # Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
    kiosk_mode_allow_sleep_button: Optional[bool] = None
    # Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
    kiosk_mode_allow_touchscreen: Optional[bool] = None
    # Indicates whether or not to allow access to the voice over settings while in kiosk mode.
    kiosk_mode_allow_voice_over_settings: Optional[bool] = None
    # Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
    kiosk_mode_allow_volume_buttons: Optional[bool] = None
    # Indicates whether or not to allow access to the zoom settings while in kiosk mode.
    kiosk_mode_allow_zoom_settings: Optional[bool] = None
    # URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
    kiosk_mode_app_store_url: Optional[str] = None
    # ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
    kiosk_mode_built_in_app_id: Optional[str] = None
    # Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
    kiosk_mode_managed_app_id: Optional[str] = None
    # Indicates whether or not to require assistive touch while in kiosk mode.
    kiosk_mode_require_assistive_touch: Optional[bool] = None
    # Indicates whether or not to require color inversion while in kiosk mode.
    kiosk_mode_require_color_inversion: Optional[bool] = None
    # Indicates whether or not to require mono audio while in kiosk mode.
    kiosk_mode_require_mono_audio: Optional[bool] = None
    # Indicates whether or not to require voice over while in kiosk mode.
    kiosk_mode_require_voice_over: Optional[bool] = None
    # Indicates whether or not to require zoom while in kiosk mode.
    kiosk_mode_require_zoom: Optional[bool] = None
    # Indicates whether or not to block the user from using control center on the lock screen.
    lock_screen_block_control_center: Optional[bool] = None
    # Indicates whether or not to block the user from using the notification view on the lock screen.
    lock_screen_block_notification_view: Optional[bool] = None
    # Indicates whether or not to block the user from using passbook when the device is locked.
    lock_screen_block_passbook: Optional[bool] = None
    # Indicates whether or not to block the user from using the Today View on the lock screen.
    lock_screen_block_today_view: Optional[bool] = None
    # Apps rating as in media content
    media_content_rating_apps: Optional[RatingAppsType] = None
    # Media content rating settings for Australia
    media_content_rating_australia: Optional[MediaContentRatingAustralia] = None
    # Media content rating settings for Canada
    media_content_rating_canada: Optional[MediaContentRatingCanada] = None
    # Media content rating settings for France
    media_content_rating_france: Optional[MediaContentRatingFrance] = None
    # Media content rating settings for Germany
    media_content_rating_germany: Optional[MediaContentRatingGermany] = None
    # Media content rating settings for Ireland
    media_content_rating_ireland: Optional[MediaContentRatingIreland] = None
    # Media content rating settings for Japan
    media_content_rating_japan: Optional[MediaContentRatingJapan] = None
    # Media content rating settings for New Zealand
    media_content_rating_new_zealand: Optional[MediaContentRatingNewZealand] = None
    # Media content rating settings for United Kingdom
    media_content_rating_united_kingdom: Optional[MediaContentRatingUnitedKingdom] = None
    # Media content rating settings for United States
    media_content_rating_united_states: Optional[MediaContentRatingUnitedStates] = None
    # Indicates whether or not to block the user from using the Messages app on the supervised device.
    messages_blocked: Optional[bool] = None
    # List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
    network_usage_rules: Optional[list[IosNetworkUsageRule]] = None
    # Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
    notifications_block_settings_modification: Optional[bool] = None
    # Block modification of registered Touch ID fingerprints when in supervised mode.
    passcode_block_fingerprint_modification: Optional[bool] = None
    # Indicates whether or not to block fingerprint unlock.
    passcode_block_fingerprint_unlock: Optional[bool] = None
    # Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
    passcode_block_modification: Optional[bool] = None
    # Indicates whether or not to block simple passcodes.
    passcode_block_simple: Optional[bool] = None
    # Number of days before the passcode expires. Valid values 1 to 65535
    passcode_expiration_days: Optional[int] = None
    # Number of character sets a passcode must contain. Valid values 0 to 4
    passcode_minimum_character_set_count: Optional[int] = None
    # Minimum length of passcode. Valid values 4 to 14
    passcode_minimum_length: Optional[int] = None
    # Minutes of inactivity before a passcode is required.
    passcode_minutes_of_inactivity_before_lock: Optional[int] = None
    # Minutes of inactivity before the screen times out.
    passcode_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous passcodes to block. Valid values 1 to 24
    passcode_previous_passcode_block_count: Optional[int] = None
    # Indicates whether or not to require a passcode.
    passcode_required: Optional[bool] = None
    # Possible values of required passwords.
    passcode_required_type: Optional[RequiredPasswordType] = None
    # Number of sign in failures allowed before wiping the device. Valid values 2 to 11
    passcode_sign_in_failure_count_before_wipe: Optional[int] = None
    # Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
    podcasts_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
    safari_block_autofill: Optional[bool] = None
    # Indicates whether or not to block JavaScript in Safari.
    safari_block_java_script: Optional[bool] = None
    # Indicates whether or not to block popups in Safari.
    safari_block_popups: Optional[bool] = None
    # Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
    safari_blocked: Optional[bool] = None
    # Web Browser Cookie Settings.
    safari_cookie_settings: Optional[WebBrowserCookieSettings] = None
    # URLs matching the patterns listed here will be considered managed.
    safari_managed_domains: Optional[list[str]] = None
    # Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
    safari_password_auto_fill_domains: Optional[list[str]] = None
    # Indicates whether or not to require fraud warning in Safari.
    safari_require_fraud_warning: Optional[bool] = None
    # Indicates whether or not to block the user from taking Screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
    siri_block_user_generated_content: Optional[bool] = None
    # Indicates whether or not to block the user from using Siri.
    siri_blocked: Optional[bool] = None
    # Indicates whether or not to block the user from using Siri when locked.
    siri_blocked_when_locked: Optional[bool] = None
    # Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
    siri_require_profanity_filter: Optional[bool] = None
    # Indicates whether or not to block Spotlight search from returning internet results on supervised device.
    spotlight_block_internet_results: Optional[bool] = None
    # Indicates whether or not to block voice dialing.
    voice_dialing_blocked: Optional[bool] = None
    # Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
    wallpaper_block_modification: Optional[bool] = None
    # Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
    wi_fi_connect_only_to_configured_networks: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .ios_network_usage_rule import IosNetworkUsageRule
        from .media_content_rating_australia import MediaContentRatingAustralia
        from .media_content_rating_canada import MediaContentRatingCanada
        from .media_content_rating_france import MediaContentRatingFrance
        from .media_content_rating_germany import MediaContentRatingGermany
        from .media_content_rating_ireland import MediaContentRatingIreland
        from .media_content_rating_japan import MediaContentRatingJapan
        from .media_content_rating_new_zealand import MediaContentRatingNewZealand
        from .media_content_rating_united_kingdom import MediaContentRatingUnitedKingdom
        from .media_content_rating_united_states import MediaContentRatingUnitedStates
        from .rating_apps_type import RatingAppsType
        from .required_password_type import RequiredPasswordType
        from .web_browser_cookie_settings import WebBrowserCookieSettings

        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .ios_network_usage_rule import IosNetworkUsageRule
        from .media_content_rating_australia import MediaContentRatingAustralia
        from .media_content_rating_canada import MediaContentRatingCanada
        from .media_content_rating_france import MediaContentRatingFrance
        from .media_content_rating_germany import MediaContentRatingGermany
        from .media_content_rating_ireland import MediaContentRatingIreland
        from .media_content_rating_japan import MediaContentRatingJapan
        from .media_content_rating_new_zealand import MediaContentRatingNewZealand
        from .media_content_rating_united_kingdom import MediaContentRatingUnitedKingdom
        from .media_content_rating_united_states import MediaContentRatingUnitedStates
        from .rating_apps_type import RatingAppsType
        from .required_password_type import RequiredPasswordType
        from .web_browser_cookie_settings import WebBrowserCookieSettings

        fields: dict[str, Callable[[Any], None]] = {
            "accountBlockModification": lambda n : setattr(self, 'account_block_modification', n.get_bool_value()),
            "activationLockAllowWhenSupervised": lambda n : setattr(self, 'activation_lock_allow_when_supervised', n.get_bool_value()),
            "airDropBlocked": lambda n : setattr(self, 'air_drop_blocked', n.get_bool_value()),
            "airDropForceUnmanagedDropTarget": lambda n : setattr(self, 'air_drop_force_unmanaged_drop_target', n.get_bool_value()),
            "airPlayForcePairingPasswordForOutgoingRequests": lambda n : setattr(self, 'air_play_force_pairing_password_for_outgoing_requests', n.get_bool_value()),
            "appStoreBlockAutomaticDownloads": lambda n : setattr(self, 'app_store_block_automatic_downloads', n.get_bool_value()),
            "appStoreBlockInAppPurchases": lambda n : setattr(self, 'app_store_block_in_app_purchases', n.get_bool_value()),
            "appStoreBlockUIAppInstallation": lambda n : setattr(self, 'app_store_block_u_i_app_installation', n.get_bool_value()),
            "appStoreBlocked": lambda n : setattr(self, 'app_store_blocked', n.get_bool_value()),
            "appStoreRequirePassword": lambda n : setattr(self, 'app_store_require_password', n.get_bool_value()),
            "appleNewsBlocked": lambda n : setattr(self, 'apple_news_blocked', n.get_bool_value()),
            "appleWatchBlockPairing": lambda n : setattr(self, 'apple_watch_block_pairing', n.get_bool_value()),
            "appleWatchForceWristDetection": lambda n : setattr(self, 'apple_watch_force_wrist_detection', n.get_bool_value()),
            "appsSingleAppModeList": lambda n : setattr(self, 'apps_single_app_mode_list', n.get_collection_of_object_values(AppListItem)),
            "appsVisibilityList": lambda n : setattr(self, 'apps_visibility_list', n.get_collection_of_object_values(AppListItem)),
            "appsVisibilityListType": lambda n : setattr(self, 'apps_visibility_list_type', n.get_enum_value(AppListType)),
            "bluetoothBlockModification": lambda n : setattr(self, 'bluetooth_block_modification', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellularBlockDataRoaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "cellularBlockGlobalBackgroundFetchWhileRoaming": lambda n : setattr(self, 'cellular_block_global_background_fetch_while_roaming', n.get_bool_value()),
            "cellularBlockPerAppDataModification": lambda n : setattr(self, 'cellular_block_per_app_data_modification', n.get_bool_value()),
            "cellularBlockPersonalHotspot": lambda n : setattr(self, 'cellular_block_personal_hotspot', n.get_bool_value()),
            "cellularBlockVoiceRoaming": lambda n : setattr(self, 'cellular_block_voice_roaming', n.get_bool_value()),
            "certificatesBlockUntrustedTlsCertificates": lambda n : setattr(self, 'certificates_block_untrusted_tls_certificates', n.get_bool_value()),
            "classroomAppBlockRemoteScreenObservation": lambda n : setattr(self, 'classroom_app_block_remote_screen_observation', n.get_bool_value()),
            "classroomAppForceUnpromptedScreenObservation": lambda n : setattr(self, 'classroom_app_force_unprompted_screen_observation', n.get_bool_value()),
            "compliantAppListType": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(AppListType)),
            "compliantAppsList": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(AppListItem)),
            "configurationProfileBlockChanges": lambda n : setattr(self, 'configuration_profile_block_changes', n.get_bool_value()),
            "definitionLookupBlocked": lambda n : setattr(self, 'definition_lookup_blocked', n.get_bool_value()),
            "deviceBlockEnableRestrictions": lambda n : setattr(self, 'device_block_enable_restrictions', n.get_bool_value()),
            "deviceBlockEraseContentAndSettings": lambda n : setattr(self, 'device_block_erase_content_and_settings', n.get_bool_value()),
            "deviceBlockNameModification": lambda n : setattr(self, 'device_block_name_modification', n.get_bool_value()),
            "diagnosticDataBlockSubmission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "diagnosticDataBlockSubmissionModification": lambda n : setattr(self, 'diagnostic_data_block_submission_modification', n.get_bool_value()),
            "documentsBlockManagedDocumentsInUnmanagedApps": lambda n : setattr(self, 'documents_block_managed_documents_in_unmanaged_apps', n.get_bool_value()),
            "documentsBlockUnmanagedDocumentsInManagedApps": lambda n : setattr(self, 'documents_block_unmanaged_documents_in_managed_apps', n.get_bool_value()),
            "emailInDomainSuffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "enterpriseAppBlockTrust": lambda n : setattr(self, 'enterprise_app_block_trust', n.get_bool_value()),
            "enterpriseAppBlockTrustModification": lambda n : setattr(self, 'enterprise_app_block_trust_modification', n.get_bool_value()),
            "faceTimeBlocked": lambda n : setattr(self, 'face_time_blocked', n.get_bool_value()),
            "findMyFriendsBlocked": lambda n : setattr(self, 'find_my_friends_blocked', n.get_bool_value()),
            "gameCenterBlocked": lambda n : setattr(self, 'game_center_blocked', n.get_bool_value()),
            "gamingBlockGameCenterFriends": lambda n : setattr(self, 'gaming_block_game_center_friends', n.get_bool_value()),
            "gamingBlockMultiplayer": lambda n : setattr(self, 'gaming_block_multiplayer', n.get_bool_value()),
            "hostPairingBlocked": lambda n : setattr(self, 'host_pairing_blocked', n.get_bool_value()),
            "iBooksStoreBlockErotica": lambda n : setattr(self, 'i_books_store_block_erotica', n.get_bool_value()),
            "iBooksStoreBlocked": lambda n : setattr(self, 'i_books_store_blocked', n.get_bool_value()),
            "iCloudBlockActivityContinuation": lambda n : setattr(self, 'i_cloud_block_activity_continuation', n.get_bool_value()),
            "iCloudBlockBackup": lambda n : setattr(self, 'i_cloud_block_backup', n.get_bool_value()),
            "iCloudBlockDocumentSync": lambda n : setattr(self, 'i_cloud_block_document_sync', n.get_bool_value()),
            "iCloudBlockManagedAppsSync": lambda n : setattr(self, 'i_cloud_block_managed_apps_sync', n.get_bool_value()),
            "iCloudBlockPhotoLibrary": lambda n : setattr(self, 'i_cloud_block_photo_library', n.get_bool_value()),
            "iCloudBlockPhotoStreamSync": lambda n : setattr(self, 'i_cloud_block_photo_stream_sync', n.get_bool_value()),
            "iCloudBlockSharedPhotoStream": lambda n : setattr(self, 'i_cloud_block_shared_photo_stream', n.get_bool_value()),
            "iCloudRequireEncryptedBackup": lambda n : setattr(self, 'i_cloud_require_encrypted_backup', n.get_bool_value()),
            "iTunesBlockExplicitContent": lambda n : setattr(self, 'i_tunes_block_explicit_content', n.get_bool_value()),
            "iTunesBlockMusicService": lambda n : setattr(self, 'i_tunes_block_music_service', n.get_bool_value()),
            "iTunesBlockRadio": lambda n : setattr(self, 'i_tunes_block_radio', n.get_bool_value()),
            "keyboardBlockAutoCorrect": lambda n : setattr(self, 'keyboard_block_auto_correct', n.get_bool_value()),
            "keyboardBlockDictation": lambda n : setattr(self, 'keyboard_block_dictation', n.get_bool_value()),
            "keyboardBlockPredictive": lambda n : setattr(self, 'keyboard_block_predictive', n.get_bool_value()),
            "keyboardBlockShortcuts": lambda n : setattr(self, 'keyboard_block_shortcuts', n.get_bool_value()),
            "keyboardBlockSpellCheck": lambda n : setattr(self, 'keyboard_block_spell_check', n.get_bool_value()),
            "kioskModeAllowAssistiveSpeak": lambda n : setattr(self, 'kiosk_mode_allow_assistive_speak', n.get_bool_value()),
            "kioskModeAllowAssistiveTouchSettings": lambda n : setattr(self, 'kiosk_mode_allow_assistive_touch_settings', n.get_bool_value()),
            "kioskModeAllowAutoLock": lambda n : setattr(self, 'kiosk_mode_allow_auto_lock', n.get_bool_value()),
            "kioskModeAllowColorInversionSettings": lambda n : setattr(self, 'kiosk_mode_allow_color_inversion_settings', n.get_bool_value()),
            "kioskModeAllowRingerSwitch": lambda n : setattr(self, 'kiosk_mode_allow_ringer_switch', n.get_bool_value()),
            "kioskModeAllowScreenRotation": lambda n : setattr(self, 'kiosk_mode_allow_screen_rotation', n.get_bool_value()),
            "kioskModeAllowSleepButton": lambda n : setattr(self, 'kiosk_mode_allow_sleep_button', n.get_bool_value()),
            "kioskModeAllowTouchscreen": lambda n : setattr(self, 'kiosk_mode_allow_touchscreen', n.get_bool_value()),
            "kioskModeAllowVoiceOverSettings": lambda n : setattr(self, 'kiosk_mode_allow_voice_over_settings', n.get_bool_value()),
            "kioskModeAllowVolumeButtons": lambda n : setattr(self, 'kiosk_mode_allow_volume_buttons', n.get_bool_value()),
            "kioskModeAllowZoomSettings": lambda n : setattr(self, 'kiosk_mode_allow_zoom_settings', n.get_bool_value()),
            "kioskModeAppStoreUrl": lambda n : setattr(self, 'kiosk_mode_app_store_url', n.get_str_value()),
            "kioskModeBuiltInAppId": lambda n : setattr(self, 'kiosk_mode_built_in_app_id', n.get_str_value()),
            "kioskModeManagedAppId": lambda n : setattr(self, 'kiosk_mode_managed_app_id', n.get_str_value()),
            "kioskModeRequireAssistiveTouch": lambda n : setattr(self, 'kiosk_mode_require_assistive_touch', n.get_bool_value()),
            "kioskModeRequireColorInversion": lambda n : setattr(self, 'kiosk_mode_require_color_inversion', n.get_bool_value()),
            "kioskModeRequireMonoAudio": lambda n : setattr(self, 'kiosk_mode_require_mono_audio', n.get_bool_value()),
            "kioskModeRequireVoiceOver": lambda n : setattr(self, 'kiosk_mode_require_voice_over', n.get_bool_value()),
            "kioskModeRequireZoom": lambda n : setattr(self, 'kiosk_mode_require_zoom', n.get_bool_value()),
            "lockScreenBlockControlCenter": lambda n : setattr(self, 'lock_screen_block_control_center', n.get_bool_value()),
            "lockScreenBlockNotificationView": lambda n : setattr(self, 'lock_screen_block_notification_view', n.get_bool_value()),
            "lockScreenBlockPassbook": lambda n : setattr(self, 'lock_screen_block_passbook', n.get_bool_value()),
            "lockScreenBlockTodayView": lambda n : setattr(self, 'lock_screen_block_today_view', n.get_bool_value()),
            "mediaContentRatingApps": lambda n : setattr(self, 'media_content_rating_apps', n.get_enum_value(RatingAppsType)),
            "mediaContentRatingAustralia": lambda n : setattr(self, 'media_content_rating_australia', n.get_object_value(MediaContentRatingAustralia)),
            "mediaContentRatingCanada": lambda n : setattr(self, 'media_content_rating_canada', n.get_object_value(MediaContentRatingCanada)),
            "mediaContentRatingFrance": lambda n : setattr(self, 'media_content_rating_france', n.get_object_value(MediaContentRatingFrance)),
            "mediaContentRatingGermany": lambda n : setattr(self, 'media_content_rating_germany', n.get_object_value(MediaContentRatingGermany)),
            "mediaContentRatingIreland": lambda n : setattr(self, 'media_content_rating_ireland', n.get_object_value(MediaContentRatingIreland)),
            "mediaContentRatingJapan": lambda n : setattr(self, 'media_content_rating_japan', n.get_object_value(MediaContentRatingJapan)),
            "mediaContentRatingNewZealand": lambda n : setattr(self, 'media_content_rating_new_zealand', n.get_object_value(MediaContentRatingNewZealand)),
            "mediaContentRatingUnitedKingdom": lambda n : setattr(self, 'media_content_rating_united_kingdom', n.get_object_value(MediaContentRatingUnitedKingdom)),
            "mediaContentRatingUnitedStates": lambda n : setattr(self, 'media_content_rating_united_states', n.get_object_value(MediaContentRatingUnitedStates)),
            "messagesBlocked": lambda n : setattr(self, 'messages_blocked', n.get_bool_value()),
            "networkUsageRules": lambda n : setattr(self, 'network_usage_rules', n.get_collection_of_object_values(IosNetworkUsageRule)),
            "notificationsBlockSettingsModification": lambda n : setattr(self, 'notifications_block_settings_modification', n.get_bool_value()),
            "passcodeBlockFingerprintModification": lambda n : setattr(self, 'passcode_block_fingerprint_modification', n.get_bool_value()),
            "passcodeBlockFingerprintUnlock": lambda n : setattr(self, 'passcode_block_fingerprint_unlock', n.get_bool_value()),
            "passcodeBlockModification": lambda n : setattr(self, 'passcode_block_modification', n.get_bool_value()),
            "passcodeBlockSimple": lambda n : setattr(self, 'passcode_block_simple', n.get_bool_value()),
            "passcodeExpirationDays": lambda n : setattr(self, 'passcode_expiration_days', n.get_int_value()),
            "passcodeMinimumCharacterSetCount": lambda n : setattr(self, 'passcode_minimum_character_set_count', n.get_int_value()),
            "passcodeMinimumLength": lambda n : setattr(self, 'passcode_minimum_length', n.get_int_value()),
            "passcodeMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passcodeMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passcodePreviousPasscodeBlockCount": lambda n : setattr(self, 'passcode_previous_passcode_block_count', n.get_int_value()),
            "passcodeRequired": lambda n : setattr(self, 'passcode_required', n.get_bool_value()),
            "passcodeRequiredType": lambda n : setattr(self, 'passcode_required_type', n.get_enum_value(RequiredPasswordType)),
            "passcodeSignInFailureCountBeforeWipe": lambda n : setattr(self, 'passcode_sign_in_failure_count_before_wipe', n.get_int_value()),
            "podcastsBlocked": lambda n : setattr(self, 'podcasts_blocked', n.get_bool_value()),
            "safariBlockAutofill": lambda n : setattr(self, 'safari_block_autofill', n.get_bool_value()),
            "safariBlockJavaScript": lambda n : setattr(self, 'safari_block_java_script', n.get_bool_value()),
            "safariBlockPopups": lambda n : setattr(self, 'safari_block_popups', n.get_bool_value()),
            "safariBlocked": lambda n : setattr(self, 'safari_blocked', n.get_bool_value()),
            "safariCookieSettings": lambda n : setattr(self, 'safari_cookie_settings', n.get_enum_value(WebBrowserCookieSettings)),
            "safariManagedDomains": lambda n : setattr(self, 'safari_managed_domains', n.get_collection_of_primitive_values(str)),
            "safariPasswordAutoFillDomains": lambda n : setattr(self, 'safari_password_auto_fill_domains', n.get_collection_of_primitive_values(str)),
            "safariRequireFraudWarning": lambda n : setattr(self, 'safari_require_fraud_warning', n.get_bool_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "siriBlockUserGeneratedContent": lambda n : setattr(self, 'siri_block_user_generated_content', n.get_bool_value()),
            "siriBlocked": lambda n : setattr(self, 'siri_blocked', n.get_bool_value()),
            "siriBlockedWhenLocked": lambda n : setattr(self, 'siri_blocked_when_locked', n.get_bool_value()),
            "siriRequireProfanityFilter": lambda n : setattr(self, 'siri_require_profanity_filter', n.get_bool_value()),
            "spotlightBlockInternetResults": lambda n : setattr(self, 'spotlight_block_internet_results', n.get_bool_value()),
            "voiceDialingBlocked": lambda n : setattr(self, 'voice_dialing_blocked', n.get_bool_value()),
            "wallpaperBlockModification": lambda n : setattr(self, 'wallpaper_block_modification', n.get_bool_value()),
            "wiFiConnectOnlyToConfiguredNetworks": lambda n : setattr(self, 'wi_fi_connect_only_to_configured_networks', n.get_bool_value()),
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
        writer.write_bool_value("accountBlockModification", self.account_block_modification)
        writer.write_bool_value("activationLockAllowWhenSupervised", self.activation_lock_allow_when_supervised)
        writer.write_bool_value("airDropBlocked", self.air_drop_blocked)
        writer.write_bool_value("airDropForceUnmanagedDropTarget", self.air_drop_force_unmanaged_drop_target)
        writer.write_bool_value("airPlayForcePairingPasswordForOutgoingRequests", self.air_play_force_pairing_password_for_outgoing_requests)
        writer.write_bool_value("appStoreBlockAutomaticDownloads", self.app_store_block_automatic_downloads)
        writer.write_bool_value("appStoreBlockInAppPurchases", self.app_store_block_in_app_purchases)
        writer.write_bool_value("appStoreBlockUIAppInstallation", self.app_store_block_u_i_app_installation)
        writer.write_bool_value("appStoreBlocked", self.app_store_blocked)
        writer.write_bool_value("appStoreRequirePassword", self.app_store_require_password)
        writer.write_bool_value("appleNewsBlocked", self.apple_news_blocked)
        writer.write_bool_value("appleWatchBlockPairing", self.apple_watch_block_pairing)
        writer.write_bool_value("appleWatchForceWristDetection", self.apple_watch_force_wrist_detection)
        writer.write_collection_of_object_values("appsSingleAppModeList", self.apps_single_app_mode_list)
        writer.write_collection_of_object_values("appsVisibilityList", self.apps_visibility_list)
        writer.write_enum_value("appsVisibilityListType", self.apps_visibility_list_type)
        writer.write_bool_value("bluetoothBlockModification", self.bluetooth_block_modification)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockDataRoaming", self.cellular_block_data_roaming)
        writer.write_bool_value("cellularBlockGlobalBackgroundFetchWhileRoaming", self.cellular_block_global_background_fetch_while_roaming)
        writer.write_bool_value("cellularBlockPerAppDataModification", self.cellular_block_per_app_data_modification)
        writer.write_bool_value("cellularBlockPersonalHotspot", self.cellular_block_personal_hotspot)
        writer.write_bool_value("cellularBlockVoiceRoaming", self.cellular_block_voice_roaming)
        writer.write_bool_value("certificatesBlockUntrustedTlsCertificates", self.certificates_block_untrusted_tls_certificates)
        writer.write_bool_value("classroomAppBlockRemoteScreenObservation", self.classroom_app_block_remote_screen_observation)
        writer.write_bool_value("classroomAppForceUnpromptedScreenObservation", self.classroom_app_force_unprompted_screen_observation)
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_bool_value("configurationProfileBlockChanges", self.configuration_profile_block_changes)
        writer.write_bool_value("definitionLookupBlocked", self.definition_lookup_blocked)
        writer.write_bool_value("deviceBlockEnableRestrictions", self.device_block_enable_restrictions)
        writer.write_bool_value("deviceBlockEraseContentAndSettings", self.device_block_erase_content_and_settings)
        writer.write_bool_value("deviceBlockNameModification", self.device_block_name_modification)
        writer.write_bool_value("diagnosticDataBlockSubmission", self.diagnostic_data_block_submission)
        writer.write_bool_value("diagnosticDataBlockSubmissionModification", self.diagnostic_data_block_submission_modification)
        writer.write_bool_value("documentsBlockManagedDocumentsInUnmanagedApps", self.documents_block_managed_documents_in_unmanaged_apps)
        writer.write_bool_value("documentsBlockUnmanagedDocumentsInManagedApps", self.documents_block_unmanaged_documents_in_managed_apps)
        writer.write_collection_of_primitive_values("emailInDomainSuffixes", self.email_in_domain_suffixes)
        writer.write_bool_value("enterpriseAppBlockTrust", self.enterprise_app_block_trust)
        writer.write_bool_value("enterpriseAppBlockTrustModification", self.enterprise_app_block_trust_modification)
        writer.write_bool_value("faceTimeBlocked", self.face_time_blocked)
        writer.write_bool_value("findMyFriendsBlocked", self.find_my_friends_blocked)
        writer.write_bool_value("gameCenterBlocked", self.game_center_blocked)
        writer.write_bool_value("gamingBlockGameCenterFriends", self.gaming_block_game_center_friends)
        writer.write_bool_value("gamingBlockMultiplayer", self.gaming_block_multiplayer)
        writer.write_bool_value("hostPairingBlocked", self.host_pairing_blocked)
        writer.write_bool_value("iBooksStoreBlockErotica", self.i_books_store_block_erotica)
        writer.write_bool_value("iBooksStoreBlocked", self.i_books_store_blocked)
        writer.write_bool_value("iCloudBlockActivityContinuation", self.i_cloud_block_activity_continuation)
        writer.write_bool_value("iCloudBlockBackup", self.i_cloud_block_backup)
        writer.write_bool_value("iCloudBlockDocumentSync", self.i_cloud_block_document_sync)
        writer.write_bool_value("iCloudBlockManagedAppsSync", self.i_cloud_block_managed_apps_sync)
        writer.write_bool_value("iCloudBlockPhotoLibrary", self.i_cloud_block_photo_library)
        writer.write_bool_value("iCloudBlockPhotoStreamSync", self.i_cloud_block_photo_stream_sync)
        writer.write_bool_value("iCloudBlockSharedPhotoStream", self.i_cloud_block_shared_photo_stream)
        writer.write_bool_value("iCloudRequireEncryptedBackup", self.i_cloud_require_encrypted_backup)
        writer.write_bool_value("iTunesBlockExplicitContent", self.i_tunes_block_explicit_content)
        writer.write_bool_value("iTunesBlockMusicService", self.i_tunes_block_music_service)
        writer.write_bool_value("iTunesBlockRadio", self.i_tunes_block_radio)
        writer.write_bool_value("keyboardBlockAutoCorrect", self.keyboard_block_auto_correct)
        writer.write_bool_value("keyboardBlockDictation", self.keyboard_block_dictation)
        writer.write_bool_value("keyboardBlockPredictive", self.keyboard_block_predictive)
        writer.write_bool_value("keyboardBlockShortcuts", self.keyboard_block_shortcuts)
        writer.write_bool_value("keyboardBlockSpellCheck", self.keyboard_block_spell_check)
        writer.write_bool_value("kioskModeAllowAssistiveSpeak", self.kiosk_mode_allow_assistive_speak)
        writer.write_bool_value("kioskModeAllowAssistiveTouchSettings", self.kiosk_mode_allow_assistive_touch_settings)
        writer.write_bool_value("kioskModeAllowAutoLock", self.kiosk_mode_allow_auto_lock)
        writer.write_bool_value("kioskModeAllowColorInversionSettings", self.kiosk_mode_allow_color_inversion_settings)
        writer.write_bool_value("kioskModeAllowRingerSwitch", self.kiosk_mode_allow_ringer_switch)
        writer.write_bool_value("kioskModeAllowScreenRotation", self.kiosk_mode_allow_screen_rotation)
        writer.write_bool_value("kioskModeAllowSleepButton", self.kiosk_mode_allow_sleep_button)
        writer.write_bool_value("kioskModeAllowTouchscreen", self.kiosk_mode_allow_touchscreen)
        writer.write_bool_value("kioskModeAllowVoiceOverSettings", self.kiosk_mode_allow_voice_over_settings)
        writer.write_bool_value("kioskModeAllowVolumeButtons", self.kiosk_mode_allow_volume_buttons)
        writer.write_bool_value("kioskModeAllowZoomSettings", self.kiosk_mode_allow_zoom_settings)
        writer.write_str_value("kioskModeAppStoreUrl", self.kiosk_mode_app_store_url)
        writer.write_str_value("kioskModeBuiltInAppId", self.kiosk_mode_built_in_app_id)
        writer.write_str_value("kioskModeManagedAppId", self.kiosk_mode_managed_app_id)
        writer.write_bool_value("kioskModeRequireAssistiveTouch", self.kiosk_mode_require_assistive_touch)
        writer.write_bool_value("kioskModeRequireColorInversion", self.kiosk_mode_require_color_inversion)
        writer.write_bool_value("kioskModeRequireMonoAudio", self.kiosk_mode_require_mono_audio)
        writer.write_bool_value("kioskModeRequireVoiceOver", self.kiosk_mode_require_voice_over)
        writer.write_bool_value("kioskModeRequireZoom", self.kiosk_mode_require_zoom)
        writer.write_bool_value("lockScreenBlockControlCenter", self.lock_screen_block_control_center)
        writer.write_bool_value("lockScreenBlockNotificationView", self.lock_screen_block_notification_view)
        writer.write_bool_value("lockScreenBlockPassbook", self.lock_screen_block_passbook)
        writer.write_bool_value("lockScreenBlockTodayView", self.lock_screen_block_today_view)
        writer.write_enum_value("mediaContentRatingApps", self.media_content_rating_apps)
        writer.write_object_value("mediaContentRatingAustralia", self.media_content_rating_australia)
        writer.write_object_value("mediaContentRatingCanada", self.media_content_rating_canada)
        writer.write_object_value("mediaContentRatingFrance", self.media_content_rating_france)
        writer.write_object_value("mediaContentRatingGermany", self.media_content_rating_germany)
        writer.write_object_value("mediaContentRatingIreland", self.media_content_rating_ireland)
        writer.write_object_value("mediaContentRatingJapan", self.media_content_rating_japan)
        writer.write_object_value("mediaContentRatingNewZealand", self.media_content_rating_new_zealand)
        writer.write_object_value("mediaContentRatingUnitedKingdom", self.media_content_rating_united_kingdom)
        writer.write_object_value("mediaContentRatingUnitedStates", self.media_content_rating_united_states)
        writer.write_bool_value("messagesBlocked", self.messages_blocked)
        writer.write_collection_of_object_values("networkUsageRules", self.network_usage_rules)
        writer.write_bool_value("notificationsBlockSettingsModification", self.notifications_block_settings_modification)
        writer.write_bool_value("passcodeBlockFingerprintModification", self.passcode_block_fingerprint_modification)
        writer.write_bool_value("passcodeBlockFingerprintUnlock", self.passcode_block_fingerprint_unlock)
        writer.write_bool_value("passcodeBlockModification", self.passcode_block_modification)
        writer.write_bool_value("passcodeBlockSimple", self.passcode_block_simple)
        writer.write_int_value("passcodeExpirationDays", self.passcode_expiration_days)
        writer.write_int_value("passcodeMinimumCharacterSetCount", self.passcode_minimum_character_set_count)
        writer.write_int_value("passcodeMinimumLength", self.passcode_minimum_length)
        writer.write_int_value("passcodeMinutesOfInactivityBeforeLock", self.passcode_minutes_of_inactivity_before_lock)
        writer.write_int_value("passcodeMinutesOfInactivityBeforeScreenTimeout", self.passcode_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passcodePreviousPasscodeBlockCount", self.passcode_previous_passcode_block_count)
        writer.write_bool_value("passcodeRequired", self.passcode_required)
        writer.write_enum_value("passcodeRequiredType", self.passcode_required_type)
        writer.write_int_value("passcodeSignInFailureCountBeforeWipe", self.passcode_sign_in_failure_count_before_wipe)
        writer.write_bool_value("podcastsBlocked", self.podcasts_blocked)
        writer.write_bool_value("safariBlockAutofill", self.safari_block_autofill)
        writer.write_bool_value("safariBlockJavaScript", self.safari_block_java_script)
        writer.write_bool_value("safariBlockPopups", self.safari_block_popups)
        writer.write_bool_value("safariBlocked", self.safari_blocked)
        writer.write_enum_value("safariCookieSettings", self.safari_cookie_settings)
        writer.write_collection_of_primitive_values("safariManagedDomains", self.safari_managed_domains)
        writer.write_collection_of_primitive_values("safariPasswordAutoFillDomains", self.safari_password_auto_fill_domains)
        writer.write_bool_value("safariRequireFraudWarning", self.safari_require_fraud_warning)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("siriBlockUserGeneratedContent", self.siri_block_user_generated_content)
        writer.write_bool_value("siriBlocked", self.siri_blocked)
        writer.write_bool_value("siriBlockedWhenLocked", self.siri_blocked_when_locked)
        writer.write_bool_value("siriRequireProfanityFilter", self.siri_require_profanity_filter)
        writer.write_bool_value("spotlightBlockInternetResults", self.spotlight_block_internet_results)
        writer.write_bool_value("voiceDialingBlocked", self.voice_dialing_blocked)
        writer.write_bool_value("wallpaperBlockModification", self.wallpaper_block_modification)
        writer.write_bool_value("wiFiConnectOnlyToConfiguredNetworks", self.wi_fi_connect_only_to_configured_networks)
    

