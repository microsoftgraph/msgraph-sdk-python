from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import details_info, provisioning_result, provisioning_step_type

@dataclass
class ProvisioningStep(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Summary of what occurred during the step.
    description: Optional[str] = None
    # Details of what occurred during the step.
    details: Optional[details_info.DetailsInfo] = None
    # Name of the step.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of step. Possible values are: import, scoping, matching, processing, referenceResolution, export, unknownFutureValue.
    provisioning_step_type: Optional[provisioning_step_type.ProvisioningStepType] = None
    # Status of the step. Possible values are: success, warning,  failure, skipped, unknownFutureValue.
    status: Optional[provisioning_result.ProvisioningResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningStep
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningStep()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import details_info, provisioning_result, provisioning_step_type

        from . import details_info, provisioning_result, provisioning_step_type

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(details_info.DetailsInfo)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioningStepType": lambda n : setattr(self, 'provisioning_step_type', n.get_enum_value(provisioning_step_type.ProvisioningStepType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(provisioning_result.ProvisioningResult)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("provisioningStepType", self.provisioning_step_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

