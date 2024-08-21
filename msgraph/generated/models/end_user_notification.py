from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .end_user_notification_detail import EndUserNotificationDetail
    from .end_user_notification_type import EndUserNotificationType
    from .entity import Entity
    from .simulation_content_source import SimulationContentSource
    from .simulation_content_status import SimulationContentStatus

from .entity import Entity

@dataclass
class EndUserNotification(Entity):
    # Identity of the user who created the notification.
    created_by: Optional[EmailIdentity] = None
    # Date and time when the notification was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the notification as defined by the user.
    description: Optional[str] = None
    # The details property
    details: Optional[List[EndUserNotificationDetail]] = None
    # Name of the notification as defined by the user.
    display_name: Optional[str] = None
    # Identity of the user who last modified the notification.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time when the notification was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Type of notification. Possible values are: unknown, positiveReinforcement, noTraining, trainingAssignment, trainingReminder, unknownFutureValue.
    notification_type: Optional[EndUserNotificationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source of the content. Possible values are: unknown, global, tenant, unknownFutureValue.
    source: Optional[SimulationContentSource] = None
    # The status of the notification. Possible values are: unknown, draft, ready, archive, delete, unknownFutureValue.
    status: Optional[SimulationContentStatus] = None
    # Supported locales for endUserNotification content.
    supported_locales: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndUserNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndUserNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndUserNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .end_user_notification_detail import EndUserNotificationDetail
        from .end_user_notification_type import EndUserNotificationType
        from .entity import Entity
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        from .email_identity import EmailIdentity
        from .end_user_notification_detail import EndUserNotificationDetail
        from .end_user_notification_type import EndUserNotificationType
        from .entity import Entity
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(EndUserNotificationDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notificationType": lambda n : setattr(self, 'notification_type', n.get_enum_value(EndUserNotificationType)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationContentStatus)),
            "supportedLocales": lambda n : setattr(self, 'supported_locales', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("notificationType", self.notification_type)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("supportedLocales", self.supported_locales)
    

