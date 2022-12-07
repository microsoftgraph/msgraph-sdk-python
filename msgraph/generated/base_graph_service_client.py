from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_abstractions.utils import lazy_import
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, Union

admin_request_builder = lazy_import('msgraph.generated.admin.admin_request_builder')
agreement_acceptances_request_builder = lazy_import('msgraph.generated.agreement_acceptances.agreement_acceptances_request_builder')
agreement_acceptance_item_request_builder = lazy_import('msgraph.generated.agreement_acceptances.item.agreement_acceptance_item_request_builder')
agreements_request_builder = lazy_import('msgraph.generated.agreements.agreements_request_builder')
agreement_item_request_builder = lazy_import('msgraph.generated.agreements.item.agreement_item_request_builder')
app_catalogs_request_builder = lazy_import('msgraph.generated.app_catalogs.app_catalogs_request_builder')
applications_request_builder = lazy_import('msgraph.generated.applications.applications_request_builder')
application_item_request_builder = lazy_import('msgraph.generated.applications.item.application_item_request_builder')
application_templates_request_builder = lazy_import('msgraph.generated.application_templates.application_templates_request_builder')
application_template_item_request_builder = lazy_import('msgraph.generated.application_templates.item.application_template_item_request_builder')
audit_logs_request_builder = lazy_import('msgraph.generated.audit_logs.audit_logs_request_builder')
authentication_method_configurations_request_builder = lazy_import('msgraph.generated.authentication_method_configurations.authentication_method_configurations_request_builder')
authentication_method_configuration_item_request_builder = lazy_import('msgraph.generated.authentication_method_configurations.item.authentication_method_configuration_item_request_builder')
authentication_methods_policy_request_builder = lazy_import('msgraph.generated.authentication_methods_policy.authentication_methods_policy_request_builder')
branding_request_builder = lazy_import('msgraph.generated.branding.branding_request_builder')
certificate_based_auth_configuration_request_builder = lazy_import('msgraph.generated.certificate_based_auth_configuration.certificate_based_auth_configuration_request_builder')
certificate_based_auth_configuration_item_request_builder = lazy_import('msgraph.generated.certificate_based_auth_configuration.item.certificate_based_auth_configuration_item_request_builder')
chats_request_builder = lazy_import('msgraph.generated.chats.chats_request_builder')
chat_item_request_builder = lazy_import('msgraph.generated.chats.item.chat_item_request_builder')
communications_request_builder = lazy_import('msgraph.generated.communications.communications_request_builder')
compliance_request_builder = lazy_import('msgraph.generated.compliance.compliance_request_builder')
connections_request_builder = lazy_import('msgraph.generated.connections.connections_request_builder')
external_connection_item_request_builder = lazy_import('msgraph.generated.connections.item.external_connection_item_request_builder')
contacts_request_builder = lazy_import('msgraph.generated.contacts.contacts_request_builder')
org_contact_item_request_builder = lazy_import('msgraph.generated.contacts.item.org_contact_item_request_builder')
contracts_request_builder = lazy_import('msgraph.generated.contracts.contracts_request_builder')
contract_item_request_builder = lazy_import('msgraph.generated.contracts.item.contract_item_request_builder')
data_policy_operations_request_builder = lazy_import('msgraph.generated.data_policy_operations.data_policy_operations_request_builder')
data_policy_operation_item_request_builder = lazy_import('msgraph.generated.data_policy_operations.item.data_policy_operation_item_request_builder')
device_app_management_request_builder = lazy_import('msgraph.generated.device_app_management.device_app_management_request_builder')
device_management_request_builder = lazy_import('msgraph.generated.device_management.device_management_request_builder')
devices_request_builder = lazy_import('msgraph.generated.devices.devices_request_builder')
device_item_request_builder = lazy_import('msgraph.generated.devices.item.device_item_request_builder')
directory_request_builder = lazy_import('msgraph.generated.directory.directory_request_builder')
directory_objects_request_builder = lazy_import('msgraph.generated.directory_objects.directory_objects_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.directory_objects.item.directory_object_item_request_builder')
directory_roles_request_builder = lazy_import('msgraph.generated.directory_roles.directory_roles_request_builder')
directory_role_item_request_builder = lazy_import('msgraph.generated.directory_roles.item.directory_role_item_request_builder')
directory_role_templates_request_builder = lazy_import('msgraph.generated.directory_role_templates.directory_role_templates_request_builder')
directory_role_template_item_request_builder = lazy_import('msgraph.generated.directory_role_templates.item.directory_role_template_item_request_builder')
domain_dns_records_request_builder = lazy_import('msgraph.generated.domain_dns_records.domain_dns_records_request_builder')
domain_dns_record_item_request_builder = lazy_import('msgraph.generated.domain_dns_records.item.domain_dns_record_item_request_builder')
domains_request_builder = lazy_import('msgraph.generated.domains.domains_request_builder')
domain_item_request_builder = lazy_import('msgraph.generated.domains.item.domain_item_request_builder')
drive_request_builder = lazy_import('msgraph.generated.drive.drive_request_builder')
drives_request_builder = lazy_import('msgraph.generated.drives.drives_request_builder')
drive_item_request_builder = lazy_import('msgraph.generated.drives.item.drive_item_request_builder')
education_request_builder = lazy_import('msgraph.generated.education.education_request_builder')
external_request_builder = lazy_import('msgraph.generated.external.external_request_builder')
group_lifecycle_policies_request_builder = lazy_import('msgraph.generated.group_lifecycle_policies.group_lifecycle_policies_request_builder')
group_lifecycle_policy_item_request_builder = lazy_import('msgraph.generated.group_lifecycle_policies.item.group_lifecycle_policy_item_request_builder')
groups_request_builder = lazy_import('msgraph.generated.groups.groups_request_builder')
group_item_request_builder = lazy_import('msgraph.generated.groups.item.group_item_request_builder')
group_settings_request_builder = lazy_import('msgraph.generated.group_settings.group_settings_request_builder')
group_setting_item_request_builder = lazy_import('msgraph.generated.group_settings.item.group_setting_item_request_builder')
group_setting_templates_request_builder = lazy_import('msgraph.generated.group_setting_templates.group_setting_templates_request_builder')
group_setting_template_item_request_builder = lazy_import('msgraph.generated.group_setting_templates.item.group_setting_template_item_request_builder')
identity_request_builder = lazy_import('msgraph.generated.identity.identity_request_builder')
identity_governance_request_builder = lazy_import('msgraph.generated.identity_governance.identity_governance_request_builder')
identity_protection_request_builder = lazy_import('msgraph.generated.identity_protection.identity_protection_request_builder')
identity_providers_request_builder = lazy_import('msgraph.generated.identity_providers.identity_providers_request_builder')
identity_provider_item_request_builder = lazy_import('msgraph.generated.identity_providers.item.identity_provider_item_request_builder')
information_protection_request_builder = lazy_import('msgraph.generated.information_protection.information_protection_request_builder')
invitations_request_builder = lazy_import('msgraph.generated.invitations.invitations_request_builder')
invitation_item_request_builder = lazy_import('msgraph.generated.invitations.item.invitation_item_request_builder')
localizations_request_builder = lazy_import('msgraph.generated.localizations.localizations_request_builder')
organizational_branding_localization_item_request_builder = lazy_import('msgraph.generated.localizations.item.organizational_branding_localization_item_request_builder')
me_request_builder = lazy_import('msgraph.generated.me.me_request_builder')
oauth2_permission_grants_request_builder = lazy_import('msgraph.generated.oauth2_permission_grants.oauth2_permission_grants_request_builder')
o_auth2_permission_grant_item_request_builder = lazy_import('msgraph.generated.oauth2_permission_grants.item.o_auth2_permission_grant_item_request_builder')
organization_request_builder = lazy_import('msgraph.generated.organization.organization_request_builder')
organization_item_request_builder = lazy_import('msgraph.generated.organization.item.organization_item_request_builder')
permission_grants_request_builder = lazy_import('msgraph.generated.permission_grants.permission_grants_request_builder')
resource_specific_permission_grant_item_request_builder = lazy_import('msgraph.generated.permission_grants.item.resource_specific_permission_grant_item_request_builder')
places_request_builder = lazy_import('msgraph.generated.places.places_request_builder')
place_item_request_builder = lazy_import('msgraph.generated.places.item.place_item_request_builder')
planner_request_builder = lazy_import('msgraph.generated.planner.planner_request_builder')
policies_request_builder = lazy_import('msgraph.generated.policies.policies_request_builder')
print_request_builder = lazy_import('msgraph.generated.print.print_request_builder')
privacy_request_builder = lazy_import('msgraph.generated.privacy.privacy_request_builder')
reports_request_builder = lazy_import('msgraph.generated.reports.reports_request_builder')
role_management_request_builder = lazy_import('msgraph.generated.role_management.role_management_request_builder')
schema_extensions_request_builder = lazy_import('msgraph.generated.schema_extensions.schema_extensions_request_builder')
schema_extension_item_request_builder = lazy_import('msgraph.generated.schema_extensions.item.schema_extension_item_request_builder')
scoped_role_memberships_request_builder = lazy_import('msgraph.generated.scoped_role_memberships.scoped_role_memberships_request_builder')
scoped_role_membership_item_request_builder = lazy_import('msgraph.generated.scoped_role_memberships.item.scoped_role_membership_item_request_builder')
search_request_builder = lazy_import('msgraph.generated.search.search_request_builder')
security_request_builder = lazy_import('msgraph.generated.security.security_request_builder')
service_principals_request_builder = lazy_import('msgraph.generated.service_principals.service_principals_request_builder')
service_principal_item_request_builder = lazy_import('msgraph.generated.service_principals.item.service_principal_item_request_builder')
shares_request_builder = lazy_import('msgraph.generated.shares.shares_request_builder')
shared_drive_item_item_request_builder = lazy_import('msgraph.generated.shares.item.shared_drive_item_item_request_builder')
sites_request_builder = lazy_import('msgraph.generated.sites.sites_request_builder')
site_item_request_builder = lazy_import('msgraph.generated.sites.item.site_item_request_builder')
solutions_request_builder = lazy_import('msgraph.generated.solutions.solutions_request_builder')
subscribed_skus_request_builder = lazy_import('msgraph.generated.subscribed_skus.subscribed_skus_request_builder')
subscribed_sku_item_request_builder = lazy_import('msgraph.generated.subscribed_skus.item.subscribed_sku_item_request_builder')
subscriptions_request_builder = lazy_import('msgraph.generated.subscriptions.subscriptions_request_builder')
subscription_item_request_builder = lazy_import('msgraph.generated.subscriptions.item.subscription_item_request_builder')
teams_request_builder = lazy_import('msgraph.generated.teams.teams_request_builder')
team_item_request_builder = lazy_import('msgraph.generated.teams.item.team_item_request_builder')
teams_templates_request_builder = lazy_import('msgraph.generated.teams_templates.teams_templates_request_builder')
teams_template_item_request_builder = lazy_import('msgraph.generated.teams_templates.item.teams_template_item_request_builder')
teamwork_request_builder = lazy_import('msgraph.generated.teamwork.teamwork_request_builder')
users_request_builder = lazy_import('msgraph.generated.users.users_request_builder')
user_item_request_builder = lazy_import('msgraph.generated.users.item.user_item_request_builder')
workbooks_request_builder = lazy_import('msgraph.generated.workbooks.workbooks_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.workbooks.item.drive_item_item_request_builder')

