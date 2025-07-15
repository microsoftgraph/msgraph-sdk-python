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
class ConditionalAccessSessionControls(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
    application_enforced_restrictions: Optional[ApplicationEnforcedRestrictionsSessionControl] = None
    # Session control to apply cloud app security.
    cloud_app_security: Optional[CloudAppSecuritySessionControl] = None
    # Session control that determines whether it is acceptable for Microsoft Entra ID to extend existing sessions based on information collected prior to an outage or not.
    disable_resilience_defaults: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
    persistent_browser: Optional[PersistentBrowserSessionControl] = None
    # The secureSignInSession property
    secure_sign_in_session: Optional[SecureSignInSessionControl] = None
    # Session control to enforce signin frequency.
    sign_in_frequency: Optional[SignInFrequencySessionControl] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessSessionControls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessSessionControls
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessSessionControls()
    
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
            "applicationEnforcedRestrictions": lambda n : setattr(self, 'application_enforced_restrictions', n.get_object_value(ApplicationEnforcedRestrictionsSessionControl)),
            "cloudAppSecurity": lambda n : setattr(self, 'cloud_app_security', n.get_object_value(CloudAppSecuritySessionControl)),
            "disableResilienceDefaults": lambda n : setattr(self, 'disable_resilience_defaults', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "persistentBrowser": lambda n : setattr(self, 'persistent_browser', n.get_object_value(PersistentBrowserSessionControl)),
            "secureSignInSession": lambda n : setattr(self, 'secure_sign_in_session', n.get_object_value(SecureSignInSessionControl)),
            "signInFrequency": lambda n : setattr(self, 'sign_in_frequency', n.get_object_value(SignInFrequencySessionControl)),
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
        writer.write_object_value("applicationEnforcedRestrictions", self.application_enforced_restrictions)
        writer.write_object_value("cloudAppSecurity", self.cloud_app_security)
        writer.write_bool_value("disableResilienceDefaults", self.disable_resilience_defaults)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("persistentBrowser", self.persistent_browser)
        writer.write_object_value("secureSignInSession", self.secure_sign_in_session)
        writer.write_object_value("signInFrequency", self.sign_in_frequency)
        writer.write_additional_data_value(self.additional_data)
    

