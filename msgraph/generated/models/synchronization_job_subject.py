from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_linked_objects import SynchronizationLinkedObjects

@dataclass
class SynchronizationJobSubject(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The links property
    links: Optional[SynchronizationLinkedObjects] = None
    # The objectId property
    object_id: Optional[str] = None
    # The objectTypeName property
    object_type_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationJobSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJobSubject
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationJobSubject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_linked_objects import SynchronizationLinkedObjects

        from .synchronization_linked_objects import SynchronizationLinkedObjects

        fields: Dict[str, Callable[[Any], None]] = {
            "links": lambda n : setattr(self, 'links', n.get_object_value(SynchronizationLinkedObjects)),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "objectTypeName": lambda n : setattr(self, 'object_type_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("links", self.links)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("objectTypeName", self.object_type_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

