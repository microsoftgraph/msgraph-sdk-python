from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_based_timeout_policy, admin_consent_request_policy, app_management_policy, authentication_flows_policy, authentication_methods_policy, authentication_strength_policy, authorization_policy, claims_mapping_policy, conditional_access_policy, cross_tenant_access_policy, entity, feature_rollout_policy, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, permission_grant_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy, unified_role_management_policy, unified_role_management_policy_assignment

from . import entity

@dataclass
class PolicyRoot(entity.Entity):
    # The policy that controls the idle time out for web sessions for applications.
    activity_based_timeout_policies: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]] = None
    # The policy by which consent requests are created and managed for the entire tenant.
    admin_consent_request_policy: Optional[admin_consent_request_policy.AdminConsentRequestPolicy] = None
    # The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
    app_management_policies: Optional[List[app_management_policy.AppManagementPolicy]] = None
    # The policy configuration of the self-service sign-up experience of external users.
    authentication_flows_policy: Optional[authentication_flows_policy.AuthenticationFlowsPolicy] = None
    # The authentication methods and the users that are allowed to use them to sign in and perform multifactor authentication (MFA) in Azure Active Directory (Azure AD).
    authentication_methods_policy: Optional[authentication_methods_policy.AuthenticationMethodsPolicy] = None
    # The authentication method combinations that are to be used in scenarios defined by Azure AD Conditional Access.
    authentication_strength_policies: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None
    # The policy that controls Azure AD authorization settings.
    authorization_policy: Optional[authorization_policy.AuthorizationPolicy] = None
    # The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
    claims_mapping_policies: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None
    # The custom rules that define an access scenario.
    conditional_access_policies: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
    # The custom rules that define an access scenario when interacting with external Azure AD tenants.
    cross_tenant_access_policy: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy] = None
    # The tenant-wide policy that enforces app management restrictions for all applications and service principals.
    default_app_management_policy: Optional[tenant_app_management_policy.TenantAppManagementPolicy] = None
    # The feature rollout policy associated with a directory object.
    feature_rollout_policies: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None
    # The policy to control Azure AD authentication behavior for federated users.
    home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
    # The policy that represents the security defaults that protect against common attacks.
    identity_security_defaults_enforcement_policy: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy that specifies the conditions under which consent can be granted.
    permission_grant_policies: Optional[List[permission_grant_policy.PermissionGrantPolicy]] = None
    # Specifies the various policies associated with scopes and roles.
    role_management_policies: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]] = None
    # The assignment of a role management policy to a role definition object.
    role_management_policy_assignments: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]] = None
    # The policy that specifies the characteristics of SAML tokens issued by Azure AD.
    token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
    # The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
    token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PolicyRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_based_timeout_policy, admin_consent_request_policy, app_management_policy, authentication_flows_policy, authentication_methods_policy, authentication_strength_policy, authorization_policy, claims_mapping_policy, conditional_access_policy, cross_tenant_access_policy, entity, feature_rollout_policy, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, permission_grant_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy, unified_role_management_policy, unified_role_management_policy_assignment

        fields: Dict[str, Callable[[Any], None]] = {
            "activityBasedTimeoutPolicies": lambda n : setattr(self, 'activity_based_timeout_policies', n.get_collection_of_object_values(activity_based_timeout_policy.ActivityBasedTimeoutPolicy)),
            "adminConsentRequestPolicy": lambda n : setattr(self, 'admin_consent_request_policy', n.get_object_value(admin_consent_request_policy.AdminConsentRequestPolicy)),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(app_management_policy.AppManagementPolicy)),
            "authenticationFlowsPolicy": lambda n : setattr(self, 'authentication_flows_policy', n.get_object_value(authentication_flows_policy.AuthenticationFlowsPolicy)),
            "authenticationMethodsPolicy": lambda n : setattr(self, 'authentication_methods_policy', n.get_object_value(authentication_methods_policy.AuthenticationMethodsPolicy)),
            "authenticationStrengthPolicies": lambda n : setattr(self, 'authentication_strength_policies', n.get_collection_of_object_values(authentication_strength_policy.AuthenticationStrengthPolicy)),
            "authorizationPolicy": lambda n : setattr(self, 'authorization_policy', n.get_object_value(authorization_policy.AuthorizationPolicy)),
            "claimsMappingPolicies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(claims_mapping_policy.ClaimsMappingPolicy)),
            "conditionalAccessPolicies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(conditional_access_policy.ConditionalAccessPolicy)),
            "crossTenantAccessPolicy": lambda n : setattr(self, 'cross_tenant_access_policy', n.get_object_value(cross_tenant_access_policy.CrossTenantAccessPolicy)),
            "defaultAppManagementPolicy": lambda n : setattr(self, 'default_app_management_policy', n.get_object_value(tenant_app_management_policy.TenantAppManagementPolicy)),
            "featureRolloutPolicies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(feature_rollout_policy.FeatureRolloutPolicy)),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "identitySecurityDefaultsEnforcementPolicy": lambda n : setattr(self, 'identity_security_defaults_enforcement_policy', n.get_object_value(identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy)),
            "permissionGrantPolicies": lambda n : setattr(self, 'permission_grant_policies', n.get_collection_of_object_values(permission_grant_policy.PermissionGrantPolicy)),
            "roleManagementPolicies": lambda n : setattr(self, 'role_management_policies', n.get_collection_of_object_values(unified_role_management_policy.UnifiedRoleManagementPolicy)),
            "roleManagementPolicyAssignments": lambda n : setattr(self, 'role_management_policy_assignments', n.get_collection_of_object_values(unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment)),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
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
        writer.write_collection_of_object_values("activityBasedTimeoutPolicies", self.activity_based_timeout_policies)
        writer.write_object_value("adminConsentRequestPolicy", self.admin_consent_request_policy)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_object_value("authenticationFlowsPolicy", self.authentication_flows_policy)
        writer.write_object_value("authenticationMethodsPolicy", self.authentication_methods_policy)
        writer.write_collection_of_object_values("authenticationStrengthPolicies", self.authentication_strength_policies)
        writer.write_object_value("authorizationPolicy", self.authorization_policy)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("conditionalAccessPolicies", self.conditional_access_policies)
        writer.write_object_value("crossTenantAccessPolicy", self.cross_tenant_access_policy)
        writer.write_object_value("defaultAppManagementPolicy", self.default_app_management_policy)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_object_value("identitySecurityDefaultsEnforcementPolicy", self.identity_security_defaults_enforcement_policy)
        writer.write_collection_of_object_values("permissionGrantPolicies", self.permission_grant_policies)
        writer.write_collection_of_object_values("roleManagementPolicies", self.role_management_policies)
        writer.write_collection_of_object_values("roleManagementPolicyAssignments", self.role_management_policy_assignments)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
    

