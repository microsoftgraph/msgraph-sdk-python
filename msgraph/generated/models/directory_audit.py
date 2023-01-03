from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audit_activity_initiator = lazy_import('msgraph.generated.models.audit_activity_initiator')
entity = lazy_import('msgraph.generated.models.entity')
key_value = lazy_import('msgraph.generated.models.key_value')
operation_result = lazy_import('msgraph.generated.models.operation_result')
target_resource = lazy_import('msgraph.generated.models.target_resource')

class DirectoryAudit(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def activity_display_name(self,) -> Optional[str]:
        """
        Gets the activityDisplayName property value. Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.
        Returns: Optional[str]
        """
        return self._activity_display_name
    
    @activity_display_name.setter
    def activity_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the activityDisplayName property value. Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.
        Args:
            value: Value to set for the activityDisplayName property.
        """
        self._activity_display_name = value
    
    @property
    def additional_details(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the additionalDetails property value. Indicates additional details on the activity.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the additionalDetails property value. Indicates additional details on the activity.
        Args:
            value: Value to set for the additionalDetails property.
        """
        self._additional_details = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new directoryAudit and sets the default values.
        """
        super().__init__()
        # Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._activity_date_time: Optional[datetime] = None
        # Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.
        self._activity_display_name: Optional[str] = None
        # Indicates additional details on the activity.
        self._additional_details: Optional[List[key_value.KeyValue]] = None
        # Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement.
        self._category: Optional[str] = None
        # Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
        self._correlation_id: Optional[str] = None
        # The initiatedBy property
        self._initiated_by: Optional[audit_activity_initiator.AuditActivityInitiator] = None
        # Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
        self._logged_by_service: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
        self._operation_type: Optional[str] = None
        # Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
        self._result: Optional[operation_result.OperationResult] = None
        # Indicates the reason for failure if the result is failure or timeout.
        self._result_reason: Optional[str] = None
        # Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.
        self._target_resources: Optional[List[target_resource.TargetResource]] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryAudit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectoryAudit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activity_display_name": lambda n : setattr(self, 'activity_display_name', n.get_str_value()),
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(key_value.KeyValue)),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "initiated_by": lambda n : setattr(self, 'initiated_by', n.get_object_value(audit_activity_initiator.AuditActivityInitiator)),
            "logged_by_service": lambda n : setattr(self, 'logged_by_service', n.get_str_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_str_value()),
            "result": lambda n : setattr(self, 'result', n.get_enum_value(operation_result.OperationResult)),
            "result_reason": lambda n : setattr(self, 'result_reason', n.get_str_value()),
            "target_resources": lambda n : setattr(self, 'target_resources', n.get_collection_of_object_values(target_resource.TargetResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiated_by(self,) -> Optional[audit_activity_initiator.AuditActivityInitiator]:
        """
        Gets the initiatedBy property value. The initiatedBy property
        Returns: Optional[audit_activity_initiator.AuditActivityInitiator]
        """
        return self._initiated_by
    
    @initiated_by.setter
    def initiated_by(self,value: Optional[audit_activity_initiator.AuditActivityInitiator] = None) -> None:
        """
        Sets the initiatedBy property value. The initiatedBy property
        Args:
            value: Value to set for the initiatedBy property.
        """
        self._initiated_by = value
    
    @property
    def logged_by_service(self,) -> Optional[str]:
        """
        Gets the loggedByService property value. Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
        Returns: Optional[str]
        """
        return self._logged_by_service
    
    @logged_by_service.setter
    def logged_by_service(self,value: Optional[str] = None) -> None:
        """
        Sets the loggedByService property value. Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.
        Args:
            value: Value to set for the loggedByService property.
        """
        self._logged_by_service = value
    
    @property
    def operation_type(self,) -> Optional[str]:
        """
        Gets the operationType property value. Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
        Returns: Optional[str]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[str] = None) -> None:
        """
        Sets the operationType property value. Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
        Args:
            value: Value to set for the operationType property.
        """
        self._operation_type = value
    
    @property
    def result(self,) -> Optional[operation_result.OperationResult]:
        """
        Gets the result property value. Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
        Returns: Optional[operation_result.OperationResult]
        """
        return self._result
    
    @result.setter
    def result(self,value: Optional[operation_result.OperationResult] = None) -> None:
        """
        Sets the result property value. Indicates the result of the activity. Possible values are: success, failure, timeout, unknownFutureValue.
        Args:
            value: Value to set for the result property.
        """
        self._result = value
    
    @property
    def result_reason(self,) -> Optional[str]:
        """
        Gets the resultReason property value. Indicates the reason for failure if the result is failure or timeout.
        Returns: Optional[str]
        """
        return self._result_reason
    
    @result_reason.setter
    def result_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the resultReason property value. Indicates the reason for failure if the result is failure or timeout.
        Args:
            value: Value to set for the resultReason property.
        """
        self._result_reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityDisplayName", self.activity_display_name)
        writer.write_collection_of_object_values("additionalDetails", self.additional_details)
        writer.write_str_value("category", self.category)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_str_value("loggedByService", self.logged_by_service)
        writer.write_str_value("operationType", self.operation_type)
        writer.write_enum_value("result", self.result)
        writer.write_str_value("resultReason", self.result_reason)
        writer.write_collection_of_object_values("targetResources", self.target_resources)
    
    @property
    def target_resources(self,) -> Optional[List[target_resource.TargetResource]]:
        """
        Gets the targetResources property value. Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.
        Returns: Optional[List[target_resource.TargetResource]]
        """
        return self._target_resources
    
    @target_resources.setter
    def target_resources(self,value: Optional[List[target_resource.TargetResource]] = None) -> None:
        """
        Sets the targetResources property value. Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.
        Args:
            value: Value to set for the targetResources property.
        """
        self._target_resources = value
    

