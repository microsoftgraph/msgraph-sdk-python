from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_app_policy_deployment_summary = lazy_import('msgraph.generated.models.managed_app_policy_deployment_summary')
managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')
targeted_managed_app_protection = lazy_import('msgraph.generated.models.targeted_managed_app_protection')

class AndroidManagedAppProtection(targeted_managed_app_protection.TargetedManagedAppProtection):
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
        Instantiates a new AndroidManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidManagedAppProtection"
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # Friendly name of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        self._custom_browser_display_name: Optional[str] = None
        # Unique identifier of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        self._custom_browser_package_id: Optional[str] = None
        # Count of apps to which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # Navigation property to deployment summary of the configuration.
        self._deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
        # When this setting is enabled, app level encryption is disabled if device level encryption is enabled
        self._disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
        # Indicates whether application data for managed apps should be encrypted
        self._encrypt_app_data: Optional[bool] = None
        # Define the oldest required Android security patch level a user can have to gain secure access to the app.
        self._minimum_required_patch_version: Optional[str] = None
        # Define the oldest recommended Android security patch level a user can have for secure access to the app.
        self._minimum_warning_patch_version: Optional[str] = None
        # Indicates whether a managed user can take screen captures of managed apps
        self._screen_capture_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedAppProtection()
    
    @property
    def custom_browser_display_name(self,) -> Optional[str]:
        """
        Gets the customBrowserDisplayName property value. Friendly name of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        Returns: Optional[str]
        """
        return self._custom_browser_display_name
    
    @custom_browser_display_name.setter
    def custom_browser_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customBrowserDisplayName property value. Friendly name of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        Args:
            value: Value to set for the customBrowserDisplayName property.
        """
        self._custom_browser_display_name = value
    
    @property
    def custom_browser_package_id(self,) -> Optional[str]:
        """
        Gets the customBrowserPackageId property value. Unique identifier of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        Returns: Optional[str]
        """
        return self._custom_browser_package_id
    
    @custom_browser_package_id.setter
    def custom_browser_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customBrowserPackageId property value. Unique identifier of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        Args:
            value: Value to set for the customBrowserPackageId property.
        """
        self._custom_browser_package_id = value
    
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
        Gets the disableAppEncryptionIfDeviceEncryptionIsEnabled property value. When this setting is enabled, app level encryption is disabled if device level encryption is enabled
        Returns: Optional[bool]
        """
        return self._disable_app_encryption_if_device_encryption_is_enabled
    
    @disable_app_encryption_if_device_encryption_is_enabled.setter
    def disable_app_encryption_if_device_encryption_is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableAppEncryptionIfDeviceEncryptionIsEnabled property value. When this setting is enabled, app level encryption is disabled if device level encryption is enabled
        Args:
            value: Value to set for the disableAppEncryptionIfDeviceEncryptionIsEnabled property.
        """
        self._disable_app_encryption_if_device_encryption_is_enabled = value
    
    @property
    def encrypt_app_data(self,) -> Optional[bool]:
        """
        Gets the encryptAppData property value. Indicates whether application data for managed apps should be encrypted
        Returns: Optional[bool]
        """
        return self._encrypt_app_data
    
    @encrypt_app_data.setter
    def encrypt_app_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the encryptAppData property value. Indicates whether application data for managed apps should be encrypted
        Args:
            value: Value to set for the encryptAppData property.
        """
        self._encrypt_app_data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "custom_browser_display_name": lambda n : setattr(self, 'custom_browser_display_name', n.get_str_value()),
            "custom_browser_package_id": lambda n : setattr(self, 'custom_browser_package_id', n.get_str_value()),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "disable_app_encryption_if_device_encryption_is_enabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "encrypt_app_data": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "minimum_required_patch_version": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimum_warning_patch_version": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_required_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredPatchVersion property value. Define the oldest required Android security patch level a user can have to gain secure access to the app.
        Returns: Optional[str]
        """
        return self._minimum_required_patch_version
    
    @minimum_required_patch_version.setter
    def minimum_required_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredPatchVersion property value. Define the oldest required Android security patch level a user can have to gain secure access to the app.
        Args:
            value: Value to set for the minimumRequiredPatchVersion property.
        """
        self._minimum_required_patch_version = value
    
    @property
    def minimum_warning_patch_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningPatchVersion property value. Define the oldest recommended Android security patch level a user can have for secure access to the app.
        Returns: Optional[str]
        """
        return self._minimum_warning_patch_version
    
    @minimum_warning_patch_version.setter
    def minimum_warning_patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningPatchVersion property value. Define the oldest recommended Android security patch level a user can have for secure access to the app.
        Args:
            value: Value to set for the minimumWarningPatchVersion property.
        """
        self._minimum_warning_patch_version = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether a managed user can take screen captures of managed apps
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether a managed user can take screen captures of managed apps
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
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_str_value("customBrowserDisplayName", self.custom_browser_display_name)
        writer.write_str_value("customBrowserPackageId", self.custom_browser_package_id)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("disableAppEncryptionIfDeviceEncryptionIsEnabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("encryptAppData", self.encrypt_app_data)
        writer.write_str_value("minimumRequiredPatchVersion", self.minimum_required_patch_version)
        writer.write_str_value("minimumWarningPatchVersion", self.minimum_warning_patch_version)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
    

