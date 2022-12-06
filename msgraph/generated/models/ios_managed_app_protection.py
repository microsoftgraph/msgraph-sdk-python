from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_app_data_encryption_type = lazy_import('msgraph.generated.models.managed_app_data_encryption_type')
managed_app_policy_deployment_summary = lazy_import('msgraph.generated.models.managed_app_policy_deployment_summary')
managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')
targeted_managed_app_protection = lazy_import('msgraph.generated.models.targeted_managed_app_protection')

class IosManagedAppProtection(targeted_managed_app_protection.TargetedManagedAppProtection):
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
        Instantiates a new IosManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosManagedAppProtection"
        # Represents the level to which app data is encrypted for managed apps
        self._app_data_encryption_type: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType] = None
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # A custom browser protocol to open weblink on iOS. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        self._custom_browser_protocol: Optional[str] = None
        # Count of apps to which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # Navigation property to deployment summary of the configuration.
        self._deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
        # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
        self._face_id_blocked: Optional[bool] = None
        # Versions less than the specified version will block the managed app from accessing company data.
        self._minimum_required_sdk_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosManagedAppProtection()
    
    @property
    def custom_browser_protocol(self,) -> Optional[str]:
        """
        Gets the customBrowserProtocol property value. A custom browser protocol to open weblink on iOS. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        Returns: Optional[str]
        """
        return self._custom_browser_protocol
    
    @custom_browser_protocol.setter
    def custom_browser_protocol(self,value: Optional[str] = None) -> None:
        """
        Sets the customBrowserProtocol property value. A custom browser protocol to open weblink on iOS. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
        Args:
            value: Value to set for the customBrowserProtocol property.
        """
        self._custom_browser_protocol = value
    
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
    def face_id_blocked(self,) -> Optional[bool]:
        """
        Gets the faceIdBlocked property value. Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
        Returns: Optional[bool]
        """
        return self._face_id_blocked
    
    @face_id_blocked.setter
    def face_id_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the faceIdBlocked property value. Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
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
            "custom_browser_protocol": lambda n : setattr(self, 'custom_browser_protocol', n.get_str_value()),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "face_id_blocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "minimum_required_sdk_version": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_required_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_required_sdk_version
    
    @minimum_required_sdk_version.setter
    def minimum_required_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Args:
            value: Value to set for the minimumRequiredSdkVersion property.
        """
        self._minimum_required_sdk_version = value
    
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
        writer.write_str_value("customBrowserProtocol", self.custom_browser_protocol)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("faceIdBlocked", self.face_id_blocked)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
    

