from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class Shared(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity of the owner of the shared item. Read-only.
    owner: Optional[IdentitySet] = None
    # Indicates the scope of how the item is shared. The possible values are: anonymous, organization, or users. Read-only.
    scope: Optional[str] = None
    # The identity of the user who shared the item. Read-only.
    shared_by: Optional[IdentitySet] = None
    # The UTC date and time when the item was shared. Read-only.
    shared_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Shared:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Shared
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Shared()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(IdentitySet)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_object_value(IdentitySet)),
            "sharedDateTime": lambda n : setattr(self, 'shared_date_time', n.get_datetime_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("owner", self.owner)
        writer.write_str_value("scope", self.scope)
        writer.write_object_value("sharedBy", self.shared_by)
        writer.write_datetime_value("sharedDateTime", self.shared_date_time)
        writer.write_additional_data_value(self.additional_data)
    

