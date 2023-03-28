from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_based_timeout_policy, app_management_policy, authorization_policy, claims_mapping_policy, cross_tenant_access_policy, directory_object, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, permission_grant_policy, sts_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy

from . import directory_object

class PolicyBase(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new policyBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.policyBase"
        # Description for this policy. Required.
        self._description: Optional[str] = None
        # Display name for this policy. Required.
        self._display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicyBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.activityBasedTimeoutPolicy":
                from . import activity_based_timeout_policy

                return activity_based_timeout_policy.ActivityBasedTimeoutPolicy()
            if mapping_value == "#microsoft.graph.appManagementPolicy":
                from . import app_management_policy

                return app_management_policy.AppManagementPolicy()
            if mapping_value == "#microsoft.graph.authorizationPolicy":
                from . import authorization_policy

                return authorization_policy.AuthorizationPolicy()
            if mapping_value == "#microsoft.graph.claimsMappingPolicy":
                from . import claims_mapping_policy

                return claims_mapping_policy.ClaimsMappingPolicy()
            if mapping_value == "#microsoft.graph.crossTenantAccessPolicy":
                from . import cross_tenant_access_policy

                return cross_tenant_access_policy.CrossTenantAccessPolicy()
            if mapping_value == "#microsoft.graph.homeRealmDiscoveryPolicy":
                from . import home_realm_discovery_policy

                return home_realm_discovery_policy.HomeRealmDiscoveryPolicy()
            if mapping_value == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy":
                from . import identity_security_defaults_enforcement_policy

                return identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy()
            if mapping_value == "#microsoft.graph.permissionGrantPolicy":
                from . import permission_grant_policy

                return permission_grant_policy.PermissionGrantPolicy()
            if mapping_value == "#microsoft.graph.stsPolicy":
                from . import sts_policy

                return sts_policy.StsPolicy()
            if mapping_value == "#microsoft.graph.tenantAppManagementPolicy":
                from . import tenant_app_management_policy

                return tenant_app_management_policy.TenantAppManagementPolicy()
            if mapping_value == "#microsoft.graph.tokenIssuancePolicy":
                from . import token_issuance_policy

                return token_issuance_policy.TokenIssuancePolicy()
            if mapping_value == "#microsoft.graph.tokenLifetimePolicy":
                from . import token_lifetime_policy

                return token_lifetime_policy.TokenLifetimePolicy()
        return PolicyBase()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for this policy. Required.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for this policy. Required.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for this policy. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for this policy. Required.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_based_timeout_policy, app_management_policy, authorization_policy, claims_mapping_policy, cross_tenant_access_policy, directory_object, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, permission_grant_policy, sts_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

