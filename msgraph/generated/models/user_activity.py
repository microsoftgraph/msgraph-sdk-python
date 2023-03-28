from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_history_item, entity, json, status, visual_info

from . import entity

class UserActivity(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userActivity and sets the default values.
        """
        super().__init__()
        # Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.
        self._activation_url: Optional[str] = None
        # Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.
        self._activity_source_host: Optional[str] = None
        # Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.
        self._app_activity_id: Optional[str] = None
        # Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.
        self._app_display_name: Optional[str] = None
        # Optional. A custom piece of data - JSON-LD extensible description of content according to schema.org syntax.
        self._content_info: Optional[json.Json] = None
        # Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).
        self._content_url: Optional[str] = None
        # Set by the server. DateTime in UTC when the object was created on the server.
        self._created_date_time: Optional[datetime] = None
        # Set by the server. DateTime in UTC when the object expired on the server.
        self._expiration_date_time: Optional[datetime] = None
        # Optional. URL used to launch the activity in a web-based app, if available.
        self._fallback_url: Optional[str] = None
        # Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.
        self._history_items: Optional[List[activity_history_item.ActivityHistoryItem]] = None
        # Set by the server. DateTime in UTC when the object was modified on the server.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Set by the server. A status code used to identify valid objects. Values: active, updated, deleted, ignored.
        self._status: Optional[status.Status] = None
        # Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.
        self._user_timezone: Optional[str] = None
        # The visualElements property
        self._visual_elements: Optional[visual_info.VisualInfo] = None
    
    @property
    def activation_url(self,) -> Optional[str]:
        """
        Gets the activationUrl property value. Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.
        Returns: Optional[str]
        """
        return self._activation_url
    
    @activation_url.setter
    def activation_url(self,value: Optional[str] = None) -> None:
        """
        Sets the activationUrl property value. Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.
        Args:
            value: Value to set for the activation_url property.
        """
        self._activation_url = value
    
    @property
    def activity_source_host(self,) -> Optional[str]:
        """
        Gets the activitySourceHost property value. Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.
        Returns: Optional[str]
        """
        return self._activity_source_host
    
    @activity_source_host.setter
    def activity_source_host(self,value: Optional[str] = None) -> None:
        """
        Sets the activitySourceHost property value. Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.
        Args:
            value: Value to set for the activity_source_host property.
        """
        self._activity_source_host = value
    
    @property
    def app_activity_id(self,) -> Optional[str]:
        """
        Gets the appActivityId property value. Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.
        Returns: Optional[str]
        """
        return self._app_activity_id
    
    @app_activity_id.setter
    def app_activity_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appActivityId property value. Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.
        Args:
            value: Value to set for the app_activity_id property.
        """
        self._app_activity_id = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.
        Args:
            value: Value to set for the app_display_name property.
        """
        self._app_display_name = value
    
    @property
    def content_info(self,) -> Optional[json.Json]:
        """
        Gets the contentInfo property value. Optional. A custom piece of data - JSON-LD extensible description of content according to schema.org syntax.
        Returns: Optional[json.Json]
        """
        return self._content_info
    
    @content_info.setter
    def content_info(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the contentInfo property value. Optional. A custom piece of data - JSON-LD extensible description of content according to schema.org syntax.
        Args:
            value: Value to set for the content_info property.
        """
        self._content_info = value
    
    @property
    def content_url(self,) -> Optional[str]:
        """
        Gets the contentUrl property value. Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).
        Returns: Optional[str]
        """
        return self._content_url
    
    @content_url.setter
    def content_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentUrl property value. Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).
        Args:
            value: Value to set for the content_url property.
        """
        self._content_url = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Set by the server. DateTime in UTC when the object was created on the server.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Set by the server. DateTime in UTC when the object was created on the server.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserActivity()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Set by the server. DateTime in UTC when the object expired on the server.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Set by the server. DateTime in UTC when the object expired on the server.
        Args:
            value: Value to set for the expiration_date_time property.
        """
        self._expiration_date_time = value
    
    @property
    def fallback_url(self,) -> Optional[str]:
        """
        Gets the fallbackUrl property value. Optional. URL used to launch the activity in a web-based app, if available.
        Returns: Optional[str]
        """
        return self._fallback_url
    
    @fallback_url.setter
    def fallback_url(self,value: Optional[str] = None) -> None:
        """
        Sets the fallbackUrl property value. Optional. URL used to launch the activity in a web-based app, if available.
        Args:
            value: Value to set for the fallback_url property.
        """
        self._fallback_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_history_item, entity, json, status, visual_info

        fields: Dict[str, Callable[[Any], None]] = {
            "activationUrl": lambda n : setattr(self, 'activation_url', n.get_str_value()),
            "activitySourceHost": lambda n : setattr(self, 'activity_source_host', n.get_str_value()),
            "appActivityId": lambda n : setattr(self, 'app_activity_id', n.get_str_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "contentInfo": lambda n : setattr(self, 'content_info', n.get_object_value(json.Json)),
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "fallbackUrl": lambda n : setattr(self, 'fallback_url', n.get_str_value()),
            "historyItems": lambda n : setattr(self, 'history_items', n.get_collection_of_object_values(activity_history_item.ActivityHistoryItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(status.Status)),
            "userTimezone": lambda n : setattr(self, 'user_timezone', n.get_str_value()),
            "visualElements": lambda n : setattr(self, 'visual_elements', n.get_object_value(visual_info.VisualInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history_items(self,) -> Optional[List[activity_history_item.ActivityHistoryItem]]:
        """
        Gets the historyItems property value. Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.
        Returns: Optional[List[activity_history_item.ActivityHistoryItem]]
        """
        return self._history_items
    
    @history_items.setter
    def history_items(self,value: Optional[List[activity_history_item.ActivityHistoryItem]] = None) -> None:
        """
        Sets the historyItems property value. Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.
        Args:
            value: Value to set for the history_items property.
        """
        self._history_items = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Set by the server. DateTime in UTC when the object was modified on the server.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Set by the server. DateTime in UTC when the object was modified on the server.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activationUrl", self.activation_url)
        writer.write_str_value("activitySourceHost", self.activity_source_host)
        writer.write_str_value("appActivityId", self.app_activity_id)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("fallbackUrl", self.fallback_url)
        writer.write_collection_of_object_values("historyItems", self.history_items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userTimezone", self.user_timezone)
        writer.write_object_value("visualElements", self.visual_elements)
    
    @property
    def status(self,) -> Optional[status.Status]:
        """
        Gets the status property value. Set by the server. A status code used to identify valid objects. Values: active, updated, deleted, ignored.
        Returns: Optional[status.Status]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[status.Status] = None) -> None:
        """
        Sets the status property value. Set by the server. A status code used to identify valid objects. Values: active, updated, deleted, ignored.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_timezone(self,) -> Optional[str]:
        """
        Gets the userTimezone property value. Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.
        Returns: Optional[str]
        """
        return self._user_timezone
    
    @user_timezone.setter
    def user_timezone(self,value: Optional[str] = None) -> None:
        """
        Sets the userTimezone property value. Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.
        Args:
            value: Value to set for the user_timezone property.
        """
        self._user_timezone = value
    
    @property
    def visual_elements(self,) -> Optional[visual_info.VisualInfo]:
        """
        Gets the visualElements property value. The visualElements property
        Returns: Optional[visual_info.VisualInfo]
        """
        return self._visual_elements
    
    @visual_elements.setter
    def visual_elements(self,value: Optional[visual_info.VisualInfo] = None) -> None:
        """
        Sets the visualElements property value. The visualElements property
        Args:
            value: Value to set for the visual_elements property.
        """
        self._visual_elements = value
    

