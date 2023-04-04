from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import mail_folder
    from .....models.o_data_errors import o_data_error
    from .child_folders import child_folders_request_builder
    from .child_folders.item import mail_folder_item_request_builder
    from .copy import copy_request_builder
    from .message_rules import message_rules_request_builder
    from .message_rules.item import message_rule_item_request_builder
    from .messages import messages_request_builder
    from .messages.item import message_item_request_builder
    from .move import move_request_builder
    from .multi_value_extended_properties import multi_value_extended_properties_request_builder
    from .multi_value_extended_properties.item import multi_value_legacy_extended_property_item_request_builder
    from .single_value_extended_properties import single_value_extended_properties_request_builder
    from .single_value_extended_properties.item import single_value_legacy_extended_property_item_request_builder

class MailFolderItemRequestBuilder():
    """
    Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MailFolderItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/mailFolders/{mailFolder%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def child_folders_by_id(self,id: str) -> MailFolderItemRequestBuilder:
        """
        Provides operations to manage the childFolders property of the microsoft.graph.mailFolder entity.
        Args:
            id: Unique identifier of the item
        Returns: MailFolderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .child_folders.item import mail_folder_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mailFolder%2Did1"] = id
        return MailFolderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[MailFolderItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property mailFolders for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[MailFolderItemRequestBuilderGetRequestConfiguration] = None) -> Optional[mail_folder.MailFolder]:
        """
        The user's mail folders. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mail_folder.MailFolder]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import mail_folder

        return await self.request_adapter.send_async(request_info, mail_folder.MailFolder, error_mapping)
    
    def message_rules_by_id(self,id: str) -> message_rule_item_request_builder.MessageRuleItemRequestBuilder:
        """
        Provides operations to manage the messageRules property of the microsoft.graph.mailFolder entity.
        Args:
            id: Unique identifier of the item
        Returns: message_rule_item_request_builder.MessageRuleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .message_rules.item import message_rule_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["messageRule%2Did"] = id
        return message_rule_item_request_builder.MessageRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def messages_by_id(self,id: str) -> message_item_request_builder.MessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.mailFolder entity.
        Args:
            id: Unique identifier of the item
        Returns: message_item_request_builder.MessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .messages.item import message_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["message%2Did"] = id
        return message_item_request_builder.MessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def multi_value_extended_properties_by_id(self,id: str) -> multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.mailFolder entity.
        Args:
            id: Unique identifier of the item
        Returns: multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .multi_value_extended_properties.item import multi_value_legacy_extended_property_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiValueLegacyExtendedProperty%2Did"] = id
        return multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[mail_folder.MailFolder] = None, request_configuration: Optional[MailFolderItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[mail_folder.MailFolder]:
        """
        Update the navigation property mailFolders in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mail_folder.MailFolder]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import mail_folder

        return await self.request_adapter.send_async(request_info, mail_folder.MailFolder, error_mapping)
    
    def single_value_extended_properties_by_id(self,id: str) -> single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.mailFolder entity.
        Args:
            id: Unique identifier of the item
        Returns: single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .single_value_extended_properties.item import single_value_legacy_extended_property_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["singleValueLegacyExtendedProperty%2Did"] = id
        return single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[MailFolderItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property mailFolders for users
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
    
    def to_get_request_information(self,request_configuration: Optional[MailFolderItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The user's mail folders. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[mail_folder.MailFolder] = None, request_configuration: Optional[MailFolderItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property mailFolders in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
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
    def child_folders(self) -> child_folders_request_builder.ChildFoldersRequestBuilder:
        """
        Provides operations to manage the childFolders property of the microsoft.graph.mailFolder entity.
        """
        from .child_folders import child_folders_request_builder

        return child_folders_request_builder.ChildFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> copy_request_builder.CopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        from .copy import copy_request_builder

        return copy_request_builder.CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def message_rules(self) -> message_rules_request_builder.MessageRulesRequestBuilder:
        """
        Provides operations to manage the messageRules property of the microsoft.graph.mailFolder entity.
        """
        from .message_rules import message_rules_request_builder

        return message_rules_request_builder.MessageRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.mailFolder entity.
        """
        from .messages import messages_request_builder

        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move(self) -> move_request_builder.MoveRequestBuilder:
        """
        Provides operations to call the move method.
        """
        from .move import move_request_builder

        return move_request_builder.MoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.mailFolder entity.
        """
        from .multi_value_extended_properties import multi_value_extended_properties_request_builder

        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.mailFolder entity.
        """
        from .single_value_extended_properties import single_value_extended_properties_request_builder

        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MailFolderItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class MailFolderItemRequestBuilderGetQueryParameters():
        """
        The user's mail folders. Read-only. Nullable.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class MailFolderItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MailFolderItemRequestBuilder.MailFolderItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MailFolderItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

