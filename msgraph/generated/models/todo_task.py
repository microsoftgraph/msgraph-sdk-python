from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment_base = lazy_import('msgraph.generated.models.attachment_base')
attachment_session = lazy_import('msgraph.generated.models.attachment_session')
checklist_item = lazy_import('msgraph.generated.models.checklist_item')
date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
entity = lazy_import('msgraph.generated.models.entity')
extension = lazy_import('msgraph.generated.models.extension')
importance = lazy_import('msgraph.generated.models.importance')
item_body = lazy_import('msgraph.generated.models.item_body')
linked_resource = lazy_import('msgraph.generated.models.linked_resource')
patterned_recurrence = lazy_import('msgraph.generated.models.patterned_recurrence')
task_status = lazy_import('msgraph.generated.models.task_status')

class TodoTask(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def attachments(self,) -> Optional[List[attachment_base.AttachmentBase]]:
        """
        Gets the attachments property value. The attachments property
        Returns: Optional[List[attachment_base.AttachmentBase]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[attachment_base.AttachmentBase]] = None) -> None:
        """
        Sets the attachments property value. The attachments property
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def attachment_sessions(self,) -> Optional[List[attachment_session.AttachmentSession]]:
        """
        Gets the attachmentSessions property value. The attachmentSessions property
        Returns: Optional[List[attachment_session.AttachmentSession]]
        """
        return self._attachment_sessions
    
    @attachment_sessions.setter
    def attachment_sessions(self,value: Optional[List[attachment_session.AttachmentSession]] = None) -> None:
        """
        Sets the attachmentSessions property value. The attachmentSessions property
        Args:
            value: Value to set for the attachmentSessions property.
        """
        self._attachment_sessions = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The task body that typically contains information about the task.
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The task body that typically contains information about the task.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def body_last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the bodyLastModifiedDateTime property value. The date and time when the task body was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._body_last_modified_date_time
    
    @body_last_modified_date_time.setter
    def body_last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the bodyLastModifiedDateTime property value. The date and time when the task body was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        Args:
            value: Value to set for the bodyLastModifiedDateTime property.
        """
        self._body_last_modified_date_time = value
    
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. The categories associated with the task. Each category corresponds to the displayName property of an outlookCategory that the user has defined.
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. The categories associated with the task. Each category corresponds to the displayName property of an outlookCategory that the user has defined.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    @property
    def checklist_items(self,) -> Optional[List[checklist_item.ChecklistItem]]:
        """
        Gets the checklistItems property value. A collection of checklistItems linked to a task.
        Returns: Optional[List[checklist_item.ChecklistItem]]
        """
        return self._checklist_items
    
    @checklist_items.setter
    def checklist_items(self,value: Optional[List[checklist_item.ChecklistItem]] = None) -> None:
        """
        Sets the checklistItems property value. A collection of checklistItems linked to a task.
        Args:
            value: Value to set for the checklistItems property.
        """
        self._checklist_items = value
    
    @property
    def completed_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the completedDateTime property value. The date and time in the specified time zone that the task was finished.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the completedDateTime property value. The date and time in the specified time zone that the task was finished.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new todoTask and sets the default values.
        """
        super().__init__()
        # The attachments property
        self._attachments: Optional[List[attachment_base.AttachmentBase]] = None
        # The attachmentSessions property
        self._attachment_sessions: Optional[List[attachment_session.AttachmentSession]] = None
        # The task body that typically contains information about the task.
        self._body: Optional[item_body.ItemBody] = None
        # The date and time when the task body was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        self._body_last_modified_date_time: Optional[datetime] = None
        # The categories associated with the task. Each category corresponds to the displayName property of an outlookCategory that the user has defined.
        self._categories: Optional[List[str]] = None
        # A collection of checklistItems linked to a task.
        self._checklist_items: Optional[List[checklist_item.ChecklistItem]] = None
        # The date and time in the specified time zone that the task was finished.
        self._completed_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The date and time when the task was created. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        self._created_date_time: Optional[datetime] = None
        # The date and time in the specified time zone that the task is to be finished.
        self._due_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The collection of open extensions defined for the task. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # The hasAttachments property
        self._has_attachments: Optional[bool] = None
        # The importance property
        self._importance: Optional[importance.Importance] = None
        # Set to true if an alert is set to remind the user of the task.
        self._is_reminder_on: Optional[bool] = None
        # The date and time when the task was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        self._last_modified_date_time: Optional[datetime] = None
        # A collection of resources linked to the task.
        self._linked_resources: Optional[List[linked_resource.LinkedResource]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The recurrence pattern for the task.
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # The date and time in the specified time zone for a reminder alert of the task to occur.
        self._reminder_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The startDateTime property
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The status property
        self._status: Optional[task_status.TaskStatus] = None
        # A brief description of the task.
        self._title: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the task was created. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the task was created. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TodoTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TodoTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TodoTask()
    
    @property
    def due_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the dueDateTime property value. The date and time in the specified time zone that the task is to be finished.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the dueDateTime property value. The date and time in the specified time zone that the task is to be finished.
        Args:
            value: Value to set for the dueDateTime property.
        """
        self._due_date_time = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the task. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the task. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(attachment_base.AttachmentBase)),
            "attachment_sessions": lambda n : setattr(self, 'attachment_sessions', n.get_collection_of_object_values(attachment_session.AttachmentSession)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "body_last_modified_date_time": lambda n : setattr(self, 'body_last_modified_date_time', n.get_datetime_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "checklist_items": lambda n : setattr(self, 'checklist_items', n.get_collection_of_object_values(checklist_item.ChecklistItem)),
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "due_date_time": lambda n : setattr(self, 'due_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(importance.Importance)),
            "is_reminder_on": lambda n : setattr(self, 'is_reminder_on', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "linked_resources": lambda n : setattr(self, 'linked_resources', n.get_collection_of_object_values(linked_resource.LinkedResource)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "reminder_date_time": lambda n : setattr(self, 'reminder_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(task_status.TaskStatus)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. The hasAttachments property
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. The hasAttachments property
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def importance(self,) -> Optional[importance.Importance]:
        """
        Gets the importance property value. The importance property
        Returns: Optional[importance.Importance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[importance.Importance] = None) -> None:
        """
        Sets the importance property value. The importance property
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
    @property
    def is_reminder_on(self,) -> Optional[bool]:
        """
        Gets the isReminderOn property value. Set to true if an alert is set to remind the user of the task.
        Returns: Optional[bool]
        """
        return self._is_reminder_on
    
    @is_reminder_on.setter
    def is_reminder_on(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReminderOn property value. Set to true if an alert is set to remind the user of the task.
        Args:
            value: Value to set for the isReminderOn property.
        """
        self._is_reminder_on = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the task was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the task was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def linked_resources(self,) -> Optional[List[linked_resource.LinkedResource]]:
        """
        Gets the linkedResources property value. A collection of resources linked to the task.
        Returns: Optional[List[linked_resource.LinkedResource]]
        """
        return self._linked_resources
    
    @linked_resources.setter
    def linked_resources(self,value: Optional[List[linked_resource.LinkedResource]] = None) -> None:
        """
        Sets the linkedResources property value. A collection of resources linked to the task.
        Args:
            value: Value to set for the linkedResources property.
        """
        self._linked_resources = value
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. The recurrence pattern for the task.
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. The recurrence pattern for the task.
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    @property
    def reminder_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the reminderDateTime property value. The date and time in the specified time zone for a reminder alert of the task to occur.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._reminder_date_time
    
    @reminder_date_time.setter
    def reminder_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the reminderDateTime property value. The date and time in the specified time zone for a reminder alert of the task to occur.
        Args:
            value: Value to set for the reminderDateTime property.
        """
        self._reminder_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_collection_of_object_values("attachmentSessions", self.attachment_sessions)
        writer.write_object_value("body", self.body)
        writer.write_datetime_value("bodyLastModifiedDateTime", self.body_last_modified_date_time)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("checklistItems", self.checklist_items)
        writer.write_object_value("completedDateTime", self.completed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_enum_value("importance", self.importance)
        writer.write_bool_value("isReminderOn", self.is_reminder_on)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("linkedResources", self.linked_resources)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_object_value("reminderDateTime", self.reminder_date_time)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
    
    @property
    def start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[task_status.TaskStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[task_status.TaskStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[task_status.TaskStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. A brief description of the task.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. A brief description of the task.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

