from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_list_item = lazy_import('msgraph.generated.models.app_list_item')
app_list_type = lazy_import('msgraph.generated.models.app_list_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
ios_network_usage_rule = lazy_import('msgraph.generated.models.ios_network_usage_rule')
media_content_rating_australia = lazy_import('msgraph.generated.models.media_content_rating_australia')
media_content_rating_canada = lazy_import('msgraph.generated.models.media_content_rating_canada')
media_content_rating_france = lazy_import('msgraph.generated.models.media_content_rating_france')
media_content_rating_germany = lazy_import('msgraph.generated.models.media_content_rating_germany')
media_content_rating_ireland = lazy_import('msgraph.generated.models.media_content_rating_ireland')
media_content_rating_japan = lazy_import('msgraph.generated.models.media_content_rating_japan')
media_content_rating_new_zealand = lazy_import('msgraph.generated.models.media_content_rating_new_zealand')
media_content_rating_united_kingdom = lazy_import('msgraph.generated.models.media_content_rating_united_kingdom')
media_content_rating_united_states = lazy_import('msgraph.generated.models.media_content_rating_united_states')
rating_apps_type = lazy_import('msgraph.generated.models.rating_apps_type')
required_password_type = lazy_import('msgraph.generated.models.required_password_type')
web_browser_cookie_settings = lazy_import('msgraph.generated.models.web_browser_cookie_settings')

class IosGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    @property
    def account_block_modification(self,) -> Optional[bool]:
        """
        Gets the accountBlockModification property value. Indicates whether or not to allow account modification when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._account_block_modification
    
    @account_block_modification.setter
    def account_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountBlockModification property value. Indicates whether or not to allow account modification when the device is in supervised mode.
        Args:
            value: Value to set for the accountBlockModification property.
        """
        self._account_block_modification = value
    
    @property
    def activation_lock_allow_when_supervised(self,) -> Optional[bool]:
        """
        Gets the activationLockAllowWhenSupervised property value. Indicates whether or not to allow activation lock when the device is in the supervised mode.
        Returns: Optional[bool]
        """
        return self._activation_lock_allow_when_supervised
    
    @activation_lock_allow_when_supervised.setter
    def activation_lock_allow_when_supervised(self,value: Optional[bool] = None) -> None:
        """
        Sets the activationLockAllowWhenSupervised property value. Indicates whether or not to allow activation lock when the device is in the supervised mode.
        Args:
            value: Value to set for the activationLockAllowWhenSupervised property.
        """
        self._activation_lock_allow_when_supervised = value
    
    @property
    def air_drop_blocked(self,) -> Optional[bool]:
        """
        Gets the airDropBlocked property value. Indicates whether or not to allow AirDrop when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._air_drop_blocked
    
    @air_drop_blocked.setter
    def air_drop_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the airDropBlocked property value. Indicates whether or not to allow AirDrop when the device is in supervised mode.
        Args:
            value: Value to set for the airDropBlocked property.
        """
        self._air_drop_blocked = value
    
    @property
    def air_drop_force_unmanaged_drop_target(self,) -> Optional[bool]:
        """
        Gets the airDropForceUnmanagedDropTarget property value. Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._air_drop_force_unmanaged_drop_target
    
    @air_drop_force_unmanaged_drop_target.setter
    def air_drop_force_unmanaged_drop_target(self,value: Optional[bool] = None) -> None:
        """
        Sets the airDropForceUnmanagedDropTarget property value. Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
        Args:
            value: Value to set for the airDropForceUnmanagedDropTarget property.
        """
        self._air_drop_force_unmanaged_drop_target = value
    
    @property
    def air_play_force_pairing_password_for_outgoing_requests(self,) -> Optional[bool]:
        """
        Gets the airPlayForcePairingPasswordForOutgoingRequests property value. Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
        Returns: Optional[bool]
        """
        return self._air_play_force_pairing_password_for_outgoing_requests
    
    @air_play_force_pairing_password_for_outgoing_requests.setter
    def air_play_force_pairing_password_for_outgoing_requests(self,value: Optional[bool] = None) -> None:
        """
        Sets the airPlayForcePairingPasswordForOutgoingRequests property value. Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
        Args:
            value: Value to set for the airPlayForcePairingPasswordForOutgoingRequests property.
        """
        self._air_play_force_pairing_password_for_outgoing_requests = value
    
    @property
    def apple_news_blocked(self,) -> Optional[bool]:
        """
        Gets the appleNewsBlocked property value. Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._apple_news_blocked
    
    @apple_news_blocked.setter
    def apple_news_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleNewsBlocked property value. Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the appleNewsBlocked property.
        """
        self._apple_news_blocked = value
    
    @property
    def apple_watch_block_pairing(self,) -> Optional[bool]:
        """
        Gets the appleWatchBlockPairing property value. Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._apple_watch_block_pairing
    
    @apple_watch_block_pairing.setter
    def apple_watch_block_pairing(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleWatchBlockPairing property value. Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the appleWatchBlockPairing property.
        """
        self._apple_watch_block_pairing = value
    
    @property
    def apple_watch_force_wrist_detection(self,) -> Optional[bool]:
        """
        Gets the appleWatchForceWristDetection property value. Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
        Returns: Optional[bool]
        """
        return self._apple_watch_force_wrist_detection
    
    @apple_watch_force_wrist_detection.setter
    def apple_watch_force_wrist_detection(self,value: Optional[bool] = None) -> None:
        """
        Sets the appleWatchForceWristDetection property value. Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
        Args:
            value: Value to set for the appleWatchForceWristDetection property.
        """
        self._apple_watch_force_wrist_detection = value
    
    @property
    def apps_single_app_mode_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsSingleAppModeList property value. Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_single_app_mode_list
    
    @apps_single_app_mode_list.setter
    def apps_single_app_mode_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsSingleAppModeList property value. Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the appsSingleAppModeList property.
        """
        self._apps_single_app_mode_list = value
    
    @property
    def app_store_block_automatic_downloads(self,) -> Optional[bool]:
        """
        Gets the appStoreBlockAutomaticDownloads property value. Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._app_store_block_automatic_downloads
    
    @app_store_block_automatic_downloads.setter
    def app_store_block_automatic_downloads(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlockAutomaticDownloads property value. Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the appStoreBlockAutomaticDownloads property.
        """
        self._app_store_block_automatic_downloads = value
    
    @property
    def app_store_blocked(self,) -> Optional[bool]:
        """
        Gets the appStoreBlocked property value. Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._app_store_blocked
    
    @app_store_blocked.setter
    def app_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlocked property value. Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the appStoreBlocked property.
        """
        self._app_store_blocked = value
    
    @property
    def app_store_block_in_app_purchases(self,) -> Optional[bool]:
        """
        Gets the appStoreBlockInAppPurchases property value. Indicates whether or not to block the user from making in app purchases.
        Returns: Optional[bool]
        """
        return self._app_store_block_in_app_purchases
    
    @app_store_block_in_app_purchases.setter
    def app_store_block_in_app_purchases(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlockInAppPurchases property value. Indicates whether or not to block the user from making in app purchases.
        Args:
            value: Value to set for the appStoreBlockInAppPurchases property.
        """
        self._app_store_block_in_app_purchases = value
    
    @property
    def app_store_block_u_i_app_installation(self,) -> Optional[bool]:
        """
        Gets the appStoreBlockUIAppInstallation property value. Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._app_store_block_u_i_app_installation
    
    @app_store_block_u_i_app_installation.setter
    def app_store_block_u_i_app_installation(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreBlockUIAppInstallation property value. Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
        Args:
            value: Value to set for the appStoreBlockUIAppInstallation property.
        """
        self._app_store_block_u_i_app_installation = value
    
    @property
    def app_store_require_password(self,) -> Optional[bool]:
        """
        Gets the appStoreRequirePassword property value. Indicates whether or not to require a password when using the app store.
        Returns: Optional[bool]
        """
        return self._app_store_require_password
    
    @app_store_require_password.setter
    def app_store_require_password(self,value: Optional[bool] = None) -> None:
        """
        Sets the appStoreRequirePassword property value. Indicates whether or not to require a password when using the app store.
        Args:
            value: Value to set for the appStoreRequirePassword property.
        """
        self._app_store_require_password = value
    
    @property
    def apps_visibility_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsVisibilityList property value. List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_visibility_list
    
    @apps_visibility_list.setter
    def apps_visibility_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsVisibilityList property value. List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the appsVisibilityList property.
        """
        self._apps_visibility_list = value
    
    @property
    def apps_visibility_list_type(self,) -> Optional[app_list_type.AppListType]:
        """
        Gets the appsVisibilityListType property value. Possible values of the compliance app list.
        Returns: Optional[app_list_type.AppListType]
        """
        return self._apps_visibility_list_type
    
    @apps_visibility_list_type.setter
    def apps_visibility_list_type(self,value: Optional[app_list_type.AppListType] = None) -> None:
        """
        Sets the appsVisibilityListType property value. Possible values of the compliance app list.
        Args:
            value: Value to set for the appsVisibilityListType property.
        """
        self._apps_visibility_list_type = value
    
    @property
    def bluetooth_block_modification(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockModification property value. Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
        Returns: Optional[bool]
        """
        return self._bluetooth_block_modification
    
    @bluetooth_block_modification.setter
    def bluetooth_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockModification property value. Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
        Args:
            value: Value to set for the bluetoothBlockModification property.
        """
        self._bluetooth_block_modification = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the cameraBlocked property.
        """
        self._camera_blocked = value
    
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
    
    @property
    def cellular_block_global_background_fetch_while_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockGlobalBackgroundFetchWhileRoaming property value. Indicates whether or not to block global background fetch while roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_global_background_fetch_while_roaming
    
    @cellular_block_global_background_fetch_while_roaming.setter
    def cellular_block_global_background_fetch_while_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockGlobalBackgroundFetchWhileRoaming property value. Indicates whether or not to block global background fetch while roaming.
        Args:
            value: Value to set for the cellularBlockGlobalBackgroundFetchWhileRoaming property.
        """
        self._cellular_block_global_background_fetch_while_roaming = value
    
    @property
    def cellular_block_per_app_data_modification(self,) -> Optional[bool]:
        """
        Gets the cellularBlockPerAppDataModification property value. Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._cellular_block_per_app_data_modification
    
    @cellular_block_per_app_data_modification.setter
    def cellular_block_per_app_data_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockPerAppDataModification property value. Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
        Args:
            value: Value to set for the cellularBlockPerAppDataModification property.
        """
        self._cellular_block_per_app_data_modification = value
    
    @property
    def cellular_block_personal_hotspot(self,) -> Optional[bool]:
        """
        Gets the cellularBlockPersonalHotspot property value. Indicates whether or not to block Personal Hotspot.
        Returns: Optional[bool]
        """
        return self._cellular_block_personal_hotspot
    
    @cellular_block_personal_hotspot.setter
    def cellular_block_personal_hotspot(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockPersonalHotspot property value. Indicates whether or not to block Personal Hotspot.
        Args:
            value: Value to set for the cellularBlockPersonalHotspot property.
        """
        self._cellular_block_personal_hotspot = value
    
    @property
    def cellular_block_voice_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockVoiceRoaming property value. Indicates whether or not to block voice roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_voice_roaming
    
    @cellular_block_voice_roaming.setter
    def cellular_block_voice_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockVoiceRoaming property value. Indicates whether or not to block voice roaming.
        Args:
            value: Value to set for the cellularBlockVoiceRoaming property.
        """
        self._cellular_block_voice_roaming = value
    
    @property
    def certificates_block_untrusted_tls_certificates(self,) -> Optional[bool]:
        """
        Gets the certificatesBlockUntrustedTlsCertificates property value. Indicates whether or not to block untrusted TLS certificates.
        Returns: Optional[bool]
        """
        return self._certificates_block_untrusted_tls_certificates
    
    @certificates_block_untrusted_tls_certificates.setter
    def certificates_block_untrusted_tls_certificates(self,value: Optional[bool] = None) -> None:
        """
        Sets the certificatesBlockUntrustedTlsCertificates property value. Indicates whether or not to block untrusted TLS certificates.
        Args:
            value: Value to set for the certificatesBlockUntrustedTlsCertificates property.
        """
        self._certificates_block_untrusted_tls_certificates = value
    
    @property
    def classroom_app_block_remote_screen_observation(self,) -> Optional[bool]:
        """
        Gets the classroomAppBlockRemoteScreenObservation property value. Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
        Returns: Optional[bool]
        """
        return self._classroom_app_block_remote_screen_observation
    
    @classroom_app_block_remote_screen_observation.setter
    def classroom_app_block_remote_screen_observation(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomAppBlockRemoteScreenObservation property value. Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
        Args:
            value: Value to set for the classroomAppBlockRemoteScreenObservation property.
        """
        self._classroom_app_block_remote_screen_observation = value
    
    @property
    def classroom_app_force_unprompted_screen_observation(self,) -> Optional[bool]:
        """
        Gets the classroomAppForceUnpromptedScreenObservation property value. Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._classroom_app_force_unprompted_screen_observation
    
    @classroom_app_force_unprompted_screen_observation.setter
    def classroom_app_force_unprompted_screen_observation(self,value: Optional[bool] = None) -> None:
        """
        Sets the classroomAppForceUnpromptedScreenObservation property value. Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
        Args:
            value: Value to set for the classroomAppForceUnpromptedScreenObservation property.
        """
        self._classroom_app_force_unprompted_screen_observation = value
    
    @property
    def compliant_app_list_type(self,) -> Optional[app_list_type.AppListType]:
        """
        Gets the compliantAppListType property value. Possible values of the compliance app list.
        Returns: Optional[app_list_type.AppListType]
        """
        return self._compliant_app_list_type
    
    @compliant_app_list_type.setter
    def compliant_app_list_type(self,value: Optional[app_list_type.AppListType] = None) -> None:
        """
        Sets the compliantAppListType property value. Possible values of the compliance app list.
        Args:
            value: Value to set for the compliantAppListType property.
        """
        self._compliant_app_list_type = value
    
    @property
    def compliant_apps_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the compliantAppsList property value. List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._compliant_apps_list
    
    @compliant_apps_list.setter
    def compliant_apps_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the compliantAppsList property value. List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the compliantAppsList property.
        """
        self._compliant_apps_list = value
    
    @property
    def configuration_profile_block_changes(self,) -> Optional[bool]:
        """
        Gets the configurationProfileBlockChanges property value. Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._configuration_profile_block_changes
    
    @configuration_profile_block_changes.setter
    def configuration_profile_block_changes(self,value: Optional[bool] = None) -> None:
        """
        Sets the configurationProfileBlockChanges property value. Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
        Args:
            value: Value to set for the configurationProfileBlockChanges property.
        """
        self._configuration_profile_block_changes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosGeneralDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosGeneralDeviceConfiguration"
        # Indicates whether or not to allow account modification when the device is in supervised mode.
        self._account_block_modification: Optional[bool] = None
        # Indicates whether or not to allow activation lock when the device is in the supervised mode.
        self._activation_lock_allow_when_supervised: Optional[bool] = None
        # Indicates whether or not to allow AirDrop when the device is in supervised mode.
        self._air_drop_blocked: Optional[bool] = None
        # Indicates whether or not to cause AirDrop to be considered an unmanaged drop target (iOS 9.0 and later).
        self._air_drop_force_unmanaged_drop_target: Optional[bool] = None
        # Indicates whether or not to enforce all devices receiving AirPlay requests from this device to use a pairing password.
        self._air_play_force_pairing_password_for_outgoing_requests: Optional[bool] = None
        # Indicates whether or not to block the user from using News when the device is in supervised mode (iOS 9.0 and later).
        self._apple_news_blocked: Optional[bool] = None
        # Indicates whether or not to allow Apple Watch pairing when the device is in supervised mode (iOS 9.0 and later).
        self._apple_watch_block_pairing: Optional[bool] = None
        # Indicates whether or not to force a paired Apple Watch to use Wrist Detection (iOS 8.2 and later).
        self._apple_watch_force_wrist_detection: Optional[bool] = None
        # Gets or sets the list of iOS apps allowed to autonomously enter Single App Mode. Supervised only. iOS 7.0 and later. This collection can contain a maximum of 500 elements.
        self._apps_single_app_mode_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block the automatic downloading of apps purchased on other devices when the device is in supervised mode (iOS 9.0 and later).
        self._app_store_block_automatic_downloads: Optional[bool] = None
        # Indicates whether or not to block the user from using the App Store. Requires a supervised device for iOS 13 and later.
        self._app_store_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from making in app purchases.
        self._app_store_block_in_app_purchases: Optional[bool] = None
        # Indicates whether or not to block the App Store app, not restricting installation through Host apps. Applies to supervised mode only (iOS 9.0 and later).
        self._app_store_block_u_i_app_installation: Optional[bool] = None
        # Indicates whether or not to require a password when using the app store.
        self._app_store_require_password: Optional[bool] = None
        # List of apps in the visibility list (either visible/launchable apps list or hidden/unlaunchable apps list, controlled by AppsVisibilityListType) (iOS 9.3 and later). This collection can contain a maximum of 10000 elements.
        self._apps_visibility_list: Optional[List[app_list_item.AppListItem]] = None
        # Possible values of the compliance app list.
        self._apps_visibility_list_type: Optional[app_list_type.AppListType] = None
        # Indicates whether or not to allow modification of Bluetooth settings when the device is in supervised mode (iOS 10.0 and later).
        self._bluetooth_block_modification: Optional[bool] = None
        # Indicates whether or not to block the user from accessing the camera of the device. Requires a supervised device for iOS 13 and later.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not to block data roaming.
        self._cellular_block_data_roaming: Optional[bool] = None
        # Indicates whether or not to block global background fetch while roaming.
        self._cellular_block_global_background_fetch_while_roaming: Optional[bool] = None
        # Indicates whether or not to allow changes to cellular app data usage settings when the device is in supervised mode.
        self._cellular_block_per_app_data_modification: Optional[bool] = None
        # Indicates whether or not to block Personal Hotspot.
        self._cellular_block_personal_hotspot: Optional[bool] = None
        # Indicates whether or not to block voice roaming.
        self._cellular_block_voice_roaming: Optional[bool] = None
        # Indicates whether or not to block untrusted TLS certificates.
        self._certificates_block_untrusted_tls_certificates: Optional[bool] = None
        # Indicates whether or not to allow remote screen observation by Classroom app when the device is in supervised mode (iOS 9.3 and later).
        self._classroom_app_block_remote_screen_observation: Optional[bool] = None
        # Indicates whether or not to automatically give permission to the teacher of a managed course on the Classroom app to view a student's screen without prompting when the device is in supervised mode.
        self._classroom_app_force_unprompted_screen_observation: Optional[bool] = None
        # Possible values of the compliance app list.
        self._compliant_app_list_type: Optional[app_list_type.AppListType] = None
        # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        self._compliant_apps_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block the user from installing configuration profiles and certificates interactively when the device is in supervised mode.
        self._configuration_profile_block_changes: Optional[bool] = None
        # Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
        self._definition_lookup_blocked: Optional[bool] = None
        # Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
        self._device_block_enable_restrictions: Optional[bool] = None
        # Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
        self._device_block_erase_content_and_settings: Optional[bool] = None
        # Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
        self._device_block_name_modification: Optional[bool] = None
        # Indicates whether or not to block diagnostic data submission.
        self._diagnostic_data_block_submission: Optional[bool] = None
        # Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
        self._diagnostic_data_block_submission_modification: Optional[bool] = None
        # Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
        self._documents_block_managed_documents_in_unmanaged_apps: Optional[bool] = None
        # Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
        self._documents_block_unmanaged_documents_in_managed_apps: Optional[bool] = None
        # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        self._email_in_domain_suffixes: Optional[List[str]] = None
        # Indicates whether or not to block the user from trusting an enterprise app.
        self._enterprise_app_block_trust: Optional[bool] = None
        # [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
        self._enterprise_app_block_trust_modification: Optional[bool] = None
        # Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
        self._face_time_blocked: Optional[bool] = None
        # Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
        self._find_my_friends_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
        self._game_center_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
        self._gaming_block_game_center_friends: Optional[bool] = None
        # Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
        self._gaming_block_multiplayer: Optional[bool] = None
        # indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
        self._host_pairing_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
        self._i_books_store_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
        self._i_books_store_block_erotica: Optional[bool] = None
        # Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
        self._i_cloud_block_activity_continuation: Optional[bool] = None
        # Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
        self._i_cloud_block_backup: Optional[bool] = None
        # Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
        self._i_cloud_block_document_sync: Optional[bool] = None
        # Indicates whether or not to block Managed Apps Cloud Sync.
        self._i_cloud_block_managed_apps_sync: Optional[bool] = None
        # Indicates whether or not to block iCloud Photo Library.
        self._i_cloud_block_photo_library: Optional[bool] = None
        # Indicates whether or not to block iCloud Photo Stream Sync.
        self._i_cloud_block_photo_stream_sync: Optional[bool] = None
        # Indicates whether or not to block Shared Photo Stream.
        self._i_cloud_block_shared_photo_stream: Optional[bool] = None
        # Indicates whether or not to require backups to iCloud be encrypted.
        self._i_cloud_require_encrypted_backup: Optional[bool] = None
        # Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
        self._i_tunes_block_explicit_content: Optional[bool] = None
        # Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
        self._i_tunes_block_music_service: Optional[bool] = None
        # Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
        self._i_tunes_block_radio: Optional[bool] = None
        # Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
        self._keyboard_block_auto_correct: Optional[bool] = None
        # Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
        self._keyboard_block_dictation: Optional[bool] = None
        # Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
        self._keyboard_block_predictive: Optional[bool] = None
        # Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
        self._keyboard_block_shortcuts: Optional[bool] = None
        # Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
        self._keyboard_block_spell_check: Optional[bool] = None
        # Indicates whether or not to allow assistive speak while in kiosk mode.
        self._kiosk_mode_allow_assistive_speak: Optional[bool] = None
        # Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
        self._kiosk_mode_allow_assistive_touch_settings: Optional[bool] = None
        # Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
        self._kiosk_mode_allow_auto_lock: Optional[bool] = None
        # Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
        self._kiosk_mode_allow_color_inversion_settings: Optional[bool] = None
        # Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
        self._kiosk_mode_allow_ringer_switch: Optional[bool] = None
        # Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
        self._kiosk_mode_allow_screen_rotation: Optional[bool] = None
        # Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
        self._kiosk_mode_allow_sleep_button: Optional[bool] = None
        # Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
        self._kiosk_mode_allow_touchscreen: Optional[bool] = None
        # Indicates whether or not to allow access to the voice over settings while in kiosk mode.
        self._kiosk_mode_allow_voice_over_settings: Optional[bool] = None
        # Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
        self._kiosk_mode_allow_volume_buttons: Optional[bool] = None
        # Indicates whether or not to allow access to the zoom settings while in kiosk mode.
        self._kiosk_mode_allow_zoom_settings: Optional[bool] = None
        # URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
        self._kiosk_mode_app_store_url: Optional[str] = None
        # ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
        self._kiosk_mode_built_in_app_id: Optional[str] = None
        # Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
        self._kiosk_mode_managed_app_id: Optional[str] = None
        # Indicates whether or not to require assistive touch while in kiosk mode.
        self._kiosk_mode_require_assistive_touch: Optional[bool] = None
        # Indicates whether or not to require color inversion while in kiosk mode.
        self._kiosk_mode_require_color_inversion: Optional[bool] = None
        # Indicates whether or not to require mono audio while in kiosk mode.
        self._kiosk_mode_require_mono_audio: Optional[bool] = None
        # Indicates whether or not to require voice over while in kiosk mode.
        self._kiosk_mode_require_voice_over: Optional[bool] = None
        # Indicates whether or not to require zoom while in kiosk mode.
        self._kiosk_mode_require_zoom: Optional[bool] = None
        # Indicates whether or not to block the user from using control center on the lock screen.
        self._lock_screen_block_control_center: Optional[bool] = None
        # Indicates whether or not to block the user from using the notification view on the lock screen.
        self._lock_screen_block_notification_view: Optional[bool] = None
        # Indicates whether or not to block the user from using passbook when the device is locked.
        self._lock_screen_block_passbook: Optional[bool] = None
        # Indicates whether or not to block the user from using the Today View on the lock screen.
        self._lock_screen_block_today_view: Optional[bool] = None
        # Apps rating as in media content
        self._media_content_rating_apps: Optional[rating_apps_type.RatingAppsType] = None
        # Media content rating settings for Australia
        self._media_content_rating_australia: Optional[media_content_rating_australia.MediaContentRatingAustralia] = None
        # Media content rating settings for Canada
        self._media_content_rating_canada: Optional[media_content_rating_canada.MediaContentRatingCanada] = None
        # Media content rating settings for France
        self._media_content_rating_france: Optional[media_content_rating_france.MediaContentRatingFrance] = None
        # Media content rating settings for Germany
        self._media_content_rating_germany: Optional[media_content_rating_germany.MediaContentRatingGermany] = None
        # Media content rating settings for Ireland
        self._media_content_rating_ireland: Optional[media_content_rating_ireland.MediaContentRatingIreland] = None
        # Media content rating settings for Japan
        self._media_content_rating_japan: Optional[media_content_rating_japan.MediaContentRatingJapan] = None
        # Media content rating settings for New Zealand
        self._media_content_rating_new_zealand: Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand] = None
        # Media content rating settings for United Kingdom
        self._media_content_rating_united_kingdom: Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom] = None
        # Media content rating settings for United States
        self._media_content_rating_united_states: Optional[media_content_rating_united_states.MediaContentRatingUnitedStates] = None
        # Indicates whether or not to block the user from using the Messages app on the supervised device.
        self._messages_blocked: Optional[bool] = None
        # List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
        self._network_usage_rules: Optional[List[ios_network_usage_rule.IosNetworkUsageRule]] = None
        # Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
        self._notifications_block_settings_modification: Optional[bool] = None
        # Block modification of registered Touch ID fingerprints when in supervised mode.
        self._passcode_block_fingerprint_modification: Optional[bool] = None
        # Indicates whether or not to block fingerprint unlock.
        self._passcode_block_fingerprint_unlock: Optional[bool] = None
        # Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
        self._passcode_block_modification: Optional[bool] = None
        # Indicates whether or not to block simple passcodes.
        self._passcode_block_simple: Optional[bool] = None
        # Number of days before the passcode expires. Valid values 1 to 65535
        self._passcode_expiration_days: Optional[int] = None
        # Number of character sets a passcode must contain. Valid values 0 to 4
        self._passcode_minimum_character_set_count: Optional[int] = None
        # Minimum length of passcode. Valid values 4 to 14
        self._passcode_minimum_length: Optional[int] = None
        # Minutes of inactivity before a passcode is required.
        self._passcode_minutes_of_inactivity_before_lock: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._passcode_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Number of previous passcodes to block. Valid values 1 to 24
        self._passcode_previous_passcode_block_count: Optional[int] = None
        # Indicates whether or not to require a passcode.
        self._passcode_required: Optional[bool] = None
        # Possible values of required passwords.
        self._passcode_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Number of sign in failures allowed before wiping the device. Valid values 2 to 11
        self._passcode_sign_in_failure_count_before_wipe: Optional[int] = None
        # Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
        self._podcasts_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
        self._safari_block_autofill: Optional[bool] = None
        # Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
        self._safari_blocked: Optional[bool] = None
        # Indicates whether or not to block JavaScript in Safari.
        self._safari_block_java_script: Optional[bool] = None
        # Indicates whether or not to block popups in Safari.
        self._safari_block_popups: Optional[bool] = None
        # Web Browser Cookie Settings.
        self._safari_cookie_settings: Optional[web_browser_cookie_settings.WebBrowserCookieSettings] = None
        # URLs matching the patterns listed here will be considered managed.
        self._safari_managed_domains: Optional[List[str]] = None
        # Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
        self._safari_password_auto_fill_domains: Optional[List[str]] = None
        # Indicates whether or not to require fraud warning in Safari.
        self._safari_require_fraud_warning: Optional[bool] = None
        # Indicates whether or not to block the user from taking Screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using Siri.
        self._siri_blocked: Optional[bool] = None
        # Indicates whether or not to block the user from using Siri when locked.
        self._siri_blocked_when_locked: Optional[bool] = None
        # Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
        self._siri_block_user_generated_content: Optional[bool] = None
        # Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
        self._siri_require_profanity_filter: Optional[bool] = None
        # Indicates whether or not to block Spotlight search from returning internet results on supervised device.
        self._spotlight_block_internet_results: Optional[bool] = None
        # Indicates whether or not to block voice dialing.
        self._voice_dialing_blocked: Optional[bool] = None
        # Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
        self._wallpaper_block_modification: Optional[bool] = None
        # Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
        self._wi_fi_connect_only_to_configured_networks: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosGeneralDeviceConfiguration()
    
    @property
    def definition_lookup_blocked(self,) -> Optional[bool]:
        """
        Gets the definitionLookupBlocked property value. Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
        Returns: Optional[bool]
        """
        return self._definition_lookup_blocked
    
    @definition_lookup_blocked.setter
    def definition_lookup_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the definitionLookupBlocked property value. Indicates whether or not to block definition lookup when the device is in supervised mode (iOS 8.1.3 and later ).
        Args:
            value: Value to set for the definitionLookupBlocked property.
        """
        self._definition_lookup_blocked = value
    
    @property
    def device_block_enable_restrictions(self,) -> Optional[bool]:
        """
        Gets the deviceBlockEnableRestrictions property value. Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._device_block_enable_restrictions
    
    @device_block_enable_restrictions.setter
    def device_block_enable_restrictions(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceBlockEnableRestrictions property value. Indicates whether or not to allow the user to enables restrictions in the device settings when the device is in supervised mode.
        Args:
            value: Value to set for the deviceBlockEnableRestrictions property.
        """
        self._device_block_enable_restrictions = value
    
    @property
    def device_block_erase_content_and_settings(self,) -> Optional[bool]:
        """
        Gets the deviceBlockEraseContentAndSettings property value. Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._device_block_erase_content_and_settings
    
    @device_block_erase_content_and_settings.setter
    def device_block_erase_content_and_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceBlockEraseContentAndSettings property value. Indicates whether or not to allow the use of the 'Erase all content and settings' option on the device when the device is in supervised mode.
        Args:
            value: Value to set for the deviceBlockEraseContentAndSettings property.
        """
        self._device_block_erase_content_and_settings = value
    
    @property
    def device_block_name_modification(self,) -> Optional[bool]:
        """
        Gets the deviceBlockNameModification property value. Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._device_block_name_modification
    
    @device_block_name_modification.setter
    def device_block_name_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceBlockNameModification property value. Indicates whether or not to allow device name modification when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the deviceBlockNameModification property.
        """
        self._device_block_name_modification = value
    
    @property
    def diagnostic_data_block_submission(self,) -> Optional[bool]:
        """
        Gets the diagnosticDataBlockSubmission property value. Indicates whether or not to block diagnostic data submission.
        Returns: Optional[bool]
        """
        return self._diagnostic_data_block_submission
    
    @diagnostic_data_block_submission.setter
    def diagnostic_data_block_submission(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticDataBlockSubmission property value. Indicates whether or not to block diagnostic data submission.
        Args:
            value: Value to set for the diagnosticDataBlockSubmission property.
        """
        self._diagnostic_data_block_submission = value
    
    @property
    def diagnostic_data_block_submission_modification(self,) -> Optional[bool]:
        """
        Gets the diagnosticDataBlockSubmissionModification property value. Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
        Returns: Optional[bool]
        """
        return self._diagnostic_data_block_submission_modification
    
    @diagnostic_data_block_submission_modification.setter
    def diagnostic_data_block_submission_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticDataBlockSubmissionModification property value. Indicates whether or not to allow diagnostics submission settings modification when the device is in supervised mode (iOS 9.3.2 and later).
        Args:
            value: Value to set for the diagnosticDataBlockSubmissionModification property.
        """
        self._diagnostic_data_block_submission_modification = value
    
    @property
    def documents_block_managed_documents_in_unmanaged_apps(self,) -> Optional[bool]:
        """
        Gets the documentsBlockManagedDocumentsInUnmanagedApps property value. Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
        Returns: Optional[bool]
        """
        return self._documents_block_managed_documents_in_unmanaged_apps
    
    @documents_block_managed_documents_in_unmanaged_apps.setter
    def documents_block_managed_documents_in_unmanaged_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the documentsBlockManagedDocumentsInUnmanagedApps property value. Indicates whether or not to block the user from viewing managed documents in unmanaged apps.
        Args:
            value: Value to set for the documentsBlockManagedDocumentsInUnmanagedApps property.
        """
        self._documents_block_managed_documents_in_unmanaged_apps = value
    
    @property
    def documents_block_unmanaged_documents_in_managed_apps(self,) -> Optional[bool]:
        """
        Gets the documentsBlockUnmanagedDocumentsInManagedApps property value. Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
        Returns: Optional[bool]
        """
        return self._documents_block_unmanaged_documents_in_managed_apps
    
    @documents_block_unmanaged_documents_in_managed_apps.setter
    def documents_block_unmanaged_documents_in_managed_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the documentsBlockUnmanagedDocumentsInManagedApps property value. Indicates whether or not to block the user from viewing unmanaged documents in managed apps.
        Args:
            value: Value to set for the documentsBlockUnmanagedDocumentsInManagedApps property.
        """
        self._documents_block_unmanaged_documents_in_managed_apps = value
    
    @property
    def email_in_domain_suffixes(self,) -> Optional[List[str]]:
        """
        Gets the emailInDomainSuffixes property value. An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        Returns: Optional[List[str]]
        """
        return self._email_in_domain_suffixes
    
    @email_in_domain_suffixes.setter
    def email_in_domain_suffixes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the emailInDomainSuffixes property value. An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
        Args:
            value: Value to set for the emailInDomainSuffixes property.
        """
        self._email_in_domain_suffixes = value
    
    @property
    def enterprise_app_block_trust(self,) -> Optional[bool]:
        """
        Gets the enterpriseAppBlockTrust property value. Indicates whether or not to block the user from trusting an enterprise app.
        Returns: Optional[bool]
        """
        return self._enterprise_app_block_trust
    
    @enterprise_app_block_trust.setter
    def enterprise_app_block_trust(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseAppBlockTrust property value. Indicates whether or not to block the user from trusting an enterprise app.
        Args:
            value: Value to set for the enterpriseAppBlockTrust property.
        """
        self._enterprise_app_block_trust = value
    
    @property
    def enterprise_app_block_trust_modification(self,) -> Optional[bool]:
        """
        Gets the enterpriseAppBlockTrustModification property value. [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
        Returns: Optional[bool]
        """
        return self._enterprise_app_block_trust_modification
    
    @enterprise_app_block_trust_modification.setter
    def enterprise_app_block_trust_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseAppBlockTrustModification property value. [Deprecated] Configuring this setting and setting the value to 'true' has no effect on the device.
        Args:
            value: Value to set for the enterpriseAppBlockTrustModification property.
        """
        self._enterprise_app_block_trust_modification = value
    
    @property
    def face_time_blocked(self,) -> Optional[bool]:
        """
        Gets the faceTimeBlocked property value. Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._face_time_blocked
    
    @face_time_blocked.setter
    def face_time_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the faceTimeBlocked property value. Indicates whether or not to block the user from using FaceTime. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the faceTimeBlocked property.
        """
        self._face_time_blocked = value
    
    @property
    def find_my_friends_blocked(self,) -> Optional[bool]:
        """
        Gets the findMyFriendsBlocked property value. Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._find_my_friends_blocked
    
    @find_my_friends_blocked.setter
    def find_my_friends_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the findMyFriendsBlocked property value. Indicates whether or not to block changes to Find My Friends when the device is in supervised mode.
        Args:
            value: Value to set for the findMyFriendsBlocked property.
        """
        self._find_my_friends_blocked = value
    
    @property
    def game_center_blocked(self,) -> Optional[bool]:
        """
        Gets the gameCenterBlocked property value. Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._game_center_blocked
    
    @game_center_blocked.setter
    def game_center_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the gameCenterBlocked property value. Indicates whether or not to block the user from using Game Center when the device is in supervised mode.
        Args:
            value: Value to set for the gameCenterBlocked property.
        """
        self._game_center_blocked = value
    
    @property
    def gaming_block_game_center_friends(self,) -> Optional[bool]:
        """
        Gets the gamingBlockGameCenterFriends property value. Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._gaming_block_game_center_friends
    
    @gaming_block_game_center_friends.setter
    def gaming_block_game_center_friends(self,value: Optional[bool] = None) -> None:
        """
        Sets the gamingBlockGameCenterFriends property value. Indicates whether or not to block the user from having friends in Game Center. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the gamingBlockGameCenterFriends property.
        """
        self._gaming_block_game_center_friends = value
    
    @property
    def gaming_block_multiplayer(self,) -> Optional[bool]:
        """
        Gets the gamingBlockMultiplayer property value. Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._gaming_block_multiplayer
    
    @gaming_block_multiplayer.setter
    def gaming_block_multiplayer(self,value: Optional[bool] = None) -> None:
        """
        Sets the gamingBlockMultiplayer property value. Indicates whether or not to block the user from using multiplayer gaming. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the gamingBlockMultiplayer property.
        """
        self._gaming_block_multiplayer = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_block_modification": lambda n : setattr(self, 'account_block_modification', n.get_bool_value()),
            "activation_lock_allow_when_supervised": lambda n : setattr(self, 'activation_lock_allow_when_supervised', n.get_bool_value()),
            "air_drop_blocked": lambda n : setattr(self, 'air_drop_blocked', n.get_bool_value()),
            "air_drop_force_unmanaged_drop_target": lambda n : setattr(self, 'air_drop_force_unmanaged_drop_target', n.get_bool_value()),
            "air_play_force_pairing_password_for_outgoing_requests": lambda n : setattr(self, 'air_play_force_pairing_password_for_outgoing_requests', n.get_bool_value()),
            "apple_news_blocked": lambda n : setattr(self, 'apple_news_blocked', n.get_bool_value()),
            "apple_watch_block_pairing": lambda n : setattr(self, 'apple_watch_block_pairing', n.get_bool_value()),
            "apple_watch_force_wrist_detection": lambda n : setattr(self, 'apple_watch_force_wrist_detection', n.get_bool_value()),
            "apps_single_app_mode_list": lambda n : setattr(self, 'apps_single_app_mode_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "app_store_block_automatic_downloads": lambda n : setattr(self, 'app_store_block_automatic_downloads', n.get_bool_value()),
            "app_store_blocked": lambda n : setattr(self, 'app_store_blocked', n.get_bool_value()),
            "app_store_block_in_app_purchases": lambda n : setattr(self, 'app_store_block_in_app_purchases', n.get_bool_value()),
            "app_store_block_u_i_app_installation": lambda n : setattr(self, 'app_store_block_u_i_app_installation', n.get_bool_value()),
            "app_store_require_password": lambda n : setattr(self, 'app_store_require_password', n.get_bool_value()),
            "apps_visibility_list": lambda n : setattr(self, 'apps_visibility_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "apps_visibility_list_type": lambda n : setattr(self, 'apps_visibility_list_type', n.get_enum_value(app_list_type.AppListType)),
            "bluetooth_block_modification": lambda n : setattr(self, 'bluetooth_block_modification', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_data_roaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "cellular_block_global_background_fetch_while_roaming": lambda n : setattr(self, 'cellular_block_global_background_fetch_while_roaming', n.get_bool_value()),
            "cellular_block_per_app_data_modification": lambda n : setattr(self, 'cellular_block_per_app_data_modification', n.get_bool_value()),
            "cellular_block_personal_hotspot": lambda n : setattr(self, 'cellular_block_personal_hotspot', n.get_bool_value()),
            "cellular_block_voice_roaming": lambda n : setattr(self, 'cellular_block_voice_roaming', n.get_bool_value()),
            "certificates_block_untrusted_tls_certificates": lambda n : setattr(self, 'certificates_block_untrusted_tls_certificates', n.get_bool_value()),
            "classroom_app_block_remote_screen_observation": lambda n : setattr(self, 'classroom_app_block_remote_screen_observation', n.get_bool_value()),
            "classroom_app_force_unprompted_screen_observation": lambda n : setattr(self, 'classroom_app_force_unprompted_screen_observation', n.get_bool_value()),
            "compliant_app_list_type": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(app_list_type.AppListType)),
            "compliant_apps_list": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "configuration_profile_block_changes": lambda n : setattr(self, 'configuration_profile_block_changes', n.get_bool_value()),
            "definition_lookup_blocked": lambda n : setattr(self, 'definition_lookup_blocked', n.get_bool_value()),
            "device_block_enable_restrictions": lambda n : setattr(self, 'device_block_enable_restrictions', n.get_bool_value()),
            "device_block_erase_content_and_settings": lambda n : setattr(self, 'device_block_erase_content_and_settings', n.get_bool_value()),
            "device_block_name_modification": lambda n : setattr(self, 'device_block_name_modification', n.get_bool_value()),
            "diagnostic_data_block_submission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "diagnostic_data_block_submission_modification": lambda n : setattr(self, 'diagnostic_data_block_submission_modification', n.get_bool_value()),
            "documents_block_managed_documents_in_unmanaged_apps": lambda n : setattr(self, 'documents_block_managed_documents_in_unmanaged_apps', n.get_bool_value()),
            "documents_block_unmanaged_documents_in_managed_apps": lambda n : setattr(self, 'documents_block_unmanaged_documents_in_managed_apps', n.get_bool_value()),
            "email_in_domain_suffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "enterprise_app_block_trust": lambda n : setattr(self, 'enterprise_app_block_trust', n.get_bool_value()),
            "enterprise_app_block_trust_modification": lambda n : setattr(self, 'enterprise_app_block_trust_modification', n.get_bool_value()),
            "face_time_blocked": lambda n : setattr(self, 'face_time_blocked', n.get_bool_value()),
            "find_my_friends_blocked": lambda n : setattr(self, 'find_my_friends_blocked', n.get_bool_value()),
            "game_center_blocked": lambda n : setattr(self, 'game_center_blocked', n.get_bool_value()),
            "gaming_block_game_center_friends": lambda n : setattr(self, 'gaming_block_game_center_friends', n.get_bool_value()),
            "gaming_block_multiplayer": lambda n : setattr(self, 'gaming_block_multiplayer', n.get_bool_value()),
            "host_pairing_blocked": lambda n : setattr(self, 'host_pairing_blocked', n.get_bool_value()),
            "i_books_store_blocked": lambda n : setattr(self, 'i_books_store_blocked', n.get_bool_value()),
            "i_books_store_block_erotica": lambda n : setattr(self, 'i_books_store_block_erotica', n.get_bool_value()),
            "i_cloud_block_activity_continuation": lambda n : setattr(self, 'i_cloud_block_activity_continuation', n.get_bool_value()),
            "i_cloud_block_backup": lambda n : setattr(self, 'i_cloud_block_backup', n.get_bool_value()),
            "i_cloud_block_document_sync": lambda n : setattr(self, 'i_cloud_block_document_sync', n.get_bool_value()),
            "i_cloud_block_managed_apps_sync": lambda n : setattr(self, 'i_cloud_block_managed_apps_sync', n.get_bool_value()),
            "i_cloud_block_photo_library": lambda n : setattr(self, 'i_cloud_block_photo_library', n.get_bool_value()),
            "i_cloud_block_photo_stream_sync": lambda n : setattr(self, 'i_cloud_block_photo_stream_sync', n.get_bool_value()),
            "i_cloud_block_shared_photo_stream": lambda n : setattr(self, 'i_cloud_block_shared_photo_stream', n.get_bool_value()),
            "i_cloud_require_encrypted_backup": lambda n : setattr(self, 'i_cloud_require_encrypted_backup', n.get_bool_value()),
            "i_tunes_block_explicit_content": lambda n : setattr(self, 'i_tunes_block_explicit_content', n.get_bool_value()),
            "i_tunes_block_music_service": lambda n : setattr(self, 'i_tunes_block_music_service', n.get_bool_value()),
            "i_tunes_block_radio": lambda n : setattr(self, 'i_tunes_block_radio', n.get_bool_value()),
            "keyboard_block_auto_correct": lambda n : setattr(self, 'keyboard_block_auto_correct', n.get_bool_value()),
            "keyboard_block_dictation": lambda n : setattr(self, 'keyboard_block_dictation', n.get_bool_value()),
            "keyboard_block_predictive": lambda n : setattr(self, 'keyboard_block_predictive', n.get_bool_value()),
            "keyboard_block_shortcuts": lambda n : setattr(self, 'keyboard_block_shortcuts', n.get_bool_value()),
            "keyboard_block_spell_check": lambda n : setattr(self, 'keyboard_block_spell_check', n.get_bool_value()),
            "kiosk_mode_allow_assistive_speak": lambda n : setattr(self, 'kiosk_mode_allow_assistive_speak', n.get_bool_value()),
            "kiosk_mode_allow_assistive_touch_settings": lambda n : setattr(self, 'kiosk_mode_allow_assistive_touch_settings', n.get_bool_value()),
            "kiosk_mode_allow_auto_lock": lambda n : setattr(self, 'kiosk_mode_allow_auto_lock', n.get_bool_value()),
            "kiosk_mode_allow_color_inversion_settings": lambda n : setattr(self, 'kiosk_mode_allow_color_inversion_settings', n.get_bool_value()),
            "kiosk_mode_allow_ringer_switch": lambda n : setattr(self, 'kiosk_mode_allow_ringer_switch', n.get_bool_value()),
            "kiosk_mode_allow_screen_rotation": lambda n : setattr(self, 'kiosk_mode_allow_screen_rotation', n.get_bool_value()),
            "kiosk_mode_allow_sleep_button": lambda n : setattr(self, 'kiosk_mode_allow_sleep_button', n.get_bool_value()),
            "kiosk_mode_allow_touchscreen": lambda n : setattr(self, 'kiosk_mode_allow_touchscreen', n.get_bool_value()),
            "kiosk_mode_allow_voice_over_settings": lambda n : setattr(self, 'kiosk_mode_allow_voice_over_settings', n.get_bool_value()),
            "kiosk_mode_allow_volume_buttons": lambda n : setattr(self, 'kiosk_mode_allow_volume_buttons', n.get_bool_value()),
            "kiosk_mode_allow_zoom_settings": lambda n : setattr(self, 'kiosk_mode_allow_zoom_settings', n.get_bool_value()),
            "kiosk_mode_app_store_url": lambda n : setattr(self, 'kiosk_mode_app_store_url', n.get_str_value()),
            "kiosk_mode_built_in_app_id": lambda n : setattr(self, 'kiosk_mode_built_in_app_id', n.get_str_value()),
            "kiosk_mode_managed_app_id": lambda n : setattr(self, 'kiosk_mode_managed_app_id', n.get_str_value()),
            "kiosk_mode_require_assistive_touch": lambda n : setattr(self, 'kiosk_mode_require_assistive_touch', n.get_bool_value()),
            "kiosk_mode_require_color_inversion": lambda n : setattr(self, 'kiosk_mode_require_color_inversion', n.get_bool_value()),
            "kiosk_mode_require_mono_audio": lambda n : setattr(self, 'kiosk_mode_require_mono_audio', n.get_bool_value()),
            "kiosk_mode_require_voice_over": lambda n : setattr(self, 'kiosk_mode_require_voice_over', n.get_bool_value()),
            "kiosk_mode_require_zoom": lambda n : setattr(self, 'kiosk_mode_require_zoom', n.get_bool_value()),
            "lock_screen_block_control_center": lambda n : setattr(self, 'lock_screen_block_control_center', n.get_bool_value()),
            "lock_screen_block_notification_view": lambda n : setattr(self, 'lock_screen_block_notification_view', n.get_bool_value()),
            "lock_screen_block_passbook": lambda n : setattr(self, 'lock_screen_block_passbook', n.get_bool_value()),
            "lock_screen_block_today_view": lambda n : setattr(self, 'lock_screen_block_today_view', n.get_bool_value()),
            "media_content_rating_apps": lambda n : setattr(self, 'media_content_rating_apps', n.get_enum_value(rating_apps_type.RatingAppsType)),
            "media_content_rating_australia": lambda n : setattr(self, 'media_content_rating_australia', n.get_object_value(media_content_rating_australia.MediaContentRatingAustralia)),
            "media_content_rating_canada": lambda n : setattr(self, 'media_content_rating_canada', n.get_object_value(media_content_rating_canada.MediaContentRatingCanada)),
            "media_content_rating_france": lambda n : setattr(self, 'media_content_rating_france', n.get_object_value(media_content_rating_france.MediaContentRatingFrance)),
            "media_content_rating_germany": lambda n : setattr(self, 'media_content_rating_germany', n.get_object_value(media_content_rating_germany.MediaContentRatingGermany)),
            "media_content_rating_ireland": lambda n : setattr(self, 'media_content_rating_ireland', n.get_object_value(media_content_rating_ireland.MediaContentRatingIreland)),
            "media_content_rating_japan": lambda n : setattr(self, 'media_content_rating_japan', n.get_object_value(media_content_rating_japan.MediaContentRatingJapan)),
            "media_content_rating_new_zealand": lambda n : setattr(self, 'media_content_rating_new_zealand', n.get_object_value(media_content_rating_new_zealand.MediaContentRatingNewZealand)),
            "media_content_rating_united_kingdom": lambda n : setattr(self, 'media_content_rating_united_kingdom', n.get_object_value(media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom)),
            "media_content_rating_united_states": lambda n : setattr(self, 'media_content_rating_united_states', n.get_object_value(media_content_rating_united_states.MediaContentRatingUnitedStates)),
            "messages_blocked": lambda n : setattr(self, 'messages_blocked', n.get_bool_value()),
            "network_usage_rules": lambda n : setattr(self, 'network_usage_rules', n.get_collection_of_object_values(ios_network_usage_rule.IosNetworkUsageRule)),
            "notifications_block_settings_modification": lambda n : setattr(self, 'notifications_block_settings_modification', n.get_bool_value()),
            "passcode_block_fingerprint_modification": lambda n : setattr(self, 'passcode_block_fingerprint_modification', n.get_bool_value()),
            "passcode_block_fingerprint_unlock": lambda n : setattr(self, 'passcode_block_fingerprint_unlock', n.get_bool_value()),
            "passcode_block_modification": lambda n : setattr(self, 'passcode_block_modification', n.get_bool_value()),
            "passcode_block_simple": lambda n : setattr(self, 'passcode_block_simple', n.get_bool_value()),
            "passcode_expiration_days": lambda n : setattr(self, 'passcode_expiration_days', n.get_int_value()),
            "passcode_minimum_character_set_count": lambda n : setattr(self, 'passcode_minimum_character_set_count', n.get_int_value()),
            "passcode_minimum_length": lambda n : setattr(self, 'passcode_minimum_length', n.get_int_value()),
            "passcode_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passcode_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passcode_previous_passcode_block_count": lambda n : setattr(self, 'passcode_previous_passcode_block_count', n.get_int_value()),
            "passcode_required": lambda n : setattr(self, 'passcode_required', n.get_bool_value()),
            "passcode_required_type": lambda n : setattr(self, 'passcode_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "passcode_sign_in_failure_count_before_wipe": lambda n : setattr(self, 'passcode_sign_in_failure_count_before_wipe', n.get_int_value()),
            "podcasts_blocked": lambda n : setattr(self, 'podcasts_blocked', n.get_bool_value()),
            "safari_block_autofill": lambda n : setattr(self, 'safari_block_autofill', n.get_bool_value()),
            "safari_blocked": lambda n : setattr(self, 'safari_blocked', n.get_bool_value()),
            "safari_block_java_script": lambda n : setattr(self, 'safari_block_java_script', n.get_bool_value()),
            "safari_block_popups": lambda n : setattr(self, 'safari_block_popups', n.get_bool_value()),
            "safari_cookie_settings": lambda n : setattr(self, 'safari_cookie_settings', n.get_enum_value(web_browser_cookie_settings.WebBrowserCookieSettings)),
            "safari_managed_domains": lambda n : setattr(self, 'safari_managed_domains', n.get_collection_of_primitive_values(str)),
            "safari_password_auto_fill_domains": lambda n : setattr(self, 'safari_password_auto_fill_domains', n.get_collection_of_primitive_values(str)),
            "safari_require_fraud_warning": lambda n : setattr(self, 'safari_require_fraud_warning', n.get_bool_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "siri_blocked": lambda n : setattr(self, 'siri_blocked', n.get_bool_value()),
            "siri_blocked_when_locked": lambda n : setattr(self, 'siri_blocked_when_locked', n.get_bool_value()),
            "siri_block_user_generated_content": lambda n : setattr(self, 'siri_block_user_generated_content', n.get_bool_value()),
            "siri_require_profanity_filter": lambda n : setattr(self, 'siri_require_profanity_filter', n.get_bool_value()),
            "spotlight_block_internet_results": lambda n : setattr(self, 'spotlight_block_internet_results', n.get_bool_value()),
            "voice_dialing_blocked": lambda n : setattr(self, 'voice_dialing_blocked', n.get_bool_value()),
            "wallpaper_block_modification": lambda n : setattr(self, 'wallpaper_block_modification', n.get_bool_value()),
            "wi_fi_connect_only_to_configured_networks": lambda n : setattr(self, 'wi_fi_connect_only_to_configured_networks', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def host_pairing_blocked(self,) -> Optional[bool]:
        """
        Gets the hostPairingBlocked property value. indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._host_pairing_blocked
    
    @host_pairing_blocked.setter
    def host_pairing_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the hostPairingBlocked property value. indicates whether or not to allow host pairing to control the devices an iOS device can pair with when the iOS device is in supervised mode.
        Args:
            value: Value to set for the hostPairingBlocked property.
        """
        self._host_pairing_blocked = value
    
    @property
    def i_books_store_blocked(self,) -> Optional[bool]:
        """
        Gets the iBooksStoreBlocked property value. Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._i_books_store_blocked
    
    @i_books_store_blocked.setter
    def i_books_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the iBooksStoreBlocked property value. Indicates whether or not to block the user from using the iBooks Store when the device is in supervised mode.
        Args:
            value: Value to set for the iBooksStoreBlocked property.
        """
        self._i_books_store_blocked = value
    
    @property
    def i_books_store_block_erotica(self,) -> Optional[bool]:
        """
        Gets the iBooksStoreBlockErotica property value. Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
        Returns: Optional[bool]
        """
        return self._i_books_store_block_erotica
    
    @i_books_store_block_erotica.setter
    def i_books_store_block_erotica(self,value: Optional[bool] = None) -> None:
        """
        Sets the iBooksStoreBlockErotica property value. Indicates whether or not to block the user from downloading media from the iBookstore that has been tagged as erotica.
        Args:
            value: Value to set for the iBooksStoreBlockErotica property.
        """
        self._i_books_store_block_erotica = value
    
    @property
    def i_cloud_block_activity_continuation(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockActivityContinuation property value. Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_activity_continuation
    
    @i_cloud_block_activity_continuation.setter
    def i_cloud_block_activity_continuation(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockActivityContinuation property value. Indicates whether or not to block the user from continuing work they started on iOS device to another iOS or macOS device.
        Args:
            value: Value to set for the iCloudBlockActivityContinuation property.
        """
        self._i_cloud_block_activity_continuation = value
    
    @property
    def i_cloud_block_backup(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockBackup property value. Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_backup
    
    @i_cloud_block_backup.setter
    def i_cloud_block_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockBackup property value. Indicates whether or not to block iCloud backup. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the iCloudBlockBackup property.
        """
        self._i_cloud_block_backup = value
    
    @property
    def i_cloud_block_document_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockDocumentSync property value. Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_document_sync
    
    @i_cloud_block_document_sync.setter
    def i_cloud_block_document_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockDocumentSync property value. Indicates whether or not to block iCloud document sync. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the iCloudBlockDocumentSync property.
        """
        self._i_cloud_block_document_sync = value
    
    @property
    def i_cloud_block_managed_apps_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockManagedAppsSync property value. Indicates whether or not to block Managed Apps Cloud Sync.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_managed_apps_sync
    
    @i_cloud_block_managed_apps_sync.setter
    def i_cloud_block_managed_apps_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockManagedAppsSync property value. Indicates whether or not to block Managed Apps Cloud Sync.
        Args:
            value: Value to set for the iCloudBlockManagedAppsSync property.
        """
        self._i_cloud_block_managed_apps_sync = value
    
    @property
    def i_cloud_block_photo_library(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockPhotoLibrary property value. Indicates whether or not to block iCloud Photo Library.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_photo_library
    
    @i_cloud_block_photo_library.setter
    def i_cloud_block_photo_library(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockPhotoLibrary property value. Indicates whether or not to block iCloud Photo Library.
        Args:
            value: Value to set for the iCloudBlockPhotoLibrary property.
        """
        self._i_cloud_block_photo_library = value
    
    @property
    def i_cloud_block_photo_stream_sync(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockPhotoStreamSync property value. Indicates whether or not to block iCloud Photo Stream Sync.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_photo_stream_sync
    
    @i_cloud_block_photo_stream_sync.setter
    def i_cloud_block_photo_stream_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockPhotoStreamSync property value. Indicates whether or not to block iCloud Photo Stream Sync.
        Args:
            value: Value to set for the iCloudBlockPhotoStreamSync property.
        """
        self._i_cloud_block_photo_stream_sync = value
    
    @property
    def i_cloud_block_shared_photo_stream(self,) -> Optional[bool]:
        """
        Gets the iCloudBlockSharedPhotoStream property value. Indicates whether or not to block Shared Photo Stream.
        Returns: Optional[bool]
        """
        return self._i_cloud_block_shared_photo_stream
    
    @i_cloud_block_shared_photo_stream.setter
    def i_cloud_block_shared_photo_stream(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudBlockSharedPhotoStream property value. Indicates whether or not to block Shared Photo Stream.
        Args:
            value: Value to set for the iCloudBlockSharedPhotoStream property.
        """
        self._i_cloud_block_shared_photo_stream = value
    
    @property
    def i_cloud_require_encrypted_backup(self,) -> Optional[bool]:
        """
        Gets the iCloudRequireEncryptedBackup property value. Indicates whether or not to require backups to iCloud be encrypted.
        Returns: Optional[bool]
        """
        return self._i_cloud_require_encrypted_backup
    
    @i_cloud_require_encrypted_backup.setter
    def i_cloud_require_encrypted_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the iCloudRequireEncryptedBackup property value. Indicates whether or not to require backups to iCloud be encrypted.
        Args:
            value: Value to set for the iCloudRequireEncryptedBackup property.
        """
        self._i_cloud_require_encrypted_backup = value
    
    @property
    def i_tunes_block_explicit_content(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockExplicitContent property value. Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._i_tunes_block_explicit_content
    
    @i_tunes_block_explicit_content.setter
    def i_tunes_block_explicit_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockExplicitContent property value. Indicates whether or not to block the user from accessing explicit content in iTunes and the App Store. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the iTunesBlockExplicitContent property.
        """
        self._i_tunes_block_explicit_content = value
    
    @property
    def i_tunes_block_music_service(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockMusicService property value. Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
        Returns: Optional[bool]
        """
        return self._i_tunes_block_music_service
    
    @i_tunes_block_music_service.setter
    def i_tunes_block_music_service(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockMusicService property value. Indicates whether or not to block Music service and revert Music app to classic mode when the device is in supervised mode (iOS 9.3 and later and macOS 10.12 and later).
        Args:
            value: Value to set for the iTunesBlockMusicService property.
        """
        self._i_tunes_block_music_service = value
    
    @property
    def i_tunes_block_radio(self,) -> Optional[bool]:
        """
        Gets the iTunesBlockRadio property value. Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
        Returns: Optional[bool]
        """
        return self._i_tunes_block_radio
    
    @i_tunes_block_radio.setter
    def i_tunes_block_radio(self,value: Optional[bool] = None) -> None:
        """
        Sets the iTunesBlockRadio property value. Indicates whether or not to block the user from using iTunes Radio when the device is in supervised mode (iOS 9.3 and later).
        Args:
            value: Value to set for the iTunesBlockRadio property.
        """
        self._i_tunes_block_radio = value
    
    @property
    def keyboard_block_auto_correct(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockAutoCorrect property value. Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_auto_correct
    
    @keyboard_block_auto_correct.setter
    def keyboard_block_auto_correct(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockAutoCorrect property value. Indicates whether or not to block keyboard auto-correction when the device is in supervised mode (iOS 8.1.3 and later).
        Args:
            value: Value to set for the keyboardBlockAutoCorrect property.
        """
        self._keyboard_block_auto_correct = value
    
    @property
    def keyboard_block_dictation(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockDictation property value. Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
        Returns: Optional[bool]
        """
        return self._keyboard_block_dictation
    
    @keyboard_block_dictation.setter
    def keyboard_block_dictation(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockDictation property value. Indicates whether or not to block the user from using dictation input when the device is in supervised mode.
        Args:
            value: Value to set for the keyboardBlockDictation property.
        """
        self._keyboard_block_dictation = value
    
    @property
    def keyboard_block_predictive(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockPredictive property value. Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_predictive
    
    @keyboard_block_predictive.setter
    def keyboard_block_predictive(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockPredictive property value. Indicates whether or not to block predictive keyboards when device is in supervised mode (iOS 8.1.3 and later).
        Args:
            value: Value to set for the keyboardBlockPredictive property.
        """
        self._keyboard_block_predictive = value
    
    @property
    def keyboard_block_shortcuts(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockShortcuts property value. Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_shortcuts
    
    @keyboard_block_shortcuts.setter
    def keyboard_block_shortcuts(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockShortcuts property value. Indicates whether or not to block keyboard shortcuts when the device is in supervised mode (iOS 9.0 and later).
        Args:
            value: Value to set for the keyboardBlockShortcuts property.
        """
        self._keyboard_block_shortcuts = value
    
    @property
    def keyboard_block_spell_check(self,) -> Optional[bool]:
        """
        Gets the keyboardBlockSpellCheck property value. Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
        Returns: Optional[bool]
        """
        return self._keyboard_block_spell_check
    
    @keyboard_block_spell_check.setter
    def keyboard_block_spell_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the keyboardBlockSpellCheck property value. Indicates whether or not to block keyboard spell-checking when the device is in supervised mode (iOS 8.1.3 and later).
        Args:
            value: Value to set for the keyboardBlockSpellCheck property.
        """
        self._keyboard_block_spell_check = value
    
    @property
    def kiosk_mode_allow_assistive_speak(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowAssistiveSpeak property value. Indicates whether or not to allow assistive speak while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_assistive_speak
    
    @kiosk_mode_allow_assistive_speak.setter
    def kiosk_mode_allow_assistive_speak(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowAssistiveSpeak property value. Indicates whether or not to allow assistive speak while in kiosk mode.
        Args:
            value: Value to set for the kioskModeAllowAssistiveSpeak property.
        """
        self._kiosk_mode_allow_assistive_speak = value
    
    @property
    def kiosk_mode_allow_assistive_touch_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowAssistiveTouchSettings property value. Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_assistive_touch_settings
    
    @kiosk_mode_allow_assistive_touch_settings.setter
    def kiosk_mode_allow_assistive_touch_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowAssistiveTouchSettings property value. Indicates whether or not to allow access to the Assistive Touch Settings while in kiosk mode.
        Args:
            value: Value to set for the kioskModeAllowAssistiveTouchSettings property.
        """
        self._kiosk_mode_allow_assistive_touch_settings = value
    
    @property
    def kiosk_mode_allow_auto_lock(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowAutoLock property value. Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_auto_lock
    
    @kiosk_mode_allow_auto_lock.setter
    def kiosk_mode_allow_auto_lock(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowAutoLock property value. Indicates whether or not to allow device auto lock while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockAutoLock instead.
        Args:
            value: Value to set for the kioskModeAllowAutoLock property.
        """
        self._kiosk_mode_allow_auto_lock = value
    
    @property
    def kiosk_mode_allow_color_inversion_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowColorInversionSettings property value. Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_color_inversion_settings
    
    @kiosk_mode_allow_color_inversion_settings.setter
    def kiosk_mode_allow_color_inversion_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowColorInversionSettings property value. Indicates whether or not to allow access to the Color Inversion Settings while in kiosk mode.
        Args:
            value: Value to set for the kioskModeAllowColorInversionSettings property.
        """
        self._kiosk_mode_allow_color_inversion_settings = value
    
    @property
    def kiosk_mode_allow_ringer_switch(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowRingerSwitch property value. Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_ringer_switch
    
    @kiosk_mode_allow_ringer_switch.setter
    def kiosk_mode_allow_ringer_switch(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowRingerSwitch property value. Indicates whether or not to allow use of the ringer switch while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockRingerSwitch instead.
        Args:
            value: Value to set for the kioskModeAllowRingerSwitch property.
        """
        self._kiosk_mode_allow_ringer_switch = value
    
    @property
    def kiosk_mode_allow_screen_rotation(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowScreenRotation property value. Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_screen_rotation
    
    @kiosk_mode_allow_screen_rotation.setter
    def kiosk_mode_allow_screen_rotation(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowScreenRotation property value. Indicates whether or not to allow screen rotation while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockScreenRotation instead.
        Args:
            value: Value to set for the kioskModeAllowScreenRotation property.
        """
        self._kiosk_mode_allow_screen_rotation = value
    
    @property
    def kiosk_mode_allow_sleep_button(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowSleepButton property value. Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_sleep_button
    
    @kiosk_mode_allow_sleep_button.setter
    def kiosk_mode_allow_sleep_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowSleepButton property value. Indicates whether or not to allow use of the sleep button while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockSleepButton instead.
        Args:
            value: Value to set for the kioskModeAllowSleepButton property.
        """
        self._kiosk_mode_allow_sleep_button = value
    
    @property
    def kiosk_mode_allow_touchscreen(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowTouchscreen property value. Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_touchscreen
    
    @kiosk_mode_allow_touchscreen.setter
    def kiosk_mode_allow_touchscreen(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowTouchscreen property value. Indicates whether or not to allow use of the touchscreen while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockTouchscreen instead.
        Args:
            value: Value to set for the kioskModeAllowTouchscreen property.
        """
        self._kiosk_mode_allow_touchscreen = value
    
    @property
    def kiosk_mode_allow_voice_over_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowVoiceOverSettings property value. Indicates whether or not to allow access to the voice over settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_voice_over_settings
    
    @kiosk_mode_allow_voice_over_settings.setter
    def kiosk_mode_allow_voice_over_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowVoiceOverSettings property value. Indicates whether or not to allow access to the voice over settings while in kiosk mode.
        Args:
            value: Value to set for the kioskModeAllowVoiceOverSettings property.
        """
        self._kiosk_mode_allow_voice_over_settings = value
    
    @property
    def kiosk_mode_allow_volume_buttons(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowVolumeButtons property value. Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_volume_buttons
    
    @kiosk_mode_allow_volume_buttons.setter
    def kiosk_mode_allow_volume_buttons(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowVolumeButtons property value. Indicates whether or not to allow use of the volume buttons while in kiosk mode. This property's functionality is redundant with the OS default and is deprecated. Use KioskModeBlockVolumeButtons instead.
        Args:
            value: Value to set for the kioskModeAllowVolumeButtons property.
        """
        self._kiosk_mode_allow_volume_buttons = value
    
    @property
    def kiosk_mode_allow_zoom_settings(self,) -> Optional[bool]:
        """
        Gets the kioskModeAllowZoomSettings property value. Indicates whether or not to allow access to the zoom settings while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_allow_zoom_settings
    
    @kiosk_mode_allow_zoom_settings.setter
    def kiosk_mode_allow_zoom_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeAllowZoomSettings property value. Indicates whether or not to allow access to the zoom settings while in kiosk mode.
        Args:
            value: Value to set for the kioskModeAllowZoomSettings property.
        """
        self._kiosk_mode_allow_zoom_settings = value
    
    @property
    def kiosk_mode_app_store_url(self,) -> Optional[str]:
        """
        Gets the kioskModeAppStoreUrl property value. URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
        Returns: Optional[str]
        """
        return self._kiosk_mode_app_store_url
    
    @kiosk_mode_app_store_url.setter
    def kiosk_mode_app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeAppStoreUrl property value. URL in the app store to the app to use for kiosk mode. Use if KioskModeManagedAppId is not known.
        Args:
            value: Value to set for the kioskModeAppStoreUrl property.
        """
        self._kiosk_mode_app_store_url = value
    
    @property
    def kiosk_mode_built_in_app_id(self,) -> Optional[str]:
        """
        Gets the kioskModeBuiltInAppId property value. ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
        Returns: Optional[str]
        """
        return self._kiosk_mode_built_in_app_id
    
    @kiosk_mode_built_in_app_id.setter
    def kiosk_mode_built_in_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeBuiltInAppId property value. ID for built-in apps to use for kiosk mode. Used when KioskModeManagedAppId and KioskModeAppStoreUrl are not set.
        Args:
            value: Value to set for the kioskModeBuiltInAppId property.
        """
        self._kiosk_mode_built_in_app_id = value
    
    @property
    def kiosk_mode_managed_app_id(self,) -> Optional[str]:
        """
        Gets the kioskModeManagedAppId property value. Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
        Returns: Optional[str]
        """
        return self._kiosk_mode_managed_app_id
    
    @kiosk_mode_managed_app_id.setter
    def kiosk_mode_managed_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the kioskModeManagedAppId property value. Managed app id of the app to use for kiosk mode. If KioskModeManagedAppId is specified then KioskModeAppStoreUrl will be ignored.
        Args:
            value: Value to set for the kioskModeManagedAppId property.
        """
        self._kiosk_mode_managed_app_id = value
    
    @property
    def kiosk_mode_require_assistive_touch(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireAssistiveTouch property value. Indicates whether or not to require assistive touch while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_assistive_touch
    
    @kiosk_mode_require_assistive_touch.setter
    def kiosk_mode_require_assistive_touch(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireAssistiveTouch property value. Indicates whether or not to require assistive touch while in kiosk mode.
        Args:
            value: Value to set for the kioskModeRequireAssistiveTouch property.
        """
        self._kiosk_mode_require_assistive_touch = value
    
    @property
    def kiosk_mode_require_color_inversion(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireColorInversion property value. Indicates whether or not to require color inversion while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_color_inversion
    
    @kiosk_mode_require_color_inversion.setter
    def kiosk_mode_require_color_inversion(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireColorInversion property value. Indicates whether or not to require color inversion while in kiosk mode.
        Args:
            value: Value to set for the kioskModeRequireColorInversion property.
        """
        self._kiosk_mode_require_color_inversion = value
    
    @property
    def kiosk_mode_require_mono_audio(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireMonoAudio property value. Indicates whether or not to require mono audio while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_mono_audio
    
    @kiosk_mode_require_mono_audio.setter
    def kiosk_mode_require_mono_audio(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireMonoAudio property value. Indicates whether or not to require mono audio while in kiosk mode.
        Args:
            value: Value to set for the kioskModeRequireMonoAudio property.
        """
        self._kiosk_mode_require_mono_audio = value
    
    @property
    def kiosk_mode_require_voice_over(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireVoiceOver property value. Indicates whether or not to require voice over while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_voice_over
    
    @kiosk_mode_require_voice_over.setter
    def kiosk_mode_require_voice_over(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireVoiceOver property value. Indicates whether or not to require voice over while in kiosk mode.
        Args:
            value: Value to set for the kioskModeRequireVoiceOver property.
        """
        self._kiosk_mode_require_voice_over = value
    
    @property
    def kiosk_mode_require_zoom(self,) -> Optional[bool]:
        """
        Gets the kioskModeRequireZoom property value. Indicates whether or not to require zoom while in kiosk mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_require_zoom
    
    @kiosk_mode_require_zoom.setter
    def kiosk_mode_require_zoom(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeRequireZoom property value. Indicates whether or not to require zoom while in kiosk mode.
        Args:
            value: Value to set for the kioskModeRequireZoom property.
        """
        self._kiosk_mode_require_zoom = value
    
    @property
    def lock_screen_block_control_center(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockControlCenter property value. Indicates whether or not to block the user from using control center on the lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_control_center
    
    @lock_screen_block_control_center.setter
    def lock_screen_block_control_center(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockControlCenter property value. Indicates whether or not to block the user from using control center on the lock screen.
        Args:
            value: Value to set for the lockScreenBlockControlCenter property.
        """
        self._lock_screen_block_control_center = value
    
    @property
    def lock_screen_block_notification_view(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockNotificationView property value. Indicates whether or not to block the user from using the notification view on the lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_notification_view
    
    @lock_screen_block_notification_view.setter
    def lock_screen_block_notification_view(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockNotificationView property value. Indicates whether or not to block the user from using the notification view on the lock screen.
        Args:
            value: Value to set for the lockScreenBlockNotificationView property.
        """
        self._lock_screen_block_notification_view = value
    
    @property
    def lock_screen_block_passbook(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockPassbook property value. Indicates whether or not to block the user from using passbook when the device is locked.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_passbook
    
    @lock_screen_block_passbook.setter
    def lock_screen_block_passbook(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockPassbook property value. Indicates whether or not to block the user from using passbook when the device is locked.
        Args:
            value: Value to set for the lockScreenBlockPassbook property.
        """
        self._lock_screen_block_passbook = value
    
    @property
    def lock_screen_block_today_view(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockTodayView property value. Indicates whether or not to block the user from using the Today View on the lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_today_view
    
    @lock_screen_block_today_view.setter
    def lock_screen_block_today_view(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockTodayView property value. Indicates whether or not to block the user from using the Today View on the lock screen.
        Args:
            value: Value to set for the lockScreenBlockTodayView property.
        """
        self._lock_screen_block_today_view = value
    
    @property
    def media_content_rating_apps(self,) -> Optional[rating_apps_type.RatingAppsType]:
        """
        Gets the mediaContentRatingApps property value. Apps rating as in media content
        Returns: Optional[rating_apps_type.RatingAppsType]
        """
        return self._media_content_rating_apps
    
    @media_content_rating_apps.setter
    def media_content_rating_apps(self,value: Optional[rating_apps_type.RatingAppsType] = None) -> None:
        """
        Sets the mediaContentRatingApps property value. Apps rating as in media content
        Args:
            value: Value to set for the mediaContentRatingApps property.
        """
        self._media_content_rating_apps = value
    
    @property
    def media_content_rating_australia(self,) -> Optional[media_content_rating_australia.MediaContentRatingAustralia]:
        """
        Gets the mediaContentRatingAustralia property value. Media content rating settings for Australia
        Returns: Optional[media_content_rating_australia.MediaContentRatingAustralia]
        """
        return self._media_content_rating_australia
    
    @media_content_rating_australia.setter
    def media_content_rating_australia(self,value: Optional[media_content_rating_australia.MediaContentRatingAustralia] = None) -> None:
        """
        Sets the mediaContentRatingAustralia property value. Media content rating settings for Australia
        Args:
            value: Value to set for the mediaContentRatingAustralia property.
        """
        self._media_content_rating_australia = value
    
    @property
    def media_content_rating_canada(self,) -> Optional[media_content_rating_canada.MediaContentRatingCanada]:
        """
        Gets the mediaContentRatingCanada property value. Media content rating settings for Canada
        Returns: Optional[media_content_rating_canada.MediaContentRatingCanada]
        """
        return self._media_content_rating_canada
    
    @media_content_rating_canada.setter
    def media_content_rating_canada(self,value: Optional[media_content_rating_canada.MediaContentRatingCanada] = None) -> None:
        """
        Sets the mediaContentRatingCanada property value. Media content rating settings for Canada
        Args:
            value: Value to set for the mediaContentRatingCanada property.
        """
        self._media_content_rating_canada = value
    
    @property
    def media_content_rating_france(self,) -> Optional[media_content_rating_france.MediaContentRatingFrance]:
        """
        Gets the mediaContentRatingFrance property value. Media content rating settings for France
        Returns: Optional[media_content_rating_france.MediaContentRatingFrance]
        """
        return self._media_content_rating_france
    
    @media_content_rating_france.setter
    def media_content_rating_france(self,value: Optional[media_content_rating_france.MediaContentRatingFrance] = None) -> None:
        """
        Sets the mediaContentRatingFrance property value. Media content rating settings for France
        Args:
            value: Value to set for the mediaContentRatingFrance property.
        """
        self._media_content_rating_france = value
    
    @property
    def media_content_rating_germany(self,) -> Optional[media_content_rating_germany.MediaContentRatingGermany]:
        """
        Gets the mediaContentRatingGermany property value. Media content rating settings for Germany
        Returns: Optional[media_content_rating_germany.MediaContentRatingGermany]
        """
        return self._media_content_rating_germany
    
    @media_content_rating_germany.setter
    def media_content_rating_germany(self,value: Optional[media_content_rating_germany.MediaContentRatingGermany] = None) -> None:
        """
        Sets the mediaContentRatingGermany property value. Media content rating settings for Germany
        Args:
            value: Value to set for the mediaContentRatingGermany property.
        """
        self._media_content_rating_germany = value
    
    @property
    def media_content_rating_ireland(self,) -> Optional[media_content_rating_ireland.MediaContentRatingIreland]:
        """
        Gets the mediaContentRatingIreland property value. Media content rating settings for Ireland
        Returns: Optional[media_content_rating_ireland.MediaContentRatingIreland]
        """
        return self._media_content_rating_ireland
    
    @media_content_rating_ireland.setter
    def media_content_rating_ireland(self,value: Optional[media_content_rating_ireland.MediaContentRatingIreland] = None) -> None:
        """
        Sets the mediaContentRatingIreland property value. Media content rating settings for Ireland
        Args:
            value: Value to set for the mediaContentRatingIreland property.
        """
        self._media_content_rating_ireland = value
    
    @property
    def media_content_rating_japan(self,) -> Optional[media_content_rating_japan.MediaContentRatingJapan]:
        """
        Gets the mediaContentRatingJapan property value. Media content rating settings for Japan
        Returns: Optional[media_content_rating_japan.MediaContentRatingJapan]
        """
        return self._media_content_rating_japan
    
    @media_content_rating_japan.setter
    def media_content_rating_japan(self,value: Optional[media_content_rating_japan.MediaContentRatingJapan] = None) -> None:
        """
        Sets the mediaContentRatingJapan property value. Media content rating settings for Japan
        Args:
            value: Value to set for the mediaContentRatingJapan property.
        """
        self._media_content_rating_japan = value
    
    @property
    def media_content_rating_new_zealand(self,) -> Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand]:
        """
        Gets the mediaContentRatingNewZealand property value. Media content rating settings for New Zealand
        Returns: Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand]
        """
        return self._media_content_rating_new_zealand
    
    @media_content_rating_new_zealand.setter
    def media_content_rating_new_zealand(self,value: Optional[media_content_rating_new_zealand.MediaContentRatingNewZealand] = None) -> None:
        """
        Sets the mediaContentRatingNewZealand property value. Media content rating settings for New Zealand
        Args:
            value: Value to set for the mediaContentRatingNewZealand property.
        """
        self._media_content_rating_new_zealand = value
    
    @property
    def media_content_rating_united_kingdom(self,) -> Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom]:
        """
        Gets the mediaContentRatingUnitedKingdom property value. Media content rating settings for United Kingdom
        Returns: Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom]
        """
        return self._media_content_rating_united_kingdom
    
    @media_content_rating_united_kingdom.setter
    def media_content_rating_united_kingdom(self,value: Optional[media_content_rating_united_kingdom.MediaContentRatingUnitedKingdom] = None) -> None:
        """
        Sets the mediaContentRatingUnitedKingdom property value. Media content rating settings for United Kingdom
        Args:
            value: Value to set for the mediaContentRatingUnitedKingdom property.
        """
        self._media_content_rating_united_kingdom = value
    
    @property
    def media_content_rating_united_states(self,) -> Optional[media_content_rating_united_states.MediaContentRatingUnitedStates]:
        """
        Gets the mediaContentRatingUnitedStates property value. Media content rating settings for United States
        Returns: Optional[media_content_rating_united_states.MediaContentRatingUnitedStates]
        """
        return self._media_content_rating_united_states
    
    @media_content_rating_united_states.setter
    def media_content_rating_united_states(self,value: Optional[media_content_rating_united_states.MediaContentRatingUnitedStates] = None) -> None:
        """
        Sets the mediaContentRatingUnitedStates property value. Media content rating settings for United States
        Args:
            value: Value to set for the mediaContentRatingUnitedStates property.
        """
        self._media_content_rating_united_states = value
    
    @property
    def messages_blocked(self,) -> Optional[bool]:
        """
        Gets the messagesBlocked property value. Indicates whether or not to block the user from using the Messages app on the supervised device.
        Returns: Optional[bool]
        """
        return self._messages_blocked
    
    @messages_blocked.setter
    def messages_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the messagesBlocked property value. Indicates whether or not to block the user from using the Messages app on the supervised device.
        Args:
            value: Value to set for the messagesBlocked property.
        """
        self._messages_blocked = value
    
    @property
    def network_usage_rules(self,) -> Optional[List[ios_network_usage_rule.IosNetworkUsageRule]]:
        """
        Gets the networkUsageRules property value. List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[ios_network_usage_rule.IosNetworkUsageRule]]
        """
        return self._network_usage_rules
    
    @network_usage_rules.setter
    def network_usage_rules(self,value: Optional[List[ios_network_usage_rule.IosNetworkUsageRule]] = None) -> None:
        """
        Sets the networkUsageRules property value. List of managed apps and the network rules that applies to them. This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the networkUsageRules property.
        """
        self._network_usage_rules = value
    
    @property
    def notifications_block_settings_modification(self,) -> Optional[bool]:
        """
        Gets the notificationsBlockSettingsModification property value. Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
        Returns: Optional[bool]
        """
        return self._notifications_block_settings_modification
    
    @notifications_block_settings_modification.setter
    def notifications_block_settings_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the notificationsBlockSettingsModification property value. Indicates whether or not to allow notifications settings modification (iOS 9.3 and later).
        Args:
            value: Value to set for the notificationsBlockSettingsModification property.
        """
        self._notifications_block_settings_modification = value
    
    @property
    def passcode_block_fingerprint_modification(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockFingerprintModification property value. Block modification of registered Touch ID fingerprints when in supervised mode.
        Returns: Optional[bool]
        """
        return self._passcode_block_fingerprint_modification
    
    @passcode_block_fingerprint_modification.setter
    def passcode_block_fingerprint_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockFingerprintModification property value. Block modification of registered Touch ID fingerprints when in supervised mode.
        Args:
            value: Value to set for the passcodeBlockFingerprintModification property.
        """
        self._passcode_block_fingerprint_modification = value
    
    @property
    def passcode_block_fingerprint_unlock(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Returns: Optional[bool]
        """
        return self._passcode_block_fingerprint_unlock
    
    @passcode_block_fingerprint_unlock.setter
    def passcode_block_fingerprint_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Args:
            value: Value to set for the passcodeBlockFingerprintUnlock property.
        """
        self._passcode_block_fingerprint_unlock = value
    
    @property
    def passcode_block_modification(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockModification property value. Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
        Returns: Optional[bool]
        """
        return self._passcode_block_modification
    
    @passcode_block_modification.setter
    def passcode_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockModification property value. Indicates whether or not to allow passcode modification on the supervised device (iOS 9.0 and later).
        Args:
            value: Value to set for the passcodeBlockModification property.
        """
        self._passcode_block_modification = value
    
    @property
    def passcode_block_simple(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockSimple property value. Indicates whether or not to block simple passcodes.
        Returns: Optional[bool]
        """
        return self._passcode_block_simple
    
    @passcode_block_simple.setter
    def passcode_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockSimple property value. Indicates whether or not to block simple passcodes.
        Args:
            value: Value to set for the passcodeBlockSimple property.
        """
        self._passcode_block_simple = value
    
    @property
    def passcode_expiration_days(self,) -> Optional[int]:
        """
        Gets the passcodeExpirationDays property value. Number of days before the passcode expires. Valid values 1 to 65535
        Returns: Optional[int]
        """
        return self._passcode_expiration_days
    
    @passcode_expiration_days.setter
    def passcode_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeExpirationDays property value. Number of days before the passcode expires. Valid values 1 to 65535
        Args:
            value: Value to set for the passcodeExpirationDays property.
        """
        self._passcode_expiration_days = value
    
    @property
    def passcode_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passcodeMinimumCharacterSetCount property value. Number of character sets a passcode must contain. Valid values 0 to 4
        Returns: Optional[int]
        """
        return self._passcode_minimum_character_set_count
    
    @passcode_minimum_character_set_count.setter
    def passcode_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinimumCharacterSetCount property value. Number of character sets a passcode must contain. Valid values 0 to 4
        Args:
            value: Value to set for the passcodeMinimumCharacterSetCount property.
        """
        self._passcode_minimum_character_set_count = value
    
    @property
    def passcode_minimum_length(self,) -> Optional[int]:
        """
        Gets the passcodeMinimumLength property value. Minimum length of passcode. Valid values 4 to 14
        Returns: Optional[int]
        """
        return self._passcode_minimum_length
    
    @passcode_minimum_length.setter
    def passcode_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinimumLength property value. Minimum length of passcode. Valid values 4 to 14
        Args:
            value: Value to set for the passcodeMinimumLength property.
        """
        self._passcode_minimum_length = value
    
    @property
    def passcode_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passcodeMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a passcode is required.
        Returns: Optional[int]
        """
        return self._passcode_minutes_of_inactivity_before_lock
    
    @passcode_minutes_of_inactivity_before_lock.setter
    def passcode_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a passcode is required.
        Args:
            value: Value to set for the passcodeMinutesOfInactivityBeforeLock property.
        """
        self._passcode_minutes_of_inactivity_before_lock = value
    
    @property
    def passcode_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passcodeMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._passcode_minutes_of_inactivity_before_screen_timeout
    
    @passcode_minutes_of_inactivity_before_screen_timeout.setter
    def passcode_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the passcodeMinutesOfInactivityBeforeScreenTimeout property.
        """
        self._passcode_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def passcode_previous_passcode_block_count(self,) -> Optional[int]:
        """
        Gets the passcodePreviousPasscodeBlockCount property value. Number of previous passcodes to block. Valid values 1 to 24
        Returns: Optional[int]
        """
        return self._passcode_previous_passcode_block_count
    
    @passcode_previous_passcode_block_count.setter
    def passcode_previous_passcode_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodePreviousPasscodeBlockCount property value. Number of previous passcodes to block. Valid values 1 to 24
        Args:
            value: Value to set for the passcodePreviousPasscodeBlockCount property.
        """
        self._passcode_previous_passcode_block_count = value
    
    @property
    def passcode_required(self,) -> Optional[bool]:
        """
        Gets the passcodeRequired property value. Indicates whether or not to require a passcode.
        Returns: Optional[bool]
        """
        return self._passcode_required
    
    @passcode_required.setter
    def passcode_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeRequired property value. Indicates whether or not to require a passcode.
        Args:
            value: Value to set for the passcodeRequired property.
        """
        self._passcode_required = value
    
    @property
    def passcode_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passcodeRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._passcode_required_type
    
    @passcode_required_type.setter
    def passcode_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passcodeRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the passcodeRequiredType property.
        """
        self._passcode_required_type = value
    
    @property
    def passcode_sign_in_failure_count_before_wipe(self,) -> Optional[int]:
        """
        Gets the passcodeSignInFailureCountBeforeWipe property value. Number of sign in failures allowed before wiping the device. Valid values 2 to 11
        Returns: Optional[int]
        """
        return self._passcode_sign_in_failure_count_before_wipe
    
    @passcode_sign_in_failure_count_before_wipe.setter
    def passcode_sign_in_failure_count_before_wipe(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeSignInFailureCountBeforeWipe property value. Number of sign in failures allowed before wiping the device. Valid values 2 to 11
        Args:
            value: Value to set for the passcodeSignInFailureCountBeforeWipe property.
        """
        self._passcode_sign_in_failure_count_before_wipe = value
    
    @property
    def podcasts_blocked(self,) -> Optional[bool]:
        """
        Gets the podcastsBlocked property value. Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
        Returns: Optional[bool]
        """
        return self._podcasts_blocked
    
    @podcasts_blocked.setter
    def podcasts_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the podcastsBlocked property value. Indicates whether or not to block the user from using podcasts on the supervised device (iOS 8.0 and later).
        Args:
            value: Value to set for the podcastsBlocked property.
        """
        self._podcasts_blocked = value
    
    @property
    def safari_block_autofill(self,) -> Optional[bool]:
        """
        Gets the safariBlockAutofill property value. Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._safari_block_autofill
    
    @safari_block_autofill.setter
    def safari_block_autofill(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockAutofill property value. Indicates whether or not to block the user from using Auto fill in Safari. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the safariBlockAutofill property.
        """
        self._safari_block_autofill = value
    
    @property
    def safari_blocked(self,) -> Optional[bool]:
        """
        Gets the safariBlocked property value. Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
        Returns: Optional[bool]
        """
        return self._safari_blocked
    
    @safari_blocked.setter
    def safari_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlocked property value. Indicates whether or not to block the user from using Safari. Requires a supervised device for iOS 13 and later.
        Args:
            value: Value to set for the safariBlocked property.
        """
        self._safari_blocked = value
    
    @property
    def safari_block_java_script(self,) -> Optional[bool]:
        """
        Gets the safariBlockJavaScript property value. Indicates whether or not to block JavaScript in Safari.
        Returns: Optional[bool]
        """
        return self._safari_block_java_script
    
    @safari_block_java_script.setter
    def safari_block_java_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockJavaScript property value. Indicates whether or not to block JavaScript in Safari.
        Args:
            value: Value to set for the safariBlockJavaScript property.
        """
        self._safari_block_java_script = value
    
    @property
    def safari_block_popups(self,) -> Optional[bool]:
        """
        Gets the safariBlockPopups property value. Indicates whether or not to block popups in Safari.
        Returns: Optional[bool]
        """
        return self._safari_block_popups
    
    @safari_block_popups.setter
    def safari_block_popups(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariBlockPopups property value. Indicates whether or not to block popups in Safari.
        Args:
            value: Value to set for the safariBlockPopups property.
        """
        self._safari_block_popups = value
    
    @property
    def safari_cookie_settings(self,) -> Optional[web_browser_cookie_settings.WebBrowserCookieSettings]:
        """
        Gets the safariCookieSettings property value. Web Browser Cookie Settings.
        Returns: Optional[web_browser_cookie_settings.WebBrowserCookieSettings]
        """
        return self._safari_cookie_settings
    
    @safari_cookie_settings.setter
    def safari_cookie_settings(self,value: Optional[web_browser_cookie_settings.WebBrowserCookieSettings] = None) -> None:
        """
        Sets the safariCookieSettings property value. Web Browser Cookie Settings.
        Args:
            value: Value to set for the safariCookieSettings property.
        """
        self._safari_cookie_settings = value
    
    @property
    def safari_managed_domains(self,) -> Optional[List[str]]:
        """
        Gets the safariManagedDomains property value. URLs matching the patterns listed here will be considered managed.
        Returns: Optional[List[str]]
        """
        return self._safari_managed_domains
    
    @safari_managed_domains.setter
    def safari_managed_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the safariManagedDomains property value. URLs matching the patterns listed here will be considered managed.
        Args:
            value: Value to set for the safariManagedDomains property.
        """
        self._safari_managed_domains = value
    
    @property
    def safari_password_auto_fill_domains(self,) -> Optional[List[str]]:
        """
        Gets the safariPasswordAutoFillDomains property value. Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
        Returns: Optional[List[str]]
        """
        return self._safari_password_auto_fill_domains
    
    @safari_password_auto_fill_domains.setter
    def safari_password_auto_fill_domains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the safariPasswordAutoFillDomains property value. Users can save passwords in Safari only from URLs matching the patterns listed here. Applies to devices in supervised mode (iOS 9.3 and later).
        Args:
            value: Value to set for the safariPasswordAutoFillDomains property.
        """
        self._safari_password_auto_fill_domains = value
    
    @property
    def safari_require_fraud_warning(self,) -> Optional[bool]:
        """
        Gets the safariRequireFraudWarning property value. Indicates whether or not to require fraud warning in Safari.
        Returns: Optional[bool]
        """
        return self._safari_require_fraud_warning
    
    @safari_require_fraud_warning.setter
    def safari_require_fraud_warning(self,value: Optional[bool] = None) -> None:
        """
        Sets the safariRequireFraudWarning property value. Indicates whether or not to require fraud warning in Safari.
        Args:
            value: Value to set for the safariRequireFraudWarning property.
        """
        self._safari_require_fraud_warning = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether or not to block the user from taking Screenshots.
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether or not to block the user from taking Screenshots.
        Args:
            value: Value to set for the screenCaptureBlocked property.
        """
        self._screen_capture_blocked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountBlockModification", self.account_block_modification)
        writer.write_bool_value("activationLockAllowWhenSupervised", self.activation_lock_allow_when_supervised)
        writer.write_bool_value("airDropBlocked", self.air_drop_blocked)
        writer.write_bool_value("airDropForceUnmanagedDropTarget", self.air_drop_force_unmanaged_drop_target)
        writer.write_bool_value("airPlayForcePairingPasswordForOutgoingRequests", self.air_play_force_pairing_password_for_outgoing_requests)
        writer.write_bool_value("appleNewsBlocked", self.apple_news_blocked)
        writer.write_bool_value("appleWatchBlockPairing", self.apple_watch_block_pairing)
        writer.write_bool_value("appleWatchForceWristDetection", self.apple_watch_force_wrist_detection)
        writer.write_collection_of_object_values("appsSingleAppModeList", self.apps_single_app_mode_list)
        writer.write_bool_value("appStoreBlockAutomaticDownloads", self.app_store_block_automatic_downloads)
        writer.write_bool_value("appStoreBlocked", self.app_store_blocked)
        writer.write_bool_value("appStoreBlockInAppPurchases", self.app_store_block_in_app_purchases)
        writer.write_bool_value("appStoreBlockUIAppInstallation", self.app_store_block_u_i_app_installation)
        writer.write_bool_value("appStoreRequirePassword", self.app_store_require_password)
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
        writer.write_bool_value("iBooksStoreBlocked", self.i_books_store_blocked)
        writer.write_bool_value("iBooksStoreBlockErotica", self.i_books_store_block_erotica)
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
        writer.write_bool_value("safariBlocked", self.safari_blocked)
        writer.write_bool_value("safariBlockJavaScript", self.safari_block_java_script)
        writer.write_bool_value("safariBlockPopups", self.safari_block_popups)
        writer.write_enum_value("safariCookieSettings", self.safari_cookie_settings)
        writer.write_collection_of_primitive_values("safariManagedDomains", self.safari_managed_domains)
        writer.write_collection_of_primitive_values("safariPasswordAutoFillDomains", self.safari_password_auto_fill_domains)
        writer.write_bool_value("safariRequireFraudWarning", self.safari_require_fraud_warning)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("siriBlocked", self.siri_blocked)
        writer.write_bool_value("siriBlockedWhenLocked", self.siri_blocked_when_locked)
        writer.write_bool_value("siriBlockUserGeneratedContent", self.siri_block_user_generated_content)
        writer.write_bool_value("siriRequireProfanityFilter", self.siri_require_profanity_filter)
        writer.write_bool_value("spotlightBlockInternetResults", self.spotlight_block_internet_results)
        writer.write_bool_value("voiceDialingBlocked", self.voice_dialing_blocked)
        writer.write_bool_value("wallpaperBlockModification", self.wallpaper_block_modification)
        writer.write_bool_value("wiFiConnectOnlyToConfiguredNetworks", self.wi_fi_connect_only_to_configured_networks)
    
    @property
    def siri_blocked(self,) -> Optional[bool]:
        """
        Gets the siriBlocked property value. Indicates whether or not to block the user from using Siri.
        Returns: Optional[bool]
        """
        return self._siri_blocked
    
    @siri_blocked.setter
    def siri_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriBlocked property value. Indicates whether or not to block the user from using Siri.
        Args:
            value: Value to set for the siriBlocked property.
        """
        self._siri_blocked = value
    
    @property
    def siri_blocked_when_locked(self,) -> Optional[bool]:
        """
        Gets the siriBlockedWhenLocked property value. Indicates whether or not to block the user from using Siri when locked.
        Returns: Optional[bool]
        """
        return self._siri_blocked_when_locked
    
    @siri_blocked_when_locked.setter
    def siri_blocked_when_locked(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriBlockedWhenLocked property value. Indicates whether or not to block the user from using Siri when locked.
        Args:
            value: Value to set for the siriBlockedWhenLocked property.
        """
        self._siri_blocked_when_locked = value
    
    @property
    def siri_block_user_generated_content(self,) -> Optional[bool]:
        """
        Gets the siriBlockUserGeneratedContent property value. Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
        Returns: Optional[bool]
        """
        return self._siri_block_user_generated_content
    
    @siri_block_user_generated_content.setter
    def siri_block_user_generated_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriBlockUserGeneratedContent property value. Indicates whether or not to block Siri from querying user-generated content when used on a supervised device.
        Args:
            value: Value to set for the siriBlockUserGeneratedContent property.
        """
        self._siri_block_user_generated_content = value
    
    @property
    def siri_require_profanity_filter(self,) -> Optional[bool]:
        """
        Gets the siriRequireProfanityFilter property value. Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
        Returns: Optional[bool]
        """
        return self._siri_require_profanity_filter
    
    @siri_require_profanity_filter.setter
    def siri_require_profanity_filter(self,value: Optional[bool] = None) -> None:
        """
        Sets the siriRequireProfanityFilter property value. Indicates whether or not to prevent Siri from dictating, or speaking profane language on supervised device.
        Args:
            value: Value to set for the siriRequireProfanityFilter property.
        """
        self._siri_require_profanity_filter = value
    
    @property
    def spotlight_block_internet_results(self,) -> Optional[bool]:
        """
        Gets the spotlightBlockInternetResults property value. Indicates whether or not to block Spotlight search from returning internet results on supervised device.
        Returns: Optional[bool]
        """
        return self._spotlight_block_internet_results
    
    @spotlight_block_internet_results.setter
    def spotlight_block_internet_results(self,value: Optional[bool] = None) -> None:
        """
        Sets the spotlightBlockInternetResults property value. Indicates whether or not to block Spotlight search from returning internet results on supervised device.
        Args:
            value: Value to set for the spotlightBlockInternetResults property.
        """
        self._spotlight_block_internet_results = value
    
    @property
    def voice_dialing_blocked(self,) -> Optional[bool]:
        """
        Gets the voiceDialingBlocked property value. Indicates whether or not to block voice dialing.
        Returns: Optional[bool]
        """
        return self._voice_dialing_blocked
    
    @voice_dialing_blocked.setter
    def voice_dialing_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the voiceDialingBlocked property value. Indicates whether or not to block voice dialing.
        Args:
            value: Value to set for the voiceDialingBlocked property.
        """
        self._voice_dialing_blocked = value
    
    @property
    def wallpaper_block_modification(self,) -> Optional[bool]:
        """
        Gets the wallpaperBlockModification property value. Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
        Returns: Optional[bool]
        """
        return self._wallpaper_block_modification
    
    @wallpaper_block_modification.setter
    def wallpaper_block_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the wallpaperBlockModification property value. Indicates whether or not to allow wallpaper modification on supervised device (iOS 9.0 and later) .
        Args:
            value: Value to set for the wallpaperBlockModification property.
        """
        self._wallpaper_block_modification = value
    
    @property
    def wi_fi_connect_only_to_configured_networks(self,) -> Optional[bool]:
        """
        Gets the wiFiConnectOnlyToConfiguredNetworks property value. Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
        Returns: Optional[bool]
        """
        return self._wi_fi_connect_only_to_configured_networks
    
    @wi_fi_connect_only_to_configured_networks.setter
    def wi_fi_connect_only_to_configured_networks(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiConnectOnlyToConfiguredNetworks property value. Indicates whether or not to force the device to use only Wi-Fi networks from configuration profiles when the device is in supervised mode. Available for devices running iOS and iPadOS versions 14.4 and earlier. Devices running 14.5+ should use the setting, 'WiFiConnectToAllowedNetworksOnlyForced.
        Args:
            value: Value to set for the wiFiConnectOnlyToConfiguredNetworks property.
        """
        self._wi_fi_connect_only_to_configured_networks = value
    

