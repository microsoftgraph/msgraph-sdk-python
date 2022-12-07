from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mail_destination_routing_reason = lazy_import('msgraph.generated.models.mail_destination_routing_reason')
threat_assessment_request = lazy_import('msgraph.generated.models.threat_assessment_request')

class MailAssessmentRequest(threat_assessment_request.ThreatAssessmentRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new MailAssessmentRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mailAssessmentRequest"
        # The reason for mail routed to its destination. Possible values are: none, mailFlowRule, safeSender, blockedSender, advancedSpamFiltering, domainAllowList, domainBlockList, notInAddressBook, firstTimeSender, autoPurgeToInbox, autoPurgeToJunk, autoPurgeToDeleted, outbound, notJunk, junk.
        self._destination_routing_reason: Optional[mail_destination_routing_reason.MailDestinationRoutingReason] = None
        # The resource URI of the mail message for assessment.
        self._message_uri: Optional[str] = None
        # The mail recipient whose policies are used to assess the mail.
        self._recipient_email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MailAssessmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MailAssessmentRequest()
    
    @property
    def destination_routing_reason(self,) -> Optional[mail_destination_routing_reason.MailDestinationRoutingReason]:
        """
        Gets the destinationRoutingReason property value. The reason for mail routed to its destination. Possible values are: none, mailFlowRule, safeSender, blockedSender, advancedSpamFiltering, domainAllowList, domainBlockList, notInAddressBook, firstTimeSender, autoPurgeToInbox, autoPurgeToJunk, autoPurgeToDeleted, outbound, notJunk, junk.
        Returns: Optional[mail_destination_routing_reason.MailDestinationRoutingReason]
        """
        return self._destination_routing_reason
    
    @destination_routing_reason.setter
    def destination_routing_reason(self,value: Optional[mail_destination_routing_reason.MailDestinationRoutingReason] = None) -> None:
        """
        Sets the destinationRoutingReason property value. The reason for mail routed to its destination. Possible values are: none, mailFlowRule, safeSender, blockedSender, advancedSpamFiltering, domainAllowList, domainBlockList, notInAddressBook, firstTimeSender, autoPurgeToInbox, autoPurgeToJunk, autoPurgeToDeleted, outbound, notJunk, junk.
        Args:
            value: Value to set for the destinationRoutingReason property.
        """
        self._destination_routing_reason = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "destination_routing_reason": lambda n : setattr(self, 'destination_routing_reason', n.get_enum_value(mail_destination_routing_reason.MailDestinationRoutingReason)),
            "message_uri": lambda n : setattr(self, 'message_uri', n.get_str_value()),
            "recipient_email": lambda n : setattr(self, 'recipient_email', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message_uri(self,) -> Optional[str]:
        """
        Gets the messageUri property value. The resource URI of the mail message for assessment.
        Returns: Optional[str]
        """
        return self._message_uri
    
    @message_uri.setter
    def message_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the messageUri property value. The resource URI of the mail message for assessment.
        Args:
            value: Value to set for the messageUri property.
        """
        self._message_uri = value
    
    @property
    def recipient_email(self,) -> Optional[str]:
        """
        Gets the recipientEmail property value. The mail recipient whose policies are used to assess the mail.
        Returns: Optional[str]
        """
        return self._recipient_email
    
    @recipient_email.setter
    def recipient_email(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientEmail property value. The mail recipient whose policies are used to assess the mail.
        Args:
            value: Value to set for the recipientEmail property.
        """
        self._recipient_email = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("destinationRoutingReason", self.destination_routing_reason)
        writer.write_str_value("messageUri", self.message_uri)
        writer.write_str_value("recipientEmail", self.recipient_email)
    

