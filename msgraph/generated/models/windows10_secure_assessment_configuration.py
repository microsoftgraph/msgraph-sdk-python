from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10SecureAssessmentConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the secureAssessment resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10SecureAssessmentConfiguration"
    # Indicates whether or not to allow the app from printing during the test.
    allow_printing: Optional[bool] = None
    # Indicates whether or not to allow screen capture capability during a test.
    allow_screen_capture: Optional[bool] = None
    # Indicates whether or not to allow text suggestions during the test.
    allow_text_suggestion: Optional[bool] = None
    # The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
    configuration_account: Optional[str] = None
    # Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
    launch_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10SecureAssessmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10SecureAssessmentConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10SecureAssessmentConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration

        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "allowPrinting": lambda n : setattr(self, 'allow_printing', n.get_bool_value()),
            "allowScreenCapture": lambda n : setattr(self, 'allow_screen_capture', n.get_bool_value()),
            "allowTextSuggestion": lambda n : setattr(self, 'allow_text_suggestion', n.get_bool_value()),
            "configurationAccount": lambda n : setattr(self, 'configuration_account', n.get_str_value()),
            "launchUri": lambda n : setattr(self, 'launch_uri', n.get_str_value()),
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
        writer.write_bool_value("allowPrinting", self.allow_printing)
        writer.write_bool_value("allowScreenCapture", self.allow_screen_capture)
        writer.write_bool_value("allowTextSuggestion", self.allow_text_suggestion)
        writer.write_str_value("configurationAccount", self.configuration_account)
        writer.write_str_value("launchUri", self.launch_uri)
    

