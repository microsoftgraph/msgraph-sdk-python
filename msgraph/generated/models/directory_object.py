from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_based_timeout_policy, administrative_unit, application, app_management_policy, app_role_assignment, authorization_policy, claims_mapping_policy, contract, cross_tenant_access_policy, device, directory_object_partner_reference, directory_role, directory_role_template, endpoint, entity, extension_property, group, group_setting_template, home_realm_discovery_policy, identity_security_defaults_enforcement_policy, organization, org_contact, permission_grant_policy, policy_base, resource_specific_permission_grant, service_principal, sts_policy, tenant_app_management_policy, token_issuance_policy, token_lifetime_policy, user

from . import entity

class DirectoryObject(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new directoryObject and sets the default values.
        """
        super().__init__()
        # Date and time when this object was deleted. Always null when the object hasn't been deleted.
        self._deleted_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.activityBasedTimeoutPolicy":
                from . import activity_based_timeout_policy

                return activity_based_timeout_policy.ActivityBasedTimeoutPolicy()
            if mapping_value == "#microsoft.graph.administrativeUnit":
                from . import administrative_unit

                return administrative_unit.AdministrativeUnit()
            if mapping_value == "#microsoft.graph.application":
                from . import application

                return application.Application()
            if mapping_value == "#microsoft.graph.appManagementPolicy":
                from . import app_management_policy

                return app_management_policy.AppManagementPolicy()
            if mapping_value == "#microsoft.graph.appRoleAssignment":
                from . import app_role_assignment

                return app_role_assignment.AppRoleAssignment()
            if mapping_value == "#microsoft.graph.authorizationPolicy":
                from . import authorization_policy

                return authorization_policy.AuthorizationPolicy()
            if mapping_value == "#microsoft.graph.claimsMappingPolicy":
                from . import claims_mapping_policy

                return claims_mapping_policy.ClaimsMappingPolicy()
            if mapping_value == "#microsoft.graph.contract":
                from . import contract

                return contract.Contract()
            if mapping_value == "#microsoft.graph.crossTenantAccessPolicy":
                from . import cross_tenant_access_policy

                return cross_tenant_access_policy.CrossTenantAccessPolicy()
            if mapping_value == "#microsoft.graph.device":
                from . import device

                return device.Device()
            if mapping_value == "#microsoft.graph.directoryObjectPartnerReference":
                from . import directory_object_partner_reference

                return directory_object_partner_reference.DirectoryObjectPartnerReference()
            if mapping_value == "#microsoft.graph.directoryRole":
                from . import directory_role

                return directory_role.DirectoryRole()
            if mapping_value == "#microsoft.graph.directoryRoleTemplate":
                from . import directory_role_template

                return directory_role_template.DirectoryRoleTemplate()
            if mapping_value == "#microsoft.graph.endpoint":
                from . import endpoint

                return endpoint.Endpoint()
            if mapping_value == "#microsoft.graph.extensionProperty":
                from . import extension_property

                return extension_property.ExtensionProperty()
            if mapping_value == "#microsoft.graph.group":
                from . import group

                return group.Group()
            if mapping_value == "#microsoft.graph.groupSettingTemplate":
                from . import group_setting_template

                return group_setting_template.GroupSettingTemplate()
            if mapping_value == "#microsoft.graph.homeRealmDiscoveryPolicy":
                from . import home_realm_discovery_policy

                return home_realm_discovery_policy.HomeRealmDiscoveryPolicy()
            if mapping_value == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy":
                from . import identity_security_defaults_enforcement_policy

                return identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy()
            if mapping_value == "#microsoft.graph.organization":
                from . import organization

                return organization.Organization()
            if mapping_value == "#microsoft.graph.orgContact":
                from . import org_contact

                return org_contact.OrgContact()
            if mapping_value == "#microsoft.graph.permissionGrantPolicy":
                from . import permission_grant_policy

                return permission_grant_policy.PermissionGrantPolicy()
            if mapping_value == "#microsoft.graph.policyBase":
                from . import policy_base

                return policy_base.PolicyBase()
            if mapping_value == "#microsoft.graph.resourceSpecificPermissionGrant":
                from . import resource_specific_permission_grant

                return resource_specific_permission_grant.ResourceSpecificPermissionGrant()
            if mapping_value == "#microsoft.graph.servicePrincipal":
                from . import service_principal

                return service_principal.ServicePrincipal()
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
            if mapping_value == "#microsoft.graph.user":
                from . import user

                return user.User()
        return DirectoryObject()
    
    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. Date and time when this object was deleted. Always null when the object hasn't been deleted.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time
    
    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. Date and time when this object was deleted. Always null when the object hasn't been deleted.
        Args:
            value: Value to set for the deleted_date_time property.
        """
        self._deleted_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
    

