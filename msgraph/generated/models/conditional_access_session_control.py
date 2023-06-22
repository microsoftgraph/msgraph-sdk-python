from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, persistent_browser_session_control, sign_in_frequency_session_control

@dataclass
class ConditionalAccessSessionControl(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies whether the session control is enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessSessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessSessionControl
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationEnforcedRestrictionsSessionControl".casefold():
            from . import application_enforced_restrictions_session_control

            return application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudAppSecuritySessionControl".casefold():
            from . import cloud_app_security_session_control

            return cloud_app_security_session_control.CloudAppSecuritySessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.persistentBrowserSessionControl".casefold():
            from . import persistent_browser_session_control

            return persistent_browser_session_control.PersistentBrowserSessionControl()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.signInFrequencySessionControl".casefold():
            from . import sign_in_frequency_session_control

            return sign_in_frequency_session_control.SignInFrequencySessionControl()
        return ConditionalAccessSessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, persistent_browser_session_control, sign_in_frequency_session_control

        from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, persistent_browser_session_control, sign_in_frequency_session_control

        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

