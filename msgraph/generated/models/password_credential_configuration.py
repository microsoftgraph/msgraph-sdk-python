from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_credential_restriction_type

class PasswordCredentialConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new passwordCredentialConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The maxLifetime property
        self._max_lifetime: Optional[Timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Enforces the policy for an app created on or after the enforcement date. For existing applications, the enforcement date would be back dated. To apply to all applications, enforcement datetime would be null.
        self._restrict_for_apps_created_after_date_time: Optional[datetime] = None
        # The type of restriction being applied. The possible values are: passwordAddition, passwordLifetime, symmetricKeyAddition, symmetricKeyLifetime,customPasswordAddition, unknownFutureValue. Each value of restrictionType can be used only once per policy.
        self._restriction_type: Optional[app_credential_restriction_type.AppCredentialRestrictionType] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PasswordCredentialConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PasswordCredentialConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PasswordCredentialConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_credential_restriction_type

        fields: Dict[str, Callable[[Any], None]] = {
            "maxLifetime": lambda n : setattr(self, 'max_lifetime', n.get_object_value(Timedelta)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictionType": lambda n : setattr(self, 'restriction_type', n.get_enum_value(app_credential_restriction_type.AppCredentialRestrictionType)),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def max_lifetime(self,) -> Optional[Timedelta]:
        """
        Gets the maxLifetime property value. The maxLifetime property
        Returns: Optional[Timedelta]
        """
        return self._max_lifetime
    
    @max_lifetime.setter
    def max_lifetime(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maxLifetime property value. The maxLifetime property
        Args:
            value: Value to set for the max_lifetime property.
        """
        self._max_lifetime = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def restrict_for_apps_created_after_date_time(self,) -> Optional[datetime]:
        """
        Gets the restrictForAppsCreatedAfterDateTime property value. Enforces the policy for an app created on or after the enforcement date. For existing applications, the enforcement date would be back dated. To apply to all applications, enforcement datetime would be null.
        Returns: Optional[datetime]
        """
        return self._restrict_for_apps_created_after_date_time
    
    @restrict_for_apps_created_after_date_time.setter
    def restrict_for_apps_created_after_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the restrictForAppsCreatedAfterDateTime property value. Enforces the policy for an app created on or after the enforcement date. For existing applications, the enforcement date would be back dated. To apply to all applications, enforcement datetime would be null.
        Args:
            value: Value to set for the restrict_for_apps_created_after_date_time property.
        """
        self._restrict_for_apps_created_after_date_time = value
    
    @property
    def restriction_type(self,) -> Optional[app_credential_restriction_type.AppCredentialRestrictionType]:
        """
        Gets the restrictionType property value. The type of restriction being applied. The possible values are: passwordAddition, passwordLifetime, symmetricKeyAddition, symmetricKeyLifetime,customPasswordAddition, unknownFutureValue. Each value of restrictionType can be used only once per policy.
        Returns: Optional[app_credential_restriction_type.AppCredentialRestrictionType]
        """
        return self._restriction_type
    
    @restriction_type.setter
    def restriction_type(self,value: Optional[app_credential_restriction_type.AppCredentialRestrictionType] = None) -> None:
        """
        Sets the restrictionType property value. The type of restriction being applied. The possible values are: passwordAddition, passwordLifetime, symmetricKeyAddition, symmetricKeyLifetime,customPasswordAddition, unknownFutureValue. Each value of restrictionType can be used only once per policy.
        Args:
            value: Value to set for the restriction_type property.
        """
        self._restriction_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("maxLifetime", self.max_lifetime)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("restrictionType", self.restriction_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_additional_data_value(self.additional_data)
    

