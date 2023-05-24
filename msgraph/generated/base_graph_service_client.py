from __future__ import annotations
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin import admin_request_builder
    from .agreement_acceptances import agreement_acceptances_request_builder
    from .agreements import agreements_request_builder
    from .app_catalogs import app_catalogs_request_builder
    from .applications import applications_request_builder
    from .application_templates import application_templates_request_builder
    from .audit_logs import audit_logs_request_builder
    from .authentication_method_configurations import authentication_method_configurations_request_builder
    from .authentication_methods_policy import authentication_methods_policy_request_builder
    from .branding import branding_request_builder
    from .certificate_based_auth_configuration import certificate_based_auth_configuration_request_builder
    from .chats import chats_request_builder
    from .communications import communications_request_builder
    from .compliance import compliance_request_builder
    from .connections import connections_request_builder
    from .contacts import contacts_request_builder
    from .contracts import contracts_request_builder
    from .data_policy_operations import data_policy_operations_request_builder
    from .device_app_management import device_app_management_request_builder
    from .device_management import device_management_request_builder
    from .devices import devices_request_builder
    from .directory import directory_request_builder
    from .directory_objects import directory_objects_request_builder
    from .directory_roles import directory_roles_request_builder
    from .directory_role_templates import directory_role_templates_request_builder
    from .domain_dns_records import domain_dns_records_request_builder
    from .domains import domains_request_builder
    from .drives import drives_request_builder
    from .education import education_request_builder
    from .employee_experience import employee_experience_request_builder
    from .external import external_request_builder
    from .filter_operators import filter_operators_request_builder
    from .functions import functions_request_builder
    from .group_lifecycle_policies import group_lifecycle_policies_request_builder
    from .groups import groups_request_builder
    from .group_settings import group_settings_request_builder
    from .group_setting_templates import group_setting_templates_request_builder
    from .identity import identity_request_builder
    from .identity_governance import identity_governance_request_builder
    from .identity_protection import identity_protection_request_builder
    from .identity_providers import identity_providers_request_builder
    from .information_protection import information_protection_request_builder
    from .invitations import invitations_request_builder
    from .localizations import localizations_request_builder
    from .me import me_request_builder
    from .oauth2_permission_grants import oauth2_permission_grants_request_builder
    from .organization import organization_request_builder
    from .permission_grants import permission_grants_request_builder
    from .places import places_request_builder
    from .planner import planner_request_builder
    from .policies import policies_request_builder
    from .print import print_request_builder
    from .privacy import privacy_request_builder
    from .reports import reports_request_builder
    from .role_management import role_management_request_builder
    from .schema_extensions import schema_extensions_request_builder
    from .scoped_role_memberships import scoped_role_memberships_request_builder
    from .search import search_request_builder
    from .security import security_request_builder
    from .service_principals import service_principals_request_builder
    from .shares import shares_request_builder
    from .sites import sites_request_builder
    from .solutions import solutions_request_builder
    from .subscribed_skus import subscribed_skus_request_builder
    from .subscriptions import subscriptions_request_builder
    from .teams import teams_request_builder
    from .teams_templates import teams_templates_request_builder
    from .teamwork import teamwork_request_builder
    from .tenant_relationships import tenant_relationships_request_builder
    from .users import users_request_builder

