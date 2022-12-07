from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

pstn_call_duration_source = lazy_import('msgraph.generated.models.call_records.pstn_call_duration_source')

class PstnCallLogRow(AdditionalDataHolder, Parsable):
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
    def call_duration_source(self,) -> Optional[pstn_call_duration_source.PstnCallDurationSource]:
        """
        Gets the callDurationSource property value. The source of the call duration data. If the call uses a third-party telecommunications operator via the Operator Connect Program, the operator may provide their own call duration data. In this case, the property value is operator. Otherwise, the value is microsoft.
        Returns: Optional[pstn_call_duration_source.PstnCallDurationSource]
        """
        return self._call_duration_source
    
    @call_duration_source.setter
    def call_duration_source(self,value: Optional[pstn_call_duration_source.PstnCallDurationSource] = None) -> None:
        """
        Sets the callDurationSource property value. The source of the call duration data. If the call uses a third-party telecommunications operator via the Operator Connect Program, the operator may provide their own call duration data. In this case, the property value is operator. Otherwise, the value is microsoft.
        Args:
            value: Value to set for the callDurationSource property.
        """
        self._call_duration_source = value
    
    @property
    def callee_number(self,) -> Optional[str]:
        """
        Gets the calleeNumber property value. Number dialed in E.164 format.
        Returns: Optional[str]
        """
        return self._callee_number
    
    @callee_number.setter
    def callee_number(self,value: Optional[str] = None) -> None:
        """
        Sets the calleeNumber property value. Number dialed in E.164 format.
        Args:
            value: Value to set for the calleeNumber property.
        """
        self._callee_number = value
    
    @property
    def caller_number(self,) -> Optional[str]:
        """
        Gets the callerNumber property value. Number that received the call for inbound calls or the number dialed for outbound calls. E.164 format.
        Returns: Optional[str]
        """
        return self._caller_number
    
    @caller_number.setter
    def caller_number(self,value: Optional[str] = None) -> None:
        """
        Sets the callerNumber property value. Number that received the call for inbound calls or the number dialed for outbound calls. E.164 format.
        Args:
            value: Value to set for the callerNumber property.
        """
        self._caller_number = value
    
    @property
    def call_id(self,) -> Optional[str]:
        """
        Gets the callId property value. Call identifier. Not guaranteed to be unique.
        Returns: Optional[str]
        """
        return self._call_id
    
    @call_id.setter
    def call_id(self,value: Optional[str] = None) -> None:
        """
        Sets the callId property value. Call identifier. Not guaranteed to be unique.
        Args:
            value: Value to set for the callId property.
        """
        self._call_id = value
    
    @property
    def call_type(self,) -> Optional[str]:
        """
        Gets the callType property value. Whether the call was a PSTN outbound or inbound call and the type of call such as a call placed by a user or an audio conference.
        Returns: Optional[str]
        """
        return self._call_type
    
    @call_type.setter
    def call_type(self,value: Optional[str] = None) -> None:
        """
        Sets the callType property value. Whether the call was a PSTN outbound or inbound call and the type of call such as a call placed by a user or an audio conference.
        Args:
            value: Value to set for the callType property.
        """
        self._call_type = value
    
    @property
    def charge(self,) -> Optional[float]:
        """
        Gets the charge property value. Amount of money or cost of the call that is charged to your account.
        Returns: Optional[float]
        """
        return self._charge
    
    @charge.setter
    def charge(self,value: Optional[float] = None) -> None:
        """
        Sets the charge property value. Amount of money or cost of the call that is charged to your account.
        Args:
            value: Value to set for the charge property.
        """
        self._charge = value
    
    @property
    def conference_id(self,) -> Optional[str]:
        """
        Gets the conferenceId property value. ID of the audio conference.
        Returns: Optional[str]
        """
        return self._conference_id
    
    @conference_id.setter
    def conference_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conferenceId property value. ID of the audio conference.
        Args:
            value: Value to set for the conferenceId property.
        """
        self._conference_id = value
    
    @property
    def connection_charge(self,) -> Optional[float]:
        """
        Gets the connectionCharge property value. Connection fee price.
        Returns: Optional[float]
        """
        return self._connection_charge
    
    @connection_charge.setter
    def connection_charge(self,value: Optional[float] = None) -> None:
        """
        Sets the connectionCharge property value. Connection fee price.
        Args:
            value: Value to set for the connectionCharge property.
        """
        self._connection_charge = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new pstnCallLogRow and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The source of the call duration data. If the call uses a third-party telecommunications operator via the Operator Connect Program, the operator may provide their own call duration data. In this case, the property value is operator. Otherwise, the value is microsoft.
        self._call_duration_source: Optional[pstn_call_duration_source.PstnCallDurationSource] = None
        # Number dialed in E.164 format.
        self._callee_number: Optional[str] = None
        # Number that received the call for inbound calls or the number dialed for outbound calls. E.164 format.
        self._caller_number: Optional[str] = None
        # Call identifier. Not guaranteed to be unique.
        self._call_id: Optional[str] = None
        # Whether the call was a PSTN outbound or inbound call and the type of call such as a call placed by a user or an audio conference.
        self._call_type: Optional[str] = None
        # Amount of money or cost of the call that is charged to your account.
        self._charge: Optional[float] = None
        # ID of the audio conference.
        self._conference_id: Optional[str] = None
        # Connection fee price.
        self._connection_charge: Optional[float] = None
        # Type of currency used to calculate the cost of the call (ISO 4217).
        self._currency: Optional[str] = None
        # Whether the call was domestic (within a country or region) or international (outside a country or region) based on the user's location.
        self._destination_context: Optional[str] = None
        # Country or region dialed.
        self._destination_name: Optional[str] = None
        # How long the call was connected, in seconds.
        self._duration: Optional[int] = None
        # Call end time.
        self._end_date_time: Optional[datetime] = None
        # Unique call identifier. GUID.
        self._id: Optional[str] = None
        # User's phone number type, such as a service of toll-free number.
        self._inventory_type: Optional[str] = None
        # The license used for the call.
        self._license_capability: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The telecommunications operator which provided PSTN services for this call. This may be Microsoft, or it may be a third-party operator via the Operator Connect Program.
        self._operator: Optional[str] = None
        # Call start time.
        self._start_date_time: Optional[datetime] = None
        # Country code of the tenant, ISO 3166-1 alpha-2.
        self._tenant_country_code: Optional[str] = None
        # Country code of the user, ISO 3166-1 alpha-2.
        self._usage_country_code: Optional[str] = None
        # Display name of the user.
        self._user_display_name: Optional[str] = None
        # Calling user's ID in Graph. GUID. This and other user info will be null/empty for bot call types (ucap_in, ucap_out).
        self._user_id: Optional[str] = None
        # UserPrincipalName (sign-in name) in Azure Active Directory. This is usually the same as user's SIP Address, and can be same as user's e-mail address.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PstnCallLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PstnCallLogRow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PstnCallLogRow()
    
    @property
    def currency(self,) -> Optional[str]:
        """
        Gets the currency property value. Type of currency used to calculate the cost of the call (ISO 4217).
        Returns: Optional[str]
        """
        return self._currency
    
    @currency.setter
    def currency(self,value: Optional[str] = None) -> None:
        """
        Sets the currency property value. Type of currency used to calculate the cost of the call (ISO 4217).
        Args:
            value: Value to set for the currency property.
        """
        self._currency = value
    
    @property
    def destination_context(self,) -> Optional[str]:
        """
        Gets the destinationContext property value. Whether the call was domestic (within a country or region) or international (outside a country or region) based on the user's location.
        Returns: Optional[str]
        """
        return self._destination_context
    
    @destination_context.setter
    def destination_context(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationContext property value. Whether the call was domestic (within a country or region) or international (outside a country or region) based on the user's location.
        Args:
            value: Value to set for the destinationContext property.
        """
        self._destination_context = value
    
    @property
    def destination_name(self,) -> Optional[str]:
        """
        Gets the destinationName property value. Country or region dialed.
        Returns: Optional[str]
        """
        return self._destination_name
    
    @destination_name.setter
    def destination_name(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationName property value. Country or region dialed.
        Args:
            value: Value to set for the destinationName property.
        """
        self._destination_name = value
    
    @property
    def duration(self,) -> Optional[int]:
        """
        Gets the duration property value. How long the call was connected, in seconds.
        Returns: Optional[int]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[int] = None) -> None:
        """
        Sets the duration property value. How long the call was connected, in seconds.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. Call end time.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. Call end time.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "call_duration_source": lambda n : setattr(self, 'call_duration_source', n.get_enum_value(pstn_call_duration_source.PstnCallDurationSource)),
            "callee_number": lambda n : setattr(self, 'callee_number', n.get_str_value()),
            "caller_number": lambda n : setattr(self, 'caller_number', n.get_str_value()),
            "call_id": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "call_type": lambda n : setattr(self, 'call_type', n.get_str_value()),
            "charge": lambda n : setattr(self, 'charge', n.get_float_value()),
            "conference_id": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "connection_charge": lambda n : setattr(self, 'connection_charge', n.get_float_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "destination_context": lambda n : setattr(self, 'destination_context', n.get_str_value()),
            "destination_name": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "inventory_type": lambda n : setattr(self, 'inventory_type', n.get_str_value()),
            "license_capability": lambda n : setattr(self, 'license_capability', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "tenant_country_code": lambda n : setattr(self, 'tenant_country_code', n.get_str_value()),
            "usage_country_code": lambda n : setattr(self, 'usage_country_code', n.get_str_value()),
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
    def inventory_type(self,) -> Optional[str]:
        """
        Gets the inventoryType property value. User's phone number type, such as a service of toll-free number.
        Returns: Optional[str]
        """
        return self._inventory_type
    
    @inventory_type.setter
    def inventory_type(self,value: Optional[str] = None) -> None:
        """
        Sets the inventoryType property value. User's phone number type, such as a service of toll-free number.
        Args:
            value: Value to set for the inventoryType property.
        """
        self._inventory_type = value
    
    @property
    def license_capability(self,) -> Optional[str]:
        """
        Gets the licenseCapability property value. The license used for the call.
        Returns: Optional[str]
        """
        return self._license_capability
    
    @license_capability.setter
    def license_capability(self,value: Optional[str] = None) -> None:
        """
        Sets the licenseCapability property value. The license used for the call.
        Args:
            value: Value to set for the licenseCapability property.
        """
        self._license_capability = value
    
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
    
    @property
    def operator(self,) -> Optional[str]:
        """
        Gets the operator property value. The telecommunications operator which provided PSTN services for this call. This may be Microsoft, or it may be a third-party operator via the Operator Connect Program.
        Returns: Optional[str]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[str] = None) -> None:
        """
        Sets the operator property value. The telecommunications operator which provided PSTN services for this call. This may be Microsoft, or it may be a third-party operator via the Operator Connect Program.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("callDurationSource", self.call_duration_source)
        writer.write_str_value("calleeNumber", self.callee_number)
        writer.write_str_value("callerNumber", self.caller_number)
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callType", self.call_type)
        writer.write_float_value("charge", self.charge)
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_float_value("connectionCharge", self.connection_charge)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_int_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("inventoryType", self.inventory_type)
        writer.write_str_value("licenseCapability", self.license_capability)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("tenantCountryCode", self.tenant_country_code)
        writer.write_str_value("usageCountryCode", self.usage_country_code)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Call start time.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Call start time.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def tenant_country_code(self,) -> Optional[str]:
        """
        Gets the tenantCountryCode property value. Country code of the tenant, ISO 3166-1 alpha-2.
        Returns: Optional[str]
        """
        return self._tenant_country_code
    
    @tenant_country_code.setter
    def tenant_country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantCountryCode property value. Country code of the tenant, ISO 3166-1 alpha-2.
        Args:
            value: Value to set for the tenantCountryCode property.
        """
        self._tenant_country_code = value
    
    @property
    def usage_country_code(self,) -> Optional[str]:
        """
        Gets the usageCountryCode property value. Country code of the user, ISO 3166-1 alpha-2.
        Returns: Optional[str]
        """
        return self._usage_country_code
    
    @usage_country_code.setter
    def usage_country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the usageCountryCode property value. Country code of the user, ISO 3166-1 alpha-2.
        Args:
            value: Value to set for the usageCountryCode property.
        """
        self._usage_country_code = value
    
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
        Gets the userId property value. Calling user's ID in Graph. GUID. This and other user info will be null/empty for bot call types (ucap_in, ucap_out).
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Calling user's ID in Graph. GUID. This and other user info will be null/empty for bot call types (ucap_in, ucap_out).
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
    

