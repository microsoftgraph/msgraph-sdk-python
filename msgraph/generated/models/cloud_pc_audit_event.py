from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_audit_activity_operation_type import CloudPcAuditActivityOperationType
    from .cloud_pc_audit_activity_result import CloudPcAuditActivityResult
    from .cloud_pc_audit_actor import CloudPcAuditActor
    from .cloud_pc_audit_category import CloudPcAuditCategory
    from .cloud_pc_audit_resource import CloudPcAuditResource
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcAuditEvent(Entity, Parsable):
    # The friendly name of the audit activity.
    activity: Optional[str] = None
    # The date time in UTC when the activity was performed. Read-only.
    activity_date_time: Optional[datetime.datetime] = None
    # The activityOperationType property
    activity_operation_type: Optional[CloudPcAuditActivityOperationType] = None
    # The activityResult property
    activity_result: Optional[CloudPcAuditActivityResult] = None
    # The type of activity that was performed. Read-only.
    activity_type: Optional[str] = None
    # The actor property
    actor: Optional[CloudPcAuditActor] = None
    # The category property
    category: Optional[CloudPcAuditCategory] = None
    # The component name for the audit event. Read-only.
    component_name: Optional[str] = None
    # The client request ID that is used to correlate activity within the system. Read-only.
    correlation_id: Optional[str] = None
    # The display name for the audit event. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of cloudPcAuditResource objects. Read-only.
    resources: Optional[list[CloudPcAuditResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAuditEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAuditEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_audit_activity_operation_type import CloudPcAuditActivityOperationType
        from .cloud_pc_audit_activity_result import CloudPcAuditActivityResult
        from .cloud_pc_audit_actor import CloudPcAuditActor
        from .cloud_pc_audit_category import CloudPcAuditCategory
        from .cloud_pc_audit_resource import CloudPcAuditResource
        from .entity import Entity

        from .cloud_pc_audit_activity_operation_type import CloudPcAuditActivityOperationType
        from .cloud_pc_audit_activity_result import CloudPcAuditActivityResult
        from .cloud_pc_audit_actor import CloudPcAuditActor
        from .cloud_pc_audit_category import CloudPcAuditCategory
        from .cloud_pc_audit_resource import CloudPcAuditResource
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activityOperationType": lambda n : setattr(self, 'activity_operation_type', n.get_enum_value(CloudPcAuditActivityOperationType)),
            "activityResult": lambda n : setattr(self, 'activity_result', n.get_enum_value(CloudPcAuditActivityResult)),
            "activityType": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(CloudPcAuditActor)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(CloudPcAuditCategory)),
            "componentName": lambda n : setattr(self, 'component_name', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(CloudPcAuditResource)),
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
        writer.write_enum_value("activityOperationType", self.activity_operation_type)
        writer.write_enum_value("activityResult", self.activity_result)
        writer.write_str_value("activityType", self.activity_type)
        writer.write_object_value("actor", self.actor)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("componentName", self.component_name)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
    

