from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .service_announcement_attachment import ServiceAnnouncementAttachment
    from .service_announcement_base import ServiceAnnouncementBase
    from .service_update_category import ServiceUpdateCategory
    from .service_update_message_viewpoint import ServiceUpdateMessageViewpoint
    from .service_update_severity import ServiceUpdateSeverity

from .service_announcement_base import ServiceAnnouncementBase

@dataclass
class ServiceUpdateMessage(ServiceAnnouncementBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.serviceUpdateMessage"
    # The expected deadline of the action for the message.
    action_required_by_date_time: Optional[datetime.datetime] = None
    # A collection of serviceAnnouncementAttachments.
    attachments: Optional[list[ServiceAnnouncementAttachment]] = None
    # The zip file that contains all attachments for a message.
    attachments_archive: Optional[bytes] = None
    # The body property
    body: Optional[ItemBody] = None
    # The category property
    category: Optional[ServiceUpdateCategory] = None
    # Indicates whether the message has any attachment.
    has_attachments: Optional[bool] = None
    # Indicates whether the message describes a major update for the service.
    is_major_change: Optional[bool] = None
    # The affected services by the service message.
    services: Optional[list[str]] = None
    # The severity property
    severity: Optional[ServiceUpdateSeverity] = None
    # A collection of tags for the service message. Tags are provided by the service team/support team who post the message to tell whether this message contains privacy data, or whether this message is for a service new feature update, and so on.
    tags: Optional[list[str]] = None
    # Represents user viewpoints data of the service message. This data includes message status such as whether the user has archived, read, or marked the message as favorite. This property is null when accessed with application permissions.
    view_point: Optional[ServiceUpdateMessageViewpoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceUpdateMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceUpdateMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceUpdateMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .service_announcement_attachment import ServiceAnnouncementAttachment
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_update_category import ServiceUpdateCategory
        from .service_update_message_viewpoint import ServiceUpdateMessageViewpoint
        from .service_update_severity import ServiceUpdateSeverity

        from .item_body import ItemBody
        from .service_announcement_attachment import ServiceAnnouncementAttachment
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_update_category import ServiceUpdateCategory
        from .service_update_message_viewpoint import ServiceUpdateMessageViewpoint
        from .service_update_severity import ServiceUpdateSeverity

        fields: dict[str, Callable[[Any], None]] = {
            "actionRequiredByDateTime": lambda n : setattr(self, 'action_required_by_date_time', n.get_datetime_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(ServiceAnnouncementAttachment)),
            "attachmentsArchive": lambda n : setattr(self, 'attachments_archive', n.get_bytes_value()),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ServiceUpdateCategory)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "isMajorChange": lambda n : setattr(self, 'is_major_change', n.get_bool_value()),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_primitive_values(str)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(ServiceUpdateSeverity)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "viewPoint": lambda n : setattr(self, 'view_point', n.get_object_value(ServiceUpdateMessageViewpoint)),
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
        writer.write_datetime_value("actionRequiredByDateTime", self.action_required_by_date_time)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_bytes_value("attachmentsArchive", self.attachments_archive)
        writer.write_object_value("body", self.body)
        writer.write_enum_value("category", self.category)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_bool_value("isMajorChange", self.is_major_change)
        writer.write_collection_of_primitive_values("services", self.services)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("viewPoint", self.view_point)
    

