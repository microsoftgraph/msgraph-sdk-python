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
    from ..models.directory import Directory
    from ..models.o_data_errors.o_data_error import ODataError
    from .administrative_units.administrative_units_request_builder import AdministrativeUnitsRequestBuilder
    from .attribute_sets.attribute_sets_request_builder import AttributeSetsRequestBuilder
    from .custom_security_attribute_definitions.custom_security_attribute_definitions_request_builder import CustomSecurityAttributeDefinitionsRequestBuilder
    from .deleted_items.deleted_items_request_builder import DeletedItemsRequestBuilder
    from .device_local_credentials.device_local_credentials_request_builder import DeviceLocalCredentialsRequestBuilder
    from .federation_configurations.federation_configurations_request_builder import FederationConfigurationsRequestBuilder
    from .on_premises_synchronization.on_premises_synchronization_request_builder import OnPremisesSynchronizationRequestBuilder
    from .public_key_infrastructure.public_key_infrastructure_request_builder import PublicKeyInfrastructureRequestBuilder
    from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder
    from .subscriptions_with_commerce_subscription_id.subscriptions_with_commerce_subscription_id_request_builder import SubscriptionsWithCommerceSubscriptionIdRequestBuilder

class DirectoryRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the directory singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DirectoryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DirectoryRequestBuilderGetQueryParameters]] = None) -> Optional[Directory]:
        """
        Get directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Directory]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.directory import Directory

        return await self.request_adapter.send_async(request_info, Directory, error_mapping)
    
    async def patch(self,body: Directory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Directory]:
        """
        Update directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Directory]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.directory import Directory

        return await self.request_adapter.send_async(request_info, Directory, error_mapping)
    
    def subscriptions_with_commerce_subscription_id(self,commerce_subscription_id: str) -> SubscriptionsWithCommerceSubscriptionIdRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.directory entity.
        param commerce_subscription_id: Alternate key of companySubscription
        Returns: SubscriptionsWithCommerceSubscriptionIdRequestBuilder
        """
        if commerce_subscription_id is None:
            raise TypeError("commerce_subscription_id cannot be null.")
        from .subscriptions_with_commerce_subscription_id.subscriptions_with_commerce_subscription_id_request_builder import SubscriptionsWithCommerceSubscriptionIdRequestBuilder

        return SubscriptionsWithCommerceSubscriptionIdRequestBuilder(self.request_adapter, self.path_parameters, commerce_subscription_id)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DirectoryRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Directory, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update directory
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
    
    def with_url(self,raw_url: str) -> DirectoryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DirectoryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DirectoryRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def administrative_units(self) -> AdministrativeUnitsRequestBuilder:
        """
        Provides operations to manage the administrativeUnits property of the microsoft.graph.directory entity.
        """
        from .administrative_units.administrative_units_request_builder import AdministrativeUnitsRequestBuilder

        return AdministrativeUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attribute_sets(self) -> AttributeSetsRequestBuilder:
        """
        Provides operations to manage the attributeSets property of the microsoft.graph.directory entity.
        """
        from .attribute_sets.attribute_sets_request_builder import AttributeSetsRequestBuilder

        return AttributeSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_security_attribute_definitions(self) -> CustomSecurityAttributeDefinitionsRequestBuilder:
        """
        Provides operations to manage the customSecurityAttributeDefinitions property of the microsoft.graph.directory entity.
        """
        from .custom_security_attribute_definitions.custom_security_attribute_definitions_request_builder import CustomSecurityAttributeDefinitionsRequestBuilder

        return CustomSecurityAttributeDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deleted_items(self) -> DeletedItemsRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        """
        from .deleted_items.deleted_items_request_builder import DeletedItemsRequestBuilder

        return DeletedItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_local_credentials(self) -> DeviceLocalCredentialsRequestBuilder:
        """
        Provides operations to manage the deviceLocalCredentials property of the microsoft.graph.directory entity.
        """
        from .device_local_credentials.device_local_credentials_request_builder import DeviceLocalCredentialsRequestBuilder

        return DeviceLocalCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federation_configurations(self) -> FederationConfigurationsRequestBuilder:
        """
        Provides operations to manage the federationConfigurations property of the microsoft.graph.directory entity.
        """
        from .federation_configurations.federation_configurations_request_builder import FederationConfigurationsRequestBuilder

        return FederationConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_synchronization(self) -> OnPremisesSynchronizationRequestBuilder:
        """
        Provides operations to manage the onPremisesSynchronization property of the microsoft.graph.directory entity.
        """
        from .on_premises_synchronization.on_premises_synchronization_request_builder import OnPremisesSynchronizationRequestBuilder

        return OnPremisesSynchronizationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def public_key_infrastructure(self) -> PublicKeyInfrastructureRequestBuilder:
        """
        Provides operations to manage the publicKeyInfrastructure property of the microsoft.graph.directory entity.
        """
        from .public_key_infrastructure.public_key_infrastructure_request_builder import PublicKeyInfrastructureRequestBuilder

        return PublicKeyInfrastructureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.directory entity.
        """
        from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder

        return SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DirectoryRequestBuilderGetQueryParameters():
        """
        Get directory
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
    class DirectoryRequestBuilderGetRequestConfiguration(RequestConfiguration[DirectoryRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DirectoryRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

