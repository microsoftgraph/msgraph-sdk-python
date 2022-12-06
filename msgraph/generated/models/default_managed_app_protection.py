from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
managed_app_data_encryption_type = lazy_import('msgraph.generated.models.managed_app_data_encryption_type')
managed_app_policy_deployment_summary = lazy_import('msgraph.generated.models.managed_app_policy_deployment_summary')
managed_app_protection = lazy_import('msgraph.generated.models.managed_app_protection')
managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')

class DefaultManagedAppProtection(managed_app_protection.ManagedAppProtection):
    @property
    def app_data_encryption_type(self,) -> Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType]:
        """
        Gets the appDataEncryptionType property value. Represents the level to which app data is encrypted for managed apps
        Returns: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType]
        """
        return self._app_data_encryption_type
    
    @app_data_encryption_type.setter
    def app_data_encryption_type(self,value: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType] = None) -> None:
        """
        Sets the appDataEncryptionType property value. Represents the level to which app data is encrypted for managed apps
        Args:
            value: Value to set for the appDataEncryptionType property.
        """
        self._app_data_encryption_type = value
    
    @property
    def apps(self,) -> Optional[List[managed_mobile_app.ManagedMobileApp]]:
        """
        Gets the apps property value. List of apps to which the policy is deployed.
        Returns: Optional[List[managed_mobile_app.ManagedMobileApp]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[managed_mobile_app.ManagedMobileApp]] = None) -> None:
        """
        Sets the apps property value. List of apps to which the policy is deployed.
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DefaultManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.defaultManagedAppProtection"
        # Represents the level to which app data is encrypted for managed apps
        self._app_data_encryption_type: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType] = None
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # A set of string key and string value pairs to be sent to the affected users, unalterned by this service
        self._custom_settings: Optional[List[key_value_pair.KeyValuePair]] = None
        # Count of apps to which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # Navigation property to deployment summary of the configuration.
        self._deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
        # When this setting is enabled, app level encryption is disabled if device level encryption is enabled. (Android only)
        self._disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
        # Indicates whether managed-app data should be encrypted. (Android only)
        self._encrypt_app_data: Optional[bool] = None
        # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True. (iOS Only)
        self._face_id_blocked: Optional[bool] = None
        # Define the oldest required Android security patch level a user can have to gain secure access to the app. (Android only)
        self._minimum_required_patch_version: Optional[str] = None
        # Versions less than the specified version will block the managed app from accessing company data. (iOS Only)
        self._minimum_required_sdk_version: Optional[str] = None
        # Define the oldest recommended Android security patch level a user can have for secure access to the app. (Android only)
        self._minimum_warning_patch_version: Optional[str] = None
        # Indicates whether screen capture is blocked. (Android only)
        self._screen_capture_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DefaultManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DefaultManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DefaultManagedAppProtection()
    
    @property
    def custom_settings(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the customSettings property value. A set of string key and string value pairs to be sent to the affected users, unalterned by this service
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._custom_settings
    
    @custom_settings.setter
    def custom_settings(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the customSettings property value. A set of string key and string value pairs to be sent to the affected users, unalterned by this service
        Args:
            value: Value to set for the customSettings property.
        """
        self._custom_settings = value
    
    @property
    def deployed_app_count(self,) -> Optional[int]:
        """
        Gets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Returns: Optional[int]
        """
        return self._deployed_app_count
    
    @deployed_app_count.setter
    def deployed_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Args:
            value: Value to set for the deployedAppCount property.
        """
        self._deployed_app_count = value
    
    @property
    def deployment_summary(self,) -> Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]:
        """
        Gets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Returns: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]
        """
        return self._deployment_summary
    
    @deployment_summary.setter
    def deployment_summary(self,value: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None) -> None:
        """
        Sets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Args:
            value: Value to set for the deploymentSummary property.
        """
        self._deployment_summary = value
    
    @property
    def disable_app_encryption_if_device_encryption_is_enabled(self,) -> Optional[bool]:
        """
        Gets the disableAppEncryptionIfDeviceEncryptionIsEnabled property value. When this setting is enabled, app level encryption is disabled if device level encryption is enabled. (Android only)
        Returns: Optional[bool]
        """
        return self._disable_app_encryption_if_device_encryption_is_enabled
    
    @disable_app_encryption_if_device_encryption_is_enabled.setter
    def disable_app_encryption_if_device_encryption_is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableAppEncryptionIfDeviceEncryptionIsEnabled property value. When this setting is enabled, app level encryption is disabled if device level encryption is enabled. (Android only)
        Args:
            value: Value to set for the disableAppEncryptionIfDeviceEncryptionIsEnabled property.
        """
        self._disable_app_encryption_if_device_encryption_is_enabled = value
    
    @property
    def encrypt_app_data(self,) -> Optional[bool]:
        """
        Gets the encryptAppData property value. Indicates whether managed-app data should be encrypted. (Android only)
        Returns: Optional[bool]
        """
        return self._encrypt_app_data
    
    @encrypt_app_data.setter
    def encrypt_app_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the encryptAppData property value. Indicates whether managed-app data should be encrypted. (Android only)
        Args:
            value: Value to set for the encryptAppData property.
        """
        self._encrypt_app_data = value
    
    @property
    def face_id_blocked(self,) -> Optional[bool]:
        """
        Gets the faceIdBlocked property value. Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True. (iOS Only)
        Returns: Optional[bool]
        """
        return self._face_id_blocked
    
    @face_id_blocked.setter
    def face_id_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the faceIdBlocked property value. Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True. (iOS Only)
        Args:
            value: Value to set for the faceIdBlocked property.
        """
        self._face_id_blocked = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_data_encryption_type": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(managed_app_data_encryption_type.ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "custom_settings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "disable_app_encryption_if_device_encryption_is_enabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "encrypt_app_data": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "face_id_blocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "minimum_required_patch_version": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimum_required_sdk_version": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimum_warning_patch_version": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_required_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredPatchVersion property value. Define the oldest required Android security patch level a user can have to gain secure access to the app. (Android only)
        Returns: Optional[str]
        """
        return self._minimum_required_patch_version
    
    @minimum_required_patch_version.setter
    def minimum_required_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredPatchVersion property value. Define the oldest required Android security patch level a user can have to gain secure access to the app. (Android only)
        Args:
            value: Value to set for the minimumRequiredPatchVersion property.
        """
        self._minimum_required_patch_version = value
    
    @property
    def minimum_required_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data. (iOS Only)
        Returns: Optional[str]
        """
        return self._minimum_required_sdk_version
    
    @minimum_required_sdk_version.setter
    def minimum_required_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data. (iOS Only)
        Args:
            value: Value to set for the minimumRequiredSdkVersion property.
        """
        self._minimum_required_sdk_version = value
    
    @property
    def minimum_warning_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningPatchVersion property value. Define the oldest recommended Android security patch level a user can have for secure access to the app. (Android only)
        Returns: Optional[str]
        """
        return self._minimum_warning_patch_version
    
    @minimum_warning_patch_version.setter
    def minimum_warning_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningPatchVersion property value. Define the oldest recommended Android security patch level a user can have for secure access to the app. (Android only)
        Args:
            value: Value to set for the minimumWarningPatchVersion property.
        """
        self._minimum_warning_patch_version = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether screen capture is blocked. (Android only)
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether screen capture is blocked. (Android only)
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
        writer.write_enum_value("appDataEncryptionType", self.app_data_encryption_type)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_collection_of_object_values("customSettings", self.custom_settings)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("disableAppEncryptionIfDeviceEncryptionIsEnabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("encryptAppData", self.encrypt_app_data)
        writer.write_bool_value("faceIdBlocked", self.face_id_blocked)
        writer.write_str_value("minimumRequiredPatchVersion", self.minimum_required_patch_version)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
        writer.write_str_value("minimumWarningPatchVersion", self.minimum_warning_patch_version)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
    

