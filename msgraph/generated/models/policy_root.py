from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_based_timeout_policy = lazy_import('msgraph.generated.models.activity_based_timeout_policy')
admin_consent_request_policy = lazy_import('msgraph.generated.models.admin_consent_request_policy')
authentication_flows_policy = lazy_import('msgraph.generated.models.authentication_flows_policy')
authentication_methods_policy = lazy_import('msgraph.generated.models.authentication_methods_policy')
authorization_policy = lazy_import('msgraph.generated.models.authorization_policy')
claims_mapping_policy = lazy_import('msgraph.generated.models.claims_mapping_policy')
conditional_access_policy = lazy_import('msgraph.generated.models.conditional_access_policy')
cross_tenant_access_policy = lazy_import('msgraph.generated.models.cross_tenant_access_policy')
entity = lazy_import('msgraph.generated.models.entity')
feature_rollout_policy = lazy_import('msgraph.generated.models.feature_rollout_policy')
home_realm_discovery_policy = lazy_import('msgraph.generated.models.home_realm_discovery_policy')
identity_security_defaults_enforcement_policy = lazy_import('msgraph.generated.models.identity_security_defaults_enforcement_policy')
permission_grant_policy = lazy_import('msgraph.generated.models.permission_grant_policy')
token_issuance_policy = lazy_import('msgraph.generated.models.token_issuance_policy')
token_lifetime_policy = lazy_import('msgraph.generated.models.token_lifetime_policy')
unified_role_management_policy = lazy_import('msgraph.generated.models.unified_role_management_policy')
unified_role_management_policy_assignment = lazy_import('msgraph.generated.models.unified_role_management_policy_assignment')

