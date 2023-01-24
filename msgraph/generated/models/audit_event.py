from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audit_actor = lazy_import('msgraph.generated.models.audit_actor')
audit_resource = lazy_import('msgraph.generated.models.audit_resource')
entity = lazy_import('msgraph.generated.models.entity')

class AuditEvent(entity.Entity):
    """
    A class containing the properties for Audit Event.
    """
    @property
    def activity(self,) -> Optional[str]:
        """
        Gets the activity property value. Friendly name of the activity.
        Returns: Optional[str]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[str] = None) -> None:
        """
        Sets the activity property value. Friendly name of the activity.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. The date time in UTC when the activity was performed.
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. The date time in UTC when the activity was performed.
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def activity_operation_type(self,) -> Optional[str]:
        """
        Gets the activityOperationType property value. The HTTP operation type of the activity.
        Returns: Optional[str]
        """
        return self._activity_operation_type
    
    @activity_operation_type.setter
    def activity_operation_type(self,value: Optional[str] = None) -> None:
        """
        Sets the activityOperationType property value. The HTTP operation type of the activity.
        Args:
            value: Value to set for the activityOperationType property.
        """
        self._activity_operation_type = value
    
    @property
    def activity_result(self,) -> Optional[str]:
        """
        Gets the activityResult property value. The result of the activity.
        Returns: Optional[str]
        """
        return self._activity_result
    
    @activity_result.setter
    def activity_result(self,value: Optional[str] = None) -> None:
        """
        Sets the activityResult property value. The result of the activity.
        Args:
            value: Value to set for the activityResult property.
        """
        self._activity_result = value
    
    @property
    def activity_type(self,) -> Optional[str]:
        """
        Gets the activityType property value. The type of activity that was being performed.
        Returns: Optional[str]
        """
        return self._activity_type
    
    @activity_type.setter
    def activity_type(self,value: Optional[str] = None) -> None:
        """
        Sets the activityType property value. The type of activity that was being performed.
        Args:
            value: Value to set for the activityType property.
        """
        self._activity_type = value
    
    @property
    def actor(self,) -> Optional[audit_actor.AuditActor]:
        """
        Gets the actor property value. AAD user and application that are associated with the audit event.
        Returns: Optional[audit_actor.AuditActor]
        """
        return self._actor
    
    @actor.setter
    def actor(self,value: Optional[audit_actor.AuditActor] = None) -> None:
        """
        Sets the actor property value. AAD user and application that are associated with the audit event.
        Args:
            value: Value to set for the actor property.
        """
        self._actor = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. Audit category.
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. Audit category.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def component_name(self,) -> Optional[str]:
        """
        Gets the componentName property value. Component name.
        Returns: Optional[str]
        """
        return self._component_name
    
    @component_name.setter
    def component_name(self,value: Optional[str] = None) -> None:
        """
        Sets the componentName property value. Component name.
        Args:
            value: Value to set for the componentName property.
        """
        self._component_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new auditEvent and sets the default values.
        """
        super().__init__()
        # Friendly name of the activity.
        self._activity: Optional[str] = None
        # The date time in UTC when the activity was performed.
        self._activity_date_time: Optional[datetime] = None
        # The HTTP operation type of the activity.
        self._activity_operation_type: Optional[str] = None
        # The result of the activity.
        self._activity_result: Optional[str] = None
        # The type of activity that was being performed.
        self._activity_type: Optional[str] = None
        # AAD user and application that are associated with the audit event.
        self._actor: Optional[audit_actor.AuditActor] = None
        # Audit category.
        self._category: Optional[str] = None
        # Component name.
        self._component_name: Optional[str] = None
        # The client request Id that is used to correlate activity within the system.
        self._correlation_id: Optional[Guid] = None
        # Event display name.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resources being modified.
        self._resources: Optional[List[audit_resource.AuditResource]] = None
    
    @property
    def correlation_id(self,) -> Optional[Guid]:
        """
        Gets the correlationId property value. The client request Id that is used to correlate activity within the system.
        Returns: Optional[Guid]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the correlationId property value. The client request Id that is used to correlate activity within the system.
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditEvent()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Event display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Event display name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "activity_operation_type": lambda n : setattr(self, 'activity_operation_type', n.get_str_value()),
            "activity_result": lambda n : setattr(self, 'activity_result', n.get_str_value()),
            "activity_type": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(audit_actor.AuditActor)),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "component_name": lambda n : setattr(self, 'component_name', n.get_str_value()),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_object_value(Guid)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(audit_resource.AuditResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resources(self,) -> Optional[List[audit_resource.AuditResource]]:
        """
        Gets the resources property value. Resources being modified.
        Returns: Optional[List[audit_resource.AuditResource]]
        """
        return self._resources
    
    @resources.setter
    def resources(self,value: Optional[List[audit_resource.AuditResource]] = None) -> None:
        """
        Sets the resources property value. Resources being modified.
        Args:
            value: Value to set for the resources property.
        """
        self._resources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("activityOperationType", self.activity_operation_type)
        writer.write_str_value("activityResult", self.activity_result)
        writer.write_str_value("activityType", self.activity_type)
        writer.write_object_value("actor", self.actor)
        writer.write_str_value("category", self.category)
        writer.write_str_value("componentName", self.component_name)
        writer.write_object_value("correlationId", self.correlation_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
    

