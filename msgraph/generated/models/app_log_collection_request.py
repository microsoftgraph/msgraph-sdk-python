from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_log_upload_state import AppLogUploadState
    from .entity import Entity

from .entity import Entity

@dataclass
class AppLogCollectionRequest(Entity):
    """
    Entity for AppLogCollectionRequest contains all logs values.
    """
    # Time at which the upload log request reached a completed state if not completed yet NULL will be returned.
    completed_date_time: Optional[datetime.datetime] = None
    # List of log folders.
    custom_log_folders: Optional[List[str]] = None
    # Indicates error message if any during the upload process.
    error_message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # AppLogUploadStatus
    status: Optional[AppLogUploadState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppLogCollectionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppLogCollectionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppLogCollectionRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_log_upload_state import AppLogUploadState
        from .entity import Entity

        from .app_log_upload_state import AppLogUploadState
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "customLogFolders": lambda n : setattr(self, 'custom_log_folders', n.get_collection_of_primitive_values(str)),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AppLogUploadState)),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_collection_of_primitive_values("customLogFolders", self.custom_log_folders)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_enum_value("status", self.status)
    

