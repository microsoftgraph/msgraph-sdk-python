from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
shared_insight = lazy_import('msgraph.generated.models.shared_insight')
trending = lazy_import('msgraph.generated.models.trending')
used_insight = lazy_import('msgraph.generated.models.used_insight')

class OfficeGraphInsights(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new officeGraphInsights and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.
        self._shared: Optional[List[shared_insight.SharedInsight]] = None
        # Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.
        self._trending: Optional[List[trending.Trending]] = None
        # Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.
        self._used: Optional[List[used_insight.UsedInsight]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfficeGraphInsights:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfficeGraphInsights
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OfficeGraphInsights()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "shared": lambda n : setattr(self, 'shared', n.get_collection_of_object_values(shared_insight.SharedInsight)),
            "trending": lambda n : setattr(self, 'trending', n.get_collection_of_object_values(trending.Trending)),
            "used": lambda n : setattr(self, 'used', n.get_collection_of_object_values(used_insight.UsedInsight)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("shared", self.shared)
        writer.write_collection_of_object_values("trending", self.trending)
        writer.write_collection_of_object_values("used", self.used)
    
    @property
    def shared(self,) -> Optional[List[shared_insight.SharedInsight]]:
        """
        Gets the shared property value. Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.
        Returns: Optional[List[shared_insight.SharedInsight]]
        """
        return self._shared
    
    @shared.setter
    def shared(self,value: Optional[List[shared_insight.SharedInsight]] = None) -> None:
        """
        Sets the shared property value. Calculated relationship identifying documents shared with or by the user. This includes URLs, file attachments, and reference attachments to OneDrive for Business and SharePoint files found in Outlook messages and meetings. This also includes URLs and reference attachments to Teams conversations. Ordered by recency of share.
        Args:
            value: Value to set for the shared property.
        """
        self._shared = value
    
    @property
    def trending(self,) -> Optional[List[trending.Trending]]:
        """
        Gets the trending property value. Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.
        Returns: Optional[List[trending.Trending]]
        """
        return self._trending
    
    @trending.setter
    def trending(self,value: Optional[List[trending.Trending]] = None) -> None:
        """
        Sets the trending property value. Calculated relationship identifying documents trending around a user. Trending documents are calculated based on activity of the user's closest network of people and include files stored in OneDrive for Business and SharePoint. Trending insights help the user to discover potentially useful content that the user has access to, but has never viewed before.
        Args:
            value: Value to set for the trending property.
        """
        self._trending = value
    
    @property
    def used(self,) -> Optional[List[used_insight.UsedInsight]]:
        """
        Gets the used property value. Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.
        Returns: Optional[List[used_insight.UsedInsight]]
        """
        return self._used
    
    @used.setter
    def used(self,value: Optional[List[used_insight.UsedInsight]] = None) -> None:
        """
        Sets the used property value. Calculated relationship identifying the latest documents viewed or modified by a user, including OneDrive for Business and SharePoint documents, ranked by recency of use.
        Args:
            value: Value to set for the used property.
        """
        self._used = value
    

