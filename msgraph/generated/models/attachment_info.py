from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment_type import AttachmentType

@dataclass
class AttachmentInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The type of the attachment. The possible values are: file, item, reference. Required.
    attachment_type: Optional[AttachmentType] = None
    # The nature of the data in the attachment. Optional.
    content_type: Optional[str] = None
    # The display name of the attachment. This can be a descriptive string and doesn't have to be the actual file name. Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The length of the attachment in bytes. Required.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttachmentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttachmentInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment_type import AttachmentType

        from .attachment_type import AttachmentType

        fields: Dict[str, Callable[[Any], None]] = {
            "attachmentType": lambda n : setattr(self, 'attachment_type', n.get_enum_value(AttachmentType)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_enum_value("attachmentType", self.attachment_type)
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    

