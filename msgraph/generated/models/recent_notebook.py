from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import onenote_source_service, recent_notebook_links

@dataclass
class RecentNotebook(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The name of the notebook.
    display_name: Optional[str] = None
    # The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_accessed_time: Optional[datetime] = None
    # Links for opening the notebook. The oneNoteClientURL link opens the notebook in the OneNote client, if it's installed. The oneNoteWebURL link opens the notebook in OneNote on the web.
    links: Optional[recent_notebook_links.RecentNotebookLinks] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The backend store where the Notebook resides, either OneDriveForBusiness or OneDrive.
    source_service: Optional[onenote_source_service.OnenoteSourceService] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import onenote_source_service, recent_notebook_links

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastAccessedTime": lambda n : setattr(self, 'last_accessed_time', n.get_datetime_value()),
            "links": lambda n : setattr(self, 'links', n.get_object_value(recent_notebook_links.RecentNotebookLinks)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceService": lambda n : setattr(self, 'source_service', n.get_enum_value(onenote_source_service.OnenoteSourceService)),
        }
        return fields
    
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
    

