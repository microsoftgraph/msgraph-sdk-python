from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_list_item import AppListItem
    from .app_list_type import AppListType
    from .device_configuration import DeviceConfiguration
    from .required_password_type import RequiredPasswordType

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSGeneralDeviceConfiguration(DeviceConfiguration):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the macOSGeneralDeviceConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSGeneralDeviceConfiguration"
    # Possible values of the compliance app list.
    compliant_app_list_type: Optional[AppListType] = None
    # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
    compliant_apps_list: Optional[List[AppListItem]] = None
    # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
    email_in_domain_suffixes: Optional[List[str]] = None
    # Block simple passwords.
    password_block_simple: Optional[bool] = None
    # Number of days before the password expires.
    password_expiration_days: Optional[int] = None
    # Number of character sets a password must contain. Valid values 0 to 4
    password_minimum_character_set_count: Optional[int] = None
    # Minimum length of passwords.
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity required before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Minutes of inactivity required before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous passwords to block.
    password_previous_password_block_count: Optional[int] = None
    # Whether or not to require a password.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSGeneralDeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .required_password_type import RequiredPasswordType

        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .required_password_type import RequiredPasswordType

        fields: Dict[str, Callable[[Any], None]] = {
            "compliant_app_list_type": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(AppListType)),
            "compliant_apps_list": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(AppListItem)),
            "email_in_domain_suffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "password_block_simple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_character_set_count": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("compliant_app_list_type", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliant_apps_list", self.compliant_apps_list)
        writer.write_collection_of_primitive_values("email_in_domain_suffixes", self.email_in_domain_suffixes)
        writer.write_bool_value("password_block_simple", self.password_block_simple)
        writer.write_int_value("password_expiration_days", self.password_expiration_days)
        writer.write_int_value("password_minimum_character_set_count", self.password_minimum_character_set_count)
        writer.write_int_value("password_minimum_length", self.password_minimum_length)
        writer.write_int_value("password_minutes_of_inactivity_before_lock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("password_minutes_of_inactivity_before_screen_timeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("password_previous_password_block_count", self.password_previous_password_block_count)
        writer.write_bool_value("password_required", self.password_required)
        writer.write_enum_value("password_required_type", self.password_required_type)
    