class BaseGraphServiceClient():
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
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
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://graph.microsoft.com/v1.0"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def admin(self) -> admin_request_builder.AdminRequestBuilder:
        """
        Provides operations to manage the admin singleton.
        """
        from .admin import admin_request_builder

        return admin_request_builder.AdminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        """
        from .agreement_acceptances import agreement_acceptances_request_builder

        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreements(self) -> agreements_request_builder.AgreementsRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        """
        from .agreements import agreements_request_builder

        return agreements_request_builder.AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_catalogs(self) -> app_catalogs_request_builder.AppCatalogsRequestBuilder:
        """
        Provides operations to manage the appCatalogs singleton.
        """
        from .app_catalogs import app_catalogs_request_builder

        return app_catalogs_request_builder.AppCatalogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def applications(self) -> applications_request_builder.ApplicationsRequestBuilder:
        """
        Provides operations to manage the collection of application entities.
        """
        from .applications import applications_request_builder

        return applications_request_builder.ApplicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def application_templates(self) -> application_templates_request_builder.ApplicationTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of applicationTemplate entities.
        """
        from .application_templates import application_templates_request_builder

        return application_templates_request_builder.ApplicationTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_logs(self) -> audit_logs_request_builder.AuditLogsRequestBuilder:
        """
        Provides operations to manage the auditLogRoot singleton.
        """
        from .audit_logs import audit_logs_request_builder

        return audit_logs_request_builder.AuditLogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_method_configurations(self) -> authentication_method_configurations_request_builder.AuthenticationMethodConfigurationsRequestBuilder:
        """
        Provides operations to manage the collection of authenticationMethodConfiguration entities.
        """
        from .authentication_method_configurations import authentication_method_configurations_request_builder

        return authentication_method_configurations_request_builder.AuthenticationMethodConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_methods_policy(self) -> authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder:
        """
        Provides operations to manage the authenticationMethodsPolicy singleton.
        """
        from .authentication_methods_policy import authentication_methods_policy_request_builder

        return authentication_methods_policy_request_builder.AuthenticationMethodsPolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def branding(self) -> branding_request_builder.BrandingRequestBuilder:
        """
        Provides operations to manage the organizationalBranding singleton.
        """
        from .branding import branding_request_builder

        return branding_request_builder.BrandingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def certificate_based_auth_configuration(self) -> certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder:
        """
        Provides operations to manage the collection of certificateBasedAuthConfiguration entities.
        """
        from .certificate_based_auth_configuration import certificate_based_auth_configuration_request_builder

        return certificate_based_auth_configuration_request_builder.CertificateBasedAuthConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> chats_request_builder.ChatsRequestBuilder:
        """
        Provides operations to manage the collection of chat entities.
        """
        from .chats import chats_request_builder

        return chats_request_builder.ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def communications(self) -> communications_request_builder.CommunicationsRequestBuilder:
        """
        Provides operations to manage the cloudCommunications singleton.
        """
        from .communications import communications_request_builder

        return communications_request_builder.CommunicationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance(self) -> compliance_request_builder.ComplianceRequestBuilder:
        """
        Provides operations to manage the compliance singleton.
        """
        from .compliance import compliance_request_builder

        return compliance_request_builder.ComplianceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connections(self) -> connections_request_builder.ConnectionsRequestBuilder:
        """
        Provides operations to manage the collection of externalConnection entities.
        """
        from .connections import connections_request_builder

        return connections_request_builder.ConnectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> contacts_request_builder.ContactsRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        """
        from .contacts import contacts_request_builder

        return contacts_request_builder.ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contracts(self) -> contracts_request_builder.ContractsRequestBuilder:
        """
        Provides operations to manage the collection of contract entities.
        """
        from .contracts import contracts_request_builder

        return contracts_request_builder.ContractsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_policy_operations(self) -> data_policy_operations_request_builder.DataPolicyOperationsRequestBuilder:
        """
        Provides operations to manage the collection of dataPolicyOperation entities.
        """
        from .data_policy_operations import data_policy_operations_request_builder

        return data_policy_operations_request_builder.DataPolicyOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_app_management(self) -> device_app_management_request_builder.DeviceAppManagementRequestBuilder:
        """
        Provides operations to manage the deviceAppManagement singleton.
        """
        from .device_app_management import device_app_management_request_builder

        return device_app_management_request_builder.DeviceAppManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management(self) -> device_management_request_builder.DeviceManagementRequestBuilder:
        """
        Provides operations to manage the deviceManagement singleton.
        """
        from .device_management import device_management_request_builder

        return device_management_request_builder.DeviceManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def devices(self) -> devices_request_builder.DevicesRequestBuilder:
        """
        Provides operations to manage the collection of device entities.
        """
        from .devices import devices_request_builder

        return devices_request_builder.DevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory(self) -> directory_request_builder.DirectoryRequestBuilder:
        """
        Provides operations to manage the directory singleton.
        """
        from .directory import directory_request_builder

        return directory_request_builder.DirectoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_objects(self) -> directory_objects_request_builder.DirectoryObjectsRequestBuilder:
        """
        Provides operations to manage the collection of directoryObject entities.
        """
        from .directory_objects import directory_objects_request_builder

        return directory_objects_request_builder.DirectoryObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_roles(self) -> directory_roles_request_builder.DirectoryRolesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRole entities.
        """
        from .directory_roles import directory_roles_request_builder

        return directory_roles_request_builder.DirectoryRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_role_templates(self) -> directory_role_templates_request_builder.DirectoryRoleTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of directoryRoleTemplate entities.
        """
        from .directory_role_templates import directory_role_templates_request_builder

        return directory_role_templates_request_builder.DirectoryRoleTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domain_dns_records(self) -> domain_dns_records_request_builder.DomainDnsRecordsRequestBuilder:
        """
        Provides operations to manage the collection of domainDnsRecord entities.
        """
        from .domain_dns_records import domain_dns_records_request_builder

        return domain_dns_records_request_builder.DomainDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def domains(self) -> domains_request_builder.DomainsRequestBuilder:
        """
        Provides operations to manage the collection of domain entities.
        """
        from .domains import domains_request_builder

        return domains_request_builder.DomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the collection of drive entities.
        """
        from .drives import drives_request_builder

        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def education(self) -> education_request_builder.EducationRequestBuilder:
        """
        Provides operations to manage the educationRoot singleton.
        """
        from .education import education_request_builder

        return education_request_builder.EducationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employee_experience(self) -> employee_experience_request_builder.EmployeeExperienceRequestBuilder:
        """
        Provides operations to manage the employeeExperience singleton.
        """
        from .employee_experience import employee_experience_request_builder

        return employee_experience_request_builder.EmployeeExperienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external(self) -> external_request_builder.ExternalRequestBuilder:
        """
        Provides operations to manage the external singleton.
        """
        from .external import external_request_builder

        return external_request_builder.ExternalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filter_operators(self) -> filter_operators_request_builder.FilterOperatorsRequestBuilder:
        """
        Provides operations to manage the collection of filterOperatorSchema entities.
        """
        from .filter_operators import filter_operators_request_builder

        return filter_operators_request_builder.FilterOperatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> functions_request_builder.FunctionsRequestBuilder:
        """
        Provides operations to manage the collection of attributeMappingFunctionSchema entities.
        """
        from .functions import functions_request_builder

        return functions_request_builder.FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_lifecycle_policies(self) -> group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder:
        """
        Provides operations to manage the collection of groupLifecyclePolicy entities.
        """
        from .group_lifecycle_policies import group_lifecycle_policies_request_builder

        return group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def groups(self) -> groups_request_builder.GroupsRequestBuilder:
        """
        Provides operations to manage the collection of group entities.
        """
        from .groups import groups_request_builder

        return groups_request_builder.GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_settings(self) -> group_settings_request_builder.GroupSettingsRequestBuilder:
        """
        Provides operations to manage the collection of groupSetting entities.
        """
        from .group_settings import group_settings_request_builder

        return group_settings_request_builder.GroupSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_setting_templates(self) -> group_setting_templates_request_builder.GroupSettingTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of groupSettingTemplate entities.
        """
        from .group_setting_templates import group_setting_templates_request_builder

        return group_setting_templates_request_builder.GroupSettingTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity(self) -> identity_request_builder.IdentityRequestBuilder:
        """
        Provides operations to manage the identityContainer singleton.
        """
        from .identity import identity_request_builder

        return identity_request_builder.IdentityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_governance(self) -> identity_governance_request_builder.IdentityGovernanceRequestBuilder:
        """
        Provides operations to manage the identityGovernance singleton.
        """
        from .identity_governance import identity_governance_request_builder

        return identity_governance_request_builder.IdentityGovernanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_protection(self) -> identity_protection_request_builder.IdentityProtectionRequestBuilder:
        """
        Provides operations to manage the identityProtectionRoot singleton.
        """
        from .identity_protection import identity_protection_request_builder

        return identity_protection_request_builder.IdentityProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_providers(self) -> identity_providers_request_builder.IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the collection of identityProvider entities.
        """
        from .identity_providers import identity_providers_request_builder

        return identity_providers_request_builder.IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def information_protection(self) -> information_protection_request_builder.InformationProtectionRequestBuilder:
        """
        Provides operations to manage the informationProtection singleton.
        """
        from .information_protection import information_protection_request_builder

        return information_protection_request_builder.InformationProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invitations(self) -> invitations_request_builder.InvitationsRequestBuilder:
        """
        Provides operations to manage the collection of invitation entities.
        """
        from .invitations import invitations_request_builder

        return invitations_request_builder.InvitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def localizations(self) -> localizations_request_builder.LocalizationsRequestBuilder:
        """
        Provides operations to manage the collection of organizationalBrandingLocalization entities.
        """
        from .localizations import localizations_request_builder

        return localizations_request_builder.LocalizationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def me(self) -> me_request_builder.MeRequestBuilder:
        """
        Provides operations to manage the user singleton.
        """
        from .me import me_request_builder

        return me_request_builder.MeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of oAuth2PermissionGrant entities.
        """
        from .oauth2_permission_grants import oauth2_permission_grants_request_builder

        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def organization(self) -> organization_request_builder.OrganizationRequestBuilder:
        """
        Provides operations to manage the collection of organization entities.
        """
        from .organization import organization_request_builder

        return organization_request_builder.OrganizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> permission_grants_request_builder.PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        """
        from .permission_grants import permission_grants_request_builder

        return permission_grants_request_builder.PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def places(self) -> places_request_builder.PlacesRequestBuilder:
        """
        The places property
        """
        from .places import places_request_builder

        return places_request_builder.PlacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner singleton.
        """
        from .planner import planner_request_builder

        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> policies_request_builder.PoliciesRequestBuilder:
        """
        Provides operations to manage the policyRoot singleton.
        """
        from .policies import policies_request_builder

        return policies_request_builder.PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def print(self) -> print_request_builder.PrintRequestBuilder:
        """
        Provides operations to manage the print singleton.
        """
        from .print import print_request_builder

        return print_request_builder.PrintRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privacy(self) -> privacy_request_builder.PrivacyRequestBuilder:
        """
        Provides operations to manage the privacy singleton.
        """
        from .privacy import privacy_request_builder

        return privacy_request_builder.PrivacyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reportRoot singleton.
        """
        from .reports import reports_request_builder

        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_management(self) -> role_management_request_builder.RoleManagementRequestBuilder:
        """
        Provides operations to manage the roleManagement singleton.
        """
        from .role_management import role_management_request_builder

        return role_management_request_builder.RoleManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema_extensions(self) -> schema_extensions_request_builder.SchemaExtensionsRequestBuilder:
        """
        Provides operations to manage the collection of schemaExtension entities.
        """
        from .schema_extensions import schema_extensions_request_builder

        return schema_extensions_request_builder.SchemaExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scoped_role_memberships(self) -> scoped_role_memberships_request_builder.ScopedRoleMembershipsRequestBuilder:
        """
        Provides operations to manage the collection of scopedRoleMembership entities.
        """
        from .scoped_role_memberships import scoped_role_memberships_request_builder

        return scoped_role_memberships_request_builder.ScopedRoleMembershipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> search_request_builder.SearchRequestBuilder:
        """
        Provides operations to manage the searchEntity singleton.
        """
        from .search import search_request_builder

        return search_request_builder.SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> security_request_builder.SecurityRequestBuilder:
        """
        Provides operations to manage the security singleton.
        """
        from .security import security_request_builder

        return security_request_builder.SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principals(self) -> service_principals_request_builder.ServicePrincipalsRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        """
        from .service_principals import service_principals_request_builder

        return service_principals_request_builder.ServicePrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shares(self) -> shares_request_builder.SharesRequestBuilder:
        """
        Provides operations to manage the collection of sharedDriveItem entities.
        """
        from .shares import shares_request_builder

        return shares_request_builder.SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the collection of site entities.
        """
        from .sites import sites_request_builder

        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def solutions(self) -> solutions_request_builder.SolutionsRequestBuilder:
        """
        Provides operations to manage the solutionsRoot singleton.
        """
        from .solutions import solutions_request_builder

        return solutions_request_builder.SolutionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribed_skus(self) -> subscribed_skus_request_builder.SubscribedSkusRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        """
        from .subscribed_skus import subscribed_skus_request_builder

        return subscribed_skus_request_builder.SubscribedSkusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the collection of subscription entities.
        """
        from .subscriptions import subscriptions_request_builder

        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams(self) -> teams_request_builder.TeamsRequestBuilder:
        """
        Provides operations to manage the collection of team entities.
        """
        from .teams import teams_request_builder

        return teams_request_builder.TeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams_templates(self) -> teams_templates_request_builder.TeamsTemplatesRequestBuilder:
        """
        Provides operations to manage the collection of teamsTemplate entities.
        """
        from .teams_templates import teams_templates_request_builder

        return teams_templates_request_builder.TeamsTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teamwork(self) -> teamwork_request_builder.TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork singleton.
        """
        from .teamwork import teamwork_request_builder

        return teamwork_request_builder.TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenant_relationships(self) -> tenant_relationships_request_builder.TenantRelationshipsRequestBuilder:
        """
        Provides operations to manage the tenantRelationship singleton.
        """
        from .tenant_relationships import tenant_relationships_request_builder

        return tenant_relationships_request_builder.TenantRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the collection of user entities.
        """
        from .users import users_request_builder

        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    

