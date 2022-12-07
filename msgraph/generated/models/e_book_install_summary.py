from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class EBookInstallSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new eBookInstallSummary and sets the default values.
        """
        super().__init__()
        # Number of Devices that have failed to install this book.
        self._failed_device_count: Optional[int] = None
        # Number of Users that have 1 or more device that failed to install this book.
        self._failed_user_count: Optional[int] = None
        # Number of Devices that have successfully installed this book.
        self._installed_device_count: Optional[int] = None
        # Number of Users whose devices have all succeeded to install this book.
        self._installed_user_count: Optional[int] = None
        # Number of Devices that does not have this book installed.
        self._not_installed_device_count: Optional[int] = None
        # Number of Users that did not install this book.
        self._not_installed_user_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EBookInstallSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EBookInstallSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EBookInstallSummary()
    
    @property
    def failed_device_count(self,) -> Optional[int]:
        """
        Gets the failedDeviceCount property value. Number of Devices that have failed to install this book.
        Returns: Optional[int]
        """
        return self._failed_device_count
    
    @failed_device_count.setter
    def failed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedDeviceCount property value. Number of Devices that have failed to install this book.
        Args:
            value: Value to set for the failedDeviceCount property.
        """
        self._failed_device_count = value
    
    @property
    def failed_user_count(self,) -> Optional[int]:
        """
        Gets the failedUserCount property value. Number of Users that have 1 or more device that failed to install this book.
        Returns: Optional[int]
        """
        return self._failed_user_count
    
    @failed_user_count.setter
    def failed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedUserCount property value. Number of Users that have 1 or more device that failed to install this book.
        Args:
            value: Value to set for the failedUserCount property.
        """
        self._failed_user_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "failed_device_count": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "failed_user_count": lambda n : setattr(self, 'failed_user_count', n.get_int_value()),
            "installed_device_count": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "installed_user_count": lambda n : setattr(self, 'installed_user_count', n.get_int_value()),
            "not_installed_device_count": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
            "not_installed_user_count": lambda n : setattr(self, 'not_installed_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def installed_device_count(self,) -> Optional[int]:
        """
        Gets the installedDeviceCount property value. Number of Devices that have successfully installed this book.
        Returns: Optional[int]
        """
        return self._installed_device_count
    
    @installed_device_count.setter
    def installed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the installedDeviceCount property value. Number of Devices that have successfully installed this book.
        Args:
            value: Value to set for the installedDeviceCount property.
        """
        self._installed_device_count = value
    
    @property
    def installed_user_count(self,) -> Optional[int]:
        """
        Gets the installedUserCount property value. Number of Users whose devices have all succeeded to install this book.
        Returns: Optional[int]
        """
        return self._installed_user_count
    
    @installed_user_count.setter
    def installed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the installedUserCount property value. Number of Users whose devices have all succeeded to install this book.
        Args:
            value: Value to set for the installedUserCount property.
        """
        self._installed_user_count = value
    
    @property
    def not_installed_device_count(self,) -> Optional[int]:
        """
        Gets the notInstalledDeviceCount property value. Number of Devices that does not have this book installed.
        Returns: Optional[int]
        """
        return self._not_installed_device_count
    
    @not_installed_device_count.setter
    def not_installed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notInstalledDeviceCount property value. Number of Devices that does not have this book installed.
        Args:
            value: Value to set for the notInstalledDeviceCount property.
        """
        self._not_installed_device_count = value
    
    @property
    def not_installed_user_count(self,) -> Optional[int]:
        """
        Gets the notInstalledUserCount property value. Number of Users that did not install this book.
        Returns: Optional[int]
        """
        return self._not_installed_user_count
    
    @not_installed_user_count.setter
    def not_installed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notInstalledUserCount property value. Number of Users that did not install this book.
        Args:
            value: Value to set for the notInstalledUserCount property.
        """
        self._not_installed_user_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("failedUserCount", self.failed_user_count)
        writer.write_int_value("installedDeviceCount", self.installed_device_count)
        writer.write_int_value("installedUserCount", self.installed_user_count)
        writer.write_int_value("notInstalledDeviceCount", self.not_installed_device_count)
        writer.write_int_value("notInstalledUserCount", self.not_installed_user_count)
    

