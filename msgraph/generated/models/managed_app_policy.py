from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .default_managed_app_protection import DefaultManagedAppProtection
    from .entity import Entity
    from .ios_managed_app_protection import IosManagedAppProtection
    from .managed_app_configuration import ManagedAppConfiguration
    from .managed_app_protection import ManagedAppProtection
    from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from .targeted_managed_app_protection import TargetedManagedAppProtection
    from .windows_information_protection import WindowsInformationProtection
    from .windows_information_protection_policy import WindowsInformationProtectionPolicy

from .entity import Entity

@dataclass
class ManagedAppPolicy(Entity, Parsable):
    """
    The ManagedAppPolicy resource represents a base type for platform specific policies.
    """
    # The date and time the policy was created.
    created_date_time: Optional[datetime.datetime] = None
    # The policy's description.
    description: Optional[str] = None
    # Policy display name.
    display_name: Optional[str] = None
    # Last time the policy was modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from .android_managed_app_protection import AndroidManagedAppProtection

            return AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultManagedAppProtection".casefold():
            from .default_managed_app_protection import DefaultManagedAppProtection

            return DefaultManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from .ios_managed_app_protection import IosManagedAppProtection

            return IosManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppConfiguration".casefold():
            from .managed_app_configuration import ManagedAppConfiguration

            return ManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtection".casefold():
            from .managed_app_protection import ManagedAppProtection

            return ManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicy".casefold():
            from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

            return MdmWindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfiguration".casefold():
            from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

            return TargetedManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppProtection".casefold():
            from .targeted_managed_app_protection import TargetedManagedAppProtection

            return TargetedManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtection".casefold():
            from .windows_information_protection import WindowsInformationProtection

            return WindowsInformationProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionPolicy".casefold():
            from .windows_information_protection_policy import WindowsInformationProtectionPolicy

            return WindowsInformationProtectionPolicy()
        return ManagedAppPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .entity import Entity
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_protection import ManagedAppProtection
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .targeted_managed_app_protection import TargetedManagedAppProtection
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy

        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .entity import Entity
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_protection import ManagedAppProtection
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .targeted_managed_app_protection import TargetedManagedAppProtection
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("version", self.version)
    

