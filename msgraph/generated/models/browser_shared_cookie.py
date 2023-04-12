from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_shared_cookie_history, browser_shared_cookie_source_environment, browser_shared_cookie_status, entity, identity_set

from . import entity

class BrowserSharedCookie(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new browserSharedCookie and sets the default values.
        """
        super().__init__()
        # The comment for the shared cookie.
        self._comment: Optional[str] = None
        # The date and time when the shared cookie was created.
        self._created_date_time: Optional[datetime] = None
        # The date and time when the shared cookie was deleted.
        self._deleted_date_time: Optional[datetime] = None
        # The name of the cookie.
        self._display_name: Optional[str] = None
        # The history of modifications applied to the cookie.
        self._history: Optional[List[browser_shared_cookie_history.BrowserSharedCookieHistory]] = None
        # Controls whether a cookie is a host-only or domain cookie.
        self._host_only: Optional[bool] = None
        # The URL of the cookie.
        self._host_or_domain: Optional[str] = None
        # The user who last modified the cookie.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the cookie was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The path of the cookie.
        self._path: Optional[str] = None
        # The sourceEnvironment property
        self._source_environment: Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment] = None
        # The status property
        self._status: Optional[browser_shared_cookie_status.BrowserSharedCookieStatus] = None
    
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The comment for the shared cookie.
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The comment for the shared cookie.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the shared cookie was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the shared cookie was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSharedCookie:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSharedCookie
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BrowserSharedCookie()
    
    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. The date and time when the shared cookie was deleted.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time
    
    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. The date and time when the shared cookie was deleted.
        Args:
            value: Value to set for the deleted_date_time property.
        """
        self._deleted_date_time = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the cookie.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the cookie.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import browser_shared_cookie_history, browser_shared_cookie_source_environment, browser_shared_cookie_status, entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(browser_shared_cookie_history.BrowserSharedCookieHistory)),
            "hostOnly": lambda n : setattr(self, 'host_only', n.get_bool_value()),
            "hostOrDomain": lambda n : setattr(self, 'host_or_domain', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "sourceEnvironment": lambda n : setattr(self, 'source_environment', n.get_enum_value(browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(browser_shared_cookie_status.BrowserSharedCookieStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history(self,) -> Optional[List[browser_shared_cookie_history.BrowserSharedCookieHistory]]:
        """
        Gets the history property value. The history of modifications applied to the cookie.
        Returns: Optional[List[browser_shared_cookie_history.BrowserSharedCookieHistory]]
        """
        return self._history
    
    @history.setter
    def history(self,value: Optional[List[browser_shared_cookie_history.BrowserSharedCookieHistory]] = None) -> None:
        """
        Sets the history property value. The history of modifications applied to the cookie.
        Args:
            value: Value to set for the history property.
        """
        self._history = value
    
    @property
    def host_only(self,) -> Optional[bool]:
        """
        Gets the hostOnly property value. Controls whether a cookie is a host-only or domain cookie.
        Returns: Optional[bool]
        """
        return self._host_only
    
    @host_only.setter
    def host_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the hostOnly property value. Controls whether a cookie is a host-only or domain cookie.
        Args:
            value: Value to set for the host_only property.
        """
        self._host_only = value
    
    @property
    def host_or_domain(self,) -> Optional[str]:
        """
        Gets the hostOrDomain property value. The URL of the cookie.
        Returns: Optional[str]
        """
        return self._host_or_domain
    
    @host_or_domain.setter
    def host_or_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the hostOrDomain property value. The URL of the cookie.
        Args:
            value: Value to set for the host_or_domain property.
        """
        self._host_or_domain = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The user who last modified the cookie.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The user who last modified the cookie.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the cookie was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the cookie was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def path(self,) -> Optional[str]:
        """
        Gets the path property value. The path of the cookie.
        Returns: Optional[str]
        """
        return self._path
    
    @path.setter
    def path(self,value: Optional[str] = None) -> None:
        """
        Sets the path property value. The path of the cookie.
        Args:
            value: Value to set for the path property.
        """
        self._path = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("comment", self.comment)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_bool_value("hostOnly", self.host_only)
        writer.write_str_value("hostOrDomain", self.host_or_domain)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("path", self.path)
        writer.write_enum_value("sourceEnvironment", self.source_environment)
        writer.write_enum_value("status", self.status)
    
    @property
    def source_environment(self,) -> Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment]:
        """
        Gets the sourceEnvironment property value. The sourceEnvironment property
        Returns: Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment]
        """
        return self._source_environment
    
    @source_environment.setter
    def source_environment(self,value: Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment] = None) -> None:
        """
        Sets the sourceEnvironment property value. The sourceEnvironment property
        Args:
            value: Value to set for the source_environment property.
        """
        self._source_environment = value
    
    @property
    def status(self,) -> Optional[browser_shared_cookie_status.BrowserSharedCookieStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[browser_shared_cookie_status.BrowserSharedCookieStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[browser_shared_cookie_status.BrowserSharedCookieStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

