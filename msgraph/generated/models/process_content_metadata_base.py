from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_base import ContentBase
    from .process_conversation_metadata import ProcessConversationMetadata
    from .process_file_metadata import ProcessFileMetadata

@dataclass
class ProcessContentMetadataBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Represents the actual content, either as text (textContent) or binary data (binaryContent). Optional if metadata alone is sufficient for policy evaluation. Do not use for contentActivities.
    content: Optional[ContentBase] = None
    # An identifier used to group multiple related content entries (for example, different parts of the same file upload, messages in a conversation).
    correlation_id: Optional[str] = None
    # Required. Timestamp indicating when the original content was created (for example, file creation time, message sent time).
    created_date_time: Optional[datetime.datetime] = None
    # Required. A unique identifier for this specific content entry within the context of the calling application or enforcement plane (for example, message ID, file path/URL).
    identifier: Optional[str] = None
    # Required. Indicates if the provided content has been truncated from its original form (for example, due to size limits).
    is_truncated: Optional[bool] = None
    # The length of the original content in bytes.
    length: Optional[int] = None
    # Required. Timestamp indicating when the original content was last modified. For ephemeral content like messages, this might be the same as createdDateTime.
    modified_date_time: Optional[datetime.datetime] = None
    # Required. A descriptive name for the content (for example, file name, web page title, 'Chat Message').
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A sequence number indicating the order in which content was generated or should be processed, required when correlationId is used.
    sequence_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessContentMetadataBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessContentMetadataBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.processConversationMetadata".casefold():
            from .process_conversation_metadata import ProcessConversationMetadata

            return ProcessConversationMetadata()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.processFileMetadata".casefold():
            from .process_file_metadata import ProcessFileMetadata

            return ProcessFileMetadata()
        return ProcessContentMetadataBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_base import ContentBase
        from .process_conversation_metadata import ProcessConversationMetadata
        from .process_file_metadata import ProcessFileMetadata

        from .content_base import ContentBase
        from .process_conversation_metadata import ProcessConversationMetadata
        from .process_file_metadata import ProcessFileMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(ContentBase)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "isTruncated": lambda n : setattr(self, 'is_truncated', n.get_bool_value()),
            "length": lambda n : setattr(self, 'length', n.get_int_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sequenceNumber": lambda n : setattr(self, 'sequence_number', n.get_int_value()),
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
        writer.write_object_value("content", self.content)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("identifier", self.identifier)
        writer.write_bool_value("isTruncated", self.is_truncated)
        writer.write_int_value("length", self.length)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("sequenceNumber", self.sequence_number)
        writer.write_additional_data_value(self.additional_data)
    

