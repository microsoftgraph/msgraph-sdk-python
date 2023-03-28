from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_configuration, authentication_method_target, external_email_otp_state

from . import authentication_method_configuration

class EmailAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new EmailAuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.emailAuthenticationMethodConfiguration"
        # Determines whether email OTP is usable by external users for authentication. Possible values are: default, enabled, disabled, unknownFutureValue. Tenants in the default state who did not use public preview will automatically have email OTP enabled beginning in October 2021.
        self._allow_external_id_to_use_email_otp: Optional[external_email_otp_state.ExternalEmailOtpState] = None
        # A collection of groups that are enabled to use the authentication method.
        self._include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
    
    @property
    def allow_external_id_to_use_email_otp(self,) -> Optional[external_email_otp_state.ExternalEmailOtpState]:
        """
        Gets the allowExternalIdToUseEmailOtp property value. Determines whether email OTP is usable by external users for authentication. Possible values are: default, enabled, disabled, unknownFutureValue. Tenants in the default state who did not use public preview will automatically have email OTP enabled beginning in October 2021.
        Returns: Optional[external_email_otp_state.ExternalEmailOtpState]
        """
        return self._allow_external_id_to_use_email_otp
    
    @allow_external_id_to_use_email_otp.setter
    def allow_external_id_to_use_email_otp(self,value: Optional[external_email_otp_state.ExternalEmailOtpState] = None) -> None:
        """
        Sets the allowExternalIdToUseEmailOtp property value. Determines whether email OTP is usable by external users for authentication. Possible values are: default, enabled, disabled, unknownFutureValue. Tenants in the default state who did not use public preview will automatically have email OTP enabled beginning in October 2021.
        Args:
            value: Value to set for the allow_external_id_to_use_email_otp property.
        """
        self._allow_external_id_to_use_email_otp = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_configuration, authentication_method_target, external_email_otp_state

        fields: Dict[str, Callable[[Any], None]] = {
            "allowExternalIdToUseEmailOtp": lambda n : setattr(self, 'allow_external_id_to_use_email_otp', n.get_enum_value(external_email_otp_state.ExternalEmailOtpState)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[authentication_method_target.AuthenticationMethodTarget]]:
        """
        Gets the includeTargets property value. A collection of groups that are enabled to use the authentication method.
        Returns: Optional[List[authentication_method_target.AuthenticationMethodTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None) -> None:
        """
        Sets the includeTargets property value. A collection of groups that are enabled to use the authentication method.
        Args:
            value: Value to set for the include_targets property.
        """
        self._include_targets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowExternalIdToUseEmailOtp", self.allow_external_id_to_use_email_otp)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

