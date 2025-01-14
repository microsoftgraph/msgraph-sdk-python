from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JoinMeetingIdSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether a passcode is required to join a meeting when using joinMeetingId. Optional.
    is_passcode_required: Optional[bool] = None
    # The meeting ID to be used to join a meeting. Optional. Read-only.
    join_meeting_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The passcode to join a meeting.  Optional. Read-only.
    passcode: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JoinMeetingIdSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JoinMeetingIdSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JoinMeetingIdSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isPasscodeRequired": lambda n : setattr(self, 'is_passcode_required', n.get_bool_value()),
            "joinMeetingId": lambda n : setattr(self, 'join_meeting_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
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
        writer.write_bool_value("isPasscodeRequired", self.is_passcode_required)
        writer.write_str_value("joinMeetingId", self.join_meeting_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("passcode", self.passcode)
        writer.write_additional_data_value(self.additional_data)
    

