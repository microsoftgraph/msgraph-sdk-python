from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_mobile_app import ManagedMobileApp
    from .targeted_managed_app_protection import TargetedManagedAppProtection

from .targeted_managed_app_protection import TargetedManagedAppProtection

@dataclass
class IosManagedAppProtection(TargetedManagedAppProtection, Parsable):
    """
    Policy used to configure detailed management settings targeted to specific security groups and for a specified set of apps on an iOS device
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosManagedAppProtection"
    # Represents the level to which app data is encrypted for managed apps
    app_data_encryption_type: Optional[ManagedAppDataEncryptionType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[list[ManagedMobileApp]] = None
    # A custom browser protocol to open weblink on iOS. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
    custom_browser_protocol: Optional[str] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
    face_id_blocked: Optional[bool] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_required_sdk_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosManagedAppProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosManagedAppProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        fields: dict[str, Callable[[Any], None]] = {
            "appDataEncryptionType": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "customBrowserProtocol": lambda n : setattr(self, 'custom_browser_protocol', n.get_str_value()),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "faceIdBlocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
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
        writer.write_str_value("customBrowserProtocol", self.custom_browser_protocol)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("faceIdBlocked", self.face_id_blocked)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
    

