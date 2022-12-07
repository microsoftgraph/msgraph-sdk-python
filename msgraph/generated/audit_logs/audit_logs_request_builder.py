from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_audits_request_builder = lazy_import('msgraph.generated.audit_logs.directory_audits.directory_audits_request_builder')
directory_audit_item_request_builder = lazy_import('msgraph.generated.audit_logs.directory_audits.item.directory_audit_item_request_builder')
provisioning_request_builder = lazy_import('msgraph.generated.audit_logs.provisioning.provisioning_request_builder')
provisioning_object_summary_item_request_builder = lazy_import('msgraph.generated.audit_logs.provisioning.item.provisioning_object_summary_item_request_builder')
sign_ins_request_builder = lazy_import('msgraph.generated.audit_logs.sign_ins.sign_ins_request_builder')
sign_in_item_request_builder = lazy_import('msgraph.generated.audit_logs.sign_ins.item.sign_in_item_request_builder')
audit_log_root = lazy_import('msgraph.generated.models.audit_log_root')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AuditLogsRequestBuilder():
    """
    Provides operations to manage the auditLogRoot singleton.
    """
    def directory_audits(self) -> directory_audits_request_builder.DirectoryAuditsRequestBuilder:
        """
        Provides operations to manage the directoryAudits property of the microsoft.graph.auditLogRoot entity.
        """
        return directory_audits_request_builder.DirectoryAuditsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def provisioning(self) -> provisioning_request_builder.ProvisioningRequestBuilder:
        """
        Provides operations to manage the provisioning property of the microsoft.graph.auditLogRoot entity.
        """
        return provisioning_request_builder.ProvisioningRequestBuilder(self.request_adapter, self.path_parameters)
    
    def sign_ins(self) -> sign_ins_request_builder.SignInsRequestBuilder:
        """
        Provides operations to manage the signIns property of the microsoft.graph.auditLogRoot entity.
        """
        return sign_ins_request_builder.SignInsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuditLogsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/auditLogs{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[AuditLogsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get auditLogs
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[audit_log_root.AuditLogRoot] = None, request_configuration: Optional[AuditLogsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update auditLogs
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def directory_audits_by_id(self,id: str) -> directory_audit_item_request_builder.DirectoryAuditItemRequestBuilder:
        """
        Provides operations to manage the directoryAudits property of the microsoft.graph.auditLogRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_audit_item_request_builder.DirectoryAuditItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryAudit%2Did"] = id
        return directory_audit_item_request_builder.DirectoryAuditItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AuditLogsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[audit_log_root.AuditLogRoot]:
        """
        Get auditLogs
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[audit_log_root.AuditLogRoot]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, audit_log_root.AuditLogRoot, response_handler, error_mapping)
    
    async def patch(self,body: Optional[audit_log_root.AuditLogRoot] = None, request_configuration: Optional[AuditLogsRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[audit_log_root.AuditLogRoot]:
        """
        Update auditLogs
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[audit_log_root.AuditLogRoot]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, audit_log_root.AuditLogRoot, response_handler, error_mapping)
    
    def provisioning_by_id(self,id: str) -> provisioning_object_summary_item_request_builder.ProvisioningObjectSummaryItemRequestBuilder:
        """
        Provides operations to manage the provisioning property of the microsoft.graph.auditLogRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: provisioning_object_summary_item_request_builder.ProvisioningObjectSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["provisioningObjectSummary%2Did"] = id
        return provisioning_object_summary_item_request_builder.ProvisioningObjectSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sign_ins_by_id(self,id: str) -> sign_in_item_request_builder.SignInItemRequestBuilder:
        """
        Provides operations to manage the signIns property of the microsoft.graph.auditLogRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: sign_in_item_request_builder.SignInItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["signIn%2Did"] = id
        return sign_in_item_request_builder.SignInItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class AuditLogsRequestBuilderGetQueryParameters():
        """
        Get auditLogs
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class AuditLogsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AuditLogsRequestBuilder.AuditLogsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AuditLogsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

