from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import browser_site_compatibility_mode, browser_site_history, browser_site_merge_type, browser_site_status, browser_site_target_environment, entity, identity_set

from . import entity

class BrowserSite(entity.Entity):
    """
    Singleton entity which is used to specify IE mode site metadata
    """
    def __init__(self,) -> None:
        """
        Instantiates a new browserSite and sets the default values.
        """
        super().__init__()
        # Controls the behavior of redirected sites. If true, indicates that the site will open in Internet Explorer 11 or Microsoft Edge even if the site is navigated to as part of a HTTP or meta refresh redirection chain.
        self._allow_redirect: Optional[bool] = None
        # The comment for the site.
        self._comment: Optional[str] = None
        # The compatibilityMode property
        self._compatibility_mode: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode] = None
        # The date and time when the site was created.
        self._created_date_time: Optional[datetime] = None
        # The date and time when the site was deleted.
        self._deleted_date_time: Optional[datetime] = None
        # The history of modifications applied to the site.
        self._history: Optional[List[browser_site_history.BrowserSiteHistory]] = None
        # The user who last modified the site.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The date and time when the site was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The mergeType property
        self._merge_type: Optional[browser_site_merge_type.BrowserSiteMergeType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[browser_site_status.BrowserSiteStatus] = None
        # The targetEnvironment property
        self._target_environment: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment] = None
        # The URL of the site.
        self._web_url: Optional[str] = None
    
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
        Gets the compatibilityMode property value. The compatibilityMode property
        Returns: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode]
        """
        return self._compatibility_mode
    
    @compatibility_mode.setter
    def compatibility_mode(self,value: Optional[browser_site_compatibility_mode.BrowserSiteCompatibilityMode] = None) -> None:
        """
        Sets the compatibilityMode property value. The compatibilityMode property
        Args:
            value: Value to set for the compatibility_mode property.
        """
        self._compatibility_mode = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the site was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the site was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BrowserSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BrowserSite
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BrowserSite()
    
    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. The date and time when the site was deleted.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time
    
    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. The date and time when the site was deleted.
        Args:
            value: Value to set for the deleted_date_time property.
        """
        self._deleted_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def history(self,) -> Optional[List[browser_site_history.BrowserSiteHistory]]:
        """
        Gets the history property value. The history of modifications applied to the site.
        Returns: Optional[List[browser_site_history.BrowserSiteHistory]]
        """
        return self._history
    
    @history.setter
    def history(self,value: Optional[List[browser_site_history.BrowserSiteHistory]] = None) -> None:
        """
        Sets the history property value. The history of modifications applied to the site.
        Args:
            value: Value to set for the history property.
        """
        self._history = value
    
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
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the site was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the site was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def merge_type(self,) -> Optional[browser_site_merge_type.BrowserSiteMergeType]:
        """
        Gets the mergeType property value. The mergeType property
        Returns: Optional[browser_site_merge_type.BrowserSiteMergeType]
        """
        return self._merge_type
    
    @merge_type.setter
    def merge_type(self,value: Optional[browser_site_merge_type.BrowserSiteMergeType] = None) -> None:
        """
        Sets the mergeType property value. The mergeType property
        Args:
            value: Value to set for the merge_type property.
        """
        self._merge_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def status(self,) -> Optional[browser_site_status.BrowserSiteStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[browser_site_status.BrowserSiteStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[browser_site_status.BrowserSiteStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def target_environment(self,) -> Optional[browser_site_target_environment.BrowserSiteTargetEnvironment]:
        """
        Gets the targetEnvironment property value. The targetEnvironment property
        Returns: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment]
        """
        return self._target_environment
    
    @target_environment.setter
    def target_environment(self,value: Optional[browser_site_target_environment.BrowserSiteTargetEnvironment] = None) -> None:
        """
        Sets the targetEnvironment property value. The targetEnvironment property
        Args:
            value: Value to set for the target_environment property.
        """
        self._target_environment = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The URL of the site.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The URL of the site.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

