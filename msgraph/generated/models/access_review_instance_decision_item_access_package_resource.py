from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

@dataclass
class AccessReviewInstanceDecisionItemAccessPackageResource(AccessReviewInstanceDecisionItemResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageResource"
    # Display name of the access package assignment policy through which access is granted.
    access_package_assignment_policy_display_name: Optional[str] = None
    # Identifier of the access package assignment policy through which access is granted.
    access_package_assignment_policy_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewInstanceDecisionItemAccessPackageResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemAccessPackageResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInstanceDecisionItemAccessPackageResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentPolicyDisplayName": lambda n : setattr(self, 'access_package_assignment_policy_display_name', n.get_str_value()),
            "accessPackageAssignmentPolicyId": lambda n : setattr(self, 'access_package_assignment_policy_id', n.get_str_value()),
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
        writer.write_str_value("accessPackageAssignmentPolicyDisplayName", self.access_package_assignment_policy_display_name)
        writer.write_str_value("accessPackageAssignmentPolicyId", self.access_package_assignment_policy_id)
    

