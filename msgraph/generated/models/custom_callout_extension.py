from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
    from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
    from .custom_authentication_extension import CustomAuthenticationExtension
    from .entity import Entity
    from .identity_governance.custom_task_extension import CustomTaskExtension
    from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
    from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
    from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

from .entity import Entity

@dataclass
class CustomCalloutExtension(Entity, Parsable):
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomCalloutExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomCalloutExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequestWorkflowExtension".casefold():
            from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension

            return AccessPackageAssignmentRequestWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentWorkflowExtension".casefold():
            from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension

            return AccessPackageAssignmentWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAuthenticationExtension".casefold():
            from .custom_authentication_extension import CustomAuthenticationExtension

            return CustomAuthenticationExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.customTaskExtension".casefold():
            from .identity_governance.custom_task_extension import CustomTaskExtension

            return CustomTaskExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionStartCustomExtension".casefold():
            from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension

            return OnAttributeCollectionStartCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionSubmitCustomExtension".casefold():
            from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension

            return OnAttributeCollectionSubmitCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartCustomExtension".casefold():
            from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

            return OnTokenIssuanceStartCustomExtension()
        return CustomCalloutExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .entity import Entity
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .entity import Entity
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        fields: dict[str, Callable[[Any], None]] = {
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
    

