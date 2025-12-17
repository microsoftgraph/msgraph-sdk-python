from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .authentication_method_key_strength import AuthenticationMethodKeyStrength
    from .authentication_method_platform import AuthenticationMethodPlatform
    from .device import Device

from .authentication_method import AuthenticationMethod

@dataclass
class PlatformCredentialAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.platformCredentialAuthenticationMethod"
    # The date and time that this Platform Credential Key was registered.
    created_date_time: Optional[datetime.datetime] = None
    # The registered device on which this Platform Credential resides. Supports $expand. When you get a user's Platform Credential registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/platformCredentialAuthenticationMethod/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
    device: Optional[Device] = None
    # The name of the device on which Platform Credential is registered.
    display_name: Optional[str] = None
    # Key strength of this Platform Credential key. The possible values are: normal, weak, unknown.
    key_strength: Optional[AuthenticationMethodKeyStrength] = None
    # Platform on which this Platform Credential key is present. The possible values are: unknown, windows, macOS,iOS, android, linux.
    platform: Optional[AuthenticationMethodPlatform] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlatformCredentialAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlatformCredentialAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlatformCredentialAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .authentication_method_key_strength import AuthenticationMethodKeyStrength
        from .authentication_method_platform import AuthenticationMethodPlatform
        from .device import Device

        from .authentication_method import AuthenticationMethod
        from .authentication_method_key_strength import AuthenticationMethodKeyStrength
        from .authentication_method_platform import AuthenticationMethodPlatform
        from .device import Device

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Device)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "keyStrength": lambda n : setattr(self, 'key_strength', n.get_enum_value(AuthenticationMethodKeyStrength)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(AuthenticationMethodPlatform)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("device", self.device)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("keyStrength", self.key_strength)
        writer.write_enum_value("platform", self.platform)
    

