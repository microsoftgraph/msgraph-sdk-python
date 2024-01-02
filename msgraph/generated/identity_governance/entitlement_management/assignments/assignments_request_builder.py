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
    from ....models.access_package_assignment import AccessPackageAssignment
    from ....models.access_package_assignment_collection_response import AccessPackageAssignmentCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .additional_access.additional_access_request_builder import AdditionalAccessRequestBuilder
    from .additional_access_with_access_package_id_with_incompatible_access_package_id.additional_access_with_access_package_id_with_incompatible_access_package_id_request_builder import AdditionalAccessWithAccessPackageIdWithIncompatibleAccessPackageIdRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .filter_by_current_user_with_on.filter_by_current_user_with_on_request_builder import FilterByCurrentUserWithOnRequestBuilder
    from .item.access_package_assignment_item_request_builder import AccessPackageAssignmentItemRequestBuilder

class AssignmentsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the assignments property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AssignmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignments{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def additional_access_with_access_package_id_with_incompatible_access_package_id(self,access_package_id: Optional[str] = None, incompatible_access_package_id: Optional[str] = None) -> AdditionalAccessWithAccessPackageIdWithIncompatibleAccessPackageIdRequestBuilder:
        """
        Provides operations to call the additionalAccess method.
        param access_package_id: Usage: accessPackageId='{accessPackageId}'
        param incompatible_access_package_id: Usage: incompatibleAccessPackageId='{incompatibleAccessPackageId}'
        Returns: AdditionalAccessWithAccessPackageIdWithIncompatibleAccessPackageIdRequestBuilder
        """
        if not access_package_id:
            raise TypeError("access_package_id cannot be null.")
        if not incompatible_access_package_id:
            raise TypeError("incompatible_access_package_id cannot be null.")
        from .additional_access_with_access_package_id_with_incompatible_access_package_id.additional_access_with_access_package_id_with_incompatible_access_package_id_request_builder import AdditionalAccessWithAccessPackageIdWithIncompatibleAccessPackageIdRequestBuilder

        return AdditionalAccessWithAccessPackageIdWithIncompatibleAccessPackageIdRequestBuilder(self.request_adapter, self.path_parameters, access_package_id, incompatible_access_package_id)
    
    def by_access_package_assignment_id(self,access_package_assignment_id: str) -> AccessPackageAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.entitlementManagement entity.
        param access_package_assignment_id: The unique identifier of accessPackageAssignment
        Returns: AccessPackageAssignmentItemRequestBuilder
        """
        if not access_package_assignment_id:
            raise TypeError("access_package_assignment_id cannot be null.")
        from .item.access_package_assignment_item_request_builder import AccessPackageAssignmentItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignment%2Did"] = access_package_assignment_id
        return AccessPackageAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def filter_by_current_user_with_on(self,on: Optional[str] = None) -> FilterByCurrentUserWithOnRequestBuilder:
        """
        Provides operations to call the filterByCurrentUser method.
        param on: Usage: on='{on}'
        Returns: FilterByCurrentUserWithOnRequestBuilder
        """
        if not on:
            raise TypeError("on cannot be null.")
        from .filter_by_current_user_with_on.filter_by_current_user_with_on_request_builder import FilterByCurrentUserWithOnRequestBuilder

        return FilterByCurrentUserWithOnRequestBuilder(self.request_adapter, self.path_parameters, on)
    
    async def get(self,request_configuration: Optional[AssignmentsRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageAssignmentCollectionResponse]:
        """
        In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignment objects. For directory-wide administrators, the resulting list includes all the assignments, current and well as expired, that the caller has access to read, across all catalogs and access packages.  If the caller is on behalf of a delegated user who is assigned only to catalog-specific delegated administrative roles, the request must supply a filter to indicate a specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/entitlementmanagement-list-assignments?view=graph-rest-1.0
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
        from ....models.access_package_assignment_collection_response import AccessPackageAssignmentCollectionResponse

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[AccessPackageAssignment] = None, request_configuration: Optional[AssignmentsRequestBuilderPostRequestConfiguration] = None) -> Optional[AccessPackageAssignment]:
        """
        Create new navigation property to assignments for identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignment]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.access_package_assignment import AccessPackageAssignment

        return await self.request_adapter.send_async(request_info, AccessPackageAssignment, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AssignmentsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignment objects. For directory-wide administrators, the resulting list includes all the assignments, current and well as expired, that the caller has access to read, across all catalogs and access packages.  If the caller is on behalf of a delegated user who is assigned only to catalog-specific delegated administrative roles, the request must supply a filter to indicate a specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'.
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
    
    def to_post_request_information(self,body: Optional[AccessPackageAssignment] = None, request_configuration: Optional[AssignmentsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to assignments for identityGovernance
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AssignmentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignmentsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AssignmentsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def additional_access(self) -> AdditionalAccessRequestBuilder:
        """
        Provides operations to call the additionalAccess method.
        """
        from .additional_access.additional_access_request_builder import AdditionalAccessRequestBuilder

        return AdditionalAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AssignmentsRequestBuilderGetQueryParameters():
        """
        In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignment objects. For directory-wide administrators, the resulting list includes all the assignments, current and well as expired, that the caller has access to read, across all catalogs and access packages.  If the caller is on behalf of a delegated user who is assigned only to catalog-specific delegated administrative roles, the request must supply a filter to indicate a specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignmentsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AssignmentsRequestBuilder.AssignmentsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignmentsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

