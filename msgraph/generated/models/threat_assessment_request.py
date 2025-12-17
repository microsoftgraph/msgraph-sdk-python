from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_file_assessment_request import EmailFileAssessmentRequest
    from .entity import Entity
    from .file_assessment_request import FileAssessmentRequest
    from .identity_set import IdentitySet
    from .mail_assessment_request import MailAssessmentRequest
    from .threat_assessment_content_type import ThreatAssessmentContentType
    from .threat_assessment_request_source import ThreatAssessmentRequestSource
    from .threat_assessment_result import ThreatAssessmentResult
    from .threat_assessment_status import ThreatAssessmentStatus
    from .threat_category import ThreatCategory
    from .threat_expected_assessment import ThreatExpectedAssessment
    from .url_assessment_request import UrlAssessmentRequest

from .entity import Entity

@dataclass
class ThreatAssessmentRequest(Entity, Parsable):
    # The category property
    category: Optional[ThreatCategory] = None
    # The content type of threat assessment. The possible values are: mail, url, file.
    content_type: Optional[ThreatAssessmentContentType] = None
    # The threat assessment request creator.
    created_by: Optional[IdentitySet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The expectedAssessment property
    expected_assessment: Optional[ThreatExpectedAssessment] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source of the threat assessment request. The possible values are: administrator.
    request_source: Optional[ThreatAssessmentRequestSource] = None
    # A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.
    results: Optional[list[ThreatAssessmentResult]] = None
    # The assessment process status. The possible values are: pending, completed.
    status: Optional[ThreatAssessmentStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatAssessmentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailFileAssessmentRequest".casefold():
            from .email_file_assessment_request import EmailFileAssessmentRequest

            return EmailFileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAssessmentRequest".casefold():
            from .file_assessment_request import FileAssessmentRequest

            return FileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailAssessmentRequest".casefold():
            from .mail_assessment_request import MailAssessmentRequest

            return MailAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.urlAssessmentRequest".casefold():
            from .url_assessment_request import UrlAssessmentRequest

            return UrlAssessmentRequest()
        return ThreatAssessmentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_file_assessment_request import EmailFileAssessmentRequest
        from .entity import Entity
        from .file_assessment_request import FileAssessmentRequest
        from .identity_set import IdentitySet
        from .mail_assessment_request import MailAssessmentRequest
        from .threat_assessment_content_type import ThreatAssessmentContentType
        from .threat_assessment_request_source import ThreatAssessmentRequestSource
        from .threat_assessment_result import ThreatAssessmentResult
        from .threat_assessment_status import ThreatAssessmentStatus
        from .threat_category import ThreatCategory
        from .threat_expected_assessment import ThreatExpectedAssessment
        from .url_assessment_request import UrlAssessmentRequest

        from .email_file_assessment_request import EmailFileAssessmentRequest
        from .entity import Entity
        from .file_assessment_request import FileAssessmentRequest
        from .identity_set import IdentitySet
        from .mail_assessment_request import MailAssessmentRequest
        from .threat_assessment_content_type import ThreatAssessmentContentType
        from .threat_assessment_request_source import ThreatAssessmentRequestSource
        from .threat_assessment_result import ThreatAssessmentResult
        from .threat_assessment_status import ThreatAssessmentStatus
        from .threat_category import ThreatCategory
        from .threat_expected_assessment import ThreatExpectedAssessment
        from .url_assessment_request import UrlAssessmentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ThreatCategory)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_enum_value(ThreatAssessmentContentType)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expectedAssessment": lambda n : setattr(self, 'expected_assessment', n.get_enum_value(ThreatExpectedAssessment)),
            "requestSource": lambda n : setattr(self, 'request_source', n.get_enum_value(ThreatAssessmentRequestSource)),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(ThreatAssessmentResult)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ThreatAssessmentStatus)),
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
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("contentType", self.content_type)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("expectedAssessment", self.expected_assessment)
        writer.write_enum_value("requestSource", self.request_source)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_enum_value("status", self.status)
    

