from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import browser_shared_cookie, browser_site

class PublishPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new publishPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The revision property
        self._revision: Optional[str] = None
        # The sharedCookies property
        self._shared_cookies: Optional[List[browser_shared_cookie.BrowserSharedCookie]] = None
        # The sites property
        self._sites: Optional[List[browser_site.BrowserSite]] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PublishPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PublishPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PublishPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models import browser_shared_cookie, browser_site

        fields: Dict[str, Callable[[Any], None]] = {
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "sharedCookies": lambda n : setattr(self, 'shared_cookies', n.get_collection_of_object_values(browser_shared_cookie.BrowserSharedCookie)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(browser_site.BrowserSite)),
        }
        return fields
    
    @property
    def revision(self,) -> Optional[str]:
        """
        Gets the revision property value. The revision property
        Returns: Optional[str]
        """
        return self._revision
    
    @revision.setter
    def revision(self,value: Optional[str] = None) -> None:
        """
        Sets the revision property value. The revision property
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
        writer.write_str_value("revision", self.revision)
        writer.write_collection_of_object_values("sharedCookies", self.shared_cookies)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def shared_cookies(self,) -> Optional[List[browser_shared_cookie.BrowserSharedCookie]]:
        """
        Gets the sharedCookies property value. The sharedCookies property
        Returns: Optional[List[browser_shared_cookie.BrowserSharedCookie]]
        """
        return self._shared_cookies
    
    @shared_cookies.setter
    def shared_cookies(self,value: Optional[List[browser_shared_cookie.BrowserSharedCookie]] = None) -> None:
        """
        Sets the sharedCookies property value. The sharedCookies property
        Args:
            value: Value to set for the shared_cookies property.
        """
        self._shared_cookies = value
    
    @property
    def sites(self,) -> Optional[List[browser_site.BrowserSite]]:
        """
        Gets the sites property value. The sites property
        Returns: Optional[List[browser_site.BrowserSite]]
        """
        return self._sites
    
    @sites.setter
    def sites(self,value: Optional[List[browser_site.BrowserSite]] = None) -> None:
        """
        Sets the sites property value. The sites property
        Args:
            value: Value to set for the sites property.
        """
        self._sites = value
    

