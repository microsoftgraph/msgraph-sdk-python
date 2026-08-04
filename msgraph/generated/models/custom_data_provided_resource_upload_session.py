from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_data_provided_resource_access_review_upload_session import CustomDataProvidedResourceAccessReviewUploadSession
    from .custom_data_provided_resource_file import CustomDataProvidedResourceFile
    from .custom_data_provided_resource_payloads.data import Data
    from .custom_data_provided_resource_upload_stats import CustomDataProvidedResourceUploadStats
    from .custom_data_provided_resource_upload_status import CustomDataProvidedResourceUploadStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomDataProvidedResourceUploadSession(Entity, Parsable):
    # DateTime when the upload session was created. Read-only. Supports $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # An object containing the context for which this data is being uploaded.
    data: Optional[Data] = None
    # The files uploaded during this upload session. Supports $expand and $expand with nested $filter and $orderby.
    files: Optional[list[CustomDataProvidedResourceFile]] = None
    # Indicates if all the necessary files have been uploaded to this session.
    is_upload_done: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the context for which data is being uploaded, for example, the Access Review instance ID. Supports $filter (eq).
    reference_id: Optional[str] = None
    # The stats property
    stats: Optional[CustomDataProvidedResourceUploadStats] = None
    # The status property
    status: Optional[CustomDataProvidedResourceUploadStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomDataProvidedResourceUploadSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomDataProvidedResourceUploadSession
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customDataProvidedResourceAccessReviewUploadSession".casefold():
            from .custom_data_provided_resource_access_review_upload_session import CustomDataProvidedResourceAccessReviewUploadSession

            return CustomDataProvidedResourceAccessReviewUploadSession()
        return CustomDataProvidedResourceUploadSession()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_data_provided_resource_access_review_upload_session import CustomDataProvidedResourceAccessReviewUploadSession
        from .custom_data_provided_resource_file import CustomDataProvidedResourceFile
        from .custom_data_provided_resource_payloads.data import Data
        from .custom_data_provided_resource_upload_stats import CustomDataProvidedResourceUploadStats
        from .custom_data_provided_resource_upload_status import CustomDataProvidedResourceUploadStatus
        from .entity import Entity

        from .custom_data_provided_resource_access_review_upload_session import CustomDataProvidedResourceAccessReviewUploadSession
        from .custom_data_provided_resource_file import CustomDataProvidedResourceFile
        from .custom_data_provided_resource_payloads.data import Data
        from .custom_data_provided_resource_upload_stats import CustomDataProvidedResourceUploadStats
        from .custom_data_provided_resource_upload_status import CustomDataProvidedResourceUploadStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "data": lambda n : setattr(self, 'data', n.get_object_value(Data)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(CustomDataProvidedResourceFile)),
            "isUploadDone": lambda n : setattr(self, 'is_upload_done', n.get_bool_value()),
            "referenceId": lambda n : setattr(self, 'reference_id', n.get_str_value()),
            "stats": lambda n : setattr(self, 'stats', n.get_object_value(CustomDataProvidedResourceUploadStats)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CustomDataProvidedResourceUploadStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("data", self.data)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_bool_value("isUploadDone", self.is_upload_done)
        writer.write_str_value("referenceId", self.reference_id)
        writer.write_object_value("stats", self.stats)
        writer.write_enum_value("status", self.status)
    

