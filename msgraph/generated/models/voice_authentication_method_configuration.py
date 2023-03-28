from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_configuration, authentication_method_target

from . import authentication_method_configuration

class VoiceAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new VoiceAuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.voiceAuthenticationMethodConfiguration"
        # A collection of groups that are enabled to use the authentication method. Expanded by default.
        self._include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
        # true if users can register office phones, otherwise, false.
        self._is_office_phone_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VoiceAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VoiceAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VoiceAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_configuration, authentication_method_target

        fields: Dict[str, Callable[[Any], None]] = {
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
            "isOfficePhoneAllowed": lambda n : setattr(self, 'is_office_phone_allowed', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[authentication_method_target.AuthenticationMethodTarget]]:
        """
        Gets the includeTargets property value. A collection of groups that are enabled to use the authentication method. Expanded by default.
        Returns: Optional[List[authentication_method_target.AuthenticationMethodTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None) -> None:
        """
        Sets the includeTargets property value. A collection of groups that are enabled to use the authentication method. Expanded by default.
        Args:
            value: Value to set for the include_targets property.
        """
        self._include_targets = value
    
    @property
    def is_office_phone_allowed(self,) -> Optional[bool]:
        """
        Gets the isOfficePhoneAllowed property value. true if users can register office phones, otherwise, false.
        Returns: Optional[bool]
        """
        return self._is_office_phone_allowed
    
    @is_office_phone_allowed.setter
    def is_office_phone_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOfficePhoneAllowed property value. true if users can register office phones, otherwise, false.
        Args:
            value: Value to set for the is_office_phone_allowed property.
        """
        self._is_office_phone_allowed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isOfficePhoneAllowed", self.is_office_phone_allowed)
    

