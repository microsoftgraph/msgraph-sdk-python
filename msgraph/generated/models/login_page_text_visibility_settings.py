from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LoginPageTextVisibilitySettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Option to hide the self-service password reset (SSPR) hyperlinks such as 'Can't access your account?', 'Forgot my password' and 'Reset it now' on the sign-in form.
    hide_account_reset_credentials: Optional[bool] = None
    # Option to hide the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in form.
    hide_cannot_access_your_account: Optional[bool] = None
    # Option to hide the self-service password reset (SSPR) 'Forgot my password' hyperlink on the sign-in form.
    hide_forgot_my_password: Optional[bool] = None
    # Option to hide the 'Privacy & Cookies' hyperlink in the footer.
    hide_privacy_and_cookies: Optional[bool] = None
    # Option to hide the self-service password reset (SSPR) 'reset it now' hyperlink on the sign-in form.
    hide_reset_it_now: Optional[bool] = None
    # Option to hide the 'Terms of Use' hyperlink in the footer.
    hide_terms_of_use: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoginPageTextVisibilitySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoginPageTextVisibilitySettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoginPageTextVisibilitySettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("hideAccountResetCredentials", self.hide_account_reset_credentials)
        writer.write_bool_value("hideCannotAccessYourAccount", self.hide_cannot_access_your_account)
        writer.write_bool_value("hideForgotMyPassword", self.hide_forgot_my_password)
        writer.write_bool_value("hidePrivacyAndCookies", self.hide_privacy_and_cookies)
        writer.write_bool_value("hideResetItNow", self.hide_reset_it_now)
        writer.write_bool_value("hideTermsOfUse", self.hide_terms_of_use)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

