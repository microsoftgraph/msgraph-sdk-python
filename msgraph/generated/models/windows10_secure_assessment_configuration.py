from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class Windows10SecureAssessmentConfiguration(device_configuration.DeviceConfiguration):
    @property
    def allow_printing(self,) -> Optional[bool]:
        """
        Gets the allowPrinting property value. Indicates whether or not to allow the app from printing during the test.
        Returns: Optional[bool]
        """
        return self._allow_printing
    
    @allow_printing.setter
    def allow_printing(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPrinting property value. Indicates whether or not to allow the app from printing during the test.
        Args:
            value: Value to set for the allowPrinting property.
        """
        self._allow_printing = value
    
    @property
    def allow_screen_capture(self,) -> Optional[bool]:
        """
        Gets the allowScreenCapture property value. Indicates whether or not to allow screen capture capability during a test.
        Returns: Optional[bool]
        """
        return self._allow_screen_capture
    
    @allow_screen_capture.setter
    def allow_screen_capture(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowScreenCapture property value. Indicates whether or not to allow screen capture capability during a test.
        Args:
            value: Value to set for the allowScreenCapture property.
        """
        self._allow_screen_capture = value
    
    @property
    def allow_text_suggestion(self,) -> Optional[bool]:
        """
        Gets the allowTextSuggestion property value. Indicates whether or not to allow text suggestions during the test.
        Returns: Optional[bool]
        """
        return self._allow_text_suggestion
    
    @allow_text_suggestion.setter
    def allow_text_suggestion(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowTextSuggestion property value. Indicates whether or not to allow text suggestions during the test.
        Args:
            value: Value to set for the allowTextSuggestion property.
        """
        self._allow_text_suggestion = value
    
    @property
    def configuration_account(self,) -> Optional[str]:
        """
        Gets the configurationAccount property value. The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
        Returns: Optional[str]
        """
        return self._configuration_account
    
    @configuration_account.setter
    def configuration_account(self,value: Optional[str] = None) -> None:
        """
        Sets the configurationAccount property value. The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
        Args:
            value: Value to set for the configurationAccount property.
        """
        self._configuration_account = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10SecureAssessmentConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10SecureAssessmentConfiguration"
        # Indicates whether or not to allow the app from printing during the test.
        self._allow_printing: Optional[bool] = None
        # Indicates whether or not to allow screen capture capability during a test.
        self._allow_screen_capture: Optional[bool] = None
        # Indicates whether or not to allow text suggestions during the test.
        self._allow_text_suggestion: Optional[bool] = None
        # The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
        self._configuration_account: Optional[str] = None
        # Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
        self._launch_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10SecureAssessmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10SecureAssessmentConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10SecureAssessmentConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_printing": lambda n : setattr(self, 'allow_printing', n.get_bool_value()),
            "allow_screen_capture": lambda n : setattr(self, 'allow_screen_capture', n.get_bool_value()),
            "allow_text_suggestion": lambda n : setattr(self, 'allow_text_suggestion', n.get_bool_value()),
            "configuration_account": lambda n : setattr(self, 'configuration_account', n.get_str_value()),
            "launch_uri": lambda n : setattr(self, 'launch_uri', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def launch_uri(self,) -> Optional[str]:
        """
        Gets the launchUri property value. Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
        Returns: Optional[str]
        """
        return self._launch_uri
    
    @launch_uri.setter
    def launch_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the launchUri property value. Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
        Args:
            value: Value to set for the launchUri property.
        """
        self._launch_uri = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowPrinting", self.allow_printing)
        writer.write_bool_value("allowScreenCapture", self.allow_screen_capture)
        writer.write_bool_value("allowTextSuggestion", self.allow_text_suggestion)
        writer.write_str_value("configurationAccount", self.configuration_account)
        writer.write_str_value("launchUri", self.launch_uri)
    

