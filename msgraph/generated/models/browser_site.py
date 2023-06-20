from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_site_compatibility_mode, browser_site_history, browser_site_merge_type, browser_site_status, browser_site_target_environment, entity, identity_set

from . import entity

@dataclass
class BrowserSite(entity.Entity):
    """
    Singleton entity which is used to specify IE mode site metadata
    """
    # Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
    allow_redirect: Optional[bool] = None
    # The comment for the site.
    comment: Optional[str] = None
    # The compatibilityMode property
    compatibility_mode: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode] = None
    # The date and time when the site was created.
    created_date_time: Optional[datetime] = None
    # The date and time when the site was deleted.
    deleted_date_time: Optional[datetime] = None
    # The history of modifications applied to the site.
    history: Optional[List[browser_site_history.BrowserSiteHistory]] = None
    # The user who last modified the site.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the site was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The mergeType property
    merge_type: Optional[browser_site_merge_type.BrowserSiteMergeType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[browser_site_status.BrowserSiteStatus] = None
    # The targetEnvironment property
    target_environment: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment] = None
    # The URL of the site.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSite
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BrowserSite()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import browser_site_compatibility_mode, browser_site_history, browser_site_merge_type, browser_site_status, browser_site_target_environment, entity, identity_set

        from . import browser_site_compatibility_mode, browser_site_history, browser_site_merge_type, browser_site_status, browser_site_target_environment, entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "allowRedirect": lambda n : setattr(self, 'allow_redirect', n.get_bool_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "compatibilityMode": lambda n : setattr(self, 'compatibility_mode', n.get_enum_value(browser_site_compatibility_mode.BrowserSiteCompatibilityMode)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(browser_site_history.BrowserSiteHistory)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "mergeType": lambda n : setattr(self, 'merge_type', n.get_enum_value(browser_site_merge_type.BrowserSiteMergeType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(browser_site_status.BrowserSiteStatus)),
            "targetEnvironment": lambda n : setattr(self, 'target_environment', n.get_enum_value(browser_site_target_environment.BrowserSiteTargetEnvironment)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        if not writer:
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
    

