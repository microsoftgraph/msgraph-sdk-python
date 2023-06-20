from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import group
    from ...models.o_data_errors import o_data_error
    from .accepted_senders import accepted_senders_request_builder
    from .add_favorite import add_favorite_request_builder
    from .app_role_assignments import app_role_assignments_request_builder
    from .assign_license import assign_license_request_builder
    from .calendar import calendar_request_builder
    from .calendar_view import calendar_view_request_builder
    from .check_granted_permissions_for_app import check_granted_permissions_for_app_request_builder
    from .check_member_groups import check_member_groups_request_builder
    from .check_member_objects import check_member_objects_request_builder
    from .conversations import conversations_request_builder
    from .created_on_behalf_of import created_on_behalf_of_request_builder
    from .drive import drive_request_builder
    from .drives import drives_request_builder
    from .events import events_request_builder
    from .extensions import extensions_request_builder
    from .get_member_groups import get_member_groups_request_builder
    from .get_member_objects import get_member_objects_request_builder
    from .group_lifecycle_policies import group_lifecycle_policies_request_builder
    from .member_of import member_of_request_builder
    from .members import members_request_builder
    from .members_with_license_errors import members_with_license_errors_request_builder
    from .onenote import onenote_request_builder
    from .owners import owners_request_builder
    from .permission_grants import permission_grants_request_builder
    from .photo import photo_request_builder
    from .photos import photos_request_builder
    from .planner import planner_request_builder
    from .rejected_senders import rejected_senders_request_builder
    from .remove_favorite import remove_favorite_request_builder
    from .renew import renew_request_builder
    from .reset_unseen_count import reset_unseen_count_request_builder
    from .restore import restore_request_builder
    from .settings import settings_request_builder
    from .sites import sites_request_builder
    from .subscribe_by_mail import subscribe_by_mail_request_builder
    from .team import team_request_builder
    from .threads import threads_request_builder
    from .transitive_member_of import transitive_member_of_request_builder
    from .transitive_members import transitive_members_request_builder
    from .unsubscribe_by_mail import unsubscribe_by_mail_request_builder
    from .validate_properties import validate_properties_request_builder

