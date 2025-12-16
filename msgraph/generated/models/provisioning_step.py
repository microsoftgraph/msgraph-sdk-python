from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .details_info import DetailsInfo
    from .provisioning_result import ProvisioningResult
    from .provisioning_step_type import ProvisioningStepType

@dataclass
class ProvisioningStep(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Summary of what occurred during the step.
    description: Optional[str] = None
    # Details of what occurred during the step.
    details: Optional[DetailsInfo] = None
    # Name of the step.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of step. The possible values are: import, scoping, matching, processing, referenceResolution, export, unknownFutureValue.
    provisioning_step_type: Optional[ProvisioningStepType] = None
    # Status of the step. The possible values are: success, warning,  failure, skipped, unknownFutureValue.
    status: Optional[ProvisioningResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisioningStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningStep
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningStep()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .details_info import DetailsInfo
        from .provisioning_result import ProvisioningResult
        from .provisioning_step_type import ProvisioningStepType

        from .details_info import DetailsInfo
        from .provisioning_result import ProvisioningResult
        from .provisioning_step_type import ProvisioningStepType

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(DetailsInfo)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioningStepType": lambda n : setattr(self, 'provisioning_step_type', n.get_enum_value(ProvisioningStepType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProvisioningResult)),
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
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("provisioningStepType", self.provisioning_step_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

