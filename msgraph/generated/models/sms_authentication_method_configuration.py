from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .sms_authentication_method_target import SmsAuthenticationMethodTarget

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class SmsAuthenticationMethodConfiguration(AuthenticationMethodConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.smsAuthenticationMethodConfiguration"
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[List[SmsAuthenticationMethodTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(SmsAuthenticationMethodTarget)),
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
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