class GroupItemRequestBuilder():
    """
    Provides operations to manage the collection of group entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GroupItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[GroupItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete group. When deleted, Microsoft 365 groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This isn't applicable to Security groups and Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[GroupItemRequestBuilderGetRequestConfiguration] = None) -> Optional[group.Group]:
        """
        Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that are _not_ returned by default, specify them in a `$select` OData query option. The **hasMembersWithLicenseErrors** and **isArchived** properties are an exception and are not returned in the `$select` query.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group.Group]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import group

        return await self.request_adapter.send_async(request_info, group.Group, error_mapping)
    
    async def patch(self,body: Optional[group.Group] = None, request_configuration: Optional[GroupItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[group.Group]:
        """
        Update the properties of a group object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group.Group]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import group

        return await self.request_adapter.send_async(request_info, group.Group, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[GroupItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete group. When deleted, Microsoft 365 groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This isn't applicable to Security groups and Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[GroupItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that are _not_ returned by default, specify them in a `$select` OData query option. The **hasMembersWithLicenseErrors** and **isArchived** properties are an exception and are not returned in the `$select` query.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[group.Group] = None, request_configuration: Optional[GroupItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a group object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def accepted_senders(self) -> accepted_senders_request_builder.AcceptedSendersRequestBuilder:
        """
        Provides operations to manage the acceptedSenders property of the microsoft.graph.group entity.
        """
        from .accepted_senders import accepted_senders_request_builder

        return accepted_senders_request_builder.AcceptedSendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_favorite(self) -> add_favorite_request_builder.AddFavoriteRequestBuilder:
        """
        Provides operations to call the addFavorite method.
        """
        from .add_favorite import add_favorite_request_builder

        return add_favorite_request_builder.AddFavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.group entity.
        """
        from .app_role_assignments import app_role_assignments_request_builder

        return app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_license(self) -> assign_license_request_builder.AssignLicenseRequestBuilder:
        """
        Provides operations to call the assignLicense method.
        """
        from .assign_license import assign_license_request_builder

        return assign_license_request_builder.AssignLicenseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.group entity.
        """
        from .calendar import calendar_request_builder

        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.group entity.
        """
        from .calendar_view import calendar_view_request_builder

        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_granted_permissions_for_app(self) -> check_granted_permissions_for_app_request_builder.CheckGrantedPermissionsForAppRequestBuilder:
        """
        Provides operations to call the checkGrantedPermissionsForApp method.
        """
        from .check_granted_permissions_for_app import check_granted_permissions_for_app_request_builder

        return check_granted_permissions_for_app_request_builder.CheckGrantedPermissionsForAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups import check_member_groups_request_builder

        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects import check_member_objects_request_builder

        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conversations(self) -> conversations_request_builder.ConversationsRequestBuilder:
        """
        Provides operations to manage the conversations property of the microsoft.graph.group entity.
        """
        from .conversations import conversations_request_builder

        return conversations_request_builder.ConversationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_on_behalf_of(self) -> created_on_behalf_of_request_builder.CreatedOnBehalfOfRequestBuilder:
        """
        Provides operations to manage the createdOnBehalfOf property of the microsoft.graph.group entity.
        """
        from .created_on_behalf_of import created_on_behalf_of_request_builder

        return created_on_behalf_of_request_builder.CreatedOnBehalfOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.group entity.
        """
        from .drive import drive_request_builder

        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.group entity.
        """
        from .drives import drives_request_builder

        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> events_request_builder.EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.group entity.
        """
        from .events import events_request_builder

        return events_request_builder.EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.group entity.
        """
        from .extensions import extensions_request_builder

        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups import get_member_groups_request_builder

        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects import get_member_objects_request_builder

        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_lifecycle_policies(self) -> group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder:
        """
        Provides operations to manage the groupLifecyclePolicies property of the microsoft.graph.group entity.
        """
        from .group_lifecycle_policies import group_lifecycle_policies_request_builder

        return group_lifecycle_policies_request_builder.GroupLifecyclePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.group entity.
        """
        from .member_of import member_of_request_builder

        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.group entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members_with_license_errors(self) -> members_with_license_errors_request_builder.MembersWithLicenseErrorsRequestBuilder:
        """
        Provides operations to manage the membersWithLicenseErrors property of the microsoft.graph.group entity.
        """
        from .members_with_license_errors import members_with_license_errors_request_builder

        return members_with_license_errors_request_builder.MembersWithLicenseErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> onenote_request_builder.OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.group entity.
        """
        from .onenote import onenote_request_builder

        return onenote_request_builder.OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> owners_request_builder.OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.group entity.
        """
        from .owners import owners_request_builder

        return owners_request_builder.OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> permission_grants_request_builder.PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.group entity.
        """
        from .permission_grants import permission_grants_request_builder

        return permission_grants_request_builder.PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> photo_request_builder.PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.group entity.
        """
        from .photo import photo_request_builder

        return photo_request_builder.PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photos(self) -> photos_request_builder.PhotosRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.group entity.
        """
        from .photos import photos_request_builder

        return photos_request_builder.PhotosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner property of the microsoft.graph.group entity.
        """
        from .planner import planner_request_builder

        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rejected_senders(self) -> rejected_senders_request_builder.RejectedSendersRequestBuilder:
        """
        Provides operations to manage the rejectedSenders property of the microsoft.graph.group entity.
        """
        from .rejected_senders import rejected_senders_request_builder

        return rejected_senders_request_builder.RejectedSendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_favorite(self) -> remove_favorite_request_builder.RemoveFavoriteRequestBuilder:
        """
        Provides operations to call the removeFavorite method.
        """
        from .remove_favorite import remove_favorite_request_builder

        return remove_favorite_request_builder.RemoveFavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def renew(self) -> renew_request_builder.RenewRequestBuilder:
        """
        Provides operations to call the renew method.
        """
        from .renew import renew_request_builder

        return renew_request_builder.RenewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_unseen_count(self) -> reset_unseen_count_request_builder.ResetUnseenCountRequestBuilder:
        """
        Provides operations to call the resetUnseenCount method.
        """
        from .reset_unseen_count import reset_unseen_count_request_builder

        return reset_unseen_count_request_builder.ResetUnseenCountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore import restore_request_builder

        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.group entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.group entity.
        """
        from .sites import sites_request_builder

        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribe_by_mail(self) -> subscribe_by_mail_request_builder.SubscribeByMailRequestBuilder:
        """
        Provides operations to call the subscribeByMail method.
        """
        from .subscribe_by_mail import subscribe_by_mail_request_builder

        return subscribe_by_mail_request_builder.SubscribeByMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team(self) -> team_request_builder.TeamRequestBuilder:
        """
        Provides operations to manage the team property of the microsoft.graph.group entity.
        """
        from .team import team_request_builder

        return team_request_builder.TeamRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threads(self) -> threads_request_builder.ThreadsRequestBuilder:
        """
        Provides operations to manage the threads property of the microsoft.graph.group entity.
        """
        from .threads import threads_request_builder

        return threads_request_builder.ThreadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.group entity.
        """
        from .transitive_member_of import transitive_member_of_request_builder

        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_members(self) -> transitive_members_request_builder.TransitiveMembersRequestBuilder:
        """
        Provides operations to manage the transitiveMembers property of the microsoft.graph.group entity.
        """
        from .transitive_members import transitive_members_request_builder

        return transitive_members_request_builder.TransitiveMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsubscribe_by_mail(self) -> unsubscribe_by_mail_request_builder.UnsubscribeByMailRequestBuilder:
        """
        Provides operations to call the unsubscribeByMail method.
        """
        from .unsubscribe_by_mail import unsubscribe_by_mail_request_builder

        return unsubscribe_by_mail_request_builder.UnsubscribeByMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_properties(self) -> validate_properties_request_builder.ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        from .validate_properties import validate_properties_request_builder

        return validate_properties_request_builder.ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GroupItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that are _not_ returned by default, specify them in a `$select` OData query option. The **hasMembersWithLicenseErrors** and **isArchived** properties are an exception and are not returned in the `$select` query.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class GroupItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GroupItemRequestBuilder.GroupItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GroupItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

