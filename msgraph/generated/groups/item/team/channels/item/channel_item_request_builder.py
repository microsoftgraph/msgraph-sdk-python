from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.channel import Channel
    from ......models.o_data_errors.o_data_error import ODataError
    from .all_members.all_members_request_builder import AllMembersRequestBuilder
    from .archive.archive_request_builder import ArchiveRequestBuilder
    from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder
    from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name.does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder import DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder
    from .files_folder.files_folder_request_builder import FilesFolderRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .provision_email.provision_email_request_builder import ProvisionEmailRequestBuilder
    from .remove_email.remove_email_request_builder import RemoveEmailRequestBuilder
    from .shared_with_teams.shared_with_teams_request_builder import SharedWithTeamsRequestBuilder
    from .tabs.tabs_request_builder import TabsRequestBuilder
    from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

class ChannelItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the channels property of the microsoft.graph.team entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChannelItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/team/channels/{channel%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property channels for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ChannelItemRequestBuilderGetQueryParameters]] = None) -> Optional[Channel]:
        """
        The collection of channels and messages associated with the team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Channel]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.channel import Channel

        return await self.request_adapter.send_async(request_info, Channel, error_mapping)
    
    async def patch(self,body: Channel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Channel]:
        """
        Update the navigation property channels in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Channel]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.channel import Channel

        return await self.request_adapter.send_async(request_info, Channel, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property channels for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ChannelItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The collection of channels and messages associated with the team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Channel, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property channels in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ChannelItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChannelItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChannelItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all_members(self) -> AllMembersRequestBuilder:
        """
        Provides operations to manage the allMembers property of the microsoft.graph.channel entity.
        """
        from .all_members.all_members_request_builder import AllMembersRequestBuilder

        return AllMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def archive(self) -> ArchiveRequestBuilder:
        """
        Provides operations to call the archive method.
        """
        from .archive.archive_request_builder import ArchiveRequestBuilder

        return ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    @property
    def unarchive(self) -> UnarchiveRequestBuilder:
        """
        Provides operations to call the unarchive method.
        """
        from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

        return UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChannelItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChannelItemRequestBuilderGetQueryParameters():
        """
        The collection of channels and messages associated with the team.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class ChannelItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ChannelItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChannelItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

