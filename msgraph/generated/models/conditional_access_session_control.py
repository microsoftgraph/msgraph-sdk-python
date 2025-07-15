from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl
    from .cloud_app_security_session_control import CloudAppSecuritySessionControl
    from .persistent_browser_session_control import PersistentBrowserSessionControl
    from .secure_sign_in_session_control import SecureSignInSessionControl
    from .sign_in_frequency_session_control import SignInFrequencySessionControl

@dataclass
class ConditionalAccessSessionControl(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Specifies whether the session control is enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessSessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessSessionControl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationEnforcedRestrictionsSessionControl".casefold():
            from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl

            return ApplicationEnforcedRestrictionsSessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudAppSecuritySessionControl".casefold():
            from .cloud_app_security_session_control import CloudAppSecuritySessionControl

            return CloudAppSecuritySessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.persistentBrowserSessionControl".casefold():
            from .persistent_browser_session_control import PersistentBrowserSessionControl

            return PersistentBrowserSessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureSignInSessionControl".casefold():
            from .secure_sign_in_session_control import SecureSignInSessionControl

            return SecureSignInSessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.signInFrequencySessionControl".casefold():
            from .sign_in_frequency_session_control import SignInFrequencySessionControl

            return SignInFrequencySessionControl()
        return ConditionalAccessSessionControl()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl
        from .cloud_app_security_session_control import CloudAppSecuritySessionControl
        from .persistent_browser_session_control import PersistentBrowserSessionControl
        from .secure_sign_in_session_control import SecureSignInSessionControl
        from .sign_in_frequency_session_control import SignInFrequencySessionControl

        from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl
        from .cloud_app_security_session_control import CloudAppSecuritySessionControl
        from .persistent_browser_session_control import PersistentBrowserSessionControl
        from .secure_sign_in_session_control import SecureSignInSessionControl
        from .sign_in_frequency_session_control import SignInFrequencySessionControl

        fields: dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

