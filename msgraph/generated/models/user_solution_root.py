from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .working_time_schedule import WorkingTimeSchedule

from .entity import Entity

@dataclass
class UserSolutionRoot(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The working time schedule entity associated with the solution.
    working_time_schedule: Optional[WorkingTimeSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSolutionRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSolutionRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSolutionRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .working_time_schedule import WorkingTimeSchedule

        from .entity import Entity
        from .working_time_schedule import WorkingTimeSchedule

        fields: Dict[str, Callable[[Any], None]] = {
            "workingTimeSchedule": lambda n : setattr(self, 'working_time_schedule', n.get_object_value(WorkingTimeSchedule)),
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
        writer.write_object_value("workingTimeSchedule", self.working_time_schedule)
    

