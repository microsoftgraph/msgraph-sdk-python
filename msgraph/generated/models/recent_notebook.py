from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

onenote_source_service = lazy_import('msgraph.generated.models.onenote_source_service')
recent_notebook_links = lazy_import('msgraph.generated.models.recent_notebook_links')

class RecentNotebook(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new recentNotebook and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the notebook.
        self._display_name: Optional[str] = None
        # The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._last_accessed_time: Optional[datetime] = None
        # Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote client, if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
        self._links: Optional[recent_notebook_links.RecentNotebookLinks] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The backend store where the Notebook resides, either OneDriveForBusiness or OneDrive.
        self._source_service: Optional[onenote_source_service.OnenoteSourceService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecentNotebook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecentNotebook
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecentNotebook()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the notebook.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the notebook.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_accessed_time": lambda n : setattr(self, 'last_accessed_time', n.get_datetime_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(recent_notebook_links.RecentNotebookLinks)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source_service": lambda n : setattr(self, 'source_service', n.get_enum_value(onenote_source_service.OnenoteSourceService)),
        }
        return fields
    
    @property
    def last_accessed_time(self,) -> Optional[datetime]:
        """
        Gets the lastAccessedTime property value. The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_accessed_time
    
    @last_accessed_time.setter
    def last_accessed_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastAccessedTime property value. The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the lastAccessedTime property.
        """
        self._last_accessed_time = value
    
    @property
    def links(self,) -> Optional[recent_notebook_links.RecentNotebookLinks]:
        """
        Gets the links property value. Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote client, if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
        Returns: Optional[recent_notebook_links.RecentNotebookLinks]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[recent_notebook_links.RecentNotebookLinks] = None) -> None:
        """
        Sets the links property value. Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote client, if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastAccessedTime", self.last_accessed_time)
        writer.write_object_value("links", self.links)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("sourceService", self.source_service)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_service(self,) -> Optional[onenote_source_service.OnenoteSourceService]:
        """
        Gets the sourceService property value. The backend store where the Notebook resides, either OneDriveForBusiness or OneDrive.
        Returns: Optional[onenote_source_service.OnenoteSourceService]
        """
        return self._source_service
    
    @source_service.setter
    def source_service(self,value: Optional[onenote_source_service.OnenoteSourceService] = None) -> None:
        """
        Sets the sourceService property value. The backend store where the Notebook resides, either OneDriveForBusiness or OneDrive.
        Args:
            value: Value to set for the sourceService property.
        """
        self._source_service = value
    

