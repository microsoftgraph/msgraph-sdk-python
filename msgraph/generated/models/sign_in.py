from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

applied_conditional_access_policy = lazy_import('msgraph.generated.models.applied_conditional_access_policy')
conditional_access_status = lazy_import('msgraph.generated.models.conditional_access_status')
device_detail = lazy_import('msgraph.generated.models.device_detail')
entity = lazy_import('msgraph.generated.models.entity')
risk_detail = lazy_import('msgraph.generated.models.risk_detail')
risk_event_type = lazy_import('msgraph.generated.models.risk_event_type')
risk_level = lazy_import('msgraph.generated.models.risk_level')
risk_state = lazy_import('msgraph.generated.models.risk_state')
sign_in_location = lazy_import('msgraph.generated.models.sign_in_location')
sign_in_status = lazy_import('msgraph.generated.models.sign_in_status')

class SignIn(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. App name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. App name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. Unique GUID representing the app ID in the Azure Active Directory. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. Unique GUID representing the app ID in the Azure Active Directory. Supports $filter (eq operator only).
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def applied_conditional_access_policies(self,) -> Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]]:
        """
        Gets the appliedConditionalAccessPolicies property value. The appliedConditionalAccessPolicies property
        Returns: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]]
        """
        return self._applied_conditional_access_policies
    
    @applied_conditional_access_policies.setter
    def applied_conditional_access_policies(self,value: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]] = None) -> None:
        """
        Sets the appliedConditionalAccessPolicies property value. The appliedConditionalAccessPolicies property
        Args:
            value: Value to set for the appliedConditionalAccessPolicies property.
        """
        self._applied_conditional_access_policies = value
    
    @property
    def client_app_used(self,) -> Optional[str]:
        """
        Gets the clientAppUsed property value. Identifies the client used for the sign-in activity. Modern authentication clients include Browser and modern clients. Legacy authentication clients include Exchange ActiveSync, IMAP, MAPI, SMTP, POP, and other clients. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._client_app_used
    
    @client_app_used.setter
    def client_app_used(self,value: Optional[str] = None) -> None:
        """
        Sets the clientAppUsed property value. Identifies the client used for the sign-in activity. Modern authentication clients include Browser and modern clients. Legacy authentication clients include Exchange ActiveSync, IMAP, MAPI, SMTP, POP, and other clients. Supports $filter (eq operator only).
        Args:
            value: Value to set for the clientAppUsed property.
        """
        self._client_app_used = value
    
    @property
    def conditional_access_status(self,) -> Optional[conditional_access_status.ConditionalAccessStatus]:
        """
        Gets the conditionalAccessStatus property value. Reports status of an activated conditional access policy. Possible values are: success, failure, notApplied, and unknownFutureValue. Supports $filter (eq operator only).
        Returns: Optional[conditional_access_status.ConditionalAccessStatus]
        """
        return self._conditional_access_status
    
    @conditional_access_status.setter
    def conditional_access_status(self,value: Optional[conditional_access_status.ConditionalAccessStatus] = None) -> None:
        """
        Sets the conditionalAccessStatus property value. Reports status of an activated conditional access policy. Possible values are: success, failure, notApplied, and unknownFutureValue. Supports $filter (eq operator only).
        Args:
            value: Value to set for the conditionalAccessStatus property.
        """
        self._conditional_access_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new signIn and sets the default values.
        """
        super().__init__()
        # App name displayed in the Azure Portal. Supports $filter (eq and startsWith operators only).
        self._app_display_name: Optional[str] = None
        # Unique GUID representing the app ID in the Azure Active Directory. Supports $filter (eq operator only).
        self._app_id: Optional[str] = None
        # The appliedConditionalAccessPolicies property
        self._applied_conditional_access_policies: Optional[List[applied_conditional_access_policy.AppliedConditionalAccessPolicy]] = None
        # Identifies the client used for the sign-in activity. Modern authentication clients include Browser and modern clients. Legacy authentication clients include Exchange ActiveSync, IMAP, MAPI, SMTP, POP, and other clients. Supports $filter (eq operator only).
        self._client_app_used: Optional[str] = None
        # Reports status of an activated conditional access policy. Possible values are: success, failure, notApplied, and unknownFutureValue. Supports $filter (eq operator only).
        self._conditional_access_status: Optional[conditional_access_status.ConditionalAccessStatus] = None
        # The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity. Supports $filter (eq operator only).
        self._correlation_id: Optional[str] = None
        # Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
        self._created_date_time: Optional[datetime] = None
        # Device information from where the sign-in occurred; includes device ID, operating system, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSytem properties.
        self._device_detail: Optional[device_detail.DeviceDetail] = None
        # IP address of the client used to sign in. Supports $filter (eq and startsWith operators only).
        self._ip_address: Optional[str] = None
        # Indicates if a sign-in is interactive or not.
        self._is_interactive: Optional[bool] = None
        # Provides the city, state, and country code where the sign-in originated. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
        self._location: Optional[sign_in_location.SignInLocation] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Name of the resource the user signed into. Supports $filter (eq operator only).
        self._resource_display_name: Optional[str] = None
        # ID of the resource that the user signed into. Supports $filter (eq operator only).
        self._resource_id: Optional[str] = None
        # Provides the 'reason' behind a specific state of a risky user, sign-in or a risk event. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far.  Supports $filter (eq operator only).Note: Details for this property require an Azure AD Premium P2 license. Other licenses return the value hidden.
        self._risk_detail: Optional[risk_detail.RiskDetail] = None
        # Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue. Supports $filter (eq operator only).
        self._risk_event_types: Optional[List[risk_event_type.RiskEventType]] = None
        # The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
        self._risk_event_types_v2: Optional[List[str]] = None
        # Aggregated risk level. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only).  Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
        self._risk_level_aggregated: Optional[risk_level.RiskLevel] = None
        # Risk level during sign-in. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection.  Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
        self._risk_level_during_sign_in: Optional[risk_level.RiskLevel] = None
        # Reports status of the risky user, sign-in, or a risk event. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue. Supports $filter (eq operator only).
        self._risk_state: Optional[risk_state.RiskState] = None
        # Sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
        self._status: Optional[sign_in_status.SignInStatus] = None
        # Display name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
        self._user_display_name: Optional[str] = None
        # ID of the user that initiated the sign-in. Supports $filter (eq operator only).
        self._user_id: Optional[str] = None
        # User principal name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
        self._user_principal_name: Optional[str] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity. Supports $filter (eq operator only).
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as 2014-01-01T00:00:00Z. Supports $orderby and $filter (eq, le, and ge operators only).
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignIn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignIn()
    
    @property
    def device_detail(self,) -> Optional[device_detail.DeviceDetail]:
        """
        Gets the deviceDetail property value. Device information from where the sign-in occurred; includes device ID, operating system, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSytem properties.
        Returns: Optional[device_detail.DeviceDetail]
        """
        return self._device_detail
    
    @device_detail.setter
    def device_detail(self,value: Optional[device_detail.DeviceDetail] = None) -> None:
        """
        Sets the deviceDetail property value. Device information from where the sign-in occurred; includes device ID, operating system, and browser. Supports $filter (eq and startsWith operators only) on browser and operatingSytem properties.
        Args:
            value: Value to set for the deviceDetail property.
        """
        self._device_detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "applied_conditional_access_policies": lambda n : setattr(self, 'applied_conditional_access_policies', n.get_collection_of_object_values(applied_conditional_access_policy.AppliedConditionalAccessPolicy)),
            "client_app_used": lambda n : setattr(self, 'client_app_used', n.get_str_value()),
            "conditional_access_status": lambda n : setattr(self, 'conditional_access_status', n.get_enum_value(conditional_access_status.ConditionalAccessStatus)),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_detail": lambda n : setattr(self, 'device_detail', n.get_object_value(device_detail.DeviceDetail)),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "is_interactive": lambda n : setattr(self, 'is_interactive', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(sign_in_location.SignInLocation)),
            "resource_display_name": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "risk_detail": lambda n : setattr(self, 'risk_detail', n.get_enum_value(risk_detail.RiskDetail)),
            "risk_event_types": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_enum_values(risk_event_type.RiskEventType)),
            "risk_event_types_v2": lambda n : setattr(self, 'risk_event_types_v2', n.get_collection_of_primitive_values(str)),
            "risk_level_aggregated": lambda n : setattr(self, 'risk_level_aggregated', n.get_enum_value(risk_level.RiskLevel)),
            "risk_level_during_sign_in": lambda n : setattr(self, 'risk_level_during_sign_in', n.get_enum_value(risk_level.RiskLevel)),
            "risk_state": lambda n : setattr(self, 'risk_state', n.get_enum_value(risk_state.RiskState)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(sign_in_status.SignInStatus)),
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
        Gets the ipAddress property value. IP address of the client used to sign in. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IP address of the client used to sign in. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def is_interactive(self,) -> Optional[bool]:
        """
        Gets the isInteractive property value. Indicates if a sign-in is interactive or not.
        Returns: Optional[bool]
        """
        return self._is_interactive
    
    @is_interactive.setter
    def is_interactive(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInteractive property value. Indicates if a sign-in is interactive or not.
        Args:
            value: Value to set for the isInteractive property.
        """
        self._is_interactive = value
    
    @property
    def location(self,) -> Optional[sign_in_location.SignInLocation]:
        """
        Gets the location property value. Provides the city, state, and country code where the sign-in originated. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
        Returns: Optional[sign_in_location.SignInLocation]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[sign_in_location.SignInLocation] = None) -> None:
        """
        Sets the location property value. Provides the city, state, and country code where the sign-in originated. Supports $filter (eq and startsWith operators only) on city, state, and countryOrRegion properties.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def resource_display_name(self,) -> Optional[str]:
        """
        Gets the resourceDisplayName property value. Name of the resource the user signed into. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._resource_display_name
    
    @resource_display_name.setter
    def resource_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceDisplayName property value. Name of the resource the user signed into. Supports $filter (eq operator only).
        Args:
            value: Value to set for the resourceDisplayName property.
        """
        self._resource_display_name = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. ID of the resource that the user signed into. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. ID of the resource that the user signed into. Supports $filter (eq operator only).
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    @property
    def risk_detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the riskDetail property value. Provides the 'reason' behind a specific state of a risky user, sign-in or a risk event. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far.  Supports $filter (eq operator only).Note: Details for this property require an Azure AD Premium P2 license. Other licenses return the value hidden.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._risk_detail
    
    @risk_detail.setter
    def risk_detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the riskDetail property value. Provides the 'reason' behind a specific state of a risky user, sign-in or a risk event. The possible values are: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, unknownFutureValue. The value none means that no action has been performed on the user or sign-in so far.  Supports $filter (eq operator only).Note: Details for this property require an Azure AD Premium P2 license. Other licenses return the value hidden.
        Args:
            value: Value to set for the riskDetail property.
        """
        self._risk_detail = value
    
    @property
    def risk_event_types(self,) -> Optional[List[risk_event_type.RiskEventType]]:
        """
        Gets the riskEventTypes property value. Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue. Supports $filter (eq operator only).
        Returns: Optional[List[risk_event_type.RiskEventType]]
        """
        return self._risk_event_types
    
    @risk_event_types.setter
    def risk_event_types(self,value: Optional[List[risk_event_type.RiskEventType]] = None) -> None:
        """
        Sets the riskEventTypes property value. Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue. Supports $filter (eq operator only).
        Args:
            value: Value to set for the riskEventTypes property.
        """
        self._risk_event_types = value
    
    @property
    def risk_event_types_v2(self,) -> Optional[List[str]]:
        """
        Gets the riskEventTypes_v2 property value. The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
        Returns: Optional[List[str]]
        """
        return self._risk_event_types_v2
    
    @risk_event_types_v2.setter
    def risk_event_types_v2(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the riskEventTypes_v2 property value. The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the riskEventTypes_v2 property.
        """
        self._risk_event_types_v2 = value
    
    @property
    def risk_level_aggregated(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevelAggregated property value. Aggregated risk level. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only).  Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level_aggregated
    
    @risk_level_aggregated.setter
    def risk_level_aggregated(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevelAggregated property value. Aggregated risk level. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Supports $filter (eq operator only).  Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
        Args:
            value: Value to set for the riskLevelAggregated property.
        """
        self._risk_level_aggregated = value
    
    @property
    def risk_level_during_sign_in(self,) -> Optional[risk_level.RiskLevel]:
        """
        Gets the riskLevelDuringSignIn property value. Risk level during sign-in. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection.  Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
        Returns: Optional[risk_level.RiskLevel]
        """
        return self._risk_level_during_sign_in
    
    @risk_level_during_sign_in.setter
    def risk_level_during_sign_in(self,value: Optional[risk_level.RiskLevel] = None) -> None:
        """
        Sets the riskLevelDuringSignIn property value. Risk level during sign-in. The possible values are: none, low, medium, high, hidden, and unknownFutureValue. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection.  Supports $filter (eq operator only). Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers will be returned hidden.
        Args:
            value: Value to set for the riskLevelDuringSignIn property.
        """
        self._risk_level_during_sign_in = value
    
    @property
    def risk_state(self,) -> Optional[risk_state.RiskState]:
        """
        Gets the riskState property value. Reports status of the risky user, sign-in, or a risk event. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue. Supports $filter (eq operator only).
        Returns: Optional[risk_state.RiskState]
        """
        return self._risk_state
    
    @risk_state.setter
    def risk_state(self,value: Optional[risk_state.RiskState] = None) -> None:
        """
        Sets the riskState property value. Reports status of the risky user, sign-in, or a risk event. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue. Supports $filter (eq operator only).
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appliedConditionalAccessPolicies", self.applied_conditional_access_policies)
        writer.write_str_value("clientAppUsed", self.client_app_used)
        writer.write_enum_value("conditionalAccessStatus", self.conditional_access_status)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("deviceDetail", self.device_detail)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isInteractive", self.is_interactive)
        writer.write_object_value("location", self.location)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_enum_value("riskDetail", self.risk_detail)
        writer.write_enum_value("riskEventTypes", self.risk_event_types)
        writer.write_collection_of_primitive_values("riskEventTypes_v2", self.risk_event_types_v2)
        writer.write_enum_value("riskLevelAggregated", self.risk_level_aggregated)
        writer.write_enum_value("riskLevelDuringSignIn", self.risk_level_during_sign_in)
        writer.write_enum_value("riskState", self.risk_state)
        writer.write_object_value("status", self.status)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def status(self,) -> Optional[sign_in_status.SignInStatus]:
        """
        Gets the status property value. Sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
        Returns: Optional[sign_in_status.SignInStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[sign_in_status.SignInStatus] = None) -> None:
        """
        Sets the status property value. Sign-in status. Includes the error code and description of the error (in case of a sign-in failure). Supports $filter (eq operator only) on errorCode property.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Display name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Display name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. ID of the user that initiated the sign-in. Supports $filter (eq operator only).
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. ID of the user that initiated the sign-in. Supports $filter (eq operator only).
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principal name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principal name of the user that initiated the sign-in. Supports $filter (eq and startsWith operators only).
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

