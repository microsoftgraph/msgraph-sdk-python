from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_msi_package_type import Win32LobAppMsiPackageType

@dataclass
class Win32LobAppMsiInformation(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains MSI app properties for a Win32 App.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the package type of an MSI Win32LobApp.
    package_type: Optional[Win32LobAppMsiPackageType] = None
    # The MSI product code.
    product_code: Optional[str] = None
    # The MSI product name.
    product_name: Optional[str] = None
    # The MSI product version.
    product_version: Optional[str] = None
    # The MSI publisher.
    publisher: Optional[str] = None
    # Whether the MSI app requires the machine to reboot to complete installation.
    requires_reboot: Optional[bool] = None
    # The MSI upgrade code.
    upgrade_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppMsiInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppMsiInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppMsiInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_msi_package_type import Win32LobAppMsiPackageType

        from .win32_lob_app_msi_package_type import Win32LobAppMsiPackageType

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "packageType": lambda n : setattr(self, 'package_type', n.get_enum_value(Win32LobAppMsiPackageType)),
            "productCode": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "requiresReboot": lambda n : setattr(self, 'requires_reboot', n.get_bool_value()),
            "upgradeCode": lambda n : setattr(self, 'upgrade_code', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("packageType", self.package_type)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_str_value("publisher", self.publisher)
        writer.write_bool_value("requiresReboot", self.requires_reboot)
        writer.write_str_value("upgradeCode", self.upgrade_code)
        writer.write_additional_data_value(self.additional_data)
    

