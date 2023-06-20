from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import calendar_role_type, email_address, entity

from . import entity

@dataclass
class CalendarPermission(entity.Entity):
    # List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
    allowed_roles: Optional[List[calendar_role_type.CalendarRoleType]] = None
    # Represents a sharee or delegate who has access to the calendar. For the 'My Organization' sharee, the address property is null. Read-only.
    email_address: Optional[email_address.EmailAddress] = None
    # True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.
    is_inside_organization: Optional[bool] = None
    # True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.
    is_removable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Current permission level of the calendar sharee or delegate.
    role: Optional[calendar_role_type.CalendarRoleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarPermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarPermission
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CalendarPermission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import calendar_role_type, email_address, entity

        from . import calendar_role_type, email_address, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedRoles": lambda n : setattr(self, 'allowed_roles', n.get_collection_of_enum_values(calendar_role_type.CalendarRoleType)),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_object_value(email_address.EmailAddress)),
            "isInsideOrganization": lambda n : setattr(self, 'is_inside_organization', n.get_bool_value()),
            "isRemovable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(calendar_role_type.CalendarRoleType)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_enum_values("allowedRoles", self.allowed_roles)
        writer.write_object_value("emailAddress", self.email_address)
        writer.write_bool_value("isInsideOrganization", self.is_inside_organization)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_enum_value("role", self.role)
    

