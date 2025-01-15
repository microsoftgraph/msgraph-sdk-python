from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsDefenderAdvancedThreatProtectionConfiguration(DeviceConfiguration, Parsable):
    """
    Windows Defender AdvancedThreatProtection Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration"
    # Windows Defender AdvancedThreatProtection 'Allow Sample Sharing' Rule
    allow_sample_sharing: Optional[bool] = None
    # Expedite Windows Defender Advanced Threat Protection telemetry reporting frequency.
    enable_expedited_telemetry_reporting: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDefenderAdvancedThreatProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderAdvancedThreatProtectionConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDefenderAdvancedThreatProtectionConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration

        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "allowSampleSharing": lambda n : setattr(self, 'allow_sample_sharing', n.get_bool_value()),
            "enableExpeditedTelemetryReporting": lambda n : setattr(self, 'enable_expedited_telemetry_reporting', n.get_bool_value()),
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
        writer.write_bool_value("allowSampleSharing", self.allow_sample_sharing)
        writer.write_bool_value("enableExpeditedTelemetryReporting", self.enable_expedited_telemetry_reporting)
    

