from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_body = lazy_import('msgraph.generated.models.item_body')
service_announcement_attachment = lazy_import('msgraph.generated.models.service_announcement_attachment')
service_announcement_base = lazy_import('msgraph.generated.models.service_announcement_base')
service_update_category = lazy_import('msgraph.generated.models.service_update_category')
service_update_message_viewpoint = lazy_import('msgraph.generated.models.service_update_message_viewpoint')
service_update_severity = lazy_import('msgraph.generated.models.service_update_severity')

class ServiceUpdateMessage(service_announcement_base.ServiceAnnouncementBase):
    @property
    def action_required_by_date_time(self,) -> Optional[datetime]:
        """
        Gets the actionRequiredByDateTime property value. The expected deadline of the action for the message.
        Returns: Optional[datetime]
        """
        return self._action_required_by_date_time
    
    @action_required_by_date_time.setter
    def action_required_by_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the actionRequiredByDateTime property value. The expected deadline of the action for the message.
        Args:
            value: Value to set for the actionRequiredByDateTime property.
        """
        self._action_required_by_date_time = value
    
    @property
    def attachments(self,) -> Optional[List[service_announcement_attachment.ServiceAnnouncementAttachment]]:
        """
        Gets the attachments property value. A collection of serviceAnnouncementAttachments.
        Returns: Optional[List[service_announcement_attachment.ServiceAnnouncementAttachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[service_announcement_attachment.ServiceAnnouncementAttachment]] = None) -> None:
        """
        Sets the attachments property value. A collection of serviceAnnouncementAttachments.
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def attachments_archive(self,) -> Optional[bytes]:
        """
        Gets the attachmentsArchive property value. The zip file that contains all attachments for a message.
        Returns: Optional[bytes]
        """
        return self._attachments_archive
    
    @attachments_archive.setter
    def attachments_archive(self,value: Optional[bytes] = None) -> None:
        """
        Sets the attachmentsArchive property value. The zip file that contains all attachments for a message.
        Args:
            value: Value to set for the attachmentsArchive property.
        """
        self._attachments_archive = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The body property
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The body property
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def category(self,) -> Optional[service_update_category.ServiceUpdateCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[service_update_category.ServiceUpdateCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[service_update_category.ServiceUpdateCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceUpdateMessage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.serviceUpdateMessage"
        # The expected deadline of the action for the message.
        self._action_required_by_date_time: Optional[datetime] = None
        # A collection of serviceAnnouncementAttachments.
        self._attachments: Optional[List[service_announcement_attachment.ServiceAnnouncementAttachment]] = None
        # The zip file that contains all attachments for a message.
        self._attachments_archive: Optional[bytes] = None
        # The body property
        self._body: Optional[item_body.ItemBody] = None
        # The category property
        self._category: Optional[service_update_category.ServiceUpdateCategory] = None
        # Indicates whether the message has any attachment.
        self._has_attachments: Optional[bool] = None
        # Indicates whether the message describes a major update for the service.
        self._is_major_change: Optional[bool] = None
        # The affected services by the service message.
        self._services: Optional[List[str]] = None
        # The severity property
        self._severity: Optional[service_update_severity.ServiceUpdateSeverity] = None
        # A collection of tags for the service message. Tags are provided by the service team/support team who post the message to tell whether this message contains privacy data, or whether this message is for a service new feature update, and so on.
        self._tags: Optional[List[str]] = None
        # Represents user viewpoints data of the service message. This data includes message status such as whether the user has archived, read, or marked the message as favorite. This property is null when accessed with application permissions.
        self._view_point: Optional[service_update_message_viewpoint.ServiceUpdateMessageViewpoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceUpdateMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceUpdateMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceUpdateMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_required_by_date_time": lambda n : setattr(self, 'action_required_by_date_time', n.get_datetime_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(service_announcement_attachment.ServiceAnnouncementAttachment)),
            "attachments_archive": lambda n : setattr(self, 'attachments_archive', n.get_bytes_value()),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(service_update_category.ServiceUpdateCategory)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "is_major_change": lambda n : setattr(self, 'is_major_change', n.get_bool_value()),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_primitive_values(str)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(service_update_severity.ServiceUpdateSeverity)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "view_point": lambda n : setattr(self, 'view_point', n.get_object_value(service_update_message_viewpoint.ServiceUpdateMessageViewpoint)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Indicates whether the message has any attachment.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Indicates whether the message has any attachment.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def is_major_change(self,) -> Optional[bool]:
        """
        Gets the isMajorChange property value. Indicates whether the message describes a major update for the service.
        Returns: Optional[bool]
        """
        return self._is_major_change
    
    @is_major_change.setter
    def is_major_change(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMajorChange property value. Indicates whether the message describes a major update for the service.
        Args:
            value: Value to set for the isMajorChange property.
        """
        self._is_major_change = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("actionRequiredByDateTime", self.action_required_by_date_time)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("attachmentsArchive", self.attachments_archive)
        writer.write_object_value("body", self.body)
        writer.write_enum_value("category", self.category)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_bool_value("isMajorChange", self.is_major_change)
        writer.write_collection_of_primitive_values("services", self.services)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("viewPoint", self.view_point)
    
    @property
    def services(self,) -> Optional[List[str]]:
        """
        Gets the services property value. The affected services by the service message.
        Returns: Optional[List[str]]
        """
        return self._services
    
    @services.setter
    def services(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the services property value. The affected services by the service message.
        Args:
            value: Value to set for the services property.
        """
        self._services = value
    
    @property
    def severity(self,) -> Optional[service_update_severity.ServiceUpdateSeverity]:
        """
        Gets the severity property value. The severity property
        Returns: Optional[service_update_severity.ServiceUpdateSeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[service_update_severity.ServiceUpdateSeverity] = None) -> None:
        """
        Sets the severity property value. The severity property
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. A collection of tags for the service message. Tags are provided by the service team/support team who post the message to tell whether this message contains privacy data, or whether this message is for a service new feature update, and so on.
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. A collection of tags for the service message. Tags are provided by the service team/support team who post the message to tell whether this message contains privacy data, or whether this message is for a service new feature update, and so on.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def view_point(self,) -> Optional[service_update_message_viewpoint.ServiceUpdateMessageViewpoint]:
        """
        Gets the viewPoint property value. Represents user viewpoints data of the service message. This data includes message status such as whether the user has archived, read, or marked the message as favorite. This property is null when accessed with application permissions.
        Returns: Optional[service_update_message_viewpoint.ServiceUpdateMessageViewpoint]
        """
        return self._view_point
    
    @view_point.setter
    def view_point(self,value: Optional[service_update_message_viewpoint.ServiceUpdateMessageViewpoint] = None) -> None:
        """
        Sets the viewPoint property value. Represents user viewpoints data of the service message. This data includes message status such as whether the user has archived, read, or marked the message as favorite. This property is null when accessed with application permissions.
        Args:
            value: Value to set for the viewPoint property.
        """
        self._view_point = value
    

