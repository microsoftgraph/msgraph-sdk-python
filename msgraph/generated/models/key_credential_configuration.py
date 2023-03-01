from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_key_credential_restriction_type = lazy_import('msgraph.generated.models.app_key_credential_restriction_type')

class KeyCredentialConfiguration(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new keyCredentialConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The maxLifetime property
        self._max_lifetime: Optional[Timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The restrictForAppsCreatedAfterDateTime property
        self._restrict_for_apps_created_after_date_time: Optional[datetime] = None
        # The restrictionType property
        self._restriction_type: Optional[app_key_credential_restriction_type.AppKeyCredentialRestrictionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KeyCredentialConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: KeyCredentialConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return KeyCredentialConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "maxLifetime": lambda n : setattr(self, 'max_lifetime', n.get_object_value(Timedelta)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictionType": lambda n : setattr(self, 'restriction_type', n.get_enum_value(app_key_credential_restriction_type.AppKeyCredentialRestrictionType)),
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
        Gets the restrictForAppsCreatedAfterDateTime property value. The restrictForAppsCreatedAfterDateTime property
        Returns: Optional[datetime]
        """
        return self._restrict_for_apps_created_after_date_time
    
    @restrict_for_apps_created_after_date_time.setter
    def restrict_for_apps_created_after_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the restrictForAppsCreatedAfterDateTime property value. The restrictForAppsCreatedAfterDateTime property
        Args:
            value: Value to set for the restrict_for_apps_created_after_date_time property.
        """
        self._restrict_for_apps_created_after_date_time = value
    
    @property
    def restriction_type(self,) -> Optional[app_key_credential_restriction_type.AppKeyCredentialRestrictionType]:
        """
        Gets the restrictionType property value. The restrictionType property
        Returns: Optional[app_key_credential_restriction_type.AppKeyCredentialRestrictionType]
        """
        return self._restriction_type
    
    @restriction_type.setter
    def restriction_type(self,value: Optional[app_key_credential_restriction_type.AppKeyCredentialRestrictionType] = None) -> None:
        """
        Sets the restrictionType property value. The restrictionType property
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
    

