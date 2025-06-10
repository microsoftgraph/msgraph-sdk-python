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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.subject_rights_request import SubjectRightsRequest
    from .approvers.approvers_request_builder import ApproversRequestBuilder
    from .approvers_with_user_principal_name.approvers_with_user_principal_name_request_builder import ApproversWithUserPrincipalNameRequestBuilder
    from .collaborators.collaborators_request_builder import CollaboratorsRequestBuilder
    from .collaborators_with_user_principal_name.collaborators_with_user_principal_name_request_builder import CollaboratorsWithUserPrincipalNameRequestBuilder
    from .get_final_attachment.get_final_attachment_request_builder import GetFinalAttachmentRequestBuilder
    from .get_final_report.get_final_report_request_builder import GetFinalReportRequestBuilder
    from .notes.notes_request_builder import NotesRequestBuilder
    from .team.team_request_builder import TeamRequestBuilder

class SubjectRightsRequestItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the subjectRightsRequests property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SubjectRightsRequestItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/subjectRightsRequests/{subjectRightsRequest%2Did}{?%24expand,%24select}", path_parameters)
    
    def approvers_with_user_principal_name(self,user_principal_name: str) -> ApproversWithUserPrincipalNameRequestBuilder:
        """
        Provides operations to manage the approvers property of the microsoft.graph.subjectRightsRequest entity.
        param user_principal_name: Alternate key of user
        Returns: ApproversWithUserPrincipalNameRequestBuilder
        """
        if user_principal_name is None:
            raise TypeError("user_principal_name cannot be null.")
        from .approvers_with_user_principal_name.approvers_with_user_principal_name_request_builder import ApproversWithUserPrincipalNameRequestBuilder

        return ApproversWithUserPrincipalNameRequestBuilder(self.request_adapter, self.path_parameters, user_principal_name)
    
    def collaborators_with_user_principal_name(self,user_principal_name: str) -> CollaboratorsWithUserPrincipalNameRequestBuilder:
        """
        Provides operations to manage the collaborators property of the microsoft.graph.subjectRightsRequest entity.
        param user_principal_name: Alternate key of user
        Returns: CollaboratorsWithUserPrincipalNameRequestBuilder
        """
        if user_principal_name is None:
            raise TypeError("user_principal_name cannot be null.")
        from .collaborators_with_user_principal_name.collaborators_with_user_principal_name_request_builder import CollaboratorsWithUserPrincipalNameRequestBuilder

        return CollaboratorsWithUserPrincipalNameRequestBuilder(self.request_adapter, self.path_parameters, user_principal_name)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property subjectRightsRequests for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SubjectRightsRequestItemRequestBuilderGetQueryParameters]] = None) -> Optional[SubjectRightsRequest]:
        """
        Get subjectRightsRequests from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SubjectRightsRequest]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.subject_rights_request import SubjectRightsRequest

        return await self.request_adapter.send_async(request_info, SubjectRightsRequest, error_mapping)
    
    async def patch(self,body: SubjectRightsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SubjectRightsRequest]:
        """
        Update the navigation property subjectRightsRequests in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SubjectRightsRequest]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.subject_rights_request import SubjectRightsRequest

        return await self.request_adapter.send_async(request_info, SubjectRightsRequest, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property subjectRightsRequests for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SubjectRightsRequestItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get subjectRightsRequests from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SubjectRightsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property subjectRightsRequests in security
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
    
    def with_url(self,raw_url: str) -> SubjectRightsRequestItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SubjectRightsRequestItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SubjectRightsRequestItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def approvers(self) -> ApproversRequestBuilder:
        """
        Provides operations to manage the approvers property of the microsoft.graph.subjectRightsRequest entity.
        """
        from .approvers.approvers_request_builder import ApproversRequestBuilder

        return ApproversRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def collaborators(self) -> CollaboratorsRequestBuilder:
        """
        Provides operations to manage the collaborators property of the microsoft.graph.subjectRightsRequest entity.
        """
        from .collaborators.collaborators_request_builder import CollaboratorsRequestBuilder

        return CollaboratorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_final_attachment(self) -> GetFinalAttachmentRequestBuilder:
        """
        Provides operations to call the getFinalAttachment method.
        """
        from .get_final_attachment.get_final_attachment_request_builder import GetFinalAttachmentRequestBuilder

        return GetFinalAttachmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_final_report(self) -> GetFinalReportRequestBuilder:
        """
        Provides operations to call the getFinalReport method.
        """
        from .get_final_report.get_final_report_request_builder import GetFinalReportRequestBuilder

        return GetFinalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notes(self) -> NotesRequestBuilder:
        """
        Provides operations to manage the notes property of the microsoft.graph.subjectRightsRequest entity.
        """
        from .notes.notes_request_builder import NotesRequestBuilder

        return NotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team(self) -> TeamRequestBuilder:
        """
        Provides operations to manage the team property of the microsoft.graph.subjectRightsRequest entity.
        """
        from .team.team_request_builder import TeamRequestBuilder

        return TeamRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SubjectRightsRequestItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SubjectRightsRequestItemRequestBuilderGetQueryParameters():
        """
        Get subjectRightsRequests from security
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
    class SubjectRightsRequestItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SubjectRightsRequestItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SubjectRightsRequestItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

