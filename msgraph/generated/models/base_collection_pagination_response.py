from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, TypeVar, Generic

from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter, \
    ParsableFactory
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton

from generated.models.entity import Entity
from generated.models.o_data_errors.o_data_error import ODataError

T = TypeVar('T', bound=Entity)


@dataclass
class BaseCollectionPaginationResponse(AdditionalDataHolder, BackedModel, Parsable, Generic[T]):
    # Stores the request adapter used for paging when an odata_next_link is available
    request_adapter: RequestAdapter = field(default=None, repr=False)
    # Stores the generic type so it can be used in the get_field_deserializers method
    entity: T = field(default=Entity)
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # The OdataNextLink property
    odata_next_link: Optional[str] = None
    value: Optional[List[T]] = None

    @classmethod
    def create_from_discriminator_value(cls, parse_node: Optional[ParseNode] = None) -> BaseCollectionPaginationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseCollectionPaginationCountResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return cls()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.nextLink": lambda n : setattr(self, 'odata_next_link', n.get_str_value()),
            "value": lambda n: setattr(self, 'value', n.get_collection_of_object_values(self.entity)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.nextLink", self.odata_next_link)
        writer.write_collection_of_object_values("value", self.value)
        writer.write_additional_data_value(self.additional_data)

    def request_information(self, method: Method = Method.GET) -> RequestInformation:
        request_info = RequestInformation()
        request_info.url = self.odata_next_link
        request_info.http_method = method
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info

    async def __anext__(self):
        if not self.value:
            raise StopAsyncIteration

        try:
            return self.value
        finally:
            if self.odata_next_link:
                error_mapping: Dict[str, ParsableFactory] = {
                    "4XX": ODataError,
                    "5XX": ODataError,
                }
                result = await BaseCollectionPaginationResponse.request_adapter.send_async(
                    request_info=self.request_information(),
                    parsable_factory=type(self),
                    error_map=error_mapping
                )
                self.value = result.value
                self.additional_data = result.additional_data
                self.odata_next_link = result.odata_next_link
            else:
                self.value = None

    def __aiter__(self):
        return self