class PolicyRoot(entity.Entity):
    @property
    def activity_based_timeout_policies(self,) -> Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]]:
        """
        Gets the activityBasedTimeoutPolicies property value. The policy that controls the idle time out for web sessions for applications.
        Returns: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]]
        """
        return self._activity_based_timeout_policies
    
    @activity_based_timeout_policies.setter
    def activity_based_timeout_policies(self,value: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]] = None) -> None:
        """
        Sets the activityBasedTimeoutPolicies property value. The policy that controls the idle time out for web sessions for applications.
        Args:
            value: Value to set for the activityBasedTimeoutPolicies property.
        """
        self._activity_based_timeout_policies = value
    
    @property
    def admin_consent_request_policy(self,) -> Optional[admin_consent_request_policy.AdminConsentRequestPolicy]:
        """
        Gets the adminConsentRequestPolicy property value. The policy by which consent requests are created and managed for the entire tenant.
        Returns: Optional[admin_consent_request_policy.AdminConsentRequestPolicy]
        """
        return self._admin_consent_request_policy
    
    @admin_consent_request_policy.setter
    def admin_consent_request_policy(self,value: Optional[admin_consent_request_policy.AdminConsentRequestPolicy] = None) -> None:
        """
        Sets the adminConsentRequestPolicy property value. The policy by which consent requests are created and managed for the entire tenant.
        Args:
            value: Value to set for the adminConsentRequestPolicy property.
        """
        self._admin_consent_request_policy = value
    
    @property
    def authentication_flows_policy(self,) -> Optional[authentication_flows_policy.AuthenticationFlowsPolicy]:
        """
        Gets the authenticationFlowsPolicy property value. The policy configuration of the self-service sign-up experience of external users.
        Returns: Optional[authentication_flows_policy.AuthenticationFlowsPolicy]
        """
        return self._authentication_flows_policy
    
    @authentication_flows_policy.setter
    def authentication_flows_policy(self,value: Optional[authentication_flows_policy.AuthenticationFlowsPolicy] = None) -> None:
        """
        Sets the authenticationFlowsPolicy property value. The policy configuration of the self-service sign-up experience of external users.
        Args:
            value: Value to set for the authenticationFlowsPolicy property.
        """
        self._authentication_flows_policy = value
    
    @property
    def authentication_methods_policy(self,) -> Optional[authentication_methods_policy.AuthenticationMethodsPolicy]:
        """
        Gets the authenticationMethodsPolicy property value. The authentication methods and the users that are allowed to use them to sign in and perform multi-factor authentication (MFA) in Azure Active Directory (Azure AD).
        Returns: Optional[authentication_methods_policy.AuthenticationMethodsPolicy]
        """
        return self._authentication_methods_policy
    
    @authentication_methods_policy.setter
    def authentication_methods_policy(self,value: Optional[authentication_methods_policy.AuthenticationMethodsPolicy] = None) -> None:
        """
        Sets the authenticationMethodsPolicy property value. The authentication methods and the users that are allowed to use them to sign in and perform multi-factor authentication (MFA) in Azure Active Directory (Azure AD).
        Args:
            value: Value to set for the authenticationMethodsPolicy property.
        """
        self._authentication_methods_policy = value
    
    @property
    def authorization_policy(self,) -> Optional[authorization_policy.AuthorizationPolicy]:
        """
        Gets the authorizationPolicy property value. The policy that controls Azure AD authorization settings.
        Returns: Optional[authorization_policy.AuthorizationPolicy]
        """
        return self._authorization_policy
    
    @authorization_policy.setter
    def authorization_policy(self,value: Optional[authorization_policy.AuthorizationPolicy] = None) -> None:
        """
        Sets the authorizationPolicy property value. The policy that controls Azure AD authorization settings.
        Args:
            value: Value to set for the authorizationPolicy property.
        """
        self._authorization_policy = value
    
    @property
    def claims_mapping_policies(self,) -> Optional[List[claims_mapping_policy.ClaimsMappingPolicy]]:
        """
        Gets the claimsMappingPolicies property value. The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
        Returns: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]]
        """
        return self._claims_mapping_policies
    
    @claims_mapping_policies.setter
    def claims_mapping_policies(self,value: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None) -> None:
        """
        Sets the claimsMappingPolicies property value. The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
        Args:
            value: Value to set for the claimsMappingPolicies property.
        """
        self._claims_mapping_policies = value
    
    @property
    def conditional_access_policies(self,) -> Optional[List[conditional_access_policy.ConditionalAccessPolicy]]:
        """
        Gets the conditionalAccessPolicies property value. The custom rules that define an access scenario.
        Returns: Optional[List[conditional_access_policy.ConditionalAccessPolicy]]
        """
        return self._conditional_access_policies
    
    @conditional_access_policies.setter
    def conditional_access_policies(self,value: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None) -> None:
        """
        Sets the conditionalAccessPolicies property value. The custom rules that define an access scenario.
        Args:
            value: Value to set for the conditionalAccessPolicies property.
        """
        self._conditional_access_policies = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PolicyRoot and sets the default values.
        """
        super().__init__()
        # The policy that controls the idle time out for web sessions for applications.
        self._activity_based_timeout_policies: Optional[List[activity_based_timeout_policy.ActivityBasedTimeoutPolicy]] = None
        # The policy by which consent requests are created and managed for the entire tenant.
        self._admin_consent_request_policy: Optional[admin_consent_request_policy.AdminConsentRequestPolicy] = None
        # The policy configuration of the self-service sign-up experience of external users.
        self._authentication_flows_policy: Optional[authentication_flows_policy.AuthenticationFlowsPolicy] = None
        # The authentication methods and the users that are allowed to use them to sign in and perform multi-factor authentication (MFA) in Azure Active Directory (Azure AD).
        self._authentication_methods_policy: Optional[authentication_methods_policy.AuthenticationMethodsPolicy] = None
        # The policy that controls Azure AD authorization settings.
        self._authorization_policy: Optional[authorization_policy.AuthorizationPolicy] = None
        # The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
        self._claims_mapping_policies: Optional[List[claims_mapping_policy.ClaimsMappingPolicy]] = None
        # The custom rules that define an access scenario.
        self._conditional_access_policies: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
        # The custom rules that define an access scenario when interacting with external Azure AD tenants.
        self._cross_tenant_access_policy: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy] = None
        # The feature rollout policy associated with a directory object.
        self._feature_rollout_policies: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None
        # The policy to control Azure AD authentication behavior for federated users.
        self._home_realm_discovery_policies: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None
        # The policy that represents the security defaults that protect against common attacks.
        self._identity_security_defaults_enforcement_policy: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policy that specifies the conditions under which consent can be granted.
        self._permission_grant_policies: Optional[List[permission_grant_policy.PermissionGrantPolicy]] = None
        # Specifies the various policies associated with scopes and roles.
        self._role_management_policies: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]] = None
        # The assignment of a role management policy to a role definition object.
        self._role_management_policy_assignments: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]] = None
        # The policy that specifies the characteristics of SAML tokens issued by Azure AD.
        self._token_issuance_policies: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None
        # The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
        self._token_lifetime_policies: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None
    
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
    
    @property
    def cross_tenant_access_policy(self,) -> Optional[cross_tenant_access_policy.CrossTenantAccessPolicy]:
        """
        Gets the crossTenantAccessPolicy property value. The custom rules that define an access scenario when interacting with external Azure AD tenants.
        Returns: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy]
        """
        return self._cross_tenant_access_policy
    
    @cross_tenant_access_policy.setter
    def cross_tenant_access_policy(self,value: Optional[cross_tenant_access_policy.CrossTenantAccessPolicy] = None) -> None:
        """
        Sets the crossTenantAccessPolicy property value. The custom rules that define an access scenario when interacting with external Azure AD tenants.
        Args:
            value: Value to set for the crossTenantAccessPolicy property.
        """
        self._cross_tenant_access_policy = value
    
    @property
    def feature_rollout_policies(self,) -> Optional[List[feature_rollout_policy.FeatureRolloutPolicy]]:
        """
        Gets the featureRolloutPolicies property value. The feature rollout policy associated with a directory object.
        Returns: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]]
        """
        return self._feature_rollout_policies
    
    @feature_rollout_policies.setter
    def feature_rollout_policies(self,value: Optional[List[feature_rollout_policy.FeatureRolloutPolicy]] = None) -> None:
        """
        Sets the featureRolloutPolicies property value. The feature rollout policy associated with a directory object.
        Args:
            value: Value to set for the featureRolloutPolicies property.
        """
        self._feature_rollout_policies = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_based_timeout_policies": lambda n : setattr(self, 'activity_based_timeout_policies', n.get_collection_of_object_values(activity_based_timeout_policy.ActivityBasedTimeoutPolicy)),
            "admin_consent_request_policy": lambda n : setattr(self, 'admin_consent_request_policy', n.get_object_value(admin_consent_request_policy.AdminConsentRequestPolicy)),
            "authentication_flows_policy": lambda n : setattr(self, 'authentication_flows_policy', n.get_object_value(authentication_flows_policy.AuthenticationFlowsPolicy)),
            "authentication_methods_policy": lambda n : setattr(self, 'authentication_methods_policy', n.get_object_value(authentication_methods_policy.AuthenticationMethodsPolicy)),
            "authorization_policy": lambda n : setattr(self, 'authorization_policy', n.get_object_value(authorization_policy.AuthorizationPolicy)),
            "claims_mapping_policies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(claims_mapping_policy.ClaimsMappingPolicy)),
            "conditional_access_policies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(conditional_access_policy.ConditionalAccessPolicy)),
            "cross_tenant_access_policy": lambda n : setattr(self, 'cross_tenant_access_policy', n.get_object_value(cross_tenant_access_policy.CrossTenantAccessPolicy)),
            "feature_rollout_policies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(feature_rollout_policy.FeatureRolloutPolicy)),
            "home_realm_discovery_policies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(home_realm_discovery_policy.HomeRealmDiscoveryPolicy)),
            "identity_security_defaults_enforcement_policy": lambda n : setattr(self, 'identity_security_defaults_enforcement_policy', n.get_object_value(identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy)),
            "permission_grant_policies": lambda n : setattr(self, 'permission_grant_policies', n.get_collection_of_object_values(permission_grant_policy.PermissionGrantPolicy)),
            "role_management_policies": lambda n : setattr(self, 'role_management_policies', n.get_collection_of_object_values(unified_role_management_policy.UnifiedRoleManagementPolicy)),
            "role_management_policy_assignments": lambda n : setattr(self, 'role_management_policy_assignments', n.get_collection_of_object_values(unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment)),
            "token_issuance_policies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(token_issuance_policy.TokenIssuancePolicy)),
            "token_lifetime_policies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(token_lifetime_policy.TokenLifetimePolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_realm_discovery_policies(self,) -> Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]:
        """
        Gets the homeRealmDiscoveryPolicies property value. The policy to control Azure AD authentication behavior for federated users.
        Returns: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]]
        """
        return self._home_realm_discovery_policies
    
    @home_realm_discovery_policies.setter
    def home_realm_discovery_policies(self,value: Optional[List[home_realm_discovery_policy.HomeRealmDiscoveryPolicy]] = None) -> None:
        """
        Sets the homeRealmDiscoveryPolicies property value. The policy to control Azure AD authentication behavior for federated users.
        Args:
            value: Value to set for the homeRealmDiscoveryPolicies property.
        """
        self._home_realm_discovery_policies = value
    
    @property
    def identity_security_defaults_enforcement_policy(self,) -> Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy]:
        """
        Gets the identitySecurityDefaultsEnforcementPolicy property value. The policy that represents the security defaults that protect against common attacks.
        Returns: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy]
        """
        return self._identity_security_defaults_enforcement_policy
    
    @identity_security_defaults_enforcement_policy.setter
    def identity_security_defaults_enforcement_policy(self,value: Optional[identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy] = None) -> None:
        """
        Sets the identitySecurityDefaultsEnforcementPolicy property value. The policy that represents the security defaults that protect against common attacks.
        Args:
            value: Value to set for the identitySecurityDefaultsEnforcementPolicy property.
        """
        self._identity_security_defaults_enforcement_policy = value
    
    @property
    def permission_grant_policies(self,) -> Optional[List[permission_grant_policy.PermissionGrantPolicy]]:
        """
        Gets the permissionGrantPolicies property value. The policy that specifies the conditions under which consent can be granted.
        Returns: Optional[List[permission_grant_policy.PermissionGrantPolicy]]
        """
        return self._permission_grant_policies
    
    @permission_grant_policies.setter
    def permission_grant_policies(self,value: Optional[List[permission_grant_policy.PermissionGrantPolicy]] = None) -> None:
        """
        Sets the permissionGrantPolicies property value. The policy that specifies the conditions under which consent can be granted.
        Args:
            value: Value to set for the permissionGrantPolicies property.
        """
        self._permission_grant_policies = value
    
    @property
    def role_management_policies(self,) -> Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]]:
        """
        Gets the roleManagementPolicies property value. Specifies the various policies associated with scopes and roles.
        Returns: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]]
        """
        return self._role_management_policies
    
    @role_management_policies.setter
    def role_management_policies(self,value: Optional[List[unified_role_management_policy.UnifiedRoleManagementPolicy]] = None) -> None:
        """
        Sets the roleManagementPolicies property value. Specifies the various policies associated with scopes and roles.
        Args:
            value: Value to set for the roleManagementPolicies property.
        """
        self._role_management_policies = value
    
    @property
    def role_management_policy_assignments(self,) -> Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]]:
        """
        Gets the roleManagementPolicyAssignments property value. The assignment of a role management policy to a role definition object.
        Returns: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]]
        """
        return self._role_management_policy_assignments
    
    @role_management_policy_assignments.setter
    def role_management_policy_assignments(self,value: Optional[List[unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment]] = None) -> None:
        """
        Sets the roleManagementPolicyAssignments property value. The assignment of a role management policy to a role definition object.
        Args:
            value: Value to set for the roleManagementPolicyAssignments property.
        """
        self._role_management_policy_assignments = value
    
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
        writer.write_object_value("authenticationFlowsPolicy", self.authentication_flows_policy)
        writer.write_object_value("authenticationMethodsPolicy", self.authentication_methods_policy)
        writer.write_object_value("authorizationPolicy", self.authorization_policy)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("conditionalAccessPolicies", self.conditional_access_policies)
        writer.write_object_value("crossTenantAccessPolicy", self.cross_tenant_access_policy)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_object_value("identitySecurityDefaultsEnforcementPolicy", self.identity_security_defaults_enforcement_policy)
        writer.write_collection_of_object_values("permissionGrantPolicies", self.permission_grant_policies)
        writer.write_collection_of_object_values("roleManagementPolicies", self.role_management_policies)
        writer.write_collection_of_object_values("roleManagementPolicyAssignments", self.role_management_policy_assignments)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
    
    @property
    def token_issuance_policies(self,) -> Optional[List[token_issuance_policy.TokenIssuancePolicy]]:
        """
        Gets the tokenIssuancePolicies property value. The policy that specifies the characteristics of SAML tokens issued by Azure AD.
        Returns: Optional[List[token_issuance_policy.TokenIssuancePolicy]]
        """
        return self._token_issuance_policies
    
    @token_issuance_policies.setter
    def token_issuance_policies(self,value: Optional[List[token_issuance_policy.TokenIssuancePolicy]] = None) -> None:
        """
        Sets the tokenIssuancePolicies property value. The policy that specifies the characteristics of SAML tokens issued by Azure AD.
        Args:
            value: Value to set for the tokenIssuancePolicies property.
        """
        self._token_issuance_policies = value
    
    @property
    def token_lifetime_policies(self,) -> Optional[List[token_lifetime_policy.TokenLifetimePolicy]]:
        """
        Gets the tokenLifetimePolicies property value. The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
        Returns: Optional[List[token_lifetime_policy.TokenLifetimePolicy]]
        """
        return self._token_lifetime_policies
    
    @token_lifetime_policies.setter
    def token_lifetime_policies(self,value: Optional[List[token_lifetime_policy.TokenLifetimePolicy]] = None) -> None:
        """
        Sets the tokenLifetimePolicies property value. The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Azure AD.
        Args:
            value: Value to set for the tokenLifetimePolicies property.
        """
        self._token_lifetime_policies = value
    

