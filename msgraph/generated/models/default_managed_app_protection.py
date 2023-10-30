from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair
    from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_protection import ManagedAppProtection
    from .managed_mobile_app import ManagedMobileApp

from .managed_app_protection import ManagedAppProtection

@dataclass
class DefaultManagedAppProtection(ManagedAppProtection):
    """
    Policy used to configure detailed management settings for a specified set of apps for all users not targeted by a TargetedManagedAppProtection Policy
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.defaultManagedAppProtection"
    # Represents the level to which app data is encrypted for managed apps
    app_data_encryption_type: Optional[ManagedAppDataEncryptionType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[List[ManagedMobileApp]] = None
    # A set of string key and string value pairs to be sent to the affected users, unalterned by this service
    custom_settings: Optional[List[KeyValuePair]] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DefaultManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultManagedAppProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DefaultManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
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

        fields: Dict[str, Callable[[Any], None]] = {
            "app_data_encryption_type": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "custom_settings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(KeyValuePair)),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("app_data_encryption_type", self.app_data_encryption_type)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_collection_of_object_values("custom_settings", self.custom_settings)
        writer.write_int_value("deployed_app_count", self.deployed_app_count)
        writer.write_object_value("deployment_summary", self.deployment_summary)
        writer.write_bool_value("disable_app_encryption_if_device_encryption_is_enabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("encrypt_app_data", self.encrypt_app_data)
        writer.write_bool_value("face_id_blocked", self.face_id_blocked)
        writer.write_str_value("minimum_required_patch_version", self.minimum_required_patch_version)
        writer.write_str_value("minimum_required_sdk_version", self.minimum_required_sdk_version)
        writer.write_str_value("minimum_warning_patch_version", self.minimum_warning_patch_version)
        writer.write_bool_value("screen_capture_blocked", self.screen_capture_blocked)
    

