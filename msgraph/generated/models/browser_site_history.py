from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_site_compatibility_mode, browser_site_merge_type, browser_site_target_environment, identity_set

@dataclass
class BrowserSiteHistory(AdditionalDataHolder, Parsable):
    """
    The history for the site modifications
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
    allow_redirect: Optional[bool] = None
    # The comment for the site.
    comment: Optional[str] = None
    # Controls what compatibility setting is used for specific sites or domains. The possible values are: default, internetExplorer8Enterprise, internetExplorer7Enterprise, internetExplorer11, internetExplorer10, internetExplorer9, internetExplorer8, internetExplorer7, internetExplorer5, unknownFutureValue.
    compatibility_mode: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode] = None
    # The user who last modified the site.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The merge type of the site. The possible values are: noMerge, default, unknownFutureValue.
    merge_type: Optional[browser_site_merge_type.BrowserSiteMergeType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the site was last published.
    published_date_time: Optional[datetime] = None
    # The target environment that the site should open in. The possible values are: internetExplorerMode, internetExplorer11, microsoftEdge, configurable, none, unknownFutureValue.Prior to June 15, 2022, the internetExplorer11 option would allow opening a site in the Internet Explorer 11 (IE11) desktop application. Following the retirement of IE11 on June 15, 2022, the internetExplorer11 option will no longer open an IE11 window and will instead behave the same as the internetExplorerMode option.
    target_environment: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSiteHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSiteHistory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BrowserSiteHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import browser_site_compatibility_mode, browser_site_merge_type, browser_site_target_environment, identity_set

        from . import browser_site_compatibility_mode, browser_site_merge_type, browser_site_target_environment, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "allowRedirect": lambda n : setattr(self, 'allow_redirect', n.get_bool_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "compatibilityMode": lambda n : setattr(self, 'compatibility_mode', n.get_enum_value(browser_site_compatibility_mode.BrowserSiteCompatibilityMode)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "mergeType": lambda n : setattr(self, 'merge_type', n.get_enum_value(browser_site_merge_type.BrowserSiteMergeType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "targetEnvironment": lambda n : setattr(self, 'target_environment', n.get_enum_value(browser_site_target_environment.BrowserSiteTargetEnvironment)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allowRedirect", self.allow_redirect)
        writer.write_str_value("comment", self.comment)
        writer.write_enum_value("compatibilityMode", self.compatibility_mode)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_enum_value("mergeType", self.merge_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_enum_value("targetEnvironment", self.target_environment)
        writer.write_additional_data_value(self.additional_data)
    

