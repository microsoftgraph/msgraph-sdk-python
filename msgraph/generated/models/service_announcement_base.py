from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .key_value_pair import KeyValuePair
    from .service_health_issue import ServiceHealthIssue
    from .service_update_message import ServiceUpdateMessage

from .entity import Entity

@dataclass
class ServiceAnnouncementBase(Entity, Parsable):
    # More details about service event. This property doesn't support filters.
    details: Optional[list[KeyValuePair]] = None
    # The end time of the service event.
    end_date_time: Optional[datetime.datetime] = None
    # The last modified time of the service event.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The start time of the service event.
    start_date_time: Optional[datetime.datetime] = None
    # The title of the service event.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceAnnouncementBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceAnnouncementBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealthIssue".casefold():
            from .service_health_issue import ServiceHealthIssue

            return ServiceHealthIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceUpdateMessage".casefold():
            from .service_update_message import ServiceUpdateMessage

            return ServiceUpdateMessage()
        return ServiceAnnouncementBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .service_health_issue import ServiceHealthIssue
        from .service_update_message import ServiceUpdateMessage

        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .service_health_issue import ServiceHealthIssue
        from .service_update_message import ServiceUpdateMessage

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(KeyValuePair)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("details", self.details)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
    

