from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_type import ActivityType
    from .entity import Entity
    from .risk_detail import RiskDetail
    from .risk_detection_timing_type import RiskDetectionTimingType
    from .risk_level import RiskLevel
    from .risk_state import RiskState
    from .sign_in_location import SignInLocation
    from .token_issuer_type import TokenIssuerType

from .entity import Entity

@dataclass
class ServicePrincipalRiskDetection(Entity, Parsable):
    # Indicates the activity type the detected risk is linked to.
    activity: Optional[ActivityType] = None
    # Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    activity_date_time: Optional[datetime.datetime] = None
    # Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.
    additional_info: Optional[str] = None
    # The unique identifier for the associated application.
    app_id: Optional[str] = None
    # Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.
    correlation_id: Optional[str] = None
    # Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    detected_date_time: Optional[datetime.datetime] = None
    # Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
    detection_timing_type: Optional[RiskDetectionTimingType] = None
    # Provides the IP address of the client from where the risk occurred.
    ip_address: Optional[str] = None
    # The unique identifier for the key credential associated with the risk detection.
    key_ids: Optional[list[str]] = None
    # Date and time when the risk detection was last updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # Location from where the sign-in was initiated.
    location: Optional[SignInLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).
    request_id: Optional[str] = None
    # Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.
    risk_detail: Optional[RiskDetail] = None
    # The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.
    risk_event_type: Optional[str] = None
    # Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.
    risk_level: Optional[RiskLevel] = None
    # The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.
    risk_state: Optional[RiskState] = None
    # The display name for the service principal.
    service_principal_display_name: Optional[str] = None
    # The unique identifier for the service principal. Supports $filter (eq).
    service_principal_id: Optional[str] = None
    # Source of the risk detection. For example, identityProtection.
    source: Optional[str] = None
    # Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.
    token_issuer_type: Optional[TokenIssuerType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalRiskDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalRiskDetection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalRiskDetection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_type import ActivityType
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_detection_timing_type import RiskDetectionTimingType
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .sign_in_location import SignInLocation
        from .token_issuer_type import TokenIssuerType

        from .activity_type import ActivityType
        from .entity import Entity
        from .risk_detail import RiskDetail
        from .risk_detection_timing_type import RiskDetectionTimingType
        from .risk_level import RiskLevel
        from .risk_state import RiskState
        from .sign_in_location import SignInLocation
        from .token_issuer_type import TokenIssuerType

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(ActivityType)),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "detectedDateTime": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "detectionTimingType": lambda n : setattr(self, 'detection_timing_type', n.get_enum_value(RiskDetectionTimingType)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "keyIds": lambda n : setattr(self, 'key_ids', n.get_collection_of_primitive_values(str)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(SignInLocation)),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(RiskDetail)),
            "riskEventType": lambda n : setattr(self, 'risk_event_type', n.get_str_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(RiskState)),
            "servicePrincipalDisplayName": lambda n : setattr(self, 'service_principal_display_name', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "tokenIssuerType": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(TokenIssuerType)),
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
        writer.write_enum_value("activity", self.activity)
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("additionalInfo", self.additional_info)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_enum_value("detectionTimingType", self.detection_timing_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_collection_of_primitive_values("keyIds", self.key_ids)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("location", self.location)
        writer.write_str_value("requestId", self.request_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_str_value("riskEventType", self.risk_event_type)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("servicePrincipalDisplayName", self.service_principal_display_name)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("source", self.source)
        writer.write_enum_value("tokenIssuerType", self.token_issuer_type)
    

