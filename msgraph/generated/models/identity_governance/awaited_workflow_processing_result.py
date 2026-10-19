from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
    from .workflow_subject import WorkflowSubject

@dataclass
class AwaitedWorkflowProcessingResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingStatus property
    processing_status: Optional[LifecycleWorkflowProcessingStatus] = None
    # A collection of reasons for the current processing status. May be empty.
    status_reasons: Optional[list[str]] = None
    # The subject that was processed by the workflow.
    subject: Optional[WorkflowSubject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwaitedWorkflowProcessingResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwaitedWorkflowProcessingResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwaitedWorkflowProcessingResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .workflow_subject import WorkflowSubject

        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .workflow_subject import WorkflowSubject

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(LifecycleWorkflowProcessingStatus)),
            "statusReasons": lambda n : setattr(self, 'status_reasons', n.get_collection_of_primitive_values(str)),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(WorkflowSubject)),
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
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_collection_of_primitive_values("statusReasons", self.status_reasons)
        writer.write_object_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    

