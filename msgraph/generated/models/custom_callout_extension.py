from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
    from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
    from .custom_authentication_extension import CustomAuthenticationExtension
    from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
    from .custom_extension_client_configuration import CustomExtensionClientConfiguration
    from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
    from .entity import Entity
    from .identity_governance.custom_task_extension import CustomTaskExtension
    from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
    from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
    from .on_otp_send_custom_extension import OnOtpSendCustomExtension
    from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

from .entity import Entity

@dataclass
class CustomCalloutExtension(Entity, Parsable):
    # Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.
    authentication_configuration: Optional[CustomExtensionAuthenticationConfiguration] = None
    # HTTP connection settings that define how long Microsoft Entra ID can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.
    client_configuration: Optional[CustomExtensionClientConfiguration] = None
    # Description for the customCalloutExtension object.
    description: Optional[str] = None
    # Display name for the customCalloutExtension object.
    display_name: Optional[str] = None
    # The type and details for configuring the endpoint to call the logic app's workflow.
    endpoint_configuration: Optional[CustomExtensionEndpointConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onOtpSendCustomExtension".casefold():
            from .on_otp_send_custom_extension import OnOtpSendCustomExtension

            return OnOtpSendCustomExtension()
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
        from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
        from .custom_extension_client_configuration import CustomExtensionClientConfiguration
        from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
        from .entity import Entity
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
        from .custom_extension_client_configuration import CustomExtensionClientConfiguration
        from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration
        from .entity import Entity
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationConfiguration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(CustomExtensionAuthenticationConfiguration)),
            "clientConfiguration": lambda n : setattr(self, 'client_configuration', n.get_object_value(CustomExtensionClientConfiguration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpointConfiguration": lambda n : setattr(self, 'endpoint_configuration', n.get_object_value(CustomExtensionEndpointConfiguration)),
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
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_object_value("clientConfiguration", self.client_configuration)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endpointConfiguration", self.endpoint_configuration)
    

