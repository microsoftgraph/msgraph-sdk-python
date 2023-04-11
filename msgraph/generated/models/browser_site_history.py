from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_site_compatibility_mode, browser_site_merge_type, browser_site_target_environment, identity_set

class BrowserSiteHistory(AdditionalDataHolder, Parsable):
    """
    The history for the site modifications
    """
    def __init__(self,) -> None:
        """
        Instantiates a new browserSiteHistory and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
        self._allow_redirect: Optional[bool] = None
        # The comment for the site.
        self._comment: Optional[str] = None
        # Controls what compatibility setting is used for specific sites or domains. The possible values are: default, internetExplorer8Enterprise, internetExplorer7Enterprise, internetExplorer11, internetExplorer10, internetExplorer9, internetExplorer8, internetExplorer7, internetExplorer5, unknownFutureValue.
        self._compatibility_mode: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode] = None
        # The user who last modified the site.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The merge type of the site. The possible values are: noMerge, default, unknownFutureValue.
        self._merge_type: Optional[browser_site_merge_type.BrowserSiteMergeType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date and time when the site was last published.
        self._published_date_time: Optional[datetime] = None
        # The target environment that the site should open in. The possible values are: internetExplorerMode, internetExplorer11, microsoftEdge, configurable, none, unknownFutureValue.Prior to June 15, 2022, the internetExplorer11 option would allow opening a site in the Internet Explorer 11 (IE11) desktop application. Following the retirement of IE11 on June 15, 2022, the internetExplorer11 option will no longer open an IE11 window and will instead behave the same as the internetExplorerMode option.
        self._target_environment: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment] = None
    
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
    def allow_redirect(self,) -> Optional[bool]:
        """
        Gets the allowRedirect property value. Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
        Returns: Optional[bool]
        """
        return self._allow_redirect
    
    @allow_redirect.setter
    def allow_redirect(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowRedirect property value. Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
        Args:
            value: Value to set for the allow_redirect property.
        """
        self._allow_redirect = value
    
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The comment for the site.
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The comment for the site.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    @property
    def compatibility_mode(self,) -> Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode]:
        """
        Gets the compatibilityMode property value. Controls what compatibility setting is used for specific sites or domains. The possible values are: default, internetExplorer8Enterprise, internetExplorer7Enterprise, internetExplorer11, internetExplorer10, internetExplorer9, internetExplorer8, internetExplorer7, internetExplorer5, unknownFutureValue.
        Returns: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode]
        """
        return self._compatibility_mode
    
    @compatibility_mode.setter
    def compatibility_mode(self,value: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode] = None) -> None:
        """
        Sets the compatibilityMode property value. Controls what compatibility setting is used for specific sites or domains. The possible values are: default, internetExplorer8Enterprise, internetExplorer7Enterprise, internetExplorer11, internetExplorer10, internetExplorer9, internetExplorer8, internetExplorer7, internetExplorer5, unknownFutureValue.
        Args:
            value: Value to set for the compatibility_mode property.
        """
        self._compatibility_mode = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSiteHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSiteHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BrowserSiteHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The user who last modified the site.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The user who last modified the site.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def merge_type(self,) -> Optional[browser_site_merge_type.BrowserSiteMergeType]:
        """
        Gets the mergeType property value. The merge type of the site. The possible values are: noMerge, default, unknownFutureValue.
        Returns: Optional[browser_site_merge_type.BrowserSiteMergeType]
        """
        return self._merge_type
    
    @merge_type.setter
    def merge_type(self,value: Optional[browser_site_merge_type.BrowserSiteMergeType] = None) -> None:
        """
        Sets the mergeType property value. The merge type of the site. The possible values are: noMerge, default, unknownFutureValue.
        Args:
            value: Value to set for the merge_type property.
        """
        self._merge_type = value
    
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
    def published_date_time(self,) -> Optional[datetime]:
        """
        Gets the publishedDateTime property value. The date and time when the site was last published.
        Returns: Optional[datetime]
        """
        return self._published_date_time
    
    @published_date_time.setter
    def published_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the publishedDateTime property value. The date and time when the site was last published.
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
        writer.write_bool_value("allowRedirect", self.allow_redirect)
        writer.write_str_value("comment", self.comment)
        writer.write_enum_value("compatibilityMode", self.compatibility_mode)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_enum_value("mergeType", self.merge_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("publishedDateTime", self.published_date_time)
        writer.write_enum_value("targetEnvironment", self.target_environment)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target_environment(self,) -> Optional[browser_site_target_environment.BrowserSiteTargetEnvironment]:
        """
        Gets the targetEnvironment property value. The target environment that the site should open in. The possible values are: internetExplorerMode, internetExplorer11, microsoftEdge, configurable, none, unknownFutureValue.Prior to June 15, 2022, the internetExplorer11 option would allow opening a site in the Internet Explorer 11 (IE11) desktop application. Following the retirement of IE11 on June 15, 2022, the internetExplorer11 option will no longer open an IE11 window and will instead behave the same as the internetExplorerMode option.
        Returns: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment]
        """
        return self._target_environment
    
    @target_environment.setter
    def target_environment(self,value: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment] = None) -> None:
        """
        Sets the targetEnvironment property value. The target environment that the site should open in. The possible values are: internetExplorerMode, internetExplorer11, microsoftEdge, configurable, none, unknownFutureValue.Prior to June 15, 2022, the internetExplorer11 option would allow opening a site in the Internet Explorer 11 (IE11) desktop application. Following the retirement of IE11 on June 15, 2022, the internetExplorer11 option will no longer open an IE11 window and will instead behave the same as the internetExplorerMode option.
        Args:
            value: Value to set for the target_environment property.
        """
        self._target_environment = value
    

