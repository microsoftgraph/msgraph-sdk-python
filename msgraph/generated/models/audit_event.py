from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .audit_actor import AuditActor
    from .audit_resource import AuditResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AuditEvent(Entity):
    """
    A class containing the properties for Audit Event.
    """
    # Friendly name of the activity.
    activity: Optional[str] = None
    # The date time in UTC when the activity was performed.
    activity_date_time: Optional[datetime.datetime] = None
    # The HTTP operation type of the activity.
    activity_operation_type: Optional[str] = None
    # The result of the activity.
    activity_result: Optional[str] = None
    # The type of activity that was being performed.
    activity_type: Optional[str] = None
    # AAD user and application that are associated with the audit event.
    actor: Optional[AuditActor] = None
    # Audit category.
    category: Optional[str] = None
    # Component name.
    component_name: Optional[str] = None
    # The client request Id that is used to correlate activity within the system.
    correlation_id: Optional[UUID] = None
    # Event display name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resources being modified.
    resources: Optional[List[AuditResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audit_actor import AuditActor
        from .audit_resource import AuditResource
        from .entity import Entity

        from .audit_actor import AuditActor
        from .audit_resource import AuditResource
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activityOperationType": lambda n : setattr(self, 'activity_operation_type', n.get_str_value()),
            "activityResult": lambda n : setattr(self, 'activity_result', n.get_str_value()),
            "activityType": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(AuditActor)),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "componentName": lambda n : setattr(self, 'component_name', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_uuid_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(AuditResource)),
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
        writer.write_str_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityOperationType", self.activity_operation_type)
        writer.write_str_value("activityResult", self.activity_result)
        writer.write_str_value("activityType", self.activity_type)
        writer.write_object_value("actor", self.actor)
        writer.write_str_value("category", self.category)
        writer.write_str_value("componentName", self.component_name)
        writer.write_uuid_value("correlationId", self.correlation_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
    

