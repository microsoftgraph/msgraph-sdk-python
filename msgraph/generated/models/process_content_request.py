from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_metadata import ActivityMetadata
    from .device_metadata import DeviceMetadata
    from .integrated_application_metadata import IntegratedApplicationMetadata
    from .process_content_metadata_base import ProcessContentMetadataBase
    from .protected_application_metadata import ProtectedApplicationMetadata

@dataclass
class ProcessContentRequest(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The activityMetadata property
    activity_metadata: Optional[ActivityMetadata] = None
    # A collection of content entries to be processed. Each entry contains the content itself and its metadata. Use conversation metadata for content like prompts and responses and file metadata for files. Required.
    content_entries: Optional[list[ProcessContentMetadataBase]] = None
    # The deviceMetadata property
    device_metadata: Optional[DeviceMetadata] = None
    # The integratedAppMetadata property
    integrated_app_metadata: Optional[IntegratedApplicationMetadata] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Metadata about the protected application making the request. Required.
    protected_app_metadata: Optional[ProtectedApplicationMetadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessContentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessContentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProcessContentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_metadata import ActivityMetadata
        from .device_metadata import DeviceMetadata
        from .integrated_application_metadata import IntegratedApplicationMetadata
        from .process_content_metadata_base import ProcessContentMetadataBase
        from .protected_application_metadata import ProtectedApplicationMetadata

        from .activity_metadata import ActivityMetadata
        from .device_metadata import DeviceMetadata
        from .integrated_application_metadata import IntegratedApplicationMetadata
        from .process_content_metadata_base import ProcessContentMetadataBase
        from .protected_application_metadata import ProtectedApplicationMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "activityMetadata": lambda n : setattr(self, 'activity_metadata', n.get_object_value(ActivityMetadata)),
            "contentEntries": lambda n : setattr(self, 'content_entries', n.get_collection_of_object_values(ProcessContentMetadataBase)),
            "deviceMetadata": lambda n : setattr(self, 'device_metadata', n.get_object_value(DeviceMetadata)),
            "integratedAppMetadata": lambda n : setattr(self, 'integrated_app_metadata', n.get_object_value(IntegratedApplicationMetadata)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protectedAppMetadata": lambda n : setattr(self, 'protected_app_metadata', n.get_object_value(ProtectedApplicationMetadata)),
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
        writer.write_object_value("activityMetadata", self.activity_metadata)
        writer.write_collection_of_object_values("contentEntries", self.content_entries)
        writer.write_object_value("deviceMetadata", self.device_metadata)
        writer.write_object_value("integratedAppMetadata", self.integrated_app_metadata)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("protectedAppMetadata", self.protected_app_metadata)
        writer.write_additional_data_value(self.additional_data)
    

