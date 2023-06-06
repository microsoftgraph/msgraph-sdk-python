from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LoginPageTextVisibilitySettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The hideAccountResetCredentials property
    hide_account_reset_credentials: Optional[bool] = None
    # The hideCannotAccessYourAccount property
    hide_cannot_access_your_account: Optional[bool] = None
    # The hideForgotMyPassword property
    hide_forgot_my_password: Optional[bool] = None
    # The hidePrivacyAndCookies property
    hide_privacy_and_cookies: Optional[bool] = None
    # The hideResetItNow property
    hide_reset_it_now: Optional[bool] = None
    # The hideTermsOfUse property
    hide_terms_of_use: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LoginPageTextVisibilitySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LoginPageTextVisibilitySettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LoginPageTextVisibilitySettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "hideAccountResetCredentials": lambda n : setattr(self, 'hide_account_reset_credentials', n.get_bool_value()),
            "hideCannotAccessYourAccount": lambda n : setattr(self, 'hide_cannot_access_your_account', n.get_bool_value()),
            "hideForgotMyPassword": lambda n : setattr(self, 'hide_forgot_my_password', n.get_bool_value()),
            "hidePrivacyAndCookies": lambda n : setattr(self, 'hide_privacy_and_cookies', n.get_bool_value()),
            "hideResetItNow": lambda n : setattr(self, 'hide_reset_it_now', n.get_bool_value()),
            "hideTermsOfUse": lambda n : setattr(self, 'hide_terms_of_use', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("hideAccountResetCredentials", self.hide_account_reset_credentials)
        writer.write_bool_value("hideCannotAccessYourAccount", self.hide_cannot_access_your_account)
        writer.write_bool_value("hideForgotMyPassword", self.hide_forgot_my_password)
        writer.write_bool_value("hidePrivacyAndCookies", self.hide_privacy_and_cookies)
        writer.write_bool_value("hideResetItNow", self.hide_reset_it_now)
        writer.write_bool_value("hideTermsOfUse", self.hide_terms_of_use)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

