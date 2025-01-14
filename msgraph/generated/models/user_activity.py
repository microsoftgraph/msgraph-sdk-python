from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_history_item import ActivityHistoryItem
    from .entity import Entity
    from .status import Status
    from .visual_info import VisualInfo

from .entity import Entity

@dataclass
class UserActivity(Entity, Parsable):
    # Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.
    activation_url: Optional[str] = None
    # Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.
    activity_source_host: Optional[str] = None
    # Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.
    app_activity_id: Optional[str] = None
    # Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.
    app_display_name: Optional[str] = None
    # Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).
    content_url: Optional[str] = None
    # Set by the server. DateTime in UTC when the object was created on the server.
    created_date_time: Optional[datetime.datetime] = None
    # Set by the server. DateTime in UTC when the object expired on the server.
    expiration_date_time: Optional[datetime.datetime] = None
    # Optional. URL used to launch the activity in a web-based app, if available.
    fallback_url: Optional[str] = None
    # Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.
    history_items: Optional[list[ActivityHistoryItem]] = None
    # Set by the server. DateTime in UTC when the object was modified on the server.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Set by the server. A status code used to identify valid objects. Values: active, updated, deleted, ignored.
    status: Optional[Status] = None
    # Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.
    user_timezone: Optional[str] = None
    # The visualElements property
    visual_elements: Optional[VisualInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_history_item import ActivityHistoryItem
        from .entity import Entity
        from .status import Status
        from .visual_info import VisualInfo

        from .activity_history_item import ActivityHistoryItem
        from .entity import Entity
        from .status import Status
        from .visual_info import VisualInfo

        fields: dict[str, Callable[[Any], None]] = {
            "activationUrl": lambda n : setattr(self, 'activation_url', n.get_str_value()),
            "activitySourceHost": lambda n : setattr(self, 'activity_source_host', n.get_str_value()),
            "appActivityId": lambda n : setattr(self, 'app_activity_id', n.get_str_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "fallbackUrl": lambda n : setattr(self, 'fallback_url', n.get_str_value()),
            "historyItems": lambda n : setattr(self, 'history_items', n.get_collection_of_object_values(ActivityHistoryItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Status)),
            "userTimezone": lambda n : setattr(self, 'user_timezone', n.get_str_value()),
            "visualElements": lambda n : setattr(self, 'visual_elements', n.get_object_value(VisualInfo)),
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
        writer.write_str_value("activationUrl", self.activation_url)
        writer.write_str_value("activitySourceHost", self.activity_source_host)
        writer.write_str_value("appActivityId", self.app_activity_id)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("fallbackUrl", self.fallback_url)
        writer.write_collection_of_object_values("historyItems", self.history_items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userTimezone", self.user_timezone)
        writer.write_object_value("visualElements", self.visual_elements)
    

