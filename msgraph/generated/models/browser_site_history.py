from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
    from .browser_site_merge_type import BrowserSiteMergeType
    from .browser_site_target_environment import BrowserSiteTargetEnvironment
    from .identity_set import IdentitySet

@dataclass
class BrowserSiteHistory(AdditionalDataHolder, BackedModel, Parsable):
    """
    The history for the site modifications
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
    allow_redirect: Optional[bool] = None
    # The comment for the site.
    comment: Optional[str] = None
    # Controls what compatibility setting is used for specific sites or domains. The possible values are: default, internetExplorer8Enterprise, internetExplorer7Enterprise, internetExplorer11, internetExplorer10, internetExplorer9, internetExplorer8, internetExplorer7, internetExplorer5, unknownFutureValue.
    compatibility_mode: Optional[BrowserSiteCompatibilityMode] = None
    # The user who last modified the site.
    last_modified_by: Optional[IdentitySet] = None
    # The merge type of the site. The possible values are: noMerge, default, unknownFutureValue.
    merge_type: Optional[BrowserSiteMergeType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the site was last published.
    published_date_time: Optional[datetime.datetime] = None
    # The target environment that the site should open in. The possible values are: internetExplorerMode, internetExplorer11, microsoftEdge, configurable, none, unknownFutureValue.Prior to June 15, 2022, the internetExplorer11 option would allow opening a site in the Internet Explorer 11 (IE11) desktop application. Following the retirement of IE11 on June 15, 2022, the internetExplorer11 option will no longer open an IE11 window and will instead behave the same as the internetExplorerMode option.
    target_environment: Optional[BrowserSiteTargetEnvironment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowserSiteHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSiteHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowserSiteHistory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
        from .browser_site_merge_type import BrowserSiteMergeType
        from .browser_site_target_environment import BrowserSiteTargetEnvironment
        from .identity_set import IdentitySet

        from .browser_site_compatibility_mode import BrowserSiteCompatibilityMode
        from .browser_site_merge_type import BrowserSiteMergeType
        from .browser_site_target_environment import BrowserSiteTargetEnvironment
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "allowRedirect": lambda n : setattr(self, 'allow_redirect', n.get_bool_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "compatibilityMode": lambda n : setattr(self, 'compatibility_mode', n.get_enum_value(BrowserSiteCompatibilityMode)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "mergeType": lambda n : setattr(self, 'merge_type', n.get_enum_value(BrowserSiteMergeType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publishedDateTime": lambda n : setattr(self, 'published_date_time', n.get_datetime_value()),
            "targetEnvironment": lambda n : setattr(self, 'target_environment', n.get_enum_value(BrowserSiteTargetEnvironment)),
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
        writer.write_bool_value("allowRedirect", self.allow_redirect)
        writer.write_str_value("comment", self.comment)
        writer.write_enum_value("compatibilityMode", self.compatibility_mode)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_enum_value("mergeType", self.merge_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_enum_value("targetEnvironment", self.target_environment)
        writer.write_additional_data_value(self.additional_data)
    

