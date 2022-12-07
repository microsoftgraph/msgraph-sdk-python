from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_msi_package_type = lazy_import('msgraph.generated.models.win32_lob_app_msi_package_type')

class Win32LobAppMsiInformation(AdditionalDataHolder, Parsable):
    """
    Contains MSI app properties for a Win32 App.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new win32LobAppMsiInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the package type of an MSI Win32LobApp.
        self._package_type: Optional[win32_lob_app_msi_package_type.Win32LobAppMsiPackageType] = None
        # The MSI product code.
        self._product_code: Optional[str] = None
        # The MSI product name.
        self._product_name: Optional[str] = None
        # The MSI product version.
        self._product_version: Optional[str] = None
        # The MSI publisher.
        self._publisher: Optional[str] = None
        # Whether the MSI app requires the machine to reboot to complete installation.
        self._requires_reboot: Optional[bool] = None
        # The MSI upgrade code.
        self._upgrade_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppMsiInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppMsiInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppMsiInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "package_type": lambda n : setattr(self, 'package_type', n.get_enum_value(win32_lob_app_msi_package_type.Win32LobAppMsiPackageType)),
            "product_code": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "product_name": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "product_version": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "requires_reboot": lambda n : setattr(self, 'requires_reboot', n.get_bool_value()),
            "upgrade_code": lambda n : setattr(self, 'upgrade_code', n.get_str_value()),
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
    def package_type(self,) -> Optional[win32_lob_app_msi_package_type.Win32LobAppMsiPackageType]:
        """
        Gets the packageType property value. Indicates the package type of an MSI Win32LobApp.
        Returns: Optional[win32_lob_app_msi_package_type.Win32LobAppMsiPackageType]
        """
        return self._package_type
    
    @package_type.setter
    def package_type(self,value: Optional[win32_lob_app_msi_package_type.Win32LobAppMsiPackageType] = None) -> None:
        """
        Sets the packageType property value. Indicates the package type of an MSI Win32LobApp.
        Args:
            value: Value to set for the packageType property.
        """
        self._package_type = value
    
    @property
    def product_code(self,) -> Optional[str]:
        """
        Gets the productCode property value. The MSI product code.
        Returns: Optional[str]
        """
        return self._product_code
    
    @product_code.setter
    def product_code(self,value: Optional[str] = None) -> None:
        """
        Sets the productCode property value. The MSI product code.
        Args:
            value: Value to set for the productCode property.
        """
        self._product_code = value
    
    @property
    def product_name(self,) -> Optional[str]:
        """
        Gets the productName property value. The MSI product name.
        Returns: Optional[str]
        """
        return self._product_name
    
    @product_name.setter
    def product_name(self,value: Optional[str] = None) -> None:
        """
        Sets the productName property value. The MSI product name.
        Args:
            value: Value to set for the productName property.
        """
        self._product_name = value
    
    @property
    def product_version(self,) -> Optional[str]:
        """
        Gets the productVersion property value. The MSI product version.
        Returns: Optional[str]
        """
        return self._product_version
    
    @product_version.setter
    def product_version(self,value: Optional[str] = None) -> None:
        """
        Sets the productVersion property value. The MSI product version.
        Args:
            value: Value to set for the productVersion property.
        """
        self._product_version = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The MSI publisher.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The MSI publisher.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    @property
    def requires_reboot(self,) -> Optional[bool]:
        """
        Gets the requiresReboot property value. Whether the MSI app requires the machine to reboot to complete installation.
        Returns: Optional[bool]
        """
        return self._requires_reboot
    
    @requires_reboot.setter
    def requires_reboot(self,value: Optional[bool] = None) -> None:
        """
        Sets the requiresReboot property value. Whether the MSI app requires the machine to reboot to complete installation.
        Args:
            value: Value to set for the requiresReboot property.
        """
        self._requires_reboot = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("packageType", self.package_type)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_str_value("publisher", self.publisher)
        writer.write_bool_value("requiresReboot", self.requires_reboot)
        writer.write_str_value("upgradeCode", self.upgrade_code)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def upgrade_code(self,) -> Optional[str]:
        """
        Gets the upgradeCode property value. The MSI upgrade code.
        Returns: Optional[str]
        """
        return self._upgrade_code
    
    @upgrade_code.setter
    def upgrade_code(self,value: Optional[str] = None) -> None:
        """
        Sets the upgradeCode property value. The MSI upgrade code.
        Args:
            value: Value to set for the upgradeCode property.
        """
        self._upgrade_code = value
    

