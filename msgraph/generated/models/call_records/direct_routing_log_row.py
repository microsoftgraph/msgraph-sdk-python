from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DirectRoutingLogRow(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def callee_number(self,) -> Optional[str]:
        """
        Gets the calleeNumber property value. Number of the user or bot who received the call. E.164 format, but may include additional data.
        Returns: Optional[str]
        """
        return self._callee_number
    
    @callee_number.setter
    def callee_number(self,value: Optional[str] = None) -> None:
        """
        Sets the calleeNumber property value. Number of the user or bot who received the call. E.164 format, but may include additional data.
        Args:
            value: Value to set for the calleeNumber property.
        """
        self._callee_number = value
    
    @property
    def call_end_sub_reason(self,) -> Optional[int]:
        """
        Gets the callEndSubReason property value. In addition to the SIP codes, Microsoft has own subcodes that indicate the specific issue.
        Returns: Optional[int]
        """
        return self._call_end_sub_reason
    
    @call_end_sub_reason.setter
    def call_end_sub_reason(self,value: Optional[int] = None) -> None:
        """
        Sets the callEndSubReason property value. In addition to the SIP codes, Microsoft has own subcodes that indicate the specific issue.
        Args:
            value: Value to set for the callEndSubReason property.
        """
        self._call_end_sub_reason = value
    
    @property
    def caller_number(self,) -> Optional[str]:
        """
        Gets the callerNumber property value. Number of the user or bot who made the call. E.164 format, but may include additional data.
        Returns: Optional[str]
        """
        return self._caller_number
    
    @caller_number.setter
    def caller_number(self,value: Optional[str] = None) -> None:
        """
        Sets the callerNumber property value. Number of the user or bot who made the call. E.164 format, but may include additional data.
        Args:
            value: Value to set for the callerNumber property.
        """
        self._caller_number = value
    
    @property
    def call_type(self,) -> Optional[str]:
        """
        Gets the callType property value. Call type and direction.
        Returns: Optional[str]
        """
        return self._call_type
    
    @call_type.setter
    def call_type(self,value: Optional[str] = None) -> None:
        """
        Sets the callType property value. Call type and direction.
        Args:
            value: Value to set for the callType property.
        """
        self._call_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new directRoutingLogRow and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of the user or bot who received the call. E.164 format, but may include additional data.
        self._callee_number: Optional[str] = None
        # In addition to the SIP codes, Microsoft has own subcodes that indicate the specific issue.
        self._call_end_sub_reason: Optional[int] = None
        # Number of the user or bot who made the call. E.164 format, but may include additional data.
        self._caller_number: Optional[str] = None
        # Call type and direction.
        self._call_type: Optional[str] = None
        # Identifier for the call that you can use when calling Microsoft Support. GUID.
        self._correlation_id: Optional[str] = None
        # Duration of the call in seconds.
        self._duration: Optional[int] = None
        # Only exists for successful (fully established) calls. Time when call ended.
        self._end_date_time: Optional[datetime] = None
        # Only exists for failed (not fully established) calls.
        self._failure_date_time: Optional[datetime] = None
        # The code with which the call ended, RFC 3261.
        self._final_sip_code: Optional[int] = None
        # Description of the SIP code and Microsoft subcode.
        self._final_sip_code_phrase: Optional[str] = None
        # Unique call identifier. GUID.
        self._id: Optional[str] = None
        # When the initial invite was sent.
        self._invite_date_time: Optional[datetime] = None
        # Indicates if the trunk was enabled for media bypass or not.
        self._media_bypass_enabled: Optional[bool] = None
        # The datacenter used for media path in non-bypass call.
        self._media_path_location: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The datacenter used for signaling for both bypass and non-bypass calls.
        self._signaling_location: Optional[str] = None
        # Call start time.For failed and unanswered calls, this can be equal to invite or failure time.
        self._start_date_time: Optional[datetime] = None
        # Success or attempt.
        self._successful_call: Optional[bool] = None
        # Fully qualified domain name of the session border controller.
        self._trunk_fully_qualified_domain_name: Optional[str] = None
        # Display name of the user.
        self._user_display_name: Optional[str] = None
        # Calling user's ID in Graph. This and other user info will be null/empty for bot call types. GUID.
        self._user_id: Optional[str] = None
        # UserPrincipalName (sign-in name) in Azure Active Directory. This is usually the same as user's SIP Address, and can be same as user's e-mail address.
        self._user_principal_name: Optional[str] = None
    
    @property
    def correlation_id(self,) -> Optional[str]:
        """
        Gets the correlationId property value. Identifier for the call that you can use when calling Microsoft Support. GUID.
        Returns: Optional[str]
        """
        return self._correlation_id
    
    @correlation_id.setter
    def correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the correlationId property value. Identifier for the call that you can use when calling Microsoft Support. GUID.
        Args:
            value: Value to set for the correlationId property.
        """
        self._correlation_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectRoutingLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectRoutingLogRow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectRoutingLogRow()
    
    @property
    def duration(self,) -> Optional[int]:
        """
        Gets the duration property value. Duration of the call in seconds.
        Returns: Optional[int]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[int] = None) -> None:
        """
        Sets the duration property value. Duration of the call in seconds.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. Only exists for successful (fully established) calls. Time when call ended.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. Only exists for successful (fully established) calls. Time when call ended.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def failure_date_time(self,) -> Optional[datetime]:
        """
        Gets the failureDateTime property value. Only exists for failed (not fully established) calls.
        Returns: Optional[datetime]
        """
        return self._failure_date_time
    
    @failure_date_time.setter
    def failure_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the failureDateTime property value. Only exists for failed (not fully established) calls.
        Args:
            value: Value to set for the failureDateTime property.
        """
        self._failure_date_time = value
    
    @property
    def final_sip_code(self,) -> Optional[int]:
        """
        Gets the finalSipCode property value. The code with which the call ended, RFC 3261.
        Returns: Optional[int]
        """
        return self._final_sip_code
    
    @final_sip_code.setter
    def final_sip_code(self,value: Optional[int] = None) -> None:
        """
        Sets the finalSipCode property value. The code with which the call ended, RFC 3261.
        Args:
            value: Value to set for the finalSipCode property.
        """
        self._final_sip_code = value
    
    @property
    def final_sip_code_phrase(self,) -> Optional[str]:
        """
        Gets the finalSipCodePhrase property value. Description of the SIP code and Microsoft subcode.
        Returns: Optional[str]
        """
        return self._final_sip_code_phrase
    
    @final_sip_code_phrase.setter
    def final_sip_code_phrase(self,value: Optional[str] = None) -> None:
        """
        Sets the finalSipCodePhrase property value. Description of the SIP code and Microsoft subcode.
        Args:
            value: Value to set for the finalSipCodePhrase property.
        """
        self._final_sip_code_phrase = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "callee_number": lambda n : setattr(self, 'callee_number', n.get_str_value()),
            "call_end_sub_reason": lambda n : setattr(self, 'call_end_sub_reason', n.get_int_value()),
            "caller_number": lambda n : setattr(self, 'caller_number', n.get_str_value()),
            "call_type": lambda n : setattr(self, 'call_type', n.get_str_value()),
            "correlation_id": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "failure_date_time": lambda n : setattr(self, 'failure_date_time', n.get_datetime_value()),
            "final_sip_code": lambda n : setattr(self, 'final_sip_code', n.get_int_value()),
            "final_sip_code_phrase": lambda n : setattr(self, 'final_sip_code_phrase', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "invite_date_time": lambda n : setattr(self, 'invite_date_time', n.get_datetime_value()),
            "media_bypass_enabled": lambda n : setattr(self, 'media_bypass_enabled', n.get_bool_value()),
            "media_path_location": lambda n : setattr(self, 'media_path_location', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "signaling_location": lambda n : setattr(self, 'signaling_location', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "successful_call": lambda n : setattr(self, 'successful_call', n.get_bool_value()),
            "trunk_fully_qualified_domain_name": lambda n : setattr(self, 'trunk_fully_qualified_domain_name', n.get_str_value()),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique call identifier. GUID.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique call identifier. GUID.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def invite_date_time(self,) -> Optional[datetime]:
        """
        Gets the inviteDateTime property value. When the initial invite was sent.
        Returns: Optional[datetime]
        """
        return self._invite_date_time
    
    @invite_date_time.setter
    def invite_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the inviteDateTime property value. When the initial invite was sent.
        Args:
            value: Value to set for the inviteDateTime property.
        """
        self._invite_date_time = value
    
    @property
    def media_bypass_enabled(self,) -> Optional[bool]:
        """
        Gets the mediaBypassEnabled property value. Indicates if the trunk was enabled for media bypass or not.
        Returns: Optional[bool]
        """
        return self._media_bypass_enabled
    
    @media_bypass_enabled.setter
    def media_bypass_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the mediaBypassEnabled property value. Indicates if the trunk was enabled for media bypass or not.
        Args:
            value: Value to set for the mediaBypassEnabled property.
        """
        self._media_bypass_enabled = value
    
    @property
    def media_path_location(self,) -> Optional[str]:
        """
        Gets the mediaPathLocation property value. The datacenter used for media path in non-bypass call.
        Returns: Optional[str]
        """
        return self._media_path_location
    
    @media_path_location.setter
    def media_path_location(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaPathLocation property value. The datacenter used for media path in non-bypass call.
        Args:
            value: Value to set for the mediaPathLocation property.
        """
        self._media_path_location = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("calleeNumber", self.callee_number)
        writer.write_int_value("callEndSubReason", self.call_end_sub_reason)
        writer.write_str_value("callerNumber", self.caller_number)
        writer.write_str_value("callType", self.call_type)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_int_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("failureDateTime", self.failure_date_time)
        writer.write_int_value("finalSipCode", self.final_sip_code)
        writer.write_str_value("finalSipCodePhrase", self.final_sip_code_phrase)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("inviteDateTime", self.invite_date_time)
        writer.write_bool_value("mediaBypassEnabled", self.media_bypass_enabled)
        writer.write_str_value("mediaPathLocation", self.media_path_location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("signalingLocation", self.signaling_location)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_bool_value("successfulCall", self.successful_call)
        writer.write_str_value("trunkFullyQualifiedDomainName", self.trunk_fully_qualified_domain_name)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def signaling_location(self,) -> Optional[str]:
        """
        Gets the signalingLocation property value. The datacenter used for signaling for both bypass and non-bypass calls.
        Returns: Optional[str]
        """
        return self._signaling_location
    
    @signaling_location.setter
    def signaling_location(self,value: Optional[str] = None) -> None:
        """
        Sets the signalingLocation property value. The datacenter used for signaling for both bypass and non-bypass calls.
        Args:
            value: Value to set for the signalingLocation property.
        """
        self._signaling_location = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Call start time.For failed and unanswered calls, this can be equal to invite or failure time.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Call start time.For failed and unanswered calls, this can be equal to invite or failure time.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def successful_call(self,) -> Optional[bool]:
        """
        Gets the successfulCall property value. Success or attempt.
        Returns: Optional[bool]
        """
        return self._successful_call
    
    @successful_call.setter
    def successful_call(self,value: Optional[bool] = None) -> None:
        """
        Sets the successfulCall property value. Success or attempt.
        Args:
            value: Value to set for the successfulCall property.
        """
        self._successful_call = value
    
    @property
    def trunk_fully_qualified_domain_name(self,) -> Optional[str]:
        """
        Gets the trunkFullyQualifiedDomainName property value. Fully qualified domain name of the session border controller.
        Returns: Optional[str]
        """
        return self._trunk_fully_qualified_domain_name
    
    @trunk_fully_qualified_domain_name.setter
    def trunk_fully_qualified_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the trunkFullyQualifiedDomainName property value. Fully qualified domain name of the session border controller.
        Args:
            value: Value to set for the trunkFullyQualifiedDomainName property.
        """
        self._trunk_fully_qualified_domain_name = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Display name of the user.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Display name of the user.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Calling user's ID in Graph. This and other user info will be null/empty for bot call types. GUID.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Calling user's ID in Graph. This and other user info will be null/empty for bot call types. GUID.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. UserPrincipalName (sign-in name) in Azure Active Directory. This is usually the same as user's SIP Address, and can be same as user's e-mail address.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. UserPrincipalName (sign-in name) in Azure Active Directory. This is usually the same as user's SIP Address, and can be same as user's e-mail address.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

