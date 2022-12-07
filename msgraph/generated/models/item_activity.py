from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_action = lazy_import('msgraph.generated.models.access_action')
drive_item = lazy_import('msgraph.generated.models.drive_item')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class ItemActivity(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def access(self,) -> Optional[access_action.AccessAction]:
        """
        Gets the access property value. An item was accessed.
        Returns: Optional[access_action.AccessAction]
        """
        return self._access
    
    @access.setter
    def access(self,value: Optional[access_action.AccessAction] = None) -> None:
        """
        Sets the access property value. An item was accessed.
        Args:
            value: Value to set for the access property.
        """
        self._access = value
    
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. Details about when the activity took place. Read-only.
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. Details about when the activity took place. Read-only.
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def actor(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the actor property value. Identity of who performed the action. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._actor
    
    @actor.setter
    def actor(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the actor property value. Identity of who performed the action. Read-only.
        Args:
            value: Value to set for the actor property.
        """
        self._actor = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemActivity and sets the default values.
        """
        super().__init__()
        # An item was accessed.
        self._access: Optional[access_action.AccessAction] = None
        # Details about when the activity took place. Read-only.
        self._activity_date_time: Optional[datetime] = None
        # Identity of who performed the action. Read-only.
        self._actor: Optional[identity_set.IdentitySet] = None
        # Exposes the driveItem that was the target of this activity.
        self._drive_item: Optional[drive_item.DriveItem] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemActivity()
    
    @property
    def drive_item(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the driveItem property value. Exposes the driveItem that was the target of this activity.
        Returns: Optional[drive_item.DriveItem]
        """
        return self._drive_item
    
    @drive_item.setter
    def drive_item(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the driveItem property value. Exposes the driveItem that was the target of this activity.
        Args:
            value: Value to set for the driveItem property.
        """
        self._drive_item = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access": lambda n : setattr(self, 'access', n.get_object_value(access_action.AccessAction)),
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(identity_set.IdentitySet)),
            "drive_item": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("access", self.access)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_object_value("actor", self.actor)
        writer.write_object_value("driveItem", self.drive_item)
    

