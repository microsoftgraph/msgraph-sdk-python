from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_shared_cookie, browser_site, browser_site_list_status, entity, identity_set

from . import entity

class BrowserSiteList(entity.Entity):
    """
    A singleton entity which is used to specify IE mode site list metadata
    """
    def __init__(self,) -> None:
        """
        Instantiates a new browserSiteList and sets the default values.
        """
        super().__init__()
        # The description of the site list.
        self._description: Optional[str] = None
        # The name of the site list.
        self._display_name: Optional[str] = None
        # The user who last modified the site list.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the site list was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user who published the site list.
        self._published_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the site list was published.
        self._published_date_time: Optional[datetime] = None
        # The current revision of the site list.
        self._revision: Optional[str] = None
        # A collection of shared cookies defined for the site list.
        self._shared_cookies: Optional[List[browser_shared_cookie.BrowserSharedCookie]] = None
        # A collection of sites defined for the site list.
        self._sites: Optional[List[browser_site.BrowserSite]] = None
        # The status property
        self._status: Optional[browser_site_list_status.BrowserSiteListStatus] = None
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the site list.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the site list.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the site list.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the site list.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
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
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The user who last modified the site list.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The user who last modified the site list.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the site list was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the site list was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def published_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the publishedBy property value. The user who published the site list.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._published_by
    
    @published_by.setter
    def published_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the publishedBy property value. The user who published the site list.
        Args:
            value: Value to set for the published_by property.
        """
        self._published_by = value
    
    @property
    def published_date_time(self,) -> Optional[datetime]:
        """
        Gets the publishedDateTime property value. The date and time when the site list was published.
        Returns: Optional[datetime]
        """
        return self._published_date_time
    
    @published_date_time.setter
    def published_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the publishedDateTime property value. The date and time when the site list was published.
        Args:
            value: Value to set for the published_date_time property.
        """
        self._published_date_time = value
    
    @property
    def revision(self,) -> Optional[str]:
        """
        Gets the revision property value. The current revision of the site list.
        Returns: Optional[str]
        """
        return self._revision
    
    @revision.setter
    def revision(self,value: Optional[str] = None) -> None:
        """
        Sets the revision property value. The current revision of the site list.
        Args:
            value: Value to set for the revision property.
        """
        self._revision = value
    
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
    
    @property
    def shared_cookies(self,) -> Optional[List[browser_shared_cookie.BrowserSharedCookie]]:
        """
        Gets the sharedCookies property value. A collection of shared cookies defined for the site list.
        Returns: Optional[List[browser_shared_cookie.BrowserSharedCookie]]
        """
        return self._shared_cookies
    
    @shared_cookies.setter
    def shared_cookies(self,value: Optional[List[browser_shared_cookie.BrowserSharedCookie]] = None) -> None:
        """
        Sets the sharedCookies property value. A collection of shared cookies defined for the site list.
        Args:
            value: Value to set for the shared_cookies property.
        """
        self._shared_cookies = value
    
    @property
    def sites(self,) -> Optional[List[browser_site.BrowserSite]]:
        """
        Gets the sites property value. A collection of sites defined for the site list.
        Returns: Optional[List[browser_site.BrowserSite]]
        """
        return self._sites
    
    @sites.setter
    def sites(self,value: Optional[List[browser_site.BrowserSite]] = None) -> None:
        """
        Sets the sites property value. A collection of sites defined for the site list.
        Args:
            value: Value to set for the sites property.
        """
        self._sites = value
    
    @property
    def status(self,) -> Optional[browser_site_list_status.BrowserSiteListStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[browser_site_list_status.BrowserSiteListStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[browser_site_list_status.BrowserSiteListStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

