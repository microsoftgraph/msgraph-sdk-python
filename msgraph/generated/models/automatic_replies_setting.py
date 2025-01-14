from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automatic_replies_status import AutomaticRepliesStatus
    from .date_time_time_zone import DateTimeTimeZone
    from .external_audience_scope import ExternalAudienceScope

@dataclass
class AutomaticRepliesSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The set of audience external to the signed-in user's organization who will receive the ExternalReplyMessage, if Status is AlwaysEnabled or Scheduled. The possible values are: none, contactsOnly, all.
    external_audience: Optional[ExternalAudienceScope] = None
    # The automatic reply to send to the specified external audience, if Status is AlwaysEnabled or Scheduled.
    external_reply_message: Optional[str] = None
    # The automatic reply to send to the audience internal to the signed-in user's organization, if Status is AlwaysEnabled or Scheduled.
    internal_reply_message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time that automatic replies are set to end, if Status is set to Scheduled.
    scheduled_end_date_time: Optional[DateTimeTimeZone] = None
    # The date and time that automatic replies are set to begin, if Status is set to Scheduled.
    scheduled_start_date_time: Optional[DateTimeTimeZone] = None
    # Configurations status for automatic replies. The possible values are: disabled, alwaysEnabled, scheduled.
    status: Optional[AutomaticRepliesStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomaticRepliesSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomaticRepliesSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomaticRepliesSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automatic_replies_status import AutomaticRepliesStatus
        from .date_time_time_zone import DateTimeTimeZone
        from .external_audience_scope import ExternalAudienceScope

        from .automatic_replies_status import AutomaticRepliesStatus
        from .date_time_time_zone import DateTimeTimeZone
        from .external_audience_scope import ExternalAudienceScope

        fields: dict[str, Callable[[Any], None]] = {
            "externalAudience": lambda n : setattr(self, 'external_audience', n.get_enum_value(ExternalAudienceScope)),
            "externalReplyMessage": lambda n : setattr(self, 'external_reply_message', n.get_str_value()),
            "internalReplyMessage": lambda n : setattr(self, 'internal_reply_message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduledEndDateTime": lambda n : setattr(self, 'scheduled_end_date_time', n.get_object_value(DateTimeTimeZone)),
            "scheduledStartDateTime": lambda n : setattr(self, 'scheduled_start_date_time', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AutomaticRepliesStatus)),
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
        writer.write_enum_value("externalAudience", self.external_audience)
        writer.write_str_value("externalReplyMessage", self.external_reply_message)
        writer.write_str_value("internalReplyMessage", self.internal_reply_message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scheduledEndDateTime", self.scheduled_end_date_time)
        writer.write_object_value("scheduledStartDateTime", self.scheduled_start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

