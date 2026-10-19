from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..custom_extension_data import CustomExtensionData
    from .custom_task_extension_operation_status import CustomTaskExtensionOperationStatus
    from .workflow_subject import WorkflowSubject

from ..custom_extension_data import CustomExtensionData

@dataclass
class CustomTaskExtensionResponseData(CustomExtensionData, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.customTaskExtensionResponseData"
    # The operationStatus property
    operation_status: Optional[CustomTaskExtensionOperationStatus] = None
    # A collection of status reason strings. May be empty.
    status_reasons: Optional[list[str]] = None
    # The workflow subject that was processed by the custom task extension.
    target_subject: Optional[WorkflowSubject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomTaskExtensionResponseData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionResponseData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomTaskExtensionResponseData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..custom_extension_data import CustomExtensionData
        from .custom_task_extension_operation_status import CustomTaskExtensionOperationStatus
        from .workflow_subject import WorkflowSubject

        from ..custom_extension_data import CustomExtensionData
        from .custom_task_extension_operation_status import CustomTaskExtensionOperationStatus
        from .workflow_subject import WorkflowSubject

        fields: dict[str, Callable[[Any], None]] = {
            "operationStatus": lambda n : setattr(self, 'operation_status', n.get_enum_value(CustomTaskExtensionOperationStatus)),
            "statusReasons": lambda n : setattr(self, 'status_reasons', n.get_collection_of_primitive_values(str)),
            "targetSubject": lambda n : setattr(self, 'target_subject', n.get_object_value(WorkflowSubject)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("operationStatus", self.operation_status)
        writer.write_collection_of_primitive_values("statusReasons", self.status_reasons)
        writer.write_object_value("targetSubject", self.target_subject)
    

