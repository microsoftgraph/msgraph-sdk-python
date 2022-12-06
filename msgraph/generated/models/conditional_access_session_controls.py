from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_enforced_restrictions_session_control = lazy_import('msgraph.generated.models.application_enforced_restrictions_session_control')
cloud_app_security_session_control = lazy_import('msgraph.generated.models.cloud_app_security_session_control')
persistent_browser_session_control = lazy_import('msgraph.generated.models.persistent_browser_session_control')
sign_in_frequency_session_control = lazy_import('msgraph.generated.models.sign_in_frequency_session_control')

class ConditionalAccessSessionControls(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def application_enforced_restrictions(self,) -> Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl]:
        """
        Gets the applicationEnforcedRestrictions property value. Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
        Returns: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl]
        """
        return self._application_enforced_restrictions
    
    @application_enforced_restrictions.setter
    def application_enforced_restrictions(self,value: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl] = None) -> None:
        """
        Sets the applicationEnforcedRestrictions property value. Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
        Args:
            value: Value to set for the applicationEnforcedRestrictions property.
        """
        self._application_enforced_restrictions = value
    
    @property
    def cloud_app_security(self,) -> Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl]:
        """
        Gets the cloudAppSecurity property value. Session control to apply cloud app security.
        Returns: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl]
        """
        return self._cloud_app_security
    
    @cloud_app_security.setter
    def cloud_app_security(self,value: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl] = None) -> None:
        """
        Sets the cloudAppSecurity property value. Session control to apply cloud app security.
        Args:
            value: Value to set for the cloudAppSecurity property.
        """
        self._cloud_app_security = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessSessionControls and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
        self._application_enforced_restrictions: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl] = None
        # Session control to apply cloud app security.
        self._cloud_app_security: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl] = None
        # Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
        self._disable_resilience_defaults: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
        self._persistent_browser: Optional[persistent_browser_session_control.PersistentBrowserSessionControl] = None
        # Session control to enforce signin frequency.
        self._sign_in_frequency: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl] = None
    
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
    
    @property
    def disable_resilience_defaults(self,) -> Optional[bool]:
        """
        Gets the disableResilienceDefaults property value. Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
        Returns: Optional[bool]
        """
        return self._disable_resilience_defaults
    
    @disable_resilience_defaults.setter
    def disable_resilience_defaults(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableResilienceDefaults property value. Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
        Args:
            value: Value to set for the disableResilienceDefaults property.
        """
        self._disable_resilience_defaults = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_enforced_restrictions": lambda n : setattr(self, 'application_enforced_restrictions', n.get_object_value(application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl)),
            "cloud_app_security": lambda n : setattr(self, 'cloud_app_security', n.get_object_value(cloud_app_security_session_control.CloudAppSecuritySessionControl)),
            "disable_resilience_defaults": lambda n : setattr(self, 'disable_resilience_defaults', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "persistent_browser": lambda n : setattr(self, 'persistent_browser', n.get_object_value(persistent_browser_session_control.PersistentBrowserSessionControl)),
            "sign_in_frequency": lambda n : setattr(self, 'sign_in_frequency', n.get_object_value(sign_in_frequency_session_control.SignInFrequencySessionControl)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def persistent_browser(self,) -> Optional[persistent_browser_session_control.PersistentBrowserSessionControl]:
        """
        Gets the persistentBrowser property value. Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
        Returns: Optional[persistent_browser_session_control.PersistentBrowserSessionControl]
        """
        return self._persistent_browser
    
    @persistent_browser.setter
    def persistent_browser(self,value: Optional[persistent_browser_session_control.PersistentBrowserSessionControl] = None) -> None:
        """
        Sets the persistentBrowser property value. Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
        Args:
            value: Value to set for the persistentBrowser property.
        """
        self._persistent_browser = value
    
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
    
    @property
    def sign_in_frequency(self,) -> Optional[sign_in_frequency_session_control.SignInFrequencySessionControl]:
        """
        Gets the signInFrequency property value. Session control to enforce signin frequency.
        Returns: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl]
        """
        return self._sign_in_frequency
    
    @sign_in_frequency.setter
    def sign_in_frequency(self,value: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl] = None) -> None:
        """
        Sets the signInFrequency property value. Session control to enforce signin frequency.
        Args:
            value: Value to set for the signInFrequency property.
        """
        self._sign_in_frequency = value
    

