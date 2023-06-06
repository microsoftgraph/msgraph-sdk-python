from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, edition_upgrade_license_type, windows10_edition_type

from . import device_configuration

@dataclass
class EditionUpgradeConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.editionUpgradeConfiguration"
    # Edition Upgrade License File Content.
    license: Optional[str] = None
    # Edition Upgrade License type
    license_type: Optional[edition_upgrade_license_type.EditionUpgradeLicenseType] = None
    # Edition Upgrade Product Key.
    product_key: Optional[str] = None
    # Windows 10 Edition type.
    target_edition: Optional[windows10_edition_type.Windows10EditionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EditionUpgradeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EditionUpgradeConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EditionUpgradeConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, edition_upgrade_license_type, windows10_edition_type

        fields: Dict[str, Callable[[Any], None]] = {
            "license": lambda n : setattr(self, 'license', n.get_str_value()),
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(edition_upgrade_license_type.EditionUpgradeLicenseType)),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "targetEdition": lambda n : setattr(self, 'target_edition', n.get_enum_value(windows10_edition_type.Windows10EditionType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("license", self.license)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_str_value("productKey", self.product_key)
        writer.write_enum_value("targetEdition", self.target_edition)
    

