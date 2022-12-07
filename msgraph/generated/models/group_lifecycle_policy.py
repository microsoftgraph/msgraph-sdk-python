from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class GroupLifecyclePolicy(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def alternate_notification_emails(self,) -> Optional[str]:
        """
        Gets the alternateNotificationEmails property value. List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.
        Returns: Optional[str]
        """
        return self._alternate_notification_emails
    
    @alternate_notification_emails.setter
    def alternate_notification_emails(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateNotificationEmails property value. List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.
        Args:
            value: Value to set for the alternateNotificationEmails property.
        """
        self._alternate_notification_emails = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupLifecyclePolicy and sets the default values.
        """
        super().__init__()
        # List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.
        self._alternate_notification_emails: Optional[str] = None
        # Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.
        self._group_lifetime_in_days: Optional[int] = None
        # The group type for which the expiration policy applies. Possible values are All, Selected or None.
        self._managed_group_types: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupLifecyclePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupLifecyclePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupLifecyclePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alternate_notification_emails": lambda n : setattr(self, 'alternate_notification_emails', n.get_str_value()),
            "group_lifetime_in_days": lambda n : setattr(self, 'group_lifetime_in_days', n.get_int_value()),
            "managed_group_types": lambda n : setattr(self, 'managed_group_types', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_lifetime_in_days(self,) -> Optional[int]:
        """
        Gets the groupLifetimeInDays property value. Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.
        Returns: Optional[int]
        """
        return self._group_lifetime_in_days
    
    @group_lifetime_in_days.setter
    def group_lifetime_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the groupLifetimeInDays property value. Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.
        Args:
            value: Value to set for the groupLifetimeInDays property.
        """
        self._group_lifetime_in_days = value
    
    @property
    def managed_group_types(self,) -> Optional[str]:
        """
        Gets the managedGroupTypes property value. The group type for which the expiration policy applies. Possible values are All, Selected or None.
        Returns: Optional[str]
        """
        return self._managed_group_types
    
    @managed_group_types.setter
    def managed_group_types(self,value: Optional[str] = None) -> None:
        """
        Sets the managedGroupTypes property value. The group type for which the expiration policy applies. Possible values are All, Selected or None.
        Args:
            value: Value to set for the managedGroupTypes property.
        """
        self._managed_group_types = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("alternateNotificationEmails", self.alternate_notification_emails)
        writer.write_int_value("groupLifetimeInDays", self.group_lifetime_in_days)
        writer.write_str_value("managedGroupTypes", self.managed_group_types)
    

