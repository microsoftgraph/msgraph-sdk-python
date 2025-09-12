from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class IosDdmLobAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign an iOS iOS Declarative Device Management (DDM) Line Of Business (LOB) mobile app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosDdmLobAppAssignmentSettings"
    # Domain names to associate with the app
    associated_domains: Optional[list[str]] = None
    # When true, the system allows direct downloads for the AssociatedDomains. When false, the system will not allow direct downloads for the AssociatedDomains. Default is false.
    associated_domains_direct_download_allowed: Optional[bool] = None
    # When true, indicates that the app should not be backed up to iCloud. When false, indicates that the app may be backed up to iCloud. Default is false.
    prevent_managed_app_backup: Optional[bool] = None
    # When true, the device locks its screen after every transaction that requires a customer’s card PIN. When false, the user can choose the behavior. Default value is false.
    tap_to_pay_screen_lock_enabled: Optional[bool] = None
    # The unique identifier of the relay to associate with the app.
    vpn_configuration_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosDdmLobAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosDdmLobAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosDdmLobAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "associatedDomains": lambda n : setattr(self, 'associated_domains', n.get_collection_of_primitive_values(str)),
            "associatedDomainsDirectDownloadAllowed": lambda n : setattr(self, 'associated_domains_direct_download_allowed', n.get_bool_value()),
            "preventManagedAppBackup": lambda n : setattr(self, 'prevent_managed_app_backup', n.get_bool_value()),
            "tapToPayScreenLockEnabled": lambda n : setattr(self, 'tap_to_pay_screen_lock_enabled', n.get_bool_value()),
            "vpnConfigurationId": lambda n : setattr(self, 'vpn_configuration_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("associatedDomains", self.associated_domains)
        writer.write_bool_value("associatedDomainsDirectDownloadAllowed", self.associated_domains_direct_download_allowed)
        writer.write_bool_value("preventManagedAppBackup", self.prevent_managed_app_backup)
        writer.write_bool_value("tapToPayScreenLockEnabled", self.tap_to_pay_screen_lock_enabled)
        writer.write_str_value("vpnConfigurationId", self.vpn_configuration_id)
    

