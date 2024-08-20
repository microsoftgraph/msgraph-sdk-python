from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
    from .identity_set import IdentitySet

@dataclass
class BrowserSharedCookieHistory(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The comment for the shared cookie.
    comment: Optional[str] = None
    # The name of the cookie.
    display_name: Optional[str] = None
    # Controls whether a cookie is a host-only or domain cookie.
    host_only: Optional[bool] = None
    # The URL of the cookie.
    host_or_domain: Optional[str] = None
    # The lastModifiedBy property
    last_modified_by: Optional[IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The path of the cookie.
    path: Optional[str] = None
    # The date and time when the cookie was last published.
    published_date_time: Optional[datetime.datetime] = None
    # Specifies how the cookies are shared between Microsoft Edge and Internet Explorer. The possible values are: microsoftEdge, internetExplorer11, both, unknownFutureValue.
    source_environment: Optional[BrowserSharedCookieSourceEnvironment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowserSharedCookieHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSharedCookieHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowserSharedCookieHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
        from .identity_set import IdentitySet

        from .browser_shared_cookie_source_environment import BrowserSharedCookieSourceEnvironment
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hostOnly": lambda n : setattr(self, 'host_only', n.get_bool_value()),
            "hostOrDomain": lambda n : setattr(self, 'host_or_domain', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "sourceEnvironment": lambda n : setattr(self, 'source_environment', n.get_enum_value(BrowserSharedCookieSourceEnvironment)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

