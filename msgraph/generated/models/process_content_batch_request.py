from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .process_content_request import ProcessContentRequest

@dataclass
class ProcessContentBatchRequest(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The contentToProcess property
    content_to_process: Optional[ProcessContentRequest] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A unique identifier provided by the client to correlate this specific request item within the batch.
    request_id: Optional[str] = None
    # The unique identifier (Object ID or UPN) of the user in whose context the content should be processed.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessContentBatchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessContentBatchRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProcessContentBatchRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .process_content_request import ProcessContentRequest

        from .process_content_request import ProcessContentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "contentToProcess": lambda n : setattr(self, 'content_to_process', n.get_object_value(ProcessContentRequest)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("contentToProcess", self.content_to_process)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("requestId", self.request_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

