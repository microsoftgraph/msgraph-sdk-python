from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ChannelSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Count of guests in a channel.
    guests_count: Optional[int] = None
    # Indicates whether external members are included on the channel.
    has_members_from_other_tenants: Optional[bool] = None
    # Count of members in a channel.
    members_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of owners in a channel.
    owners_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChannelSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChannelSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChannelSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guestsCount": lambda n : setattr(self, 'guests_count', n.get_int_value()),
            "hasMembersFromOtherTenants": lambda n : setattr(self, 'has_members_from_other_tenants', n.get_bool_value()),
            "membersCount": lambda n : setattr(self, 'members_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownersCount": lambda n : setattr(self, 'owners_count', n.get_int_value()),
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
        writer.write_int_value("guestsCount", self.guests_count)
        writer.write_bool_value("hasMembersFromOtherTenants", self.has_members_from_other_tenants)
        writer.write_int_value("membersCount", self.members_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("ownersCount", self.owners_count)
        writer.write_additional_data_value(self.additional_data)
    

