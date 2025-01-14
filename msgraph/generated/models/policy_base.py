from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .app_management_policy import AppManagementPolicy
    from .authorization_policy import AuthorizationPolicy
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .directory_object import DirectoryObject
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .permission_grant_policy import PermissionGrantPolicy
    from .sts_policy import StsPolicy
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy

from .directory_object import DirectoryObject

@dataclass
class PolicyBase(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.policyBase"
    # Description for this policy. Required.
    description: Optional[str] = None
    # Display name for this policy. Required.
    display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityBasedTimeoutPolicy".casefold():
            from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy

            return ActivityBasedTimeoutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementPolicy".casefold():
            from .app_management_policy import AppManagementPolicy

            return AppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationPolicy".casefold():
            from .authorization_policy import AuthorizationPolicy

            return AuthorizationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from .claims_mapping_policy import ClaimsMappingPolicy

            return ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from .cross_tenant_access_policy import CrossTenantAccessPolicy

            return CrossTenantAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

            return HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy".casefold():
            from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy

            return IdentitySecurityDefaultsEnforcementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantPolicy".casefold():
            from .permission_grant_policy import PermissionGrantPolicy

            return PermissionGrantPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stsPolicy".casefold():
            from .sts_policy import StsPolicy

            return StsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantAppManagementPolicy".casefold():
            from .tenant_app_management_policy import TenantAppManagementPolicy

            return TenantAppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenIssuancePolicy".casefold():
            from .token_issuance_policy import TokenIssuancePolicy

            return TokenIssuancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenLifetimePolicy".casefold():
            from .token_lifetime_policy import TokenLifetimePolicy

            return TokenLifetimePolicy()
        return PolicyBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .app_management_policy import AppManagementPolicy
        from .authorization_policy import AuthorizationPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .directory_object import DirectoryObject
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .sts_policy import StsPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy

        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .app_management_policy import AppManagementPolicy
        from .authorization_policy import AuthorizationPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .directory_object import DirectoryObject
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .sts_policy import StsPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

