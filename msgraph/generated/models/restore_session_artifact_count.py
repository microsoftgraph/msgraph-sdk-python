from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RestoreSessionArtifactCount(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The number of artifacts whose restoration completed.
    completed: Optional[int] = None
    # The number of artifacts whose restoration failed.
    failed: Optional[int] = None
    # The number of artifacts whose restoration is in progress.
    in_progress: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of artifacts present in the restore session.
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreSessionArtifactCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreSessionArtifactCount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestoreSessionArtifactCount()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completed": lambda n : setattr(self, 'completed', n.get_int_value()),
            "failed": lambda n : setattr(self, 'failed', n.get_int_value()),
            "inProgress": lambda n : setattr(self, 'in_progress', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_int_value("completed", self.completed)
        writer.write_int_value("failed", self.failed)
        writer.write_int_value("inProgress", self.in_progress)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

