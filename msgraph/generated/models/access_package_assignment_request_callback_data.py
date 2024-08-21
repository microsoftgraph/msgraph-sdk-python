from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
    from .custom_extension_data import CustomExtensionData

from .custom_extension_data import CustomExtensionData

@dataclass
class AccessPackageAssignmentRequestCallbackData(CustomExtensionData):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageAssignmentRequestCallbackData"
    # Details for the callback.
    custom_extension_stage_instance_detail: Optional[str] = None
    # Unique identifier of the callout to the custom extension.
    custom_extension_stage_instance_id: Optional[str] = None
    # Indicates the stage at which the custom callout extension is executed. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
    stage: Optional[AccessPackageCustomExtensionStage] = None
    # Allow the extension to be able to deny or cancel the request submitted by the requestor. The supported values are Denied and Canceled. This property can only be set for an assignmentRequestCreated stage.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentRequestCallbackData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestCallbackData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentRequestCallbackData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
        from .custom_extension_data import CustomExtensionData

        from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
        from .custom_extension_data import CustomExtensionData

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtensionStageInstanceDetail": lambda n : setattr(self, 'custom_extension_stage_instance_detail', n.get_str_value()),
            "customExtensionStageInstanceId": lambda n : setattr(self, 'custom_extension_stage_instance_id', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(AccessPackageCustomExtensionStage)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("customExtensionStageInstanceDetail", self.custom_extension_stage_instance_detail)
        writer.write_str_value("customExtensionStageInstanceId", self.custom_extension_stage_instance_id)
        writer.write_enum_value("stage", self.stage)
        writer.write_str_value("state", self.state)
    

