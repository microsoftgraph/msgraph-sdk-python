from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair
    from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_protection import ManagedAppProtection
    from .managed_mobile_app import ManagedMobileApp

from .managed_app_protection import ManagedAppProtection

@dataclass
class DefaultManagedAppProtection(ManagedAppProtection, Parsable):
    """
    Policy used to configure detailed management settings for a specified set of apps for all users not targeted by a TargetedManagedAppProtection Policy
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.defaultManagedAppProtection"
    # Represents the level to which app data is encrypted for managed apps
    app_data_encryption_type: Optional[ManagedAppDataEncryptionType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[list[ManagedMobileApp]] = None
    # A set of string key and string value pairs to be sent to the affected users, unalterned by this service
    custom_settings: Optional[list[KeyValuePair]] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # When this setting is enabled, app level encryption is disabled if device level encryption is enabled. (Android only)
    disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
    # Indicates whether managed-app data should be encrypted. (Android only)
    encrypt_app_data: Optional[bool] = None
    # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True. (iOS Only)
    face_id_blocked: Optional[bool] = None
    # Define the oldest required Android security patch level a user can have to gain secure access to the app. (Android only)
    minimum_required_patch_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. (iOS Only)
    minimum_required_sdk_version: Optional[str] = None
    # Define the oldest recommended Android security patch level a user can have for secure access to the app. (Android only)
    minimum_warning_patch_version: Optional[str] = None
    # Indicates whether screen capture is blocked. (Android only)
    screen_capture_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DefaultManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultManagedAppProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DefaultManagedAppProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_value_pair import KeyValuePair
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_mobile_app import ManagedMobileApp

        from .key_value_pair import KeyValuePair
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_mobile_app import ManagedMobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "appDataEncryptionType": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "customSettings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(KeyValuePair)),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "disableAppEncryptionIfDeviceEncryptionIsEnabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "encryptAppData": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "faceIdBlocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "minimumRequiredPatchVersion": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimumWarningPatchVersion": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
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
    

