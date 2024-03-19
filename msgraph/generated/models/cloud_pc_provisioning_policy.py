from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
    from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
    from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
    from .cloud_pc_provisioning_type import CloudPcProvisioningType
    from .cloud_pc_windows_setting import CloudPcWindowsSetting
    from .entity import Entity
    from .microsoft_managed_desktop import MicrosoftManagedDesktop

from .entity import Entity

@dataclass
class CloudPcProvisioningPolicy(Entity):
    # The alternateResourceUrl property
    alternate_resource_url: Optional[str] = None
    # The assignments property
    assignments: Optional[List[CloudPcProvisioningPolicyAssignment]] = None
    # The cloudPcGroupDisplayName property
    cloud_pc_group_display_name: Optional[str] = None
    # The cloudPcNamingTemplate property
    cloud_pc_naming_template: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The domainJoinConfigurations property
    domain_join_configurations: Optional[List[CloudPcDomainJoinConfiguration]] = None
    # The enableSingleSignOn property
    enable_single_sign_on: Optional[bool] = None
    # The gracePeriodInHours property
    grace_period_in_hours: Optional[int] = None
    # The imageDisplayName property
    image_display_name: Optional[str] = None
    # The imageId property
    image_id: Optional[str] = None
    # The imageType property
    image_type: Optional[CloudPcProvisioningPolicyImageType] = None
    # The localAdminEnabled property
    local_admin_enabled: Optional[bool] = None
    # The microsoftManagedDesktop property
    microsoft_managed_desktop: Optional[MicrosoftManagedDesktop] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provisioningType property
    provisioning_type: Optional[CloudPcProvisioningType] = None
    # The windowsSetting property
    windows_setting: Optional[CloudPcWindowsSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcProvisioningPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcProvisioningPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcProvisioningPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .cloud_pc_windows_setting import CloudPcWindowsSetting
        from .entity import Entity
        from .microsoft_managed_desktop import MicrosoftManagedDesktop

        from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .cloud_pc_windows_setting import CloudPcWindowsSetting
        from .entity import Entity
        from .microsoft_managed_desktop import MicrosoftManagedDesktop

        fields: Dict[str, Callable[[Any], None]] = {
            "alternateResourceUrl": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(CloudPcProvisioningPolicyAssignment)),
            "cloudPcGroupDisplayName": lambda n : setattr(self, 'cloud_pc_group_display_name', n.get_str_value()),
            "cloudPcNamingTemplate": lambda n : setattr(self, 'cloud_pc_naming_template', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainJoinConfigurations": lambda n : setattr(self, 'domain_join_configurations', n.get_collection_of_object_values(CloudPcDomainJoinConfiguration)),
            "enableSingleSignOn": lambda n : setattr(self, 'enable_single_sign_on', n.get_bool_value()),
            "gracePeriodInHours": lambda n : setattr(self, 'grace_period_in_hours', n.get_int_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "imageId": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "imageType": lambda n : setattr(self, 'image_type', n.get_enum_value(CloudPcProvisioningPolicyImageType)),
            "localAdminEnabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "microsoftManagedDesktop": lambda n : setattr(self, 'microsoft_managed_desktop', n.get_object_value(MicrosoftManagedDesktop)),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(CloudPcProvisioningType)),
            "windowsSetting": lambda n : setattr(self, 'windows_setting', n.get_object_value(CloudPcWindowsSetting)),
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
        writer.write_str_value("alternateResourceUrl", self.alternate_resource_url)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_str_value("cloudPcGroupDisplayName", self.cloud_pc_group_display_name)
        writer.write_str_value("cloudPcNamingTemplate", self.cloud_pc_naming_template)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("domainJoinConfigurations", self.domain_join_configurations)
        writer.write_bool_value("enableSingleSignOn", self.enable_single_sign_on)
        writer.write_int_value("gracePeriodInHours", self.grace_period_in_hours)
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_str_value("imageId", self.image_id)
        writer.write_enum_value("imageType", self.image_type)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_object_value("microsoftManagedDesktop", self.microsoft_managed_desktop)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_object_value("windowsSetting", self.windows_setting)
    

