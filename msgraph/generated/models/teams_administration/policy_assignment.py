from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_type import AssignmentType

@dataclass
class PolicyAssignment(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The assignmentType property
    assignment_type: Optional[AssignmentType] = None
    # Represents the name of the policy.
    display_name: Optional[str] = None
    # Represents the group identifier.
    group_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the unique identifier for the policy.
    policy_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_type import AssignmentType

        from .assignment_type import AssignmentType

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(AssignmentType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
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
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_additional_data_value(self.additional_data)
    

