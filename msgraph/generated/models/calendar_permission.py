from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

calendar_role_type = lazy_import('msgraph.generated.models.calendar_role_type')
email_address = lazy_import('msgraph.generated.models.email_address')
entity = lazy_import('msgraph.generated.models.entity')

class CalendarPermission(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def allowed_roles(self,) -> Optional[List[calendar_role_type.CalendarRoleType]]:
        """
        Gets the allowedRoles property value. List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
        Returns: Optional[List[calendar_role_type.CalendarRoleType]]
        """
        return self._allowed_roles
    
    @allowed_roles.setter
    def allowed_roles(self,value: Optional[List[calendar_role_type.CalendarRoleType]] = None) -> None:
        """
        Sets the allowedRoles property value. List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
        Args:
            value: Value to set for the allowedRoles property.
        """
        self._allowed_roles = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new calendarPermission and sets the default values.
        """
        super().__init__()
        # List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
        self._allowed_roles: Optional[List[calendar_role_type.CalendarRoleType]] = None
        # Represents a sharee or delegate who has access to the calendar. For the 'My Organization' sharee, the address property is null. Read-only.
        self._email_address: Optional[email_address.EmailAddress] = None
        # True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.
        self._is_inside_organization: Optional[bool] = None
        # True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.
        self._is_removable: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Current permission level of the calendar sharee or delegate.
        self._role: Optional[calendar_role_type.CalendarRoleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarPermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarPermission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CalendarPermission()
    
    @property
    def email_address(self,) -> Optional[email_address.EmailAddress]:
        """
        Gets the emailAddress property value. Represents a sharee or delegate who has access to the calendar. For the 'My Organization' sharee, the address property is null. Read-only.
        Returns: Optional[email_address.EmailAddress]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[email_address.EmailAddress] = None) -> None:
        """
        Sets the emailAddress property value. Represents a sharee or delegate who has access to the calendar. For the 'My Organization' sharee, the address property is null. Read-only.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_roles": lambda n : setattr(self, 'allowed_roles', n.get_collection_of_enum_values(calendar_role_type.CalendarRoleType)),
            "email_address": lambda n : setattr(self, 'email_address', n.get_object_value(email_address.EmailAddress)),
            "is_inside_organization": lambda n : setattr(self, 'is_inside_organization', n.get_bool_value()),
            "is_removable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(calendar_role_type.CalendarRoleType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_inside_organization(self,) -> Optional[bool]:
        """
        Gets the isInsideOrganization property value. True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.
        Returns: Optional[bool]
        """
        return self._is_inside_organization
    
    @is_inside_organization.setter
    def is_inside_organization(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInsideOrganization property value. True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.
        Args:
            value: Value to set for the isInsideOrganization property.
        """
        self._is_inside_organization = value
    
    @property
    def is_removable(self,) -> Optional[bool]:
        """
        Gets the isRemovable property value. True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.
        Returns: Optional[bool]
        """
        return self._is_removable
    
    @is_removable.setter
    def is_removable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRemovable property value. True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.
        Args:
            value: Value to set for the isRemovable property.
        """
        self._is_removable = value
    
    @property
    def role(self,) -> Optional[calendar_role_type.CalendarRoleType]:
        """
        Gets the role property value. Current permission level of the calendar sharee or delegate.
        Returns: Optional[calendar_role_type.CalendarRoleType]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[calendar_role_type.CalendarRoleType] = None) -> None:
        """
        Sets the role property value. Current permission level of the calendar sharee or delegate.
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowedRoles", self.allowed_roles)
        writer.write_object_value("emailAddress", self.email_address)
        writer.write_bool_value("isInsideOrganization", self.is_inside_organization)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_enum_value("role", self.role)
    

