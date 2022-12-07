from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
threat_assessment_content_type = lazy_import('msgraph.generated.models.threat_assessment_content_type')
threat_assessment_request_source = lazy_import('msgraph.generated.models.threat_assessment_request_source')
threat_assessment_result = lazy_import('msgraph.generated.models.threat_assessment_result')
threat_assessment_status = lazy_import('msgraph.generated.models.threat_assessment_status')
threat_category = lazy_import('msgraph.generated.models.threat_category')
threat_expected_assessment = lazy_import('msgraph.generated.models.threat_expected_assessment')

class ThreatAssessmentRequest(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def category(self,) -> Optional[threat_category.ThreatCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[threat_category.ThreatCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[threat_category.ThreatCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new threatAssessmentRequest and sets the default values.
        """
        super().__init__()
        # The category property
        self._category: Optional[threat_category.ThreatCategory] = None
        # The content type of threat assessment. Possible values are: mail, url, file.
        self._content_type: Optional[threat_assessment_content_type.ThreatAssessmentContentType] = None
        # The threat assessment request creator.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The expectedAssessment property
        self._expected_assessment: Optional[threat_expected_assessment.ThreatExpectedAssessment] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The source of the threat assessment request. Possible values are: administrator.
        self._request_source: Optional[threat_assessment_request_source.ThreatAssessmentRequestSource] = None
        # A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.
        self._results: Optional[List[threat_assessment_result.ThreatAssessmentResult]] = None
        # The assessment process status. Possible values are: pending, completed.
        self._status: Optional[threat_assessment_status.ThreatAssessmentStatus] = None
    
    @property
    def content_type(self,) -> Optional[threat_assessment_content_type.ThreatAssessmentContentType]:
        """
        Gets the contentType property value. The content type of threat assessment. Possible values are: mail, url, file.
        Returns: Optional[threat_assessment_content_type.ThreatAssessmentContentType]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[threat_assessment_content_type.ThreatAssessmentContentType] = None) -> None:
        """
        Sets the contentType property value. The content type of threat assessment. Possible values are: mail, url, file.
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The threat assessment request creator.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The threat assessment request creator.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ThreatAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ThreatAssessmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ThreatAssessmentRequest()
    
    @property
    def expected_assessment(self,) -> Optional[threat_expected_assessment.ThreatExpectedAssessment]:
        """
        Gets the expectedAssessment property value. The expectedAssessment property
        Returns: Optional[threat_expected_assessment.ThreatExpectedAssessment]
        """
        return self._expected_assessment
    
    @expected_assessment.setter
    def expected_assessment(self,value: Optional[threat_expected_assessment.ThreatExpectedAssessment] = None) -> None:
        """
        Sets the expectedAssessment property value. The expectedAssessment property
        Args:
            value: Value to set for the expectedAssessment property.
        """
        self._expected_assessment = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(threat_category.ThreatCategory)),
            "content_type": lambda n : setattr(self, 'content_type', n.get_enum_value(threat_assessment_content_type.ThreatAssessmentContentType)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expected_assessment": lambda n : setattr(self, 'expected_assessment', n.get_enum_value(threat_expected_assessment.ThreatExpectedAssessment)),
            "request_source": lambda n : setattr(self, 'request_source', n.get_enum_value(threat_assessment_request_source.ThreatAssessmentRequestSource)),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(threat_assessment_result.ThreatAssessmentResult)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(threat_assessment_status.ThreatAssessmentStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def request_source(self,) -> Optional[threat_assessment_request_source.ThreatAssessmentRequestSource]:
        """
        Gets the requestSource property value. The source of the threat assessment request. Possible values are: administrator.
        Returns: Optional[threat_assessment_request_source.ThreatAssessmentRequestSource]
        """
        return self._request_source
    
    @request_source.setter
    def request_source(self,value: Optional[threat_assessment_request_source.ThreatAssessmentRequestSource] = None) -> None:
        """
        Sets the requestSource property value. The source of the threat assessment request. Possible values are: administrator.
        Args:
            value: Value to set for the requestSource property.
        """
        self._request_source = value
    
    @property
    def results(self,) -> Optional[List[threat_assessment_result.ThreatAssessmentResult]]:
        """
        Gets the results property value. A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.
        Returns: Optional[List[threat_assessment_result.ThreatAssessmentResult]]
        """
        return self._results
    
    @results.setter
    def results(self,value: Optional[List[threat_assessment_result.ThreatAssessmentResult]] = None) -> None:
        """
        Sets the results property value. A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.
        Args:
            value: Value to set for the results property.
        """
        self._results = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("contentType", self.content_type)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("expectedAssessment", self.expected_assessment)
        writer.write_enum_value("requestSource", self.request_source)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[threat_assessment_status.ThreatAssessmentStatus]:
        """
        Gets the status property value. The assessment process status. Possible values are: pending, completed.
        Returns: Optional[threat_assessment_status.ThreatAssessmentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[threat_assessment_status.ThreatAssessmentStatus] = None) -> None:
        """
        Sets the status property value. The assessment process status. Possible values are: pending, completed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

