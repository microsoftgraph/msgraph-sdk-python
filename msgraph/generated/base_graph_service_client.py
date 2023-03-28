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
    from .agreement_acceptances.item import agreement_acceptance_item_request_builder
    from .agreements import agreements_request_builder
    from .agreements.item import agreement_item_request_builder
    from .app_catalogs import app_catalogs_request_builder
    from .applications import applications_request_builder
    from .applications.item import application_item_request_builder
    from .application_templates import application_templates_request_builder
    from .application_templates.item import application_template_item_request_builder
    from .audit_logs import audit_logs_request_builder
    from .authentication_method_configurations import authentication_method_configurations_request_builder
    from .authentication_method_configurations.item import authentication_method_configuration_item_request_builder
    from .authentication_methods_policy import authentication_methods_policy_request_builder
    from .branding import branding_request_builder
    from .certificate_based_auth_configuration import certificate_based_auth_configuration_request_builder
    from .certificate_based_auth_configuration.item import certificate_based_auth_configuration_item_request_builder
    from .chats import chats_request_builder
    from .chats.item import chat_item_request_builder
    from .communications import communications_request_builder
    from .compliance import compliance_request_builder
    from .connections import connections_request_builder
    from .connections.item import external_connection_item_request_builder
    from .contacts import contacts_request_builder
    from .contacts.item import org_contact_item_request_builder
    from .contracts import contracts_request_builder
    from .contracts.item import contract_item_request_builder
    from .data_policy_operations import data_policy_operations_request_builder
    from .data_policy_operations.item import data_policy_operation_item_request_builder
    from .device_app_management import device_app_management_request_builder
    from .device_management import device_management_request_builder
    from .devices import devices_request_builder
    from .devices.item import device_item_request_builder
    from .directory import directory_request_builder
    from .directory_objects import directory_objects_request_builder
    from .directory_objects.item import directory_object_item_request_builder
    from .directory_roles import directory_roles_request_builder
    from .directory_roles.item import directory_role_item_request_builder
    from .directory_role_templates import directory_role_templates_request_builder
    from .directory_role_templates.item import directory_role_template_item_request_builder
    from .domain_dns_records import domain_dns_records_request_builder
    from .domain_dns_records.item import domain_dns_record_item_request_builder
    from .domains import domains_request_builder
    from .domains.item import domain_item_request_builder
    from .drives import drives_request_builder
    from .drives.item import drive_item_request_builder
    from .education import education_request_builder
    from .employee_experience import employee_experience_request_builder
    from .external import external_request_builder
    from .group_lifecycle_policies import group_lifecycle_policies_request_builder
    from .group_lifecycle_policies.item import group_lifecycle_policy_item_request_builder
    from .groups import groups_request_builder
    from .groups.item import group_item_request_builder
    from .group_settings import group_settings_request_builder
    from .group_settings.item import group_setting_item_request_builder
    from .group_setting_templates import group_setting_templates_request_builder
    from .group_setting_templates.item import group_setting_template_item_request_builder
    from .identity import identity_request_builder
    from .identity_governance import identity_governance_request_builder
    from .identity_protection import identity_protection_request_builder
    from .identity_providers import identity_providers_request_builder
    from .identity_providers.item import identity_provider_item_request_builder
    from .information_protection import information_protection_request_builder
    from .invitations import invitations_request_builder
    from .invitations.item import invitation_item_request_builder
    from .localizations import localizations_request_builder
    from .localizations.item import organizational_branding_localization_item_request_builder
    from .me import me_request_builder
    from .oauth2_permission_grants import oauth2_permission_grants_request_builder
    from .oauth2_permission_grants.item import o_auth2_permission_grant_item_request_builder
    from .organization import organization_request_builder
    from .organization.item import organization_item_request_builder
    from .permission_grants import permission_grants_request_builder
    from .permission_grants.item import resource_specific_permission_grant_item_request_builder
    from .places import places_request_builder
    from .places.item import place_item_request_builder
    from .planner import planner_request_builder
    from .policies import policies_request_builder
    from .print import print_request_builder
    from .privacy import privacy_request_builder
    from .reports import reports_request_builder
    from .role_management import role_management_request_builder
    from .schema_extensions import schema_extensions_request_builder
    from .schema_extensions.item import schema_extension_item_request_builder
    from .scoped_role_memberships import scoped_role_memberships_request_builder
    from .scoped_role_memberships.item import scoped_role_membership_item_request_builder
    from .search import search_request_builder
    from .security import security_request_builder
    from .service_principals import service_principals_request_builder
    from .service_principals.item import service_principal_item_request_builder
    from .shares import shares_request_builder
    from .shares.item import shared_drive_item_item_request_builder
    from .sites import sites_request_builder
    from .sites.item import site_item_request_builder
    from .solutions import solutions_request_builder
    from .subscribed_skus import subscribed_skus_request_builder
    from .subscribed_skus.item import subscribed_sku_item_request_builder
    from .subscriptions import subscriptions_request_builder
    from .subscriptions.item import subscription_item_request_builder
    from .teams import teams_request_builder
    from .teams.item import team_item_request_builder
    from .teams_templates import teams_templates_request_builder
    from .teams_templates.item import teams_template_item_request_builder
    from .teamwork import teamwork_request_builder
    from .tenant_relationships import tenant_relationships_request_builder
    from .users import users_request_builder
    from .users.item import user_item_request_builder

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
    
    def agreement_acceptances_by_id(self,id: str) -> agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder:
        """
        Provides operations to manage the collection of agreementAcceptance entities.
        Args:
            id: Unique identifier of the item
        Returns: agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .agreement_acceptances.item import agreement_acceptance_item_request_builder

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
        from .agreements.item import agreement_item_request_builder

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
        from .applications.item import application_item_request_builder

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
        from .application_templates.item import application_template_item_request_builder

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
        from .authentication_method_configurations.item import authentication_method_configuration_item_request_builder

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
        from .certificate_based_auth_configuration.item import certificate_based_auth_configuration_item_request_builder

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
        from .chats.item import chat_item_request_builder

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
        from .connections.item import external_connection_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["externalConnection%2Did"] = id
        return external_connection_item_request_builder.ExternalConnectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def contacts_by_id(self,id: str) -> org_contact_item_request_builder.OrgContactItemRequestBuilder:
        """
        Provides operations to manage the collection of orgContact entities.
        Args:
            id: Unique identifier of the item
        Returns: org_contact_item_request_builder.OrgContactItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .contacts.item import org_contact_item_request_builder

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
        from .contracts.item import contract_item_request_builder

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
        from .data_policy_operations.item import data_policy_operation_item_request_builder

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
        from .devices.item import device_item_request_builder

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
        from .directory_objects.item import directory_object_item_request_builder

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
        from .directory_roles.item import directory_role_item_request_builder

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
        from .directory_role_templates.item import directory_role_template_item_request_builder

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
        from .domain_dns_records.item import domain_dns_record_item_request_builder

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
        from .domains.item import domain_item_request_builder

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
        from .drives.item import drive_item_request_builder

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
        from .group_lifecycle_policies.item import group_lifecycle_policy_item_request_builder

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
        from .groups.item import group_item_request_builder

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
        from .group_settings.item import group_setting_item_request_builder

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
        from .group_setting_templates.item import group_setting_template_item_request_builder

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
        from .identity_providers.item import identity_provider_item_request_builder

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
        from .invitations.item import invitation_item_request_builder

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
        from .localizations.item import organizational_branding_localization_item_request_builder

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
        from .oauth2_permission_grants.item import o_auth2_permission_grant_item_request_builder

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
        from .organization.item import organization_item_request_builder

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
        from .permission_grants.item import resource_specific_permission_grant_item_request_builder

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
        from .places.item import place_item_request_builder

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
        from .schema_extensions.item import schema_extension_item_request_builder

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
        from .scoped_role_memberships.item import scoped_role_membership_item_request_builder

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
        from .service_principals.item import service_principal_item_request_builder

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
        from .shares.item import shared_drive_item_item_request_builder

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
        from .sites.item import site_item_request_builder

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
        from .subscribed_skus.item import subscribed_sku_item_request_builder

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
        from .subscriptions.item import subscription_item_request_builder

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
        from .teams.item import team_item_request_builder

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
        from .teams_templates.item import teams_template_item_request_builder

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
        from .users.item import user_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["user%2Did"] = id
        return user_item_request_builder.UserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
    

