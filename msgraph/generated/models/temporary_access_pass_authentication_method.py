from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method = lazy_import('msgraph.generated.models.authentication_method')

class TemporaryAccessPassAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new TemporaryAccessPassAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.temporaryAccessPassAuthenticationMethod"
        # The date and time when the Temporary Access Pass was created.
        self._created_date_time: Optional[datetime] = None
        # The state of the authentication method that indicates whether it's currently usable by the user.
        self._is_usable: Optional[bool] = None
        # Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
        self._is_usable_once: Optional[bool] = None
        # The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
        self._lifetime_in_minutes: Optional[int] = None
        # Details about the usability state (isUsable). Reasons can include: EnabledByPolicy, DisabledByPolicy, Expired, NotYetValid, OneTimeUsed.
        self._method_usability_reason: Optional[str] = None
        # The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
        self._start_date_time: Optional[datetime] = None
        # The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
        self._temporary_access_pass: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the Temporary Access Pass was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the Temporary Access Pass was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TemporaryAccessPassAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TemporaryAccessPassAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TemporaryAccessPassAuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "is_usable": lambda n : setattr(self, 'is_usable', n.get_bool_value()),
            "is_usable_once": lambda n : setattr(self, 'is_usable_once', n.get_bool_value()),
            "lifetime_in_minutes": lambda n : setattr(self, 'lifetime_in_minutes', n.get_int_value()),
            "method_usability_reason": lambda n : setattr(self, 'method_usability_reason', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "temporary_access_pass": lambda n : setattr(self, 'temporary_access_pass', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_usable(self,) -> Optional[bool]:
        """
        Gets the isUsable property value. The state of the authentication method that indicates whether it's currently usable by the user.
        Returns: Optional[bool]
        """
        return self._is_usable
    
    @is_usable.setter
    def is_usable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUsable property value. The state of the authentication method that indicates whether it's currently usable by the user.
        Args:
            value: Value to set for the isUsable property.
        """
        self._is_usable = value
    
    @property
    def is_usable_once(self,) -> Optional[bool]:
        """
        Gets the isUsableOnce property value. Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
        Returns: Optional[bool]
        """
        return self._is_usable_once
    
    @is_usable_once.setter
    def is_usable_once(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUsableOnce property value. Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
        Args:
            value: Value to set for the isUsableOnce property.
        """
        self._is_usable_once = value
    
    @property
    def lifetime_in_minutes(self,) -> Optional[int]:
        """
        Gets the lifetimeInMinutes property value. The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
        Returns: Optional[int]
        """
        return self._lifetime_in_minutes
    
    @lifetime_in_minutes.setter
    def lifetime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the lifetimeInMinutes property value. The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
        Args:
            value: Value to set for the lifetimeInMinutes property.
        """
        self._lifetime_in_minutes = value
    
    @property
    def method_usability_reason(self,) -> Optional[str]:
        """
        Gets the methodUsabilityReason property value. Details about the usability state (isUsable). Reasons can include: EnabledByPolicy, DisabledByPolicy, Expired, NotYetValid, OneTimeUsed.
        Returns: Optional[str]
        """
        return self._method_usability_reason
    
    @method_usability_reason.setter
    def method_usability_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the methodUsabilityReason property value. Details about the usability state (isUsable). Reasons can include: EnabledByPolicy, DisabledByPolicy, Expired, NotYetValid, OneTimeUsed.
        Args:
            value: Value to set for the methodUsabilityReason property.
        """
        self._method_usability_reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isUsable", self.is_usable)
        writer.write_bool_value("isUsableOnce", self.is_usable_once)
        writer.write_int_value("lifetimeInMinutes", self.lifetime_in_minutes)
        writer.write_str_value("methodUsabilityReason", self.method_usability_reason)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("temporaryAccessPass", self.temporary_access_pass)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def temporary_access_pass(self,) -> Optional[str]:
        """
        Gets the temporaryAccessPass property value. The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
        Returns: Optional[str]
        """
        return self._temporary_access_pass
    
    @temporary_access_pass.setter
    def temporary_access_pass(self,value: Optional[str] = None) -> None:
        """
        Sets the temporaryAccessPass property value. The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
        Args:
            value: Value to set for the temporaryAccessPass property.
        """
        self._temporary_access_pass = value
    

