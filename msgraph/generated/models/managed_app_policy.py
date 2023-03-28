from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_managed_app_protection, default_managed_app_protection, entity, ios_managed_app_protection, managed_app_configuration, managed_app_protection, mdm_windows_information_protection_policy, targeted_managed_app_configuration, targeted_managed_app_protection, windows_information_protection, windows_information_protection_policy

from . import entity

class ManagedAppPolicy(entity.Entity):
    """
    The ManagedAppPolicy resource represents a base type for platform specific policies.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managedAppPolicy and sets the default values.
        """
        super().__init__()
        # The date and time the policy was created.
        self._created_date_time: Optional[datetime] = None
        # The policy's description.
        self._description: Optional[str] = None
        # Policy display name.
        self._display_name: Optional[str] = None
        # Last time the policy was modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Version of the entity.
        self._version: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the policy was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the policy was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidManagedAppProtection":
                from . import android_managed_app_protection

                return android_managed_app_protection.AndroidManagedAppProtection()
            if mapping_value == "#microsoft.graph.defaultManagedAppProtection":
                from . import default_managed_app_protection

                return default_managed_app_protection.DefaultManagedAppProtection()
            if mapping_value == "#microsoft.graph.iosManagedAppProtection":
                from . import ios_managed_app_protection

                return ios_managed_app_protection.IosManagedAppProtection()
            if mapping_value == "#microsoft.graph.managedAppConfiguration":
                from . import managed_app_configuration

                return managed_app_configuration.ManagedAppConfiguration()
            if mapping_value == "#microsoft.graph.managedAppProtection":
                from . import managed_app_protection

                return managed_app_protection.ManagedAppProtection()
            if mapping_value == "#microsoft.graph.mdmWindowsInformationProtectionPolicy":
                from . import mdm_windows_information_protection_policy

                return mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy()
            if mapping_value == "#microsoft.graph.targetedManagedAppConfiguration":
                from . import targeted_managed_app_configuration

                return targeted_managed_app_configuration.TargetedManagedAppConfiguration()
            if mapping_value == "#microsoft.graph.targetedManagedAppProtection":
                from . import targeted_managed_app_protection

                return targeted_managed_app_protection.TargetedManagedAppProtection()
            if mapping_value == "#microsoft.graph.windowsInformationProtection":
                from . import windows_information_protection

                return windows_information_protection.WindowsInformationProtection()
            if mapping_value == "#microsoft.graph.windowsInformationProtectionPolicy":
                from . import windows_information_protection_policy

                return windows_information_protection_policy.WindowsInformationProtectionPolicy()
        return ManagedAppPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The policy's description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The policy's description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Policy display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Policy display name.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_managed_app_protection, default_managed_app_protection, entity, ios_managed_app_protection, managed_app_configuration, managed_app_protection, mdm_windows_information_protection_policy, targeted_managed_app_configuration, targeted_managed_app_protection, windows_information_protection, windows_information_protection_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last time the policy was modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last time the policy was modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the entity.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the entity.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

