from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
edition_upgrade_license_type = lazy_import('msgraph.generated.models.edition_upgrade_license_type')
windows10_edition_type = lazy_import('msgraph.generated.models.windows10_edition_type')

class EditionUpgradeConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new EditionUpgradeConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.editionUpgradeConfiguration"
        # Edition Upgrade License File Content.
        self._license: Optional[str] = None
        # Edition Upgrade License type
        self._license_type: Optional[edition_upgrade_license_type.EditionUpgradeLicenseType] = None
        # Edition Upgrade Product Key.
        self._product_key: Optional[str] = None
        # Windows 10 Edition type.
        self._target_edition: Optional[windows10_edition_type.Windows10EditionType] = None
    
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
        fields = {
            "license": lambda n : setattr(self, 'license', n.get_str_value()),
            "license_type": lambda n : setattr(self, 'license_type', n.get_enum_value(edition_upgrade_license_type.EditionUpgradeLicenseType)),
            "product_key": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "target_edition": lambda n : setattr(self, 'target_edition', n.get_enum_value(windows10_edition_type.Windows10EditionType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def license(self,) -> Optional[str]:
        """
        Gets the license property value. Edition Upgrade License File Content.
        Returns: Optional[str]
        """
        return self._license
    
    @license.setter
    def license(self,value: Optional[str] = None) -> None:
        """
        Sets the license property value. Edition Upgrade License File Content.
        Args:
            value: Value to set for the license property.
        """
        self._license = value
    
    @property
    def license_type(self,) -> Optional[edition_upgrade_license_type.EditionUpgradeLicenseType]:
        """
        Gets the licenseType property value. Edition Upgrade License type
        Returns: Optional[edition_upgrade_license_type.EditionUpgradeLicenseType]
        """
        return self._license_type
    
    @license_type.setter
    def license_type(self,value: Optional[edition_upgrade_license_type.EditionUpgradeLicenseType] = None) -> None:
        """
        Sets the licenseType property value. Edition Upgrade License type
        Args:
            value: Value to set for the licenseType property.
        """
        self._license_type = value
    
    @property
    def product_key(self,) -> Optional[str]:
        """
        Gets the productKey property value. Edition Upgrade Product Key.
        Returns: Optional[str]
        """
        return self._product_key
    
    @product_key.setter
    def product_key(self,value: Optional[str] = None) -> None:
        """
        Sets the productKey property value. Edition Upgrade Product Key.
        Args:
            value: Value to set for the productKey property.
        """
        self._product_key = value
    
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
    
    @property
    def target_edition(self,) -> Optional[windows10_edition_type.Windows10EditionType]:
        """
        Gets the targetEdition property value. Windows 10 Edition type.
        Returns: Optional[windows10_edition_type.Windows10EditionType]
        """
        return self._target_edition
    
    @target_edition.setter
    def target_edition(self,value: Optional[windows10_edition_type.Windows10EditionType] = None) -> None:
        """
        Sets the targetEdition property value. Windows 10 Edition type.
        Args:
            value: Value to set for the targetEdition property.
        """
        self._target_edition = value
    

