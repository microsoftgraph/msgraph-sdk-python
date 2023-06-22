from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import insight_identity, resource_reference

@dataclass
class SharingDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The user who shared the document.
    shared_by: Optional[insight_identity.InsightIdentity] = None
    # The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    shared_date_time: Optional[datetime] = None
    # The sharingReference property
    sharing_reference: Optional[resource_reference.ResourceReference] = None
    # The subject with which the document was shared.
    sharing_subject: Optional[str] = None
    # Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.
    sharing_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharingDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharingDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SharingDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import insight_identity, resource_reference

        from . import insight_identity, resource_reference

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_object_value(insight_identity.InsightIdentity)),
            "sharedDateTime": lambda n : setattr(self, 'shared_date_time', n.get_datetime_value()),
            "sharingReference": lambda n : setattr(self, 'sharing_reference', n.get_object_value(resource_reference.ResourceReference)),
            "sharingSubject": lambda n : setattr(self, 'sharing_subject', n.get_str_value()),
            "sharingType": lambda n : setattr(self, 'sharing_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sharedBy", self.shared_by)
        writer.write_datetime_value("sharedDateTime", self.shared_date_time)
        writer.write_str_value("sharingSubject", self.sharing_subject)
        writer.write_str_value("sharingType", self.sharing_type)
        writer.write_additional_data_value(self.additional_data)
    

