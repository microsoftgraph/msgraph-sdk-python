from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .administrative_unit import AdministrativeUnit
    from .application import Application
    from .app_management_policy import AppManagementPolicy
    from .app_role_assignment import AppRoleAssignment
    from .authorization_policy import AuthorizationPolicy
    from .certificate_authority_detail import CertificateAuthorityDetail
    from .certificate_based_auth_pki import CertificateBasedAuthPki
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .contract import Contract
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .device import Device
    from .directory_object_partner_reference import DirectoryObjectPartnerReference
    from .directory_role import DirectoryRole
    from .directory_role_template import DirectoryRoleTemplate
    from .endpoint import Endpoint
    from .entity import Entity
    from .extension_property import ExtensionProperty
    from .group import Group
    from .group_setting_template import GroupSettingTemplate
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .multi_tenant_organization_member import MultiTenantOrganizationMember
    from .organization import Organization
    from .org_contact import OrgContact
    from .permission_grant_policy import PermissionGrantPolicy
    from .policy_base import PolicyBase
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .service_principal import ServicePrincipal
    from .sts_policy import StsPolicy
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .user import User

from .entity import Entity

@dataclass
class DirectoryObject(Entity, Parsable):
    # Date and time when this object was deleted. Always null when the object hasn't been deleted.
    deleted_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectoryObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObject
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.administrativeUnit".casefold():
            from .administrative_unit import AdministrativeUnit

            return AdministrativeUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.application".casefold():
            from .application import Application

            return Application()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementPolicy".casefold():
            from .app_management_policy import AppManagementPolicy

            return AppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appRoleAssignment".casefold():
            from .app_role_assignment import AppRoleAssignment

            return AppRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationPolicy".casefold():
            from .authorization_policy import AuthorizationPolicy

            return AuthorizationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateAuthorityDetail".casefold():
            from .certificate_authority_detail import CertificateAuthorityDetail

            return CertificateAuthorityDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedAuthPki".casefold():
            from .certificate_based_auth_pki import CertificateBasedAuthPki

            return CertificateBasedAuthPki()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from .claims_mapping_policy import ClaimsMappingPolicy

            return ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contract".casefold():
            from .contract import Contract

            return Contract()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from .cross_tenant_access_policy import CrossTenantAccessPolicy

            return CrossTenantAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.device".casefold():
            from .device import Device

            return Device()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObjectPartnerReference".casefold():
            from .directory_object_partner_reference import DirectoryObjectPartnerReference

            return DirectoryObjectPartnerReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRole".casefold():
            from .directory_role import DirectoryRole

            return DirectoryRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRoleTemplate".casefold():
            from .directory_role_template import DirectoryRoleTemplate

            return DirectoryRoleTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endpoint".casefold():
            from .endpoint import Endpoint

            return Endpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extensionProperty".casefold():
            from .extension_property import ExtensionProperty

            return ExtensionProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.group".casefold():
            from .group import Group

            return Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupSettingTemplate".casefold():
            from .group_setting_template import GroupSettingTemplate

            return GroupSettingTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

            return HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy".casefold():
            from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy

            return IdentitySecurityDefaultsEnforcementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationMember".casefold():
            from .multi_tenant_organization_member import MultiTenantOrganizationMember

            return MultiTenantOrganizationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organization".casefold():
            from .organization import Organization

            return Organization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.orgContact".casefold():
            from .org_contact import OrgContact

            return OrgContact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantPolicy".casefold():
            from .permission_grant_policy import PermissionGrantPolicy

            return PermissionGrantPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyBase".casefold():
            from .policy_base import PolicyBase

            return PolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceSpecificPermissionGrant".casefold():
            from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

            return ResourceSpecificPermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipal".casefold():
            from .service_principal import ServicePrincipal

            return ServicePrincipal()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.user".casefold():
            from .user import User

            return User()
        return DirectoryObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .administrative_unit import AdministrativeUnit
        from .application import Application
        from .app_management_policy import AppManagementPolicy
        from .app_role_assignment import AppRoleAssignment
        from .authorization_policy import AuthorizationPolicy
        from .certificate_authority_detail import CertificateAuthorityDetail
        from .certificate_based_auth_pki import CertificateBasedAuthPki
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .contract import Contract
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .device import Device
        from .directory_object_partner_reference import DirectoryObjectPartnerReference
        from .directory_role import DirectoryRole
        from .directory_role_template import DirectoryRoleTemplate
        from .endpoint import Endpoint
        from .entity import Entity
        from .extension_property import ExtensionProperty
        from .group import Group
        from .group_setting_template import GroupSettingTemplate
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .organization import Organization
        from .org_contact import OrgContact
        from .permission_grant_policy import PermissionGrantPolicy
        from .policy_base import PolicyBase
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .service_principal import ServicePrincipal
        from .sts_policy import StsPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .user import User

        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .administrative_unit import AdministrativeUnit
        from .application import Application
        from .app_management_policy import AppManagementPolicy
        from .app_role_assignment import AppRoleAssignment
        from .authorization_policy import AuthorizationPolicy
        from .certificate_authority_detail import CertificateAuthorityDetail
        from .certificate_based_auth_pki import CertificateBasedAuthPki
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .contract import Contract
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .device import Device
        from .directory_object_partner_reference import DirectoryObjectPartnerReference
        from .directory_role import DirectoryRole
        from .directory_role_template import DirectoryRoleTemplate
        from .endpoint import Endpoint
        from .entity import Entity
        from .extension_property import ExtensionProperty
        from .group import Group
        from .group_setting_template import GroupSettingTemplate
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .organization import Organization
        from .org_contact import OrgContact
        from .permission_grant_policy import PermissionGrantPolicy
        from .policy_base import PolicyBase
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .service_principal import ServicePrincipal
        from .sts_policy import StsPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
    

