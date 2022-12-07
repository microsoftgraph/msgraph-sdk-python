from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_source_container = lazy_import('msgraph.generated.models.security.data_source_container')
ediscovery_index_operation = lazy_import('msgraph.generated.models.security.ediscovery_index_operation')
site_source = lazy_import('msgraph.generated.models.security.site_source')
unified_group_source = lazy_import('msgraph.generated.models.security.unified_group_source')
user_source = lazy_import('msgraph.generated.models.security.user_source')

class EdiscoveryCustodian(data_source_container.DataSourceContainer):
    @property
    def acknowledged_date_time(self,) -> Optional[datetime]:
        """
        Gets the acknowledgedDateTime property value. Date and time the custodian acknowledged a hold notification.
        Returns: Optional[datetime]
        """
        return self._acknowledged_date_time
    
    @acknowledged_date_time.setter
    def acknowledged_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the acknowledgedDateTime property value. Date and time the custodian acknowledged a hold notification.
        Args:
            value: Value to set for the acknowledgedDateTime property.
        """
        self._acknowledged_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryCustodian and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryCustodian"
        # Date and time the custodian acknowledged a hold notification.
        self._acknowledged_date_time: Optional[datetime] = None
        # Email address of the custodian.
        self._email: Optional[str] = None
        # Operation entity that represents the latest indexing for the custodian.
        self._last_index_operation: Optional[ediscovery_index_operation.EdiscoveryIndexOperation] = None
        # Data source entity for SharePoint sites associated with the custodian.
        self._site_sources: Optional[List[site_source.SiteSource]] = None
        # Data source entity for groups associated with the custodian.
        self._unified_group_sources: Optional[List[unified_group_source.UnifiedGroupSource]] = None
        # Data source entity for a the custodian. This is the container for a custodian's mailbox and OneDrive for Business site.
        self._user_sources: Optional[List[user_source.UserSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryCustodian:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCustodian
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryCustodian()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. Email address of the custodian.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. Email address of the custodian.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "acknowledged_date_time": lambda n : setattr(self, 'acknowledged_date_time', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "last_index_operation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(ediscovery_index_operation.EdiscoveryIndexOperation)),
            "site_sources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(site_source.SiteSource)),
            "unified_group_sources": lambda n : setattr(self, 'unified_group_sources', n.get_collection_of_object_values(unified_group_source.UnifiedGroupSource)),
            "user_sources": lambda n : setattr(self, 'user_sources', n.get_collection_of_object_values(user_source.UserSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_index_operation(self,) -> Optional[ediscovery_index_operation.EdiscoveryIndexOperation]:
        """
        Gets the lastIndexOperation property value. Operation entity that represents the latest indexing for the custodian.
        Returns: Optional[ediscovery_index_operation.EdiscoveryIndexOperation]
        """
        return self._last_index_operation
    
    @last_index_operation.setter
    def last_index_operation(self,value: Optional[ediscovery_index_operation.EdiscoveryIndexOperation] = None) -> None:
        """
        Sets the lastIndexOperation property value. Operation entity that represents the latest indexing for the custodian.
        Args:
            value: Value to set for the lastIndexOperation property.
        """
        self._last_index_operation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("acknowledgedDateTime", self.acknowledged_date_time)
        writer.write_str_value("email", self.email)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_collection_of_object_values("unifiedGroupSources", self.unified_group_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    
    @property
    def site_sources(self,) -> Optional[List[site_source.SiteSource]]:
        """
        Gets the siteSources property value. Data source entity for SharePoint sites associated with the custodian.
        Returns: Optional[List[site_source.SiteSource]]
        """
        return self._site_sources
    
    @site_sources.setter
    def site_sources(self,value: Optional[List[site_source.SiteSource]] = None) -> None:
        """
        Sets the siteSources property value. Data source entity for SharePoint sites associated with the custodian.
        Args:
            value: Value to set for the siteSources property.
        """
        self._site_sources = value
    
    @property
    def unified_group_sources(self,) -> Optional[List[unified_group_source.UnifiedGroupSource]]:
        """
        Gets the unifiedGroupSources property value. Data source entity for groups associated with the custodian.
        Returns: Optional[List[unified_group_source.UnifiedGroupSource]]
        """
        return self._unified_group_sources
    
    @unified_group_sources.setter
    def unified_group_sources(self,value: Optional[List[unified_group_source.UnifiedGroupSource]] = None) -> None:
        """
        Sets the unifiedGroupSources property value. Data source entity for groups associated with the custodian.
        Args:
            value: Value to set for the unifiedGroupSources property.
        """
        self._unified_group_sources = value
    
    @property
    def user_sources(self,) -> Optional[List[user_source.UserSource]]:
        """
        Gets the userSources property value. Data source entity for a the custodian. This is the container for a custodian's mailbox and OneDrive for Business site.
        Returns: Optional[List[user_source.UserSource]]
        """
        return self._user_sources
    
    @user_sources.setter
    def user_sources(self,value: Optional[List[user_source.UserSource]] = None) -> None:
        """
        Sets the userSources property value. Data source entity for a the custodian. This is the container for a custodian's mailbox and OneDrive for Business site.
        Args:
            value: Value to set for the userSources property.
        """
        self._user_sources = value
    

