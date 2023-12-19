from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.channel import Channel
    from ....models.o_data_errors.o_data_error import ODataError
    from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder
    from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name.does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder import DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder
    from .files_folder.files_folder_request_builder import FilesFolderRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .provision_email.provision_email_request_builder import ProvisionEmailRequestBuilder
    from .remove_email.remove_email_request_builder import RemoveEmailRequestBuilder
    from .shared_with_teams.shared_with_teams_request_builder import SharedWithTeamsRequestBuilder
    from .tabs.tabs_request_builder import TabsRequestBuilder

class PrimaryChannelRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the primaryChannel property of the microsoft.graph.team entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrimaryChannelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/primaryChannel{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[PrimaryChannelRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property primaryChannel for teams
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PrimaryChannelRequestBuilderGetRequestConfiguration] = None) -> Optional[Channel]:
        """
        Get the default channel, General, of a team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Channel]
        Find more info here: https://learn.microsoft.com/graph/api/team-get-primarychannel?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.channel import Channel

        return await self.request_adapter.send_async(request_info, Channel, error_mapping)
    
    async def patch(self,body: Optional[Channel] = None, request_configuration: Optional[PrimaryChannelRequestBuilderPatchRequestConfiguration] = None) -> Optional[Channel]:
        """
        Update the navigation property primaryChannel in teams
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Channel]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.channel import Channel

        return await self.request_adapter.send_async(request_info, Channel, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PrimaryChannelRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property primaryChannel for teams
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[PrimaryChannelRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the default channel, General, of a team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Channel] = None, request_configuration: Optional[PrimaryChannelRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property primaryChannel in teams
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PrimaryChannelRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrimaryChannelRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PrimaryChannelRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def complete_migration(self) -> CompleteMigrationRequestBuilder:
        """
        Provides operations to call the completeMigration method.
        """
        from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder

        return CompleteMigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name(self) -> DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder:
        """
        Provides operations to call the doesUserHaveAccess method.
        """
        from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name.does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder import DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder

        return DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files_folder(self) -> FilesFolderRequestBuilder:
        """
        Provides operations to manage the filesFolder property of the microsoft.graph.channel entity.
        """
        from .files_folder.files_folder_request_builder import FilesFolderRequestBuilder

        return FilesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.channel entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.channel entity.
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provision_email(self) -> ProvisionEmailRequestBuilder:
        """
        Provides operations to call the provisionEmail method.
        """
        from .provision_email.provision_email_request_builder import ProvisionEmailRequestBuilder

        return ProvisionEmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_email(self) -> RemoveEmailRequestBuilder:
        """
        Provides operations to call the removeEmail method.
        """
        from .remove_email.remove_email_request_builder import RemoveEmailRequestBuilder

        return RemoveEmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_with_teams(self) -> SharedWithTeamsRequestBuilder:
        """
        Provides operations to manage the sharedWithTeams property of the microsoft.graph.channel entity.
        """
        from .shared_with_teams.shared_with_teams_request_builder import SharedWithTeamsRequestBuilder

        return SharedWithTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tabs(self) -> TabsRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.channel entity.
        """
        from .tabs.tabs_request_builder import TabsRequestBuilder

        return TabsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrimaryChannelRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class PrimaryChannelRequestBuilderGetQueryParameters():
        """
        Get the default channel, General, of a team.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrimaryChannelRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PrimaryChannelRequestBuilder.PrimaryChannelRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrimaryChannelRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

