from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .process_content_response import ProcessContentResponse

@dataclass
class ProcessContentResponses(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier that matches the requestId provided in the corresponding processContentBatchRequest.
    request_id: Optional[str] = None
    # The results property
    results: Optional[ProcessContentResponse] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessContentResponses:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessContentResponses
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProcessContentResponses()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .process_content_response import ProcessContentResponse

        from .process_content_response import ProcessContentResponse

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_object_value(ProcessContentResponse)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("requestId", self.request_id)
        writer.write_object_value("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

