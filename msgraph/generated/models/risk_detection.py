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

class RiskDetection(entity.Entity):
    @property
    def activity(self,) -> Optional[activity_type.ActivityType]:
        """
        Gets the activity property value. Indicates the activity type the detected risk is linked to. Possible values are: signin, user, unknownFutureValue.
        Returns: Optional[activity_type.ActivityType]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[activity_type.ActivityType] = None) -> None:
        """
        Sets the activity property value. Indicates the activity type the detected risk is linked to. Possible values are: signin, user, unknownFutureValue.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def additional_info(self,) -> Optional[str]:
        """
        Gets the additionalInfo property value. Additional information associated with the risk detection in JSON format. For example, '[{/'Key/':/'userAgent/',/'Value/':/'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36/'}]'. Possible keys in the additionalInfo JSON string are: userAgent, alertUrl, relatedEventTimeInUtc, relatedUserAgent, deviceInformation, relatedLocation, requestId, correlationId, lastActivityTimeInUtc, malwareName, clientLocation, clientIp, riskReasons. For more information about riskReasons and possible values, see riskReasons values.
        Returns: Optional[str]
        """
        return self._additional_info
    
    @additional_info.setter
    def additional_info(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInfo property value. Additional information associated with the risk detection in JSON format. For example, '[{/'Key/':/'userAgent/',/'Value/':/'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36/'}]'. Possible keys in the additionalInfo JSON string are: userAgent, alertUrl, relatedEventTimeInUtc, relatedUserAgent, deviceInformation, relatedLocation, requestId, correlationId, lastActivityTimeInUtc, malwareName, clientLocation, clientIp, riskReasons. For more information about riskReasons and possible values, see riskReasons values.
        Args:
            value: Value to set for the additionalInfo property.
        """
        self._additional_info = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new RiskDetection and sets the default values.
        """
        super().__init__()
        # Indicates the activity type the detected risk is linked to. Possible values are: signin, user, unknownFutureValue.
        self._activity: Optional[activity_type.ActivityType] = None
        # Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
        self._activity_date_time: Optional[datetime] = None
        # Additional information associated with the risk detection in JSON format. For example, '[{/'Key/':/'userAgent/',/'Value/':/'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36/'}]'. Possible keys in the additionalInfo JSON string are: userAgent, alertUrl, relatedEventTimeInUtc, relatedUserAgent, deviceInformation, relatedLocation, requestId, correlationId, lastActivityTimeInUtc, malwareName, clientLocation, clientIp, riskReasons. For more information about riskReasons and possible values, see riskReasons values.
        self._additional_info: Optional[str] = None
        # Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
        self._correlation_id: Optional[str] = None
        # Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: 2014-01-01T00:00:00Z
        self._detected_date_time: Optional[datetime] = None
        # Timing of the detected risk (real-time/offline). Possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
        self._detection_timing_type: Optional[risk_detection_timing_type.RiskDetectionTimingType] = None
        # Provides the IP address of the client from where the risk occurred.
        self._ip_address: Optional[str] = None
        # Date and time that the risk detection was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
        self._last_updated_date_time: Optional[datetime] = None
        # Location of the sign-in.
        self._location: Optional[sign_in_location.SignInLocation] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
        self._request_id: Optional[str] = None
        # Details of the detected risk. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue, m365DAdminDismissedDetection. Note that you must use the Prefer: include - unknown -enum-members request header to get the following value(s) in this evolvable enum: m365DAdminDismissedDetection.
        self._risk_detail: Optional[risk_detail.RiskDetail] = None
        # The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, generic,adminConfirmedUserCompromised, passwordSpray, impossibleTravel, newCountry, anomalousToken, tokenIssuerAnomaly,suspiciousBrowser, riskyIPAddress, mcasSuspiciousInboxManipulationRules, suspiciousInboxForwarding, and anomalousUserActivity. If the risk detection is a premium detection, will show generic. For more information about each value, see riskEventType values.
        self._risk_event_type: Optional[str] = None
        # Level of the detected risk. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
        self._risk_level: Optional[risk_level.RiskLevel] = None
        # The state of a detected risky user or sign-in. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        self._risk_state: Optional[risk_state.RiskState] = None
        # Source of the risk detection. For example, activeDirectory.
        self._source: Optional[str] = None
        # Indicates the type of token issuer for the detected sign-in risk. Possible values are: AzureAD, ADFederationServices, UnknownFutureValue.
        self._token_issuer_type: Optional[token_issuer_type.TokenIssuerType] = None
        # The user principal name (UPN) of the user.
        self._user_display_name: Optional[str] = None
        # Unique ID of the user.
        self._user_id: Optional[str] = None
        # The user principal name (UPN) of the user.
        self._user_principal_name: Optional[str] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskDetection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RiskDetection()
    
    @property
    def detected_date_time(self,) -> Optional[datetime]:
        """
        Gets the detectedDateTime property value. Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._detected_date_time
    
    @detected_date_time.setter
    def detected_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the detectedDateTime property value. Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the detectedDateTime property.
        """
        self._detected_date_time = value
    
    @property
    def detection_timing_type(self,) -> Optional[risk_detection_timing_type.RiskDetectionTimingType]:
        """
        Gets the detectionTimingType property value. Timing of the detected risk (real-time/offline). Possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
        Returns: Optional[risk_detection_timing_type.RiskDetectionTimingType]
        """
        return self._detection_timing_type
    
    @detection_timing_type.setter
    def detection_timing_type(self,value: Optional[risk_detection_timing_type.RiskDetectionTimingType] = None) -> None:
        """
        Sets the detectionTimingType property value. Timing of the detected risk (real-time/offline). Possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
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
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "additional_info": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "detected_date_time": lambda n : setattr(self, 'detected_date_time', n.get_datetime_value()),
            "detection_timing_type": lambda n : setattr(self, 'detection_timing_type', n.get_enum_value(risk_detection_timing_type.RiskDetectionTimingType)),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(sign_in_location.SignInLocation)),
            "request_id": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "risk_detail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "risk_event_type": lambda n : setattr(self, 'risk_event_type', n.get_str_value()),
            "risk_level": lambda n : setattr(self, 'risk_level', n.get_enum_value(risk_level.RiskLevel)),
            "risk_state": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "token_issuer_type": lambda n : setattr(self, 'token_issuer_type', n.get_enum_value(token_issuer_type.TokenIssuerType)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Date and time that the risk detection was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Date and time that the risk detection was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def location(self,) -> Optional[sign_in_location.SignInLocation]:
        """
        Gets the location property value. Location of the sign-in.
        Returns: Optional[sign_in_location.SignInLocation]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[sign_in_location.SignInLocation] = None) -> None:
        """
        Sets the location property value. Location of the sign-in.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def request_id(self,) -> Optional[str]:
        """
        Gets the requestId property value. Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
        Returns: Optional[str]
        """
        return self._request_id
    
    @request_id.setter
    def request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the requestId property value. Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
        Args:
            value: Value to set for the requestId property.
        """
        self._request_id = value
    
    @property
    def risk_detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the riskDetail property value. Details of the detected risk. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue, m365DAdminDismissedDetection. Note that you must use the Prefer: include - unknown -enum-members request header to get the following value(s) in this evolvable enum: m365DAdminDismissedDetection.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._risk_detail
    
    @risk_detail.setter
    def risk_detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the riskDetail property value. Details of the detected risk. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue, m365DAdminDismissedDetection. Note that you must use the Prefer: include - unknown -enum-members request header to get the following value(s) in this evolvable enum: m365DAdminDismissedDetection.
        Args:
            value: Value to set for the riskDetail property.
        """
        self._risk_detail = value
    
    @property
    def risk_event_type(self,) -> Optional[str]:
        """
        Gets the riskEventType property value. The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, generic,adminConfirmedUserCompromised, passwordSpray, impossibleTravel, newCountry, anomalousToken, tokenIssuerAnomaly,suspiciousBrowser, riskyIPAddress, mcasSuspiciousInboxManipulationRules, suspiciousInboxForwarding, and anomalousUserActivity. If the risk detection is a premium detection, will show generic. For more information about each value, see riskEventType values.
        Returns: Optional[str]
        """
        return self._risk_event_type
    
    @risk_event_type.setter
    def risk_event_type(self,value: Optional[str] = None) -> None:
        """
        Sets the riskEventType property value. The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, generic,adminConfirmedUserCompromised, passwordSpray, impossibleTravel, newCountry, anomalousToken, tokenIssuerAnomaly,suspiciousBrowser, riskyIPAddress, mcasSuspiciousInboxManipulationRules, suspiciousInboxForwarding, and anomalousUserActivity. If the risk detection is a premium detection, will show generic. For more information about each value, see riskEventType values.
        Args:
            value: Value to set for the riskEventType property.
        """
        self._risk_event_type = value
    
    @property
    def risk_level(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevel property value. Level of the detected risk. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level
    
    @risk_level.setter
    def risk_level(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevel property value. Level of the detected risk. Possible values are: low, medium, high, hidden, none, unknownFutureValue.
        Args:
            value: Value to set for the riskLevel property.
        """
        self._risk_level = value
    
    @property
    def risk_state(self,) -> Optional[risk_state.RiskState]:
        """
        Gets the riskState property value. The state of a detected risky user or sign-in. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
        Returns: Optional[risk_state.RiskState]
        """
        return self._risk_state
    
    @risk_state.setter
    def risk_state(self,value: Optional[risk_state.RiskState] = None) -> None:
        """
        Sets the riskState property value. The state of a detected risky user or sign-in. Possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
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
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("detectedDateTime", self.detected_date_time)
        writer.write_enum_value("detectionTimingType", self.detection_timing_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("location", self.location)
        writer.write_str_value("requestId", self.request_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_str_value("riskEventType", self.risk_event_type)
        writer.write_enum_value("riskLevel", self.risk_level)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_str_value("source", self.source)
        writer.write_enum_value("tokenIssuerType", self.token_issuer_type)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def source(self,) -> Optional[str]:
        """
        Gets the source property value. Source of the risk detection. For example, activeDirectory.
        Returns: Optional[str]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[str] = None) -> None:
        """
        Sets the source property value. Source of the risk detection. For example, activeDirectory.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def token_issuer_type(self,) -> Optional[token_issuer_type.TokenIssuerType]:
        """
        Gets the tokenIssuerType property value. Indicates the type of token issuer for the detected sign-in risk. Possible values are: AzureAD, ADFederationServices, UnknownFutureValue.
        Returns: Optional[token_issuer_type.TokenIssuerType]
        """
        return self._token_issuer_type
    
    @token_issuer_type.setter
    def token_issuer_type(self,value: Optional[token_issuer_type.TokenIssuerType] = None) -> None:
        """
        Sets the tokenIssuerType property value. Indicates the type of token issuer for the detected sign-in risk. Possible values are: AzureAD, ADFederationServices, UnknownFutureValue.
        Args:
            value: Value to set for the tokenIssuerType property.
        """
        self._token_issuer_type = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. The user principal name (UPN) of the user.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. The user principal name (UPN) of the user.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Unique ID of the user.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Unique ID of the user.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

