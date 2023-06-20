from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_configuration, authentication_method_target

from . import authentication_method_configuration

@dataclass
class VoiceAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    odata_type = "#microsoft.graph.voiceAuthenticationMethodConfiguration"
    # A collection of groups that are enabled to use the authentication method. Expanded by default.
    include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
    # true if users can register office phones, otherwise, false.
    is_office_phone_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VoiceAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VoiceAuthenticationMethodConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VoiceAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_configuration, authentication_method_target

        from . import authentication_method_configuration, authentication_method_target

        fields: Dict[str, Callable[[Any], None]] = {
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
            "isOfficePhoneAllowed": lambda n : setattr(self, 'is_office_phone_allowed', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isOfficePhoneAllowed", self.is_office_phone_allowed)
    

