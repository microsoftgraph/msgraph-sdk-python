from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment_base import AttachmentBase
    from .attachment_session import AttachmentSession
    from .checklist_item import ChecklistItem
    from .date_time_time_zone import DateTimeTimeZone
    from .entity import Entity
    from .extension import Extension
    from .importance import Importance
    from .item_body import ItemBody
    from .linked_resource import LinkedResource
    from .patterned_recurrence import PatternedRecurrence
    from .task_status import TaskStatus

from .entity import Entity

@dataclass
class TodoTask(Entity, Parsable):
    # The attachmentSessions property
    attachment_sessions: Optional[list[AttachmentSession]] = None
    # A collection of file attachments for the task.
    attachments: Optional[list[AttachmentBase]] = None
    # The task body that typically contains information about the task.
    body: Optional[ItemBody] = None
    # The date and time when the task body was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
    body_last_modified_date_time: Optional[datetime.datetime] = None
    # The categories associated with the task. Each category corresponds to the displayName property of an outlookCategory that the user has defined.
    categories: Optional[list[str]] = None
    # A collection of checklistItems linked to a task.
    checklist_items: Optional[list[ChecklistItem]] = None
    # The date and time in the specified time zone that the task was finished.
    completed_date_time: Optional[DateTimeTimeZone] = None
    # The date and time when the task was created. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time in the specified time zone that the task is to be finished.
    due_date_time: Optional[DateTimeTimeZone] = None
    # The collection of open extensions defined for the task. Nullable.
    extensions: Optional[list[Extension]] = None
    # Indicates whether the task has attachments.
    has_attachments: Optional[bool] = None
    # The importance property
    importance: Optional[Importance] = None
    # Set to true if an alert is set to remind the user of the task.
    is_reminder_on: Optional[bool] = None
    # The date and time when the task was last modified. By default, it is in UTC. You can provide a custom time zone in the request header. The property value uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2020 would look like this: '2020-01-01T00:00:00Z'.
    last_modified_date_time: Optional[datetime.datetime] = None
    # A collection of resources linked to the task.
    linked_resources: Optional[list[LinkedResource]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recurrence pattern for the task.
    recurrence: Optional[PatternedRecurrence] = None
    # The date and time in the specified time zone for a reminder alert of the task to occur.
    reminder_date_time: Optional[DateTimeTimeZone] = None
    # The date and time in the specified time zone at which the task is scheduled to start.
    start_date_time: Optional[DateTimeTimeZone] = None
    # The status property
    status: Optional[TaskStatus] = None
    # A brief description of the task.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TodoTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TodoTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TodoTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attachment_base import AttachmentBase
        from .attachment_session import AttachmentSession
        from .checklist_item import ChecklistItem
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .extension import Extension
        from .importance import Importance
        from .item_body import ItemBody
        from .linked_resource import LinkedResource
        from .patterned_recurrence import PatternedRecurrence
        from .task_status import TaskStatus

        from .attachment_base import AttachmentBase
        from .attachment_session import AttachmentSession
        from .checklist_item import ChecklistItem
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .extension import Extension
        from .importance import Importance
        from .item_body import ItemBody
        from .linked_resource import LinkedResource
        from .patterned_recurrence import PatternedRecurrence
        from .task_status import TaskStatus

        fields: dict[str, Callable[[Any], None]] = {
            "attachmentSessions": lambda n : setattr(self, 'attachment_sessions', n.get_collection_of_object_values(AttachmentSession)),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(AttachmentBase)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "bodyLastModifiedDateTime": lambda n : setattr(self, 'body_last_modified_date_time', n.get_datetime_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "checklistItems": lambda n : setattr(self, 'checklist_items', n.get_collection_of_object_values(ChecklistItem)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_object_value(DateTimeTimeZone)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_object_value(DateTimeTimeZone)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(Importance)),
            "isReminderOn": lambda n : setattr(self, 'is_reminder_on', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "linkedResources": lambda n : setattr(self, 'linked_resources', n.get_collection_of_object_values(LinkedResource)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "reminderDateTime": lambda n : setattr(self, 'reminder_date_time', n.get_object_value(DateTimeTimeZone)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TaskStatus)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_object_values("attachmentSessions", self.attachment_sessions)
        writer.write_collection_of_object_values("attachments", self.attachments)
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
    

