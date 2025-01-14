from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
    from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource
    from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource

@dataclass
class AccessReviewInstanceDecisionItemResource(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Display name of the resource
    display_name: Optional[str] = None
    # Identifier of the resource
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of resource. Types include: Group, ServicePrincipal, DirectoryRole, AzureRole, AccessPackageAssignmentPolicy.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewInstanceDecisionItemResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource".casefold():
            from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource

            return AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource".casefold():
            from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource

            return AccessReviewInstanceDecisionItemAzureRoleResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource".casefold():
            from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource

            return AccessReviewInstanceDecisionItemServicePrincipalResource()
        return AccessReviewInstanceDecisionItemResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
        from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource
        from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource

        from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
        from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource
        from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

