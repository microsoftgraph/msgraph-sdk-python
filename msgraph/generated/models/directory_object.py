from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_based_timeout_policy, administrative_unit, application, app_management_policy, app_role_assignment, authorization_policy, claims_mapping_policy, contract, cross_tenant_access_policy, device, directory_object_partner_reference, directory_role, directory_role_template, endpoint, entity, extension_property, group, group_setting_template, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, organization, org_contact, permission_grant_policy, policy_base, resource_specific_permission_grant, service_principal, sts_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy, user

from . import entity

@dataclass
class DirectoryObject(entity.Entity):
    # Date and time when this object was deleted. Always null when the object hasn't been deleted.
    deleted_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObject
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityBasedTimeoutPolicy".casefold():
            from . import activity_based_timeout_policy

            return activity_based_timeout_policy.ActivityBasedTimeoutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.administrativeUnit".casefold():
            from . import administrative_unit

            return administrative_unit.AdministrativeUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.application".casefold():
            from . import application

            return application.Application()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementPolicy".casefold():
            from . import app_management_policy

            return app_management_policy.AppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appRoleAssignment".casefold():
            from . import app_role_assignment

            return app_role_assignment.AppRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationPolicy".casefold():
            from . import authorization_policy

            return authorization_policy.AuthorizationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from . import claims_mapping_policy

            return claims_mapping_policy.ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contract".casefold():
            from . import contract

            return contract.Contract()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from . import cross_tenant_access_policy

            return cross_tenant_access_policy.CrossTenantAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.device".casefold():
            from . import device

            return device.Device()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObjectPartnerReference".casefold():
            from . import directory_object_partner_reference

            return directory_object_partner_reference.DirectoryObjectPartnerReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRole".casefold():
            from . import directory_role

            return directory_role.DirectoryRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRoleTemplate".casefold():
            from . import directory_role_template

            return directory_role_template.DirectoryRoleTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endpoint".casefold():
            from . import endpoint

            return endpoint.Endpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extensionProperty".casefold():
            from . import extension_property

            return extension_property.ExtensionProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.group".casefold():
            from . import group

            return group.Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupSettingTemplate".casefold():
            from . import group_setting_template

            return group_setting_template.GroupSettingTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from . import home_realm_discovery_policy

            return home_realm_discovery_policy.HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy".casefold():
            from . import identity_security_defaults_enforcement_policy

            return identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organization".casefold():
            from . import organization

            return organization.Organization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.orgContact".casefold():
            from . import org_contact

            return org_contact.OrgContact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantPolicy".casefold():
            from . import permission_grant_policy

            return permission_grant_policy.PermissionGrantPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyBase".casefold():
            from . import policy_base

            return policy_base.PolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceSpecificPermissionGrant".casefold():
            from . import resource_specific_permission_grant

            return resource_specific_permission_grant.ResourceSpecificPermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipal".casefold():
            from . import service_principal

            return service_principal.ServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stsPolicy".casefold():
            from . import sts_policy

            return sts_policy.StsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantAppManagementPolicy".casefold():
            from . import tenant_app_management_policy

            return tenant_app_management_policy.TenantAppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenIssuancePolicy".casefold():
            from . import token_issuance_policy

            return token_issuance_policy.TokenIssuancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenLifetimePolicy".casefold():
            from . import token_lifetime_policy

            return token_lifetime_policy.TokenLifetimePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.user".casefold():
            from . import user

            return user.User()
        return DirectoryObject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_based_timeout_policy, administrative_unit, application, app_management_policy, app_role_assignment, authorization_policy, claims_mapping_policy, contract, cross_tenant_access_policy, device, directory_object_partner_reference, directory_role, directory_role_template, endpoint, entity, extension_property, group, group_setting_template, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, organization, org_contact, permission_grant_policy, policy_base, resource_specific_permission_grant, service_principal, sts_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy, user

        from . import activity_based_timeout_policy, administrative_unit, application, app_management_policy, app_role_assignment, authorization_policy, claims_mapping_policy, contract, cross_tenant_access_policy, device, directory_object_partner_reference, directory_role, directory_role_template, endpoint, entity, extension_property, group, group_setting_template, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, organization, org_contact, permission_grant_policy, policy_base, resource_specific_permission_grant, service_principal, sts_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy, user

        fields: Dict[str, Callable[[Any], None]] = {
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
    

