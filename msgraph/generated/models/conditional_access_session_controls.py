from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, persistent_browser_session_control, sign_in_frequency_session_control

@dataclass
class ConditionalAccessSessionControls(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
    application_enforced_restrictions: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl] = None
    # Session control to apply cloud app security.
    cloud_app_security: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl] = None
    # Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
    disable_resilience_defaults: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
    persistent_browser: Optional[persistent_browser_session_control.PersistentBrowserSessionControl] = None
    # Session control to enforce signin frequency.
    sign_in_frequency: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessSessionControls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessSessionControls
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessSessionControls()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, persistent_browser_session_control, sign_in_frequency_session_control

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationEnforcedRestrictions": lambda n : setattr(self, 'application_enforced_restrictions', n.get_object_value(application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl)),
            "cloudAppSecurity": lambda n : setattr(self, 'cloud_app_security', n.get_object_value(cloud_app_security_session_control.CloudAppSecuritySessionControl)),
            "disableResilienceDefaults": lambda n : setattr(self, 'disable_resilience_defaults', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "persistentBrowser": lambda n : setattr(self, 'persistent_browser', n.get_object_value(persistent_browser_session_control.PersistentBrowserSessionControl)),
            "signInFrequency": lambda n : setattr(self, 'sign_in_frequency', n.get_object_value(sign_in_frequency_session_control.SignInFrequencySessionControl)),
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
        writer.write_object_value("applicationEnforcedRestrictions", self.application_enforced_restrictions)
        writer.write_object_value("cloudAppSecurity", self.cloud_app_security)
        writer.write_bool_value("disableResilienceDefaults", self.disable_resilience_defaults)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("persistentBrowser", self.persistent_browser)
        writer.write_object_value("signInFrequency", self.sign_in_frequency)
        writer.write_additional_data_value(self.additional_data)
    

