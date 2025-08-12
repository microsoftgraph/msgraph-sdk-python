from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_callout_extension import CustomCalloutExtension
    from .custom_extension_behavior_on_error import CustomExtensionBehaviorOnError
    from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
    from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
    from .on_otp_send_custom_extension import OnOtpSendCustomExtension
    from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

from .custom_callout_extension import CustomCalloutExtension

@dataclass
class CustomAuthenticationExtension(CustomCalloutExtension, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customAuthenticationExtension"
    # The behaviour on error for the custom authentication extension.
    behavior_on_error: Optional[CustomExtensionBehaviorOnError] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAuthenticationExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAuthenticationExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
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
        return CustomAuthenticationExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_behavior_on_error import CustomExtensionBehaviorOnError
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_behavior_on_error import CustomExtensionBehaviorOnError
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        fields: dict[str, Callable[[Any], None]] = {
            "behaviorOnError": lambda n : setattr(self, 'behavior_on_error', n.get_object_value(CustomExtensionBehaviorOnError)),
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
        writer.write_object_value("behaviorOnError", self.behavior_on_error)
    

