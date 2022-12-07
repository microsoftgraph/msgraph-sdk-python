from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
incomplete_data = lazy_import('msgraph.generated.models.incomplete_data')
item_action_stat = lazy_import('msgraph.generated.models.item_action_stat')
item_activity = lazy_import('msgraph.generated.models.item_activity')

class ItemActivityStat(entity.Entity):
    @property
    def access(self,) -> Optional[item_action_stat.ItemActionStat]:
        """
        Gets the access property value. Statistics about the access actions in this interval. Read-only.
        Returns: Optional[item_action_stat.ItemActionStat]
        """
        return self._access
    
    @access.setter
    def access(self,value: Optional[item_action_stat.ItemActionStat] = None) -> None:
        """
        Sets the access property value. Statistics about the access actions in this interval. Read-only.
        Args:
            value: Value to set for the access property.
        """
        self._access = value
    
    @property
    def activities(self,) -> Optional[List[item_activity.ItemActivity]]:
        """
        Gets the activities property value. Exposes the itemActivities represented in this itemActivityStat resource.
        Returns: Optional[List[item_activity.ItemActivity]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[item_activity.ItemActivity]] = None) -> None:
        """
        Sets the activities property value. Exposes the itemActivities represented in this itemActivityStat resource.
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemActivityStat and sets the default values.
        """
        super().__init__()
        # Statistics about the access actions in this interval. Read-only.
        self._access: Optional[item_action_stat.ItemActionStat] = None
        # Exposes the itemActivities represented in this itemActivityStat resource.
        self._activities: Optional[List[item_activity.ItemActivity]] = None
        # Statistics about the create actions in this interval. Read-only.
        self._create: Optional[item_action_stat.ItemActionStat] = None
        # Statistics about the delete actions in this interval. Read-only.
        self._delete: Optional[item_action_stat.ItemActionStat] = None
        # Statistics about the edit actions in this interval. Read-only.
        self._edit: Optional[item_action_stat.ItemActionStat] = None
        # When the interval ends. Read-only.
        self._end_date_time: Optional[datetime] = None
        # Indicates that the statistics in this interval are based on incomplete data. Read-only.
        self._incomplete_data: Optional[incomplete_data.IncompleteData] = None
        # Indicates whether the item is 'trending.' Read-only.
        self._is_trending: Optional[bool] = None
        # Statistics about the move actions in this interval. Read-only.
        self._move: Optional[item_action_stat.ItemActionStat] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # When the interval starts. Read-only.
        self._start_date_time: Optional[datetime] = None
    
    @property
    def create(self,) -> Optional[item_action_stat.ItemActionStat]:
        """
        Gets the create property value. Statistics about the create actions in this interval. Read-only.
        Returns: Optional[item_action_stat.ItemActionStat]
        """
        return self._create
    
    @create.setter
    def create(self,value: Optional[item_action_stat.ItemActionStat] = None) -> None:
        """
        Sets the create property value. Statistics about the create actions in this interval. Read-only.
        Args:
            value: Value to set for the create property.
        """
        self._create = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemActivityStat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityStat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemActivityStat()
    
    @property
    def delete(self,) -> Optional[item_action_stat.ItemActionStat]:
        """
        Gets the delete property value. Statistics about the delete actions in this interval. Read-only.
        Returns: Optional[item_action_stat.ItemActionStat]
        """
        return self._delete
    
    @delete.setter
    def delete(self,value: Optional[item_action_stat.ItemActionStat] = None) -> None:
        """
        Sets the delete property value. Statistics about the delete actions in this interval. Read-only.
        Args:
            value: Value to set for the delete property.
        """
        self._delete = value
    
    @property
    def edit(self,) -> Optional[item_action_stat.ItemActionStat]:
        """
        Gets the edit property value. Statistics about the edit actions in this interval. Read-only.
        Returns: Optional[item_action_stat.ItemActionStat]
        """
        return self._edit
    
    @edit.setter
    def edit(self,value: Optional[item_action_stat.ItemActionStat] = None) -> None:
        """
        Sets the edit property value. Statistics about the edit actions in this interval. Read-only.
        Args:
            value: Value to set for the edit property.
        """
        self._edit = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. When the interval ends. Read-only.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. When the interval ends. Read-only.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access": lambda n : setattr(self, 'access', n.get_object_value(item_action_stat.ItemActionStat)),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(item_activity.ItemActivity)),
            "create": lambda n : setattr(self, 'create', n.get_object_value(item_action_stat.ItemActionStat)),
            "delete": lambda n : setattr(self, 'delete', n.get_object_value(item_action_stat.ItemActionStat)),
            "edit": lambda n : setattr(self, 'edit', n.get_object_value(item_action_stat.ItemActionStat)),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "incomplete_data": lambda n : setattr(self, 'incomplete_data', n.get_object_value(incomplete_data.IncompleteData)),
            "is_trending": lambda n : setattr(self, 'is_trending', n.get_bool_value()),
            "move": lambda n : setattr(self, 'move', n.get_object_value(item_action_stat.ItemActionStat)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incomplete_data(self,) -> Optional[incomplete_data.IncompleteData]:
        """
        Gets the incompleteData property value. Indicates that the statistics in this interval are based on incomplete data. Read-only.
        Returns: Optional[incomplete_data.IncompleteData]
        """
        return self._incomplete_data
    
    @incomplete_data.setter
    def incomplete_data(self,value: Optional[incomplete_data.IncompleteData] = None) -> None:
        """
        Sets the incompleteData property value. Indicates that the statistics in this interval are based on incomplete data. Read-only.
        Args:
            value: Value to set for the incompleteData property.
        """
        self._incomplete_data = value
    
    @property
    def is_trending(self,) -> Optional[bool]:
        """
        Gets the isTrending property value. Indicates whether the item is 'trending.' Read-only.
        Returns: Optional[bool]
        """
        return self._is_trending
    
    @is_trending.setter
    def is_trending(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTrending property value. Indicates whether the item is 'trending.' Read-only.
        Args:
            value: Value to set for the isTrending property.
        """
        self._is_trending = value
    
    @property
    def move(self,) -> Optional[item_action_stat.ItemActionStat]:
        """
        Gets the move property value. Statistics about the move actions in this interval. Read-only.
        Returns: Optional[item_action_stat.ItemActionStat]
        """
        return self._move
    
    @move.setter
    def move(self,value: Optional[item_action_stat.ItemActionStat] = None) -> None:
        """
        Sets the move property value. Statistics about the move actions in this interval. Read-only.
        Args:
            value: Value to set for the move property.
        """
        self._move = value
    
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_object_value("create", self.create)
        writer.write_object_value("delete", self.delete)
        writer.write_object_value("edit", self.edit)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("incompleteData", self.incomplete_data)
        writer.write_bool_value("isTrending", self.is_trending)
        writer.write_object_value("move", self.move)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. When the interval starts. Read-only.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. When the interval starts. Read-only.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

