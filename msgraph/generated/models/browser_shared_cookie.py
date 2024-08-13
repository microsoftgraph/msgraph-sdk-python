from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browser_shared_cookie_history import BrowserSharedCookieHistory
    from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
    from .browser_shared_cookie_status import BrowserSharedCookieStatus
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class BrowserSharedCookie(Entity):
    # The comment for the shared cookie.
    comment: Optional[str] = None
    # The date and time when the shared cookie was created.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the shared cookie was deleted.
    deleted_date_time: Optional[datetime.datetime] = None
    # The name of the cookie.
    display_name: Optional[str] = None
    # The history of modifications applied to the cookie.
    history: Optional[List[BrowserSharedCookieHistory]] = None
    # Controls whether a cookie is a host-only or domain cookie.
    host_only: Optional[bool] = None
    # The URL of the cookie.
    host_or_domain: Optional[str] = None
    # The user who last modified the cookie.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the cookie was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The path of the cookie.
    path: Optional[str] = None
    # The sourceEnvironment property
    source_environment: Optional[BrowserSharedCookieSourceEnvironment] = None
    # The status property
    status: Optional[BrowserSharedCookieStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowserSharedCookie:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSharedCookie
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowserSharedCookie()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .browser_shared_cookie_history import BrowserSharedCookieHistory
        from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
        from .browser_shared_cookie_status import BrowserSharedCookieStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        from .browser_shared_cookie_history import BrowserSharedCookieHistory
        from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
        from .browser_shared_cookie_status import BrowserSharedCookieStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(BrowserSharedCookieHistory)),
            "hostOnly": lambda n : setattr(self, 'host_only', n.get_bool_value()),
            "hostOrDomain": lambda n : setattr(self, 'host_or_domain', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "sourceEnvironment": lambda n : setattr(self, 'source_environment', n.get_enum_value(BrowserSharedCookieSourceEnvironment)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BrowserSharedCookieStatus)),
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
    

