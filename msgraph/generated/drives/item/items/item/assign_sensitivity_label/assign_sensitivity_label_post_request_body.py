from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod

@dataclass
class AssignSensitivityLabelPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The assignmentMethod property
    assignment_method: Optional[SensitivityLabelAssignmentMethod] = None
    # The justificationText property
    justification_text: Optional[str] = None
    # The sensitivityLabelId property
    sensitivity_label_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignSensitivityLabelPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignSensitivityLabelPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignSensitivityLabelPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod

        from ......models.sensitivity_label_assignment_method import SensitivityLabelAssignmentMethod

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentMethod": lambda n : setattr(self, 'assignment_method', n.get_enum_value(SensitivityLabelAssignmentMethod)),
            "justificationText": lambda n : setattr(self, 'justification_text', n.get_str_value()),
            "sensitivityLabelId": lambda n : setattr(self, 'sensitivity_label_id', n.get_str_value()),
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
        writer.write_enum_value("assignmentMethod", self.assignment_method)
        writer.write_str_value("justificationText", self.justification_text)
        writer.write_str_value("sensitivityLabelId", self.sensitivity_label_id)
        writer.write_additional_data_value(self.additional_data)
    

