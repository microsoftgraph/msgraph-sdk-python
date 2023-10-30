from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audit_activity_initiator import AuditActivityInitiator
    from .entity import Entity
    from .key_value import KeyValue
    from .operation_result import OperationResult
    from .target_resource import TargetResource

from .entity import Entity

@dataclass
class DirectoryAudit(Entity):
    # Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and $orderby.
    activity_date_time: Optional[datetime.datetime] = None
    # Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For a list of activities logged, refer to Microsoft Entra audit log categories and activities. Supports $filter (eq, startswith).
    activity_display_name: Optional[str] = None
    # Indicates additional details on the activity.
    additional_details: Optional[List[KeyValue]] = None
    # Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement. For a list of categories for activities logged, refer to Microsoft Entra audit log categories and activities.
    category: Optional[str] = None
    # Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services. Supports $filter (eq).
    correlation_id: Optional[str] = None
    # The initiatedBy property
    initiated_by: Optional[AuditActivityInitiator] = None
    # Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management. Supports $filter (eq).
    logged_by_service: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
    operation_type: Optional[str] = None
    # Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
    result: Optional[OperationResult] = None
    # Indicates the reason for failure if the result is failure or timeout.
    result_reason: Optional[str] = None
    # Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other. Supports $filter (eq) for id and displayName; and $filter (startswith) for displayName.
    target_resources: Optional[List[TargetResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryAudit
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DirectoryAudit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .audit_activity_initiator import AuditActivityInitiator
        from .entity import Entity
        from .key_value import KeyValue
        from .operation_result import OperationResult
        from .target_resource import TargetResource

        from .audit_activity_initiator import AuditActivityInitiator
        from .entity import Entity
        from .key_value import KeyValue
        from .operation_result import OperationResult
        from .target_resource import TargetResource

        fields: Dict[str, Callable[[Any], None]] = {
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activity_display_name": lambda n : setattr(self, 'activity_display_name', n.get_str_value()),
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(KeyValue)),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "initiated_by": lambda n : setattr(self, 'initiated_by', n.get_object_value(AuditActivityInitiator)),
            "logged_by_service": lambda n : setattr(self, 'logged_by_service', n.get_str_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(OperationResult)),
            "result_reason": lambda n : setattr(self, 'result_reason', n.get_str_value()),
            "target_resources": lambda n : setattr(self, 'target_resources', n.get_collection_of_object_values(TargetResource)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("activity_date_time", self.activity_date_time)
        writer.write_str_value("activity_display_name", self.activity_display_name)
        writer.write_collection_of_object_values("additional_details", self.additional_details)
        writer.write_str_value("category", self.category)
        writer.write_str_value("correlation_id", self.correlation_id)
        writer.write_object_value("initiated_by", self.initiated_by)
        writer.write_str_value("logged_by_service", self.logged_by_service)
        writer.write_str_value("operation_type", self.operation_type)
        writer.write_enum_value("result", self.result)
        writer.write_str_value("result_reason", self.result_reason)
        writer.write_collection_of_object_values("target_resources", self.target_resources)
    

