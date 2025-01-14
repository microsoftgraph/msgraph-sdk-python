from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .edition_upgrade_license_type import EditionUpgradeLicenseType
    from .windows10_edition_type import Windows10EditionType

from .device_configuration import DeviceConfiguration

@dataclass
class EditionUpgradeConfiguration(DeviceConfiguration, Parsable):
    """
    Windows 10 Edition Upgrade configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.editionUpgradeConfiguration"
    # Edition Upgrade License File Content.
    license: Optional[str] = None
    # Edition Upgrade License type
    license_type: Optional[EditionUpgradeLicenseType] = None
    # Edition Upgrade Product Key.
    product_key: Optional[str] = None
    # Windows 10 Edition type.
    target_edition: Optional[Windows10EditionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EditionUpgradeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditionUpgradeConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EditionUpgradeConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .edition_upgrade_license_type import EditionUpgradeLicenseType
        from .windows10_edition_type import Windows10EditionType

        from .device_configuration import DeviceConfiguration
        from .edition_upgrade_license_type import EditionUpgradeLicenseType
        from .windows10_edition_type import Windows10EditionType

        fields: dict[str, Callable[[Any], None]] = {
            "license": lambda n : setattr(self, 'license', n.get_str_value()),
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(EditionUpgradeLicenseType)),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "targetEdition": lambda n : setattr(self, 'target_edition', n.get_enum_value(Windows10EditionType)),
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
        writer.write_str_value("license", self.license)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_str_value("productKey", self.product_key)
        writer.write_enum_value("targetEdition", self.target_edition)
    

