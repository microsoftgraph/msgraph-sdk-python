from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .request_schedule import RequestSchedule
    from .unified_role_schedule_base import UnifiedRoleScheduleBase

from .unified_role_schedule_base import UnifiedRoleScheduleBase

@dataclass
class UnifiedRoleEligibilitySchedule(UnifiedRoleScheduleBase, Parsable):
    # How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The period of the role eligibility.
    schedule_info: Optional[RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleEligibilitySchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleEligibilitySchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleEligibilitySchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .request_schedule import RequestSchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        from .request_schedule import RequestSchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        fields: dict[str, Callable[[Any], None]] = {
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
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
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

