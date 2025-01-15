from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .device import Device

from .authentication_method import AuthenticationMethod

@dataclass
class MicrosoftAuthenticatorAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod"
    # The date and time that this app was registered. This property is null if the device isn't registered for passwordless Phone Sign-In.
    created_date_time: Optional[datetime.datetime] = None
    # The registered device on which Microsoft Authenticator resides. This property is null if the device isn't registered for passwordless Phone Sign-In.
    device: Optional[Device] = None
    # Tags containing app metadata.
    device_tag: Optional[str] = None
    # The name of the device on which this app is registered.
    display_name: Optional[str] = None
    # Numerical version of this instance of the Authenticator app.
    phone_app_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftAuthenticatorAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAuthenticatorAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .device import Device

        from .authentication_method import AuthenticationMethod
        from .device import Device

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Device)),
            "deviceTag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "phoneAppVersion": lambda n : setattr(self, 'phone_app_version', n.get_str_value()),
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
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("phoneAppVersion", self.phone_app_version)
    

