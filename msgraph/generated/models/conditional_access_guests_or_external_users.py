from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_external_tenants, conditional_access_guest_or_external_user_types

class ConditionalAccessGuestsOrExternalUsers(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessGuestsOrExternalUsers and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The tenant IDs of the selected types of external users. Either all B2B tenant or a collection of tenant IDs. External tenants can be specified only when the property guestOrExternalUserTypes is not null or an empty String.
        self._external_tenants: Optional[conditional_access_external_tenants.ConditionalAccessExternalTenants] = None
        # The guestOrExternalUserTypes property
        self._guest_or_external_user_types: Optional[conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessGuestsOrExternalUsers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessGuestsOrExternalUsers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessGuestsOrExternalUsers()
    
    @property
    def external_tenants(self,) -> Optional[conditional_access_external_tenants.ConditionalAccessExternalTenants]:
        """
        Gets the externalTenants property value. The tenant IDs of the selected types of external users. Either all B2B tenant or a collection of tenant IDs. External tenants can be specified only when the property guestOrExternalUserTypes is not null or an empty String.
        Returns: Optional[conditional_access_external_tenants.ConditionalAccessExternalTenants]
        """
        return self._external_tenants
    
    @external_tenants.setter
    def external_tenants(self,value: Optional[conditional_access_external_tenants.ConditionalAccessExternalTenants] = None) -> None:
        """
        Sets the externalTenants property value. The tenant IDs of the selected types of external users. Either all B2B tenant or a collection of tenant IDs. External tenants can be specified only when the property guestOrExternalUserTypes is not null or an empty String.
        Args:
            value: Value to set for the external_tenants property.
        """
        self._external_tenants = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_external_tenants, conditional_access_guest_or_external_user_types

        fields: Dict[str, Callable[[Any], None]] = {
            "externalTenants": lambda n : setattr(self, 'external_tenants', n.get_object_value(conditional_access_external_tenants.ConditionalAccessExternalTenants)),
            "guestOrExternalUserTypes": lambda n : setattr(self, 'guest_or_external_user_types', n.get_enum_value(conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def guest_or_external_user_types(self,) -> Optional[conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes]:
        """
        Gets the guestOrExternalUserTypes property value. The guestOrExternalUserTypes property
        Returns: Optional[conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes]
        """
        return self._guest_or_external_user_types
    
    @guest_or_external_user_types.setter
    def guest_or_external_user_types(self,value: Optional[conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes] = None) -> None:
        """
        Sets the guestOrExternalUserTypes property value. The guestOrExternalUserTypes property
        Args:
            value: Value to set for the guest_or_external_user_types property.
        """
        self._guest_or_external_user_types = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("externalTenants", self.external_tenants)
        writer.write_enum_value("guestOrExternalUserTypes", self.guest_or_external_user_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

