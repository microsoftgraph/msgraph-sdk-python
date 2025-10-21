from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_request_approval_stage_callback_configuration import AccessPackageRequestApprovalStageCallbackConfiguration
    from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

@dataclass
class CustomExtensionCallbackConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The maximum duration in ISO 8601 format that Microsoft Entra ID will wait for a resume action for the callout it sent to the logic app. The valid range for custom extensions in lifecycle workflows is five minutes to three hours. The valid range for custom extensions in entitlement management is between 5 minutes and 14 days. For example, PT3H refers to three hours, P3D refers to three days, PT10M refers to ten minutes.
    timeout_duration: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomExtensionCallbackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCallbackConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageRequestApprovalStageCallbackConfiguration".casefold():
            from .access_package_request_approval_stage_callback_configuration import AccessPackageRequestApprovalStageCallbackConfiguration

            return AccessPackageRequestApprovalStageCallbackConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.customTaskExtensionCallbackConfiguration".casefold():
            from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

            return CustomTaskExtensionCallbackConfiguration()
        return CustomExtensionCallbackConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_request_approval_stage_callback_configuration import AccessPackageRequestApprovalStageCallbackConfiguration
        from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

        from .access_package_request_approval_stage_callback_configuration import AccessPackageRequestApprovalStageCallbackConfiguration
        from .identity_governance.custom_task_extension_callback_configuration import CustomTaskExtensionCallbackConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeoutDuration": lambda n : setattr(self, 'timeout_duration', n.get_timedelta_value()),
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
        writer.write_timedelta_value("timeoutDuration", self.timeout_duration)
        writer.write_additional_data_value(self.additional_data)
    

