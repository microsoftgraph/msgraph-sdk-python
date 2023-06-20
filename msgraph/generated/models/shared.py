from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set

@dataclass
class Shared(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The identity of the owner of the shared item. Read-only.
    owner: Optional[identity_set.IdentitySet] = None
    # Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.
    scope: Optional[str] = None
    # The identity of the user who shared the item. Read-only.
    shared_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the item was shared. Read-only.
    shared_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Shared:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Shared
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Shared()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set

        from . import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(identity_set.IdentitySet)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_object_value(identity_set.IdentitySet)),
            "sharedDateTime": lambda n : setattr(self, 'shared_date_time', n.get_datetime_value()),
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
        writer.write_object_value("owner", self.owner)
        writer.write_str_value("scope", self.scope)
        writer.write_object_value("sharedBy", self.shared_by)
        writer.write_datetime_value("sharedDateTime", self.shared_date_time)
        writer.write_additional_data_value(self.additional_data)
    

