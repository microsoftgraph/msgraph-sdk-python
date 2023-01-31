from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_type = lazy_import('msgraph.generated.models.activity_type')
entity = lazy_import('msgraph.generated.models.entity')
risk_detail = lazy_import('msgraph.generated.models.risk_detail')
risk_detection_timing_type = lazy_import('msgraph.generated.models.risk_detection_timing_type')
risk_level = lazy_import('msgraph.generated.models.risk_level')
risk_state = lazy_import('msgraph.generated.models.risk_state')
sign_in_location = lazy_import('msgraph.generated.models.sign_in_location')
token_issuer_type = lazy_import('msgraph.generated.models.token_issuer_type')

class ServicePrincipalRiskDetection(entity.Entity):
    @property
    def activity(self,) -> Optional[activity_type.ActivityType]:
        """
        Gets the activity property value. Indicates the activity type the detected risk is linked to.  The possible values are: signin, servicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: servicePrincipal.
        Returns: Optional[activity_type.ActivityType]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[activity_type.ActivityType] = None) -> None:
        """
        Sets the activity property value. Indicates the activity type the detected risk is linked to.  The possible values are: signin, servicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: servicePrincipal.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def additional_info(self,) -> Optional[str]:
        """
        Gets the additionalInfo property value. Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.
        Returns: Optional[str]
        """
        return self._additional_info
    
    @additional_info.setter
    def additional_info(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInfo property value. Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.
        Args:
            value: Value to set for the additionalInfo property.
        """
        self._additional_info = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The unique identifier for the associated application.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The unique identifier for the associated application.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ServicePrincipalRiskDetection and sets the default values.
        """
        super().__init__()
        # Indicates the activity type the detected risk is linked to.  The possible values are: signin, servicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: servicePrincipal.
        self._activity: Optional[activity_type.ActivityType] = None
        # Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._activity_date_time: Optional[datetime] = None
        # Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.
        self._additional_info: Optional[str] = None
        # The unique identifier for the associated application.
        self._app_id: Optional[str] = None
        # Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.
        self._correlation_id: Optional[str] = None
        # Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._detected_date_time: Optional[datetime] = None
        # Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
        self._detection_timing_type: Optional[risk_detection_timing_type.RiskDetectionTimingType] = None
        # Provides the IP address of the client from where the risk occurred.
        self._ip_address: Optional[str] = None
        # The unique identifier for the key credential associated with the risk detection.
        self._key_ids: Optional[List[str]] = None
        # Date and time when the risk detection was last updated.
        self._last_updated_date_time: Optional[datetime] = None
        # Location from where the sign-in was initiated.
        self._location: Optional[sign_in_location.SignInLocation] = None
        self.odata_type: Optional[str] = None
        # Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).
        self._request_id: Optional[str] = None
        # Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        self._risk_detail: Optional[risk_detail.RiskDetail] = None
        # The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.
        self._risk_event_type: Optional[str] = None
        # Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.
        self._risk_level: Optional[risk_level.RiskLevel] = None
        # The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.
        self._risk_state: Optional[risk_state.RiskState] = None
        # The display name for the service principal.
        self._service_principal_display_name: Optional[str] = None
        # The unique identifier for the service principal. Supports $filter (eq).
        self._service_principal_id: Optional[str] = None
        # Source of the risk detection. For example, identityProtection.
        self._source: Optional[str] = None
        # Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.
        self._token_issuer_type: Optional[token_issuer_type.TokenIssuerType] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalRiskDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalRiskDetection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePrincipalRiskDetection()
    
    @property
    def detected_date_time(self,) -> Optional[datetime]:
        """
        Gets the detectedDateTime property value. Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._detected_date_time
    
    @detected_date_time.setter
    def detected_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the detectedDateTime property value. Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the detectedDateTime property.
        """
        self._detected_date_time = value
    
    @property
    def detection_timing_type(self,) -> Optional[risk_detection_timing_type.RiskDetectionTimingType]:
        """
        Gets the detectionTimingType property value. Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
        Returns: Optional[risk_detection_timing_type.RiskDetectionTimingType]
        """
        return self._detection_timing_type
    
    @detection_timing_type.setter
    def detection_timing_type(self,value: Optional[risk_detection_timing_type.RiskDetectionTimingType] = None) -> None:
        """
        Sets the detectionTimingType property value. Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
        Args:
            value: Value to set for the detectionTimingType property.
        """
        self._detection_timing_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(activity_type.ActivityType)),
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "detectedDateTime": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "detectionTimingType": lambda n : setattr(self, 'detection_timing_type', n.get_enum_value(risk_detection_timing_type.RiskDetectionTimingType)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "keyIds": lambda n : setattr(self, 'key_ids', n.get_collection_of_primitive_values(str)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(sign_in_location.SignInLocation)),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "riskDetail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "riskEventType": lambda n : setattr(self, 'risk_event_type', n.get_str_value()),
            "riskLevel": lambda n : setattr(self, 'risk_level', n.get_enum_value(risk_level.RiskLevel)),
            "riskState": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "servicePrincipalDisplayName": lambda n : setattr(self, 'service_principal_display_name', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "tokenIssuerType": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(token_issuer_type.TokenIssuerType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. Provides the IP address of the client from where the risk occurred.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. Provides the IP address of the client from where the risk occurred.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def key_ids(self,) -> Optional[List[str]]:
        """
        Gets the keyIds property value. The unique identifier for the key credential associated with the risk detection.
        Returns: Optional[List[str]]
        """
        return self._key_ids
    
    @key_ids.setter
    def key_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the keyIds property value. The unique identifier for the key credential associated with the risk detection.
        Args:
            value: Value to set for the keyIds property.
        """
        self._key_ids = value
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Date and time when the risk detection was last updated.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Date and time when the risk detection was last updated.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def location(self,) -> Optional[sign_in_location.SignInLocation]:
        """
        Gets the location property value. Location from where the sign-in was initiated.
        Returns: Optional[sign_in_location.SignInLocation]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[sign_in_location.SignInLocation] = None) -> None:
        """
        Sets the location property value. Location from where the sign-in was initiated.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def request_id(self,) -> Optional[str]:
        """
        Gets the requestId property value. Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._request_id
    
    @request_id.setter
    def request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the requestId property value. Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).
        Args:
            value: Value to set for the requestId property.
        """
        self._request_id = value
    
    @property
    def risk_detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the riskDetail property value. Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._risk_detail
    
    @risk_detail.setter
    def risk_detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the riskDetail property value. Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        Args:
            value: Value to set for the riskDetail property.
        """
        self._risk_detail = value
    
    @property
    def risk_event_type(self,) -> Optional[str]:
        """
        Gets the riskEventType property value. The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.
        Returns: Optional[str]
        """
        return self._risk_event_type
    
    @risk_event_type.setter
    def risk_event_type(self,value: Optional[str] = None) -> None:
        """
        Sets the riskEventType property value. The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.
        Args:
            value: Value to set for the riskEventType property.
        """
        self._risk_event_type = value
    
    @property
    def risk_level(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevel property value. Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level
    
    @risk_level.setter
    def risk_level(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevel property value. Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.
        Args:
            value: Value to set for the riskLevel property.
        """
        self._risk_level = value
    
    @property
    def risk_state(self,) -> Optional[risk_state.RiskState]:
        """
        Gets the riskState property value. The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.
        Returns: Optional[risk_state.RiskState]
        """
        return self._risk_state
    
    @risk_state.setter
    def risk_state(self,value: Optional[risk_state.RiskState] = None) -> None:
        """
        Sets the riskState property value. The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.
        Args:
            value: Value to set for the riskState property.
        """
        self._risk_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def service_principal_display_name(self,) -> Optional[str]:
        """
        Gets the servicePrincipalDisplayName property value. The display name for the service principal.
        Returns: Optional[str]
        """
        return self._service_principal_display_name
    
    @service_principal_display_name.setter
    def service_principal_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalDisplayName property value. The display name for the service principal.
        Args:
            value: Value to set for the servicePrincipalDisplayName property.
        """
        self._service_principal_display_name = value
    
    @property
    def service_principal_id(self,) -> Optional[str]:
        """
        Gets the servicePrincipalId property value. The unique identifier for the service principal. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._service_principal_id
    
    @service_principal_id.setter
    def service_principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalId property value. The unique identifier for the service principal. Supports $filter (eq).
        Args:
            value: Value to set for the servicePrincipalId property.
        """
        self._service_principal_id = value
    
    @property
    def source(self,) -> Optional[str]:
        """
        Gets the source property value. Source of the risk detection. For example, identityProtection.
        Returns: Optional[str]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[str] = None) -> None:
        """
        Sets the source property value. Source of the risk detection. For example, identityProtection.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def token_issuer_type(self,) -> Optional[token_issuer_type.TokenIssuerType]:
        """
        Gets the tokenIssuerType property value. Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.
        Returns: Optional[token_issuer_type.TokenIssuerType]
        """
        return self._token_issuer_type
    
    @token_issuer_type.setter
    def token_issuer_type(self,value: Optional[token_issuer_type.TokenIssuerType] = None) -> None:
        """
        Sets the tokenIssuerType property value. Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.
        Args:
            value: Value to set for the tokenIssuerType property.
        """
        self._token_issuer_type = value
    

