from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_assignment import PolicyAssignment

@dataclass
class EffectivePolicyAssignment(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyAssignment property
    policy_assignment: Optional[PolicyAssignment] = None
    # The type of the assigned policy; for example, TeamsMeetingPolicy and TeamsCallingPolicy.
    policy_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EffectivePolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EffectivePolicyAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EffectivePolicyAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_assignment import PolicyAssignment

        from .policy_assignment import PolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyAssignment": lambda n : setattr(self, 'policy_assignment', n.get_object_value(PolicyAssignment)),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_str_value()),
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
        writer.write_object_value("policyAssignment", self.policy_assignment)
        writer.write_str_value("policyType", self.policy_type)
        writer.write_additional_data_value(self.additional_data)
    

