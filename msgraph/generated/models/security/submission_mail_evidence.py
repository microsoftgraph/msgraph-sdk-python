from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class SubmissionMailEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.submissionMailEvidence"
    # The network message ID of the email to which the submission belongs.
    network_message_id: Optional[str] = None
    # The recipient of the email.
    recipient: Optional[str] = None
    # The submission type for the specified instance that maps to Junk, Phish, Malware, or NotJunk.
    report_type: Optional[str] = None
    # The sender of the email.
    sender: Optional[str] = None
    # The sender's IP.
    sender_ip: Optional[str] = None
    # The subject of the submission mail.
    subject: Optional[str] = None
    # The reported date and time of this submission. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024 is 2024-01-01T00:00:00Z.
    submission_date_time: Optional[datetime.datetime] = None
    # The submission ID.
    submission_id: Optional[str] = None
    # The submitter's email address.
    submitter: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubmissionMailEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionMailEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubmissionMailEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "networkMessageId": lambda n : setattr(self, 'network_message_id', n.get_str_value()),
            "recipient": lambda n : setattr(self, 'recipient', n.get_str_value()),
            "reportType": lambda n : setattr(self, 'report_type', n.get_str_value()),
            "sender": lambda n : setattr(self, 'sender', n.get_str_value()),
            "senderIp": lambda n : setattr(self, 'sender_ip', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "submissionDateTime": lambda n : setattr(self, 'submission_date_time', n.get_datetime_value()),
            "submissionId": lambda n : setattr(self, 'submission_id', n.get_str_value()),
            "submitter": lambda n : setattr(self, 'submitter', n.get_str_value()),
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
        writer.write_str_value("networkMessageId", self.network_message_id)
        writer.write_str_value("recipient", self.recipient)
        writer.write_str_value("reportType", self.report_type)
        writer.write_str_value("sender", self.sender)
        writer.write_str_value("senderIp", self.sender_ip)
        writer.write_str_value("subject", self.subject)
        writer.write_datetime_value("submissionDateTime", self.submission_date_time)
        writer.write_str_value("submissionId", self.submission_id)
        writer.write_str_value("submitter", self.submitter)
    

