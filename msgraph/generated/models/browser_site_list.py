from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browser_shared_cookie import BrowserSharedCookie
    from .browser_site import BrowserSite
    from .browser_site_list_status import BrowserSiteListStatus
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class BrowserSiteList(Entity, Parsable):
    """
    A singleton entity which is used to specify IE mode site list metadata
    """
    # The description of the site list.
    description: Optional[str] = None
    # The name of the site list.
    display_name: Optional[str] = None
    # The user who last modified the site list.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the site list was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user who published the site list.
    published_by: Optional[IdentitySet] = None
    # The date and time when the site list was published.
    published_date_time: Optional[datetime.datetime] = None
    # The current revision of the site list.
    revision: Optional[str] = None
    # A collection of shared cookies defined for the site list.
    shared_cookies: Optional[list[BrowserSharedCookie]] = None
    # A collection of sites defined for the site list.
    sites: Optional[list[BrowserSite]] = None
    # The status property
    status: Optional[BrowserSiteListStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowserSiteList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSiteList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowserSiteList()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .browser_shared_cookie import BrowserSharedCookie
        from .browser_site import BrowserSite
        from .browser_site_list_status import BrowserSiteListStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        from .browser_shared_cookie import BrowserSharedCookie
        from .browser_site import BrowserSite
        from .browser_site_list_status import BrowserSiteListStatus
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publishedBy": lambda n : setattr(self, 'published_by', n.get_object_value(IdentitySet)),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "sharedCookies": lambda n : setattr(self, 'shared_cookies', n.get_collection_of_object_values(BrowserSharedCookie)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(BrowserSite)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BrowserSiteListStatus)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("publishedBy", self.published_by)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_str_value("revision", self.revision)
        writer.write_collection_of_object_values("sharedCookies", self.shared_cookies)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_enum_value("status", self.status)
    

