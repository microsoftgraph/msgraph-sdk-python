from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
planner_task = lazy_import('msgraph.generated.models.planner_task')

class PlannerBucket(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new plannerBucket and sets the default values.
        """
        super().__init__()
        # Name of the bucket.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Hint used to order items of this type in a list view. The format is defined as outlined here.
        self._order_hint: Optional[str] = None
        # Plan ID to which the bucket belongs.
        self._plan_id: Optional[str] = None
        # Read-only. Nullable. The collection of tasks in the bucket.
        self._tasks: Optional[List[planner_task.PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerBucket:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerBucket
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerBucket()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order_hint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the bucket.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the bucket.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def order_hint(self,) -> Optional[str]:
        """
        Gets the orderHint property value. Hint used to order items of this type in a list view. The format is defined as outlined here.
        Returns: Optional[str]
        """
        return self._order_hint
    
    @order_hint.setter
    def order_hint(self,value: Optional[str] = None) -> None:
        """
        Sets the orderHint property value. Hint used to order items of this type in a list view. The format is defined as outlined here.
        Args:
            value: Value to set for the orderHint property.
        """
        self._order_hint = value
    
    @property
    def plan_id(self,) -> Optional[str]:
        """
        Gets the planId property value. Plan ID to which the bucket belongs.
        Returns: Optional[str]
        """
        return self._plan_id
    
    @plan_id.setter
    def plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the planId property value. Plan ID to which the bucket belongs.
        Args:
            value: Value to set for the planId property.
        """
        self._plan_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("name", self.name)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_str_value("planId", self.plan_id)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def tasks(self,) -> Optional[List[planner_task.PlannerTask]]:
        """
        Gets the tasks property value. Read-only. Nullable. The collection of tasks in the bucket.
        Returns: Optional[List[planner_task.PlannerTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[planner_task.PlannerTask]] = None) -> None:
        """
        Sets the tasks property value. Read-only. Nullable. The collection of tasks in the bucket.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