class BaseGraphServiceClient():
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def admin(self) -> admin_request_builder.AdminRequestBuilder:
        """
        Provides operations to manage the admin singleton.
        """
        return admin_request_builder.AdminRequestBuilder(self.request_adapter, self.path_parameters)
    
    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        """
        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def agreements(self) -> agreements_request_builder.AgreementsRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        """
        return agreements_request_builder.AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def app_catalogs(self) -> app_catalogs_request_builder.AppCatalogsRequestBuilder:
        """
        Provides operations to manage the appCatalogs singleton.
        """
        return app_catalogs_request_builder.AppCatalogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def applications(self) -> applications_request_builder.ApplicationsRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        """
        return applications_request_builder.ApplicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def application_templates(self) -> application_templates_request_builder.ApplicationTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of applicationTemplate entities.
        """
        return application_templates_request_builder.ApplicationTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def audit_logs(self) -> audit_logs_request_builder.AuditLogsRequestBuilder:
        """
        Provides operations to manage the auditLogRoot singleton.
        """
        return audit_logs_request_builder.AuditLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def authentication_method_configurations(self) -> authentication_method_configurations_request_builder.AuthenticationMethodConfigurationsRequestBuilder:
        """
        Provides operations to manage the collection of authenticationMethodConfiguration entities.
        """
        return authentication_method_configurations_request_builder.AuthenticationMethodConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def authentication_methods_policy(self) -> authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy singleton.
        """
        return authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def branding(self) -> branding_request_builder.BrandingRequestBuilder:
        """
        Provides operations to manage the organizationalBranding singleton.
        """
        return branding_request_builder.BrandingRequestBuilder(self.request_adapter, self.path_parameters)
    
    def certificate_based_auth_configuration(self) -> certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder:
        """
        Provides operations to manage the collection of certificateBasedAuthConfiguration entities.
        """
        return certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def chats(self) -> chats_request_builder.ChatsRequestBuilder:
        """
        Provides operations to manage the collection of chat entities.
        """
        return chats_request_builder.ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def communications(self) -> communications_request_builder.CommunicationsRequestBuilder:
        """
        Provides operations to manage the cloudCommunications singleton.
        """
        return communications_request_builder.CommunicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def compliance(self) -> compliance_request_builder.ComplianceRequestBuilder:
        """
        Provides operations to manage the compliance singleton.
        """
        return compliance_request_builder.ComplianceRequestBuilder(self.request_adapter, self.path_parameters)
    
    def connections(self) -> connections_request_builder.ConnectionsRequestBuilder:
        """
        Provides operations to manage the collection of externalConnection entities.
        """
        return connections_request_builder.ConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def contacts(self) -> contacts_request_builder.ContactsRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        """
        return contacts_request_builder.ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def contracts(self) -> contracts_request_builder.ContractsRequestBuilder:
        """
        Provides operations to manage the collection of contract entities.
        """
        return contracts_request_builder.ContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def data_policy_operations(self) -> data_policy_operations_request_builder.DataPolicyOperationsRequestBuilder:
        """
        Provides operations to manage the collection of dataPolicyOperation entities.
        """
        return data_policy_operations_request_builder.DataPolicyOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def device_app_management(self) -> device_app_management_request_builder.DeviceAppManagementRequestBuilder:
        """
        Provides operations to manage the deviceAppManagement singleton.
        """
        return device_app_management_request_builder.DeviceAppManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    def device_management(self) -> device_management_request_builder.DeviceManagementRequestBuilder:
        """
        Provides operations to manage the deviceManagement singleton.
        """
        return device_management_request_builder.DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    def devices(self) -> devices_request_builder.DevicesRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        """
        return devices_request_builder.DevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def directory(self) -> directory_request_builder.DirectoryRequestBuilder:
        """
        Provides operations to manage the directory singleton.
        """
        return directory_request_builder.DirectoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    def directory_objects(self) -> directory_objects_request_builder.DirectoryObjectsRequestBuilder:
        """
        Provides operations to manage the collection of directoryObject entities.
        """
        return directory_objects_request_builder.DirectoryObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def directory_roles(self) -> directory_roles_request_builder.DirectoryRolesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        """
        return directory_roles_request_builder.DirectoryRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def directory_role_templates(self) -> directory_role_templates_request_builder.DirectoryRoleTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRoleTemplate entities.
        """
        return directory_role_templates_request_builder.DirectoryRoleTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def domain_dns_records(self) -> domain_dns_records_request_builder.DomainDnsRecordsRequestBuilder:
        """
        Provides operations to manage the collection of domainDnsRecord entities.
        """
        return domain_dns_records_request_builder.DomainDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def domains(self) -> domains_request_builder.DomainsRequestBuilder:
        """
        Provides operations to manage the collection of domain entities.
        """
        return domains_request_builder.DomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive singleton.
        """
        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the collection of drive entities.
        """
        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def education(self) -> education_request_builder.EducationRequestBuilder:
        """
        Provides operations to manage the educationRoot singleton.
        """
        return education_request_builder.EducationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def external(self) -> external_request_builder.ExternalRequestBuilder:
        """
        Provides operations to manage the external singleton.
        """
        return external_request_builder.ExternalRequestBuilder(self.request_adapter, self.path_parameters)
    
    def group_lifecycle_policies(self) -> group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder:
        """
        Provides operations to manage the collection of groupLifecyclePolicy entities.
        """
        return group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def groups(self) -> groups_request_builder.GroupsRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        """
        return groups_request_builder.GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def group_settings(self) -> group_settings_request_builder.GroupSettingsRequestBuilder:
        """
        Provides operations to manage the collection of groupSetting entities.
        """
        return group_settings_request_builder.GroupSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def group_setting_templates(self) -> group_setting_templates_request_builder.GroupSettingTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of groupSettingTemplate entities.
        """
        return group_setting_templates_request_builder.GroupSettingTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def identity(self) -> identity_request_builder.IdentityRequestBuilder:
        """
        Provides operations to manage the identityContainer singleton.
        """
        return identity_request_builder.IdentityRequestBuilder(self.request_adapter, self.path_parameters)
    
    def identity_governance(self) -> identity_governance_request_builder.IdentityGovernanceRequestBuilder:
        """
        Provides operations to manage the identityGovernance singleton.
        """
        return identity_governance_request_builder.IdentityGovernanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    def identity_protection(self) -> identity_protection_request_builder.IdentityProtectionRequestBuilder:
        """
        Provides operations to manage the identityProtectionRoot singleton.
        """
        return identity_protection_request_builder.IdentityProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def identity_providers(self) -> identity_providers_request_builder.IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the collection of identityProvider entities.
        """
        return identity_providers_request_builder.IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def information_protection(self) -> information_protection_request_builder.InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection singleton.
        """
        return information_protection_request_builder.InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def invitations(self) -> invitations_request_builder.InvitationsRequestBuilder:
        """
        Provides operations to manage the collection of invitation entities.
        """
        return invitations_request_builder.InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def localizations(self) -> localizations_request_builder.LocalizationsRequestBuilder:
        """
        Provides operations to manage the collection of organizationalBrandingLocalization entities.
        """
        return localizations_request_builder.LocalizationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def me(self) -> me_request_builder.MeRequestBuilder:
        """
        Provides operations to manage the user singleton.
        """
        return me_request_builder.MeRequestBuilder(self.request_adapter, self.path_parameters)
    
    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of oAuth2PermissionGrant entities.
        """
        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def organization(self) -> organization_request_builder.OrganizationRequestBuilder:
        """
        Provides operations to manage the collection of organization entities.
        """
        return organization_request_builder.OrganizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def permission_grants(self) -> permission_grants_request_builder.PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        """
        return permission_grants_request_builder.PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def places(self) -> places_request_builder.PlacesRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        """
        return places_request_builder.PlacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner singleton.
        """
        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    def policies(self) -> policies_request_builder.PoliciesRequestBuilder:
        """
        Provides operations to manage the policyRoot singleton.
        """
        return policies_request_builder.PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def print(self) -> print_request_builder.PrintRequestBuilder:
        """
        Provides operations to manage the print singleton.
        """
        return print_request_builder.PrintRequestBuilder(self.request_adapter, self.path_parameters)
    
    def privacy(self) -> privacy_request_builder.PrivacyRequestBuilder:
        """
        Provides operations to manage the privacy singleton.
        """
        return privacy_request_builder.PrivacyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reportRoot singleton.
        """
        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_management(self) -> role_management_request_builder.RoleManagementRequestBuilder:
        """
        Provides operations to manage the roleManagement singleton.
        """
        return role_management_request_builder.RoleManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    def schema_extensions(self) -> schema_extensions_request_builder.SchemaExtensionsRequestBuilder:
        """
        Provides operations to manage the collection of schemaExtension entities.
        """
        return schema_extensions_request_builder.SchemaExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def scoped_role_memberships(self) -> scoped_role_memberships_request_builder.ScopedRoleMembershipsRequestBuilder:
        """
        Provides operations to manage the collection of scopedRoleMembership entities.
        """
        return scoped_role_memberships_request_builder.ScopedRoleMembershipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def search(self) -> search_request_builder.SearchRequestBuilder:
        """
        Provides operations to manage the searchEntity singleton.
        """
        return search_request_builder.SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    def security(self) -> security_request_builder.SecurityRequestBuilder:
        """
        Provides operations to manage the security singleton.
        """
        return security_request_builder.SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    def service_principals(self) -> service_principals_request_builder.ServicePrincipalsRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        """
        return service_principals_request_builder.ServicePrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def shares(self) -> shares_request_builder.SharesRequestBuilder:
        """
        Provides operations to manage the collection of sharedDriveItem entities.
        """
        return shares_request_builder.SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the collection of site entities.
        """
        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def solutions(self) -> solutions_request_builder.SolutionsRequestBuilder:
        """
        Provides operations to manage the solutionsRoot singleton.
        """
        return solutions_request_builder.SolutionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def subscribed_skus(self) -> subscribed_skus_request_builder.SubscribedSkusRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        """
        return subscribed_skus_request_builder.SubscribedSkusRequestBuilder(self.request_adapter, self.path_parameters)
    
    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the collection of subscription entities.
        """
        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def teams(self) -> teams_request_builder.TeamsRequestBuilder:
        """
        Provides operations to manage the collection of team entities.
        """
        return teams_request_builder.TeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def teams_templates(self) -> teams_templates_request_builder.TeamsTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of teamsTemplate entities.
        """
        return teams_templates_request_builder.TeamsTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def teamwork(self) -> teamwork_request_builder.TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork singleton.
        """
        return teamwork_request_builder.TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        """
        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def workbooks(self) -> workbooks_request_builder.WorkbooksRequestBuilder:
        """
        Provides operations to manage the collection of driveItem entities.
        """
        return workbooks_request_builder.WorkbooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    def agreement_acceptances_by_id(self,id: str) -> agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        Args:
            id: Unique identifier of the item
        Returns: agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementAcceptance%2Did"] = id
        return agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def agreements_by_id(self,id: str) -> agreement_item_request_builder.AgreementItemRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        Args:
            id: Unique identifier of the item
        Returns: agreement_item_request_builder.AgreementItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreement%2Did"] = id
        return agreement_item_request_builder.AgreementItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def applications_by_id(self,id: str) -> application_item_request_builder.ApplicationItemRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        Args:
            id: Unique identifier of the item
        Returns: application_item_request_builder.ApplicationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["application%2Did"] = id
        return application_item_request_builder.ApplicationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def application_templates_by_id(self,id: str) -> application_template_item_request_builder.ApplicationTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of applicationTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: application_template_item_request_builder.ApplicationTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["applicationTemplate%2Did"] = id
        return application_template_item_request_builder.ApplicationTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def authentication_method_configurations_by_id(self,id: str) -> authentication_method_configuration_item_request_builder.AuthenticationMethodConfigurationItemRequestBuilder:
        """
        Provides operations to manage the collection of authenticationMethodConfiguration entities.
        Args:
            id: Unique identifier of the item
        Returns: authentication_method_configuration_item_request_builder.AuthenticationMethodConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationMethodConfiguration%2Did"] = id
        return authentication_method_configuration_item_request_builder.AuthenticationMethodConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def certificate_based_auth_configuration_by_id(self,id: str) -> certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder:
        """
        Provides operations to manage the collection of certificateBasedAuthConfiguration entities.
        Args:
            id: Unique identifier of the item
        Returns: certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["certificateBasedAuthConfiguration%2Did"] = id
        return certificate_based_auth_configuration_item_request_builder.CertificateBasedAuthConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def chats_by_id(self,id: str) -> chat_item_request_builder.ChatItemRequestBuilder:
        """
        Provides operations to manage the collection of chat entities.
        Args:
            id: Unique identifier of the item
        Returns: chat_item_request_builder.ChatItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chat%2Did"] = id
        return chat_item_request_builder.ChatItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def connections_by_id(self,id: str) -> external_connection_item_request_builder.ExternalConnectionItemRequestBuilder:
        """
        Provides operations to manage the collection of externalConnection entities.
        Args:
            id: Unique identifier of the item
        Returns: external_connection_item_request_builder.ExternalConnectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["externalConnection%2Did"] = id
        return external_connection_item_request_builder.ExternalConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new BaseGraphServiceClient and sets the default values.
        Args:
            requestAdapter: The request adapter to use to execute the requests.
        """
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Path parameters for the request
        self.path_parameters: Dict[str, Any] = {}

        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}"

        self.request_adapter = request_adapter
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        if not request_adapter.base_url:
            request_adapter.base_url = "https://graph.microsoft.com/v1.0"
    
    def contacts_by_id(self,id: str) -> org_contact_item_request_builder.OrgContactItemRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        Args:
            id: Unique identifier of the item
        Returns: org_contact_item_request_builder.OrgContactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["orgContact%2Did"] = id
        return org_contact_item_request_builder.OrgContactItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def contracts_by_id(self,id: str) -> contract_item_request_builder.ContractItemRequestBuilder:
        """
        Provides operations to manage the collection of contract entities.
        Args:
            id: Unique identifier of the item
        Returns: contract_item_request_builder.ContractItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contract%2Did"] = id
        return contract_item_request_builder.ContractItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def data_policy_operations_by_id(self,id: str) -> data_policy_operation_item_request_builder.DataPolicyOperationItemRequestBuilder:
        """
        Provides operations to manage the collection of dataPolicyOperation entities.
        Args:
            id: Unique identifier of the item
        Returns: data_policy_operation_item_request_builder.DataPolicyOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dataPolicyOperation%2Did"] = id
        return data_policy_operation_item_request_builder.DataPolicyOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def devices_by_id(self,id: str) -> device_item_request_builder.DeviceItemRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        Args:
            id: Unique identifier of the item
        Returns: device_item_request_builder.DeviceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["device%2Did"] = id
        return device_item_request_builder.DeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_objects_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the collection of directoryObject entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_roles_by_id(self,id: str) -> directory_role_item_request_builder.DirectoryRoleItemRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_role_item_request_builder.DirectoryRoleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryRole%2Did"] = id
        return directory_role_item_request_builder.DirectoryRoleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def directory_role_templates_by_id(self,id: str) -> directory_role_template_item_request_builder.DirectoryRoleTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of directoryRoleTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: directory_role_template_item_request_builder.DirectoryRoleTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryRoleTemplate%2Did"] = id
        return directory_role_template_item_request_builder.DirectoryRoleTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def domain_dns_records_by_id(self,id: str) -> domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder:
        """
        Provides operations to manage the collection of domainDnsRecord entities.
        Args:
            id: Unique identifier of the item
        Returns: domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domainDnsRecord%2Did"] = id
        return domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def domains_by_id(self,id: str) -> domain_item_request_builder.DomainItemRequestBuilder:
        """
        Provides operations to manage the collection of domain entities.
        Args:
            id: Unique identifier of the item
        Returns: domain_item_request_builder.DomainItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domain%2Did"] = id
        return domain_item_request_builder.DomainItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def drives_by_id(self,id: str) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the collection of drive entities.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_request_builder.DriveItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["drive%2Did"] = id
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_lifecycle_policies_by_id(self,id: str) -> group_lifecycle_policy_item_request_builder.GroupLifecyclePolicyItemRequestBuilder:
        """
        Provides operations to manage the collection of groupLifecyclePolicy entities.
        Args:
            id: Unique identifier of the item
        Returns: group_lifecycle_policy_item_request_builder.GroupLifecyclePolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupLifecyclePolicy%2Did"] = id
        return group_lifecycle_policy_item_request_builder.GroupLifecyclePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def groups_by_id(self,id: str) -> group_item_request_builder.GroupItemRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        Args:
            id: Unique identifier of the item
        Returns: group_item_request_builder.GroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["group%2Did"] = id
        return group_item_request_builder.GroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_settings_by_id(self,id: str) -> group_setting_item_request_builder.GroupSettingItemRequestBuilder:
        """
        Provides operations to manage the collection of groupSetting entities.
        Args:
            id: Unique identifier of the item
        Returns: group_setting_item_request_builder.GroupSettingItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupSetting%2Did"] = id
        return group_setting_item_request_builder.GroupSettingItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def group_setting_templates_by_id(self,id: str) -> group_setting_template_item_request_builder.GroupSettingTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of groupSettingTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: group_setting_template_item_request_builder.GroupSettingTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupSettingTemplate%2Did"] = id
        return group_setting_template_item_request_builder.GroupSettingTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def identity_providers_by_id(self,id: str) -> identity_provider_item_request_builder.IdentityProviderItemRequestBuilder:
        """
        Provides operations to manage the collection of identityProvider entities.
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_item_request_builder.IdentityProviderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProvider%2Did"] = id
        return identity_provider_item_request_builder.IdentityProviderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def invitations_by_id(self,id: str) -> invitation_item_request_builder.InvitationItemRequestBuilder:
        """
        Provides operations to manage the collection of invitation entities.
        Args:
            id: Unique identifier of the item
        Returns: invitation_item_request_builder.InvitationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["invitation%2Did"] = id
        return invitation_item_request_builder.InvitationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def localizations_by_id(self,id: str) -> organizational_branding_localization_item_request_builder.OrganizationalBrandingLocalizationItemRequestBuilder:
        """
        Provides operations to manage the collection of organizationalBrandingLocalization entities.
        Args:
            id: Unique identifier of the item
        Returns: organizational_branding_localization_item_request_builder.OrganizationalBrandingLocalizationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["organizationalBrandingLocalization%2Did"] = id
        return organizational_branding_localization_item_request_builder.OrganizationalBrandingLocalizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def oauth2_permission_grants_by_id(self,id: str) -> o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the collection of oAuth2PermissionGrant entities.
        Args:
            id: Unique identifier of the item
        Returns: o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["oAuth2PermissionGrant%2Did"] = id
        return o_auth2_permission_grant_item_request_builder.OAuth2PermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def organization_by_id(self,id: str) -> organization_item_request_builder.OrganizationItemRequestBuilder:
        """
        Provides operations to manage the collection of organization entities.
        Args:
            id: Unique identifier of the item
        Returns: organization_item_request_builder.OrganizationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["organization%2Did"] = id
        return organization_item_request_builder.OrganizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def permission_grants_by_id(self,id: str) -> resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        Args:
            id: Unique identifier of the item
        Returns: resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceSpecificPermissionGrant%2Did"] = id
        return resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def places_by_id(self,id: str) -> place_item_request_builder.PlaceItemRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        Args:
            id: Unique identifier of the item
        Returns: place_item_request_builder.PlaceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["place%2Did"] = id
        return place_item_request_builder.PlaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def schema_extensions_by_id(self,id: str) -> schema_extension_item_request_builder.SchemaExtensionItemRequestBuilder:
        """
        Provides operations to manage the collection of schemaExtension entities.
        Args:
            id: Unique identifier of the item
        Returns: schema_extension_item_request_builder.SchemaExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["schemaExtension%2Did"] = id
        return schema_extension_item_request_builder.SchemaExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def scoped_role_memberships_by_id(self,id: str) -> scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder:
        """
        Provides operations to manage the collection of scopedRoleMembership entities.
        Args:
            id: Unique identifier of the item
        Returns: scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["scopedRoleMembership%2Did"] = id
        return scoped_role_membership_item_request_builder.ScopedRoleMembershipItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def service_principals_by_id(self,id: str) -> service_principal_item_request_builder.ServicePrincipalItemRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        Args:
            id: Unique identifier of the item
        Returns: service_principal_item_request_builder.ServicePrincipalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["servicePrincipal%2Did"] = id
        return service_principal_item_request_builder.ServicePrincipalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def shares_by_id(self,id: str) -> shared_drive_item_item_request_builder.SharedDriveItemItemRequestBuilder:
        """
        Provides operations to manage the collection of sharedDriveItem entities.
        Args:
            id: Unique identifier of the item
        Returns: shared_drive_item_item_request_builder.SharedDriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sharedDriveItem%2Did"] = id
        return shared_drive_item_item_request_builder.SharedDriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sites_by_id(self,id: str) -> site_item_request_builder.SiteItemRequestBuilder:
        """
        Provides operations to manage the collection of site entities.
        Args:
            id: Unique identifier of the item
        Returns: site_item_request_builder.SiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["site%2Did"] = id
        return site_item_request_builder.SiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def subscribed_skus_by_id(self,id: str) -> subscribed_sku_item_request_builder.SubscribedSkuItemRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        Args:
            id: Unique identifier of the item
        Returns: subscribed_sku_item_request_builder.SubscribedSkuItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscribedSku%2Did"] = id
        return subscribed_sku_item_request_builder.SubscribedSkuItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def subscriptions_by_id(self,id: str) -> subscription_item_request_builder.SubscriptionItemRequestBuilder:
        """
        Provides operations to manage the collection of subscription entities.
        Args:
            id: Unique identifier of the item
        Returns: subscription_item_request_builder.SubscriptionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscription%2Did"] = id
        return subscription_item_request_builder.SubscriptionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def teams_by_id(self,id: str) -> team_item_request_builder.TeamItemRequestBuilder:
        """
        Provides operations to manage the collection of team entities.
        Args:
            id: Unique identifier of the item
        Returns: team_item_request_builder.TeamItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["team%2Did"] = id
        return team_item_request_builder.TeamItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def teams_templates_by_id(self,id: str) -> teams_template_item_request_builder.TeamsTemplateItemRequestBuilder:
        """
        Provides operations to manage the collection of teamsTemplate entities.
        Args:
            id: Unique identifier of the item
        Returns: teams_template_item_request_builder.TeamsTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsTemplate%2Did"] = id
        return teams_template_item_request_builder.TeamsTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def users_by_id(self,id: str) -> user_item_request_builder.UserItemRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        Args:
            id: Unique identifier of the item
        Returns: user_item_request_builder.UserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["user%2Did"] = id
        return user_item_request_builder.UserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def workbooks_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the collection of driveItem entities.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    

