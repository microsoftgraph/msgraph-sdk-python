from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_events_flow import AuthenticationEventsFlow
    from .on_attribute_collection_handler import OnAttributeCollectionHandler
    from .on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
    from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler
    from .on_user_create_start_handler import OnUserCreateStartHandler

from .authentication_events_flow import AuthenticationEventsFlow

@dataclass
class ExternalUsersSelfServiceSignUpEventsFlow(AuthenticationEventsFlow):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow"
    # The configuration for what to invoke when attributes are ready to be collected from the user.
    on_attribute_collection: Optional[OnAttributeCollectionHandler] = None
    # Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.  Supports $filter (eq). See support for filtering on user flows for syntax information.
    on_authentication_method_load_start: Optional[OnAuthenticationMethodLoadStartHandler] = None
    # Required. The configuration for what to invoke when an authentication flow is ready to be initiated.
    on_interactive_auth_flow_start: Optional[OnInteractiveAuthFlowStartHandler] = None
    # The configuration for what to invoke during user creation.
    on_user_create_start: Optional[OnUserCreateStartHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalUsersSelfServiceSignUpEventsFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalUsersSelfServiceSignUpEventsFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalUsersSelfServiceSignUpEventsFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_events_flow import AuthenticationEventsFlow
        from .on_attribute_collection_handler import OnAttributeCollectionHandler
        from .on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
        from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler
        from .on_user_create_start_handler import OnUserCreateStartHandler

        from .authentication_events_flow import AuthenticationEventsFlow
        from .on_attribute_collection_handler import OnAttributeCollectionHandler
        from .on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
        from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler
        from .on_user_create_start_handler import OnUserCreateStartHandler

        fields: Dict[str, Callable[[Any], None]] = {
            "onAttributeCollection": lambda n : setattr(self, 'on_attribute_collection', n.get_object_value(OnAttributeCollectionHandler)),
            "onAuthenticationMethodLoadStart": lambda n : setattr(self, 'on_authentication_method_load_start', n.get_object_value(OnAuthenticationMethodLoadStartHandler)),
            "onInteractiveAuthFlowStart": lambda n : setattr(self, 'on_interactive_auth_flow_start', n.get_object_value(OnInteractiveAuthFlowStartHandler)),
            "onUserCreateStart": lambda n : setattr(self, 'on_user_create_start', n.get_object_value(OnUserCreateStartHandler)),
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
        writer.write_object_value("onAttributeCollection", self.on_attribute_collection)
        writer.write_object_value("onAuthenticationMethodLoadStart", self.on_authentication_method_load_start)
        writer.write_object_value("onInteractiveAuthFlowStart", self.on_interactive_auth_flow_start)
        writer.write_object_value("onUserCreateStart", self.on_user_create_start)
    

