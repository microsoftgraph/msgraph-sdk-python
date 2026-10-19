from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BatchRecordDecisionsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The decision property
    decision: Optional[str] = None
    # The justification property
    justification: Optional[str] = None
    # The principalId property
    principal_id: Optional[str] = None
    # The resourceId property
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchRecordDecisionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchRecordDecisionsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchRecordDecisionsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
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
        writer.write_str_value("decision", self.decision)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    

