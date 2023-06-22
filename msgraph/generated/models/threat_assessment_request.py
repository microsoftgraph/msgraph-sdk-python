from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_file_assessment_request, entity, file_assessment_request, identity_set, mail_assessment_request, threat_assessment_content_type, threat_assessment_request_source, threat_assessment_result, threat_assessment_status, threat_category, threat_expected_assessment, url_assessment_request

from . import entity

@dataclass
class ThreatAssessmentRequest(entity.Entity):
    # The category property
    category: Optional[threat_category.ThreatCategory] = None
    # The content type of threat assessment. Possible values are: mail, url, file.
    content_type: Optional[threat_assessment_content_type.ThreatAssessmentContentType] = None
    # The threat assessment request creator.
    created_by: Optional[identity_set.IdentitySet] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # The expectedAssessment property
    expected_assessment: Optional[threat_expected_assessment.ThreatExpectedAssessment] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source of the threat assessment request. Possible values are: administrator.
    request_source: Optional[threat_assessment_request_source.ThreatAssessmentRequestSource] = None
    # A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.
    results: Optional[List[threat_assessment_result.ThreatAssessmentResult]] = None
    # The assessment process status. Possible values are: pending, completed.
    status: Optional[threat_assessment_status.ThreatAssessmentStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatAssessmentRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailFileAssessmentRequest".casefold():
            from . import email_file_assessment_request

            return email_file_assessment_request.EmailFileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAssessmentRequest".casefold():
            from . import file_assessment_request

            return file_assessment_request.FileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailAssessmentRequest".casefold():
            from . import mail_assessment_request

            return mail_assessment_request.MailAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.urlAssessmentRequest".casefold():
            from . import url_assessment_request

            return url_assessment_request.UrlAssessmentRequest()
        return ThreatAssessmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_file_assessment_request, entity, file_assessment_request, identity_set, mail_assessment_request, threat_assessment_content_type, threat_assessment_request_source, threat_assessment_result, threat_assessment_status, threat_category, threat_expected_assessment, url_assessment_request

        from . import email_file_assessment_request, entity, file_assessment_request, identity_set, mail_assessment_request, threat_assessment_content_type, threat_assessment_request_source, threat_assessment_result, threat_assessment_status, threat_category, threat_expected_assessment, url_assessment_request

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(threat_category.ThreatCategory)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_enum_value(threat_assessment_content_type.ThreatAssessmentContentType)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expectedAssessment": lambda n : setattr(self, 'expected_assessment', n.get_enum_value(threat_expected_assessment.ThreatExpectedAssessment)),
            "requestSource": lambda n : setattr(self, 'request_source', n.get_enum_value(threat_assessment_request_source.ThreatAssessmentRequestSource)),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(threat_assessment_result.ThreatAssessmentResult)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(threat_assessment_status.ThreatAssessmentStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
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
    

