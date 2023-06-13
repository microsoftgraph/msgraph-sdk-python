from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_shared_cookie, browser_site, browser_site_list_status, entity, identity_set

from . import entity

@dataclass
class BrowserSiteList(entity.Entity):
    """
    A singleton entity which is used to specify IE mode site list metadata
    """
    # The description of the site list.
    description: Optional[str] = None
    # The name of the site list.
    display_name: Optional[str] = None
    # The user who last modified the site list.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the site list was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user who published the site list.
    published_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the site list was published.
    published_date_time: Optional[datetime] = None
    # The current revision of the site list.
    revision: Optional[str] = None
    # A collection of shared cookies defined for the site list.
    shared_cookies: Optional[List[browser_shared_cookie.BrowserSharedCookie]] = None
    # A collection of sites defined for the site list.
    sites: Optional[List[browser_site.BrowserSite]] = None
    # The status property
    status: Optional[browser_site_list_status.BrowserSiteListStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSiteList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSiteList
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BrowserSiteList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import browser_shared_cookie, browser_site, browser_site_list_status, entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publishedBy": lambda n : setattr(self, 'published_by', n.get_object_value(identity_set.IdentitySet)),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "sharedCookies": lambda n : setattr(self, 'shared_cookies', n.get_collection_of_object_values(browser_shared_cookie.BrowserSharedCookie)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(browser_site.BrowserSite)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(browser_site_list_status.BrowserSiteListStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

