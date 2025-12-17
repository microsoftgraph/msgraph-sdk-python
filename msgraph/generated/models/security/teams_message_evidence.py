from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .antispam_teams_direction import AntispamTeamsDirection
    from .file_evidence import FileEvidence
    from .teams_delivery_location import TeamsDeliveryLocation
    from .teams_message_delivery_action import TeamsMessageDeliveryAction
    from .url_evidence import UrlEvidence

from .alert_evidence import AlertEvidence

@dataclass
class TeamsMessageEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.teamsMessageEvidence"
    # The identifier of the campaign that this Teams message is part of.
    campaign_id: Optional[str] = None
    # The channel ID associated with this Teams message.
    channel_id: Optional[str] = None
    # The delivery action of this Teams message. The possible values are: unknown, deliveredAsSpam, delivered, blocked, replaced, unknownFutureValue.
    delivery_action: Optional[TeamsMessageDeliveryAction] = None
    # The delivery location of this Teams message. The possible values are: unknown, teams, quarantine, failed, unknownFutureValue.
    delivery_location: Optional[TeamsDeliveryLocation] = None
    # The list of file entities that are attached to this Teams message.
    files: Optional[list[FileEvidence]] = None
    # The identifier of the team or group that this message is part of.
    group_id: Optional[str] = None
    # Indicates whether the message is owned by the organization that reported the security detection alert.
    is_external: Optional[bool] = None
    # Indicates whether the message is owned by your organization.
    is_owned: Optional[bool] = None
    # Date and time when the message was last edited. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The direction of the Teams message. The possible values are: unknown, inbound, outbound, intraorg, unknownFutureValue.
    message_direction: Optional[AntispamTeamsDirection] = None
    # Message identifier unique within the thread.
    message_id: Optional[str] = None
    # Tenant ID (GUID) of the owner of the message.
    owning_tenant_id: Optional[UUID] = None
    # Identifier of the message to which the current message is a reply; otherwise, it's the same as the messageId.
    parent_message_id: Optional[str] = None
    # The received date of this message. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    received_date_time: Optional[datetime.datetime] = None
    # The recipients of this Teams message.
    recipients: Optional[list[str]] = None
    # The SMTP format address of the sender.
    sender_from_address: Optional[str] = None
    # The IP address of the sender.
    sender_i_p: Optional[str] = None
    # Source of the message; for example, desktop and mobile.
    source_app_name: Optional[str] = None
    # The source ID of this Teams message.
    source_id: Optional[str] = None
    # The subject of this Teams message.
    subject: Optional[str] = None
    # The list of recipients who were detected as suspicious.
    suspicious_recipients: Optional[list[str]] = None
    # Identifier of the channel or chat that this message is part of.
    thread_id: Optional[str] = None
    # The Teams message type. Supported values are: Chat, Topic, Space, and Meeting.
    thread_type: Optional[str] = None
    # The URLs contained in this Teams message.
    urls: Optional[list[UrlEvidence]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsMessageEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsMessageEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsMessageEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .antispam_teams_direction import AntispamTeamsDirection
        from .file_evidence import FileEvidence
        from .teams_delivery_location import TeamsDeliveryLocation
        from .teams_message_delivery_action import TeamsMessageDeliveryAction
        from .url_evidence import UrlEvidence

        from .alert_evidence import AlertEvidence
        from .antispam_teams_direction import AntispamTeamsDirection
        from .file_evidence import FileEvidence
        from .teams_delivery_location import TeamsDeliveryLocation
        from .teams_message_delivery_action import TeamsMessageDeliveryAction
        from .url_evidence import UrlEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "channelId": lambda n : setattr(self, 'channel_id', n.get_str_value()),
            "deliveryAction": lambda n : setattr(self, 'delivery_action', n.get_enum_value(TeamsMessageDeliveryAction)),
            "deliveryLocation": lambda n : setattr(self, 'delivery_location', n.get_enum_value(TeamsDeliveryLocation)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(FileEvidence)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "isExternal": lambda n : setattr(self, 'is_external', n.get_bool_value()),
            "isOwned": lambda n : setattr(self, 'is_owned', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "messageDirection": lambda n : setattr(self, 'message_direction', n.get_enum_value(AntispamTeamsDirection)),
            "messageId": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "owningTenantId": lambda n : setattr(self, 'owning_tenant_id', n.get_uuid_value()),
            "parentMessageId": lambda n : setattr(self, 'parent_message_id', n.get_str_value()),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_primitive_values(str)),
            "senderFromAddress": lambda n : setattr(self, 'sender_from_address', n.get_str_value()),
            "senderIP": lambda n : setattr(self, 'sender_i_p', n.get_str_value()),
            "sourceAppName": lambda n : setattr(self, 'source_app_name', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "suspiciousRecipients": lambda n : setattr(self, 'suspicious_recipients', n.get_collection_of_primitive_values(str)),
            "threadId": lambda n : setattr(self, 'thread_id', n.get_str_value()),
            "threadType": lambda n : setattr(self, 'thread_type', n.get_str_value()),
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_object_values(UrlEvidence)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_str_value("channelId", self.channel_id)
        writer.write_enum_value("deliveryAction", self.delivery_action)
        writer.write_enum_value("deliveryLocation", self.delivery_location)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_str_value("groupId", self.group_id)
        writer.write_bool_value("isExternal", self.is_external)
        writer.write_bool_value("isOwned", self.is_owned)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("messageDirection", self.message_direction)
        writer.write_str_value("messageId", self.message_id)
        writer.write_uuid_value("owningTenantId", self.owning_tenant_id)
        writer.write_str_value("parentMessageId", self.parent_message_id)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_collection_of_primitive_values("recipients", self.recipients)
        writer.write_str_value("senderFromAddress", self.sender_from_address)
        writer.write_str_value("senderIP", self.sender_i_p)
        writer.write_str_value("sourceAppName", self.source_app_name)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_primitive_values("suspiciousRecipients", self.suspicious_recipients)
        writer.write_str_value("threadId", self.thread_id)
        writer.write_str_value("threadType", self.thread_type)
        writer.write_collection_of_object_values("urls", self.urls)
    

