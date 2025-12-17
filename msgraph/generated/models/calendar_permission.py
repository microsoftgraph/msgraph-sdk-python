from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calendar_role_type import CalendarRoleType
    from .email_address import EmailAddress
    from .entity import Entity

from .entity import Entity

@dataclass
class CalendarPermission(Entity, Parsable):
    # List of allowed sharing or delegating permission levels for the calendar. The possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
    allowed_roles: Optional[list[CalendarRoleType]] = None
    # Represents a share recipient or delegate who has access to the calendar. For the 'My Organization' share recipient, the address property is null. Read-only.
    email_address: Optional[EmailAddress] = None
    # True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
    is_inside_organization: Optional[bool] = None
    # True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
    is_removable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Current permission level of the calendar share recipient or delegate.
    role: Optional[CalendarRoleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalendarPermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalendarPermission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalendarPermission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .calendar_role_type import CalendarRoleType
        from .email_address import EmailAddress
        from .entity import Entity

        from .calendar_role_type import CalendarRoleType
        from .email_address import EmailAddress
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allowedRoles": lambda n : setattr(self, 'allowed_roles', n.get_collection_of_enum_values(CalendarRoleType)),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_object_value(EmailAddress)),
            "isInsideOrganization": lambda n : setattr(self, 'is_inside_organization', n.get_bool_value()),
            "isRemovable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(CalendarRoleType)),
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
        writer.write_collection_of_enum_values("allowedRoles", self.allowed_roles)
        writer.write_object_value("emailAddress", self.email_address)
        writer.write_bool_value("isInsideOrganization", self.is_inside_organization)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_enum_value("role", self.role)
    

