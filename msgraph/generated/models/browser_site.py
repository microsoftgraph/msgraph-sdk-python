from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
    from .browser_site_history import BrowserSiteHistory
    from .browser_site_merge_type import BrowserSiteMergeType
    from .browser_site_status import BrowserSiteStatus
    from .browser_site_target_environment import BrowserSiteTargetEnvironment
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class BrowserSite(Entity, Parsable):
    """
    Singleton entity which is used to specify IE mode site metadata
    """
    # Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
    allow_redirect: Optional[bool] = None
    # The comment for the site.
    comment: Optional[str] = None
    # The compatibilityMode property
    compatibility_mode: Optional[BrowserSiteCompatibilityMode] = None
    # The date and time when the site was created.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the site was deleted.
    deleted_date_time: Optional[datetime.datetime] = None
    # The history of modifications applied to the site.
    history: Optional[list[BrowserSiteHistory]] = None
    # The user who last modified the site.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the site was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The mergeType property
    merge_type: Optional[BrowserSiteMergeType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[BrowserSiteStatus] = None
    # The targetEnvironment property
    target_environment: Optional[BrowserSiteTargetEnvironment] = None
    # The URL of the site.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowserSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowserSite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
        from .browser_site_history import BrowserSiteHistory
        from .browser_site_merge_type import BrowserSiteMergeType
        from .browser_site_status import BrowserSiteStatus
        from .browser_site_target_environment import BrowserSiteTargetEnvironment
        from .entity import Entity
        from .identity_set import IdentitySet

        from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
        from .browser_site_history import BrowserSiteHistory
        from .browser_site_merge_type import BrowserSiteMergeType
        from .browser_site_status import BrowserSiteStatus
        from .browser_site_target_environment import BrowserSiteTargetEnvironment
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "allowRedirect": lambda n : setattr(self, 'allow_redirect', n.get_bool_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "compatibilityMode": lambda n : setattr(self, 'compatibility_mode', n.get_enum_value(BrowserSiteCompatibilityMode)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(BrowserSiteHistory)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "mergeType": lambda n : setattr(self, 'merge_type', n.get_enum_value(BrowserSiteMergeType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BrowserSiteStatus)),
            "targetEnvironment": lambda n : setattr(self, 'target_environment', n.get_enum_value(BrowserSiteTargetEnvironment)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_bool_value("allowRedirect", self.allow_redirect)
        writer.write_str_value("comment", self.comment)
        writer.write_enum_value("compatibilityMode", self.compatibility_mode)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("mergeType", self.merge_type)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("targetEnvironment", self.target_environment)
        writer.write_str_value("webUrl", self.web_url)
    

