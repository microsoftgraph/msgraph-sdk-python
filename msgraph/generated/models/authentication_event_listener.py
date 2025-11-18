from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_conditions import AuthenticationConditions
    from .entity import Entity
    from .on_attribute_collection_listener import OnAttributeCollectionListener
    from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
    from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
    from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
    from .on_email_otp_send_listener import OnEmailOtpSendListener
    from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener
    from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
    from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
    from .on_user_create_start_listener import OnUserCreateStartListener

from .entity import Entity

@dataclass
class AuthenticationEventListener(Entity, Parsable):
    # The identifier of the authenticationEventsFlow object.
    authentication_events_flow_id: Optional[str] = None
    # The conditions on which this authenticationEventListener should trigger.
    conditions: Optional[AuthenticationConditions] = None
    # The display name of the listener.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationEventListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationEventListener
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionListener".casefold():
            from .on_attribute_collection_listener import OnAttributeCollectionListener

            return OnAttributeCollectionListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionStartListener".casefold():
            from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener

            return OnAttributeCollectionStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionSubmitListener".casefold():
            from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener

            return OnAttributeCollectionSubmitListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAuthenticationMethodLoadStartListener".casefold():
            from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener

            return OnAuthenticationMethodLoadStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onEmailOtpSendListener".casefold():
            from .on_email_otp_send_listener import OnEmailOtpSendListener

            return OnEmailOtpSendListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onFraudProtectionLoadStartListener".casefold():
            from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener

            return OnFraudProtectionLoadStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onInteractiveAuthFlowStartListener".casefold():
            from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener

            return OnInteractiveAuthFlowStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartListener".casefold():
            from .on_token_issuance_start_listener import OnTokenIssuanceStartListener

            return OnTokenIssuanceStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onUserCreateStartListener".casefold():
            from .on_user_create_start_listener import OnUserCreateStartListener

            return OnUserCreateStartListener()
        return AuthenticationEventListener()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_conditions import AuthenticationConditions
        from .entity import Entity
        from .on_attribute_collection_listener import OnAttributeCollectionListener
        from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
        from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
        from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
        from .on_email_otp_send_listener import OnEmailOtpSendListener
        from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener
        from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
        from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
        from .on_user_create_start_listener import OnUserCreateStartListener

        from .authentication_conditions import AuthenticationConditions
        from .entity import Entity
        from .on_attribute_collection_listener import OnAttributeCollectionListener
        from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
        from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
        from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
        from .on_email_otp_send_listener import OnEmailOtpSendListener
        from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener
        from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
        from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
        from .on_user_create_start_listener import OnUserCreateStartListener

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationEventsFlowId": lambda n : setattr(self, 'authentication_events_flow_id', n.get_str_value()),
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(AuthenticationConditions)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("authenticationEventsFlowId", self.authentication_events_flow_id)
        writer.write_object_value("conditions", self.conditions)
        writer.write_str_value("displayName", self.display_name)
    

