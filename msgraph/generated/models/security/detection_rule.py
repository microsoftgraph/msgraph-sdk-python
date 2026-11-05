from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .detection_action import DetectionAction
    from .detection_rule_status import DetectionRuleStatus
    from .query_condition import QueryCondition
    from .rule_schedule import RuleSchedule

from ..entity import Entity

@dataclass
class DetectionRule(Entity, Parsable):
    # Name of the user or application that created the rule. Read-only. Supports $filter (eq, ne, not, in, startsWith, endsWith, contains).
    created_by: Optional[str] = None
    # Timestamp of rule creation. Read-only. Supports $filter (eq, ne, not, le, ge, lt, gt) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # A user-supplied description of the detection rule. Supports $filter (eq, ne, not, in, startsWith, endsWith, contains).
    description: Optional[str] = None
    # The detectionAction property
    detection_action: Optional[DetectionAction] = None
    # The display name of the rule. Supports $filter (eq, ne, not, in, startsWith, endsWith, contains) and $orderby.
    display_name: Optional[str] = None
    # Name of the user or application that last updated the rule. Read-only. Supports $filter (eq, ne, not, in, startsWith, endsWith, contains).
    last_modified_by: Optional[str] = None
    # Timestamp of when the rule was last updated. Read-only. Supports $filter (eq, ne, not, le, ge, lt, gt) and $orderby.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The queryCondition property
    query_condition: Optional[QueryCondition] = None
    # The schedule property
    schedule: Optional[RuleSchedule] = None
    # The status property
    status: Optional[DetectionRuleStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetectionRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .detection_action import DetectionAction
        from .detection_rule_status import DetectionRuleStatus
        from .query_condition import QueryCondition
        from .rule_schedule import RuleSchedule

        from ..entity import Entity
        from .detection_action import DetectionAction
        from .detection_rule_status import DetectionRuleStatus
        from .query_condition import QueryCondition
        from .rule_schedule import RuleSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionAction": lambda n : setattr(self, 'detection_action', n.get_object_value(DetectionAction)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "queryCondition": lambda n : setattr(self, 'query_condition', n.get_object_value(QueryCondition)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(RuleSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DetectionRuleStatus)),
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
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detectionAction", self.detection_action)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("queryCondition", self.query_condition)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("status", self.status)
    

