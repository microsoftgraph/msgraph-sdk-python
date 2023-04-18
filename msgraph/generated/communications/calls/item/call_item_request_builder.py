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
    from ....models import call
    from ....models.o_data_errors import o_data_error
    from .add_large_gallery_view import add_large_gallery_view_request_builder
    from .answer import answer_request_builder
    from .audio_routing_groups import audio_routing_groups_request_builder
    from .cancel_media_processing import cancel_media_processing_request_builder
    from .change_screen_sharing_role import change_screen_sharing_role_request_builder
    from .content_sharing_sessions import content_sharing_sessions_request_builder
    from .keep_alive import keep_alive_request_builder
    from .mute import mute_request_builder
    from .operations import operations_request_builder
    from .participants import participants_request_builder
    from .play_prompt import play_prompt_request_builder
    from .record_response import record_response_request_builder
    from .redirect import redirect_request_builder
    from .reject import reject_request_builder
    from .subscribe_to_tone import subscribe_to_tone_request_builder
    from .transfer import transfer_request_builder
    from .unmute import unmute_request_builder
    from .update_recording_status import update_recording_status_request_builder

class CallItemRequestBuilder():
    """
    Provides operations to manage the calls property of the microsoft.graph.cloudCommunications entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CallItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[CallItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property calls for communications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CallItemRequestBuilderGetRequestConfiguration] = None) -> Optional[call.Call]:
        """
        Get calls from communications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[call.Call]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import call

        return await self.request_adapter.send_async(request_info, call.Call, error_mapping)
    
    async def patch(self,body: Optional[call.Call] = None, request_configuration: Optional[CallItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[call.Call]:
        """
        Update the navigation property calls in communications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[call.Call]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import call

        return await self.request_adapter.send_async(request_info, call.Call, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CallItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property calls for communications
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
    
    def to_get_request_information(self,request_configuration: Optional[CallItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get calls from communications
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
    
    def to_patch_request_information(self,body: Optional[call.Call] = None, request_configuration: Optional[CallItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property calls in communications
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
    def add_large_gallery_view(self) -> add_large_gallery_view_request_builder.AddLargeGalleryViewRequestBuilder:
        """
        Provides operations to call the addLargeGalleryView method.
        """
        from .add_large_gallery_view import add_large_gallery_view_request_builder

        return add_large_gallery_view_request_builder.AddLargeGalleryViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def answer(self) -> answer_request_builder.AnswerRequestBuilder:
        """
        Provides operations to call the answer method.
        """
        from .answer import answer_request_builder

        return answer_request_builder.AnswerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audio_routing_groups(self) -> audio_routing_groups_request_builder.AudioRoutingGroupsRequestBuilder:
        """
        Provides operations to manage the audioRoutingGroups property of the microsoft.graph.call entity.
        """
        from .audio_routing_groups import audio_routing_groups_request_builder

        return audio_routing_groups_request_builder.AudioRoutingGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel_media_processing(self) -> cancel_media_processing_request_builder.CancelMediaProcessingRequestBuilder:
        """
        Provides operations to call the cancelMediaProcessing method.
        """
        from .cancel_media_processing import cancel_media_processing_request_builder

        return cancel_media_processing_request_builder.CancelMediaProcessingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def change_screen_sharing_role(self) -> change_screen_sharing_role_request_builder.ChangeScreenSharingRoleRequestBuilder:
        """
        Provides operations to call the changeScreenSharingRole method.
        """
        from .change_screen_sharing_role import change_screen_sharing_role_request_builder

        return change_screen_sharing_role_request_builder.ChangeScreenSharingRoleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_sharing_sessions(self) -> content_sharing_sessions_request_builder.ContentSharingSessionsRequestBuilder:
        """
        Provides operations to manage the contentSharingSessions property of the microsoft.graph.call entity.
        """
        from .content_sharing_sessions import content_sharing_sessions_request_builder

        return content_sharing_sessions_request_builder.ContentSharingSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def keep_alive(self) -> keep_alive_request_builder.KeepAliveRequestBuilder:
        """
        Provides operations to call the keepAlive method.
        """
        from .keep_alive import keep_alive_request_builder

        return keep_alive_request_builder.KeepAliveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mute(self) -> mute_request_builder.MuteRequestBuilder:
        """
        Provides operations to call the mute method.
        """
        from .mute import mute_request_builder

        return mute_request_builder.MuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.call entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def participants(self) -> participants_request_builder.ParticipantsRequestBuilder:
        """
        Provides operations to manage the participants property of the microsoft.graph.call entity.
        """
        from .participants import participants_request_builder

        return participants_request_builder.ParticipantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def play_prompt(self) -> play_prompt_request_builder.PlayPromptRequestBuilder:
        """
        Provides operations to call the playPrompt method.
        """
        from .play_prompt import play_prompt_request_builder

        return play_prompt_request_builder.PlayPromptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def record_response(self) -> record_response_request_builder.RecordResponseRequestBuilder:
        """
        Provides operations to call the recordResponse method.
        """
        from .record_response import record_response_request_builder

        return record_response_request_builder.RecordResponseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def redirect(self) -> redirect_request_builder.RedirectRequestBuilder:
        """
        Provides operations to call the redirect method.
        """
        from .redirect import redirect_request_builder

        return redirect_request_builder.RedirectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reject(self) -> reject_request_builder.RejectRequestBuilder:
        """
        Provides operations to call the reject method.
        """
        from .reject import reject_request_builder

        return reject_request_builder.RejectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribe_to_tone(self) -> subscribe_to_tone_request_builder.SubscribeToToneRequestBuilder:
        """
        Provides operations to call the subscribeToTone method.
        """
        from .subscribe_to_tone import subscribe_to_tone_request_builder

        return subscribe_to_tone_request_builder.SubscribeToToneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transfer(self) -> transfer_request_builder.TransferRequestBuilder:
        """
        Provides operations to call the transfer method.
        """
        from .transfer import transfer_request_builder

        return transfer_request_builder.TransferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unmute(self) -> unmute_request_builder.UnmuteRequestBuilder:
        """
        Provides operations to call the unmute method.
        """
        from .unmute import unmute_request_builder

        return unmute_request_builder.UnmuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_recording_status(self) -> update_recording_status_request_builder.UpdateRecordingStatusRequestBuilder:
        """
        Provides operations to call the updateRecordingStatus method.
        """
        from .update_recording_status import update_recording_status_request_builder

        return update_recording_status_request_builder.UpdateRecordingStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CallItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CallItemRequestBuilderGetQueryParameters():
        """
        Get calls from communications
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
    class CallItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CallItemRequestBuilder.CallItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CallItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

