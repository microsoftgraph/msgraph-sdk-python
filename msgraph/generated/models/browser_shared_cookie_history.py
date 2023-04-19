from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_shared_cookie_source_environment, identity_set

class BrowserSharedCookieHistory(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new browserSharedCookieHistory and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The comment for the shared cookie.
        self._comment: Optional[str] = None
        # The name of the cookie.
        self._display_name: Optional[str] = None
        # Controls whether a cookie is a host-only or domain cookie.
        self._host_only: Optional[bool] = None
        # The URL of the cookie.
        self._host_or_domain: Optional[str] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The path of the cookie.
        self._path: Optional[str] = None
        # The date and time when the cookie was last published.
        self._published_date_time: Optional[datetime] = None
        # Specifies how the cookies are shared between Microsoft Edge and Internet Explorer. The possible values are: microsoftEdge, internetExplorer11, both, unknownFutureValue.
        self._source_environment: Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSharedCookieHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSharedCookieHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BrowserSharedCookieHistory()
    
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
        from . import browser_shared_cookie_source_environment, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hostOnly": lambda n : setattr(self, 'host_only', n.get_bool_value()),
            "hostOrDomain": lambda n : setattr(self, 'host_or_domain', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "sourceEnvironment": lambda n : setattr(self, 'source_environment', n.get_enum_value(browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment)),
        }
        return fields
    
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
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The lastModifiedBy property
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
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
    
    @property
    def published_date_time(self,) -> Optional[datetime]:
        """
        Gets the publishedDateTime property value. The date and time when the cookie was last published.
        Returns: Optional[datetime]
        """
        return self._published_date_time
    
    @published_date_time.setter
    def published_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the publishedDateTime property value. The date and time when the cookie was last published.
        Args:
            value: Value to set for the published_date_time property.
        """
        self._published_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hostOnly", self.host_only)
        writer.write_str_value("hostOrDomain", self.host_or_domain)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("path", self.path)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_enum_value("sourceEnvironment", self.source_environment)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_environment(self,) -> Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment]:
        """
        Gets the sourceEnvironment property value. Specifies how the cookies are shared between Microsoft Edge and Internet Explorer. The possible values are: microsoftEdge, internetExplorer11, both, unknownFutureValue.
        Returns: Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment]
        """
        return self._source_environment
    
    @source_environment.setter
    def source_environment(self,value: Optional[browser_shared_cookie_source_environment.BrowserSharedCookieSourceEnvironment] = None) -> None:
        """
        Sets the sourceEnvironment property value. Specifies how the cookies are shared between Microsoft Edge and Internet Explorer. The possible values are: microsoftEdge, internetExplorer11, both, unknownFutureValue.
        Args:
            value: Value to set for the source_environment property.
        """
        self._source_environment = value
    

