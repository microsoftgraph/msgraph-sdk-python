from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_guests_or_external_users

class ConditionalAccessUsers(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessUsers and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Group IDs excluded from scope of policy.
        self._exclude_groups: Optional[List[str]] = None
        # Internal guests or external users excluded from the policy scope. Optionally populated.
        self._exclude_guests_or_external_users: Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers] = None
        # Role IDs excluded from scope of policy.
        self._exclude_roles: Optional[List[str]] = None
        # User IDs excluded from scope of policy and/or GuestsOrExternalUsers.
        self._exclude_users: Optional[List[str]] = None
        # Group IDs in scope of policy unless explicitly excluded.
        self._include_groups: Optional[List[str]] = None
        # Internal guests or external users included in the policy scope. Optionally populated.
        self._include_guests_or_external_users: Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers] = None
        # Role IDs in scope of policy unless explicitly excluded.
        self._include_roles: Optional[List[str]] = None
        # User IDs in scope of policy unless explicitly excluded, None, All, or GuestsOrExternalUsers.
        self._include_users: Optional[List[str]] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessUsers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessUsers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessUsers()
    
    @property
    def exclude_groups(self,) -> Optional[List[str]]:
        """
        Gets the excludeGroups property value. Group IDs excluded from scope of policy.
        Returns: Optional[List[str]]
        """
        return self._exclude_groups
    
    @exclude_groups.setter
    def exclude_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeGroups property value. Group IDs excluded from scope of policy.
        Args:
            value: Value to set for the exclude_groups property.
        """
        self._exclude_groups = value
    
    @property
    def exclude_guests_or_external_users(self,) -> Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers]:
        """
        Gets the excludeGuestsOrExternalUsers property value. Internal guests or external users excluded from the policy scope. Optionally populated.
        Returns: Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers]
        """
        return self._exclude_guests_or_external_users
    
    @exclude_guests_or_external_users.setter
    def exclude_guests_or_external_users(self,value: Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers] = None) -> None:
        """
        Sets the excludeGuestsOrExternalUsers property value. Internal guests or external users excluded from the policy scope. Optionally populated.
        Args:
            value: Value to set for the exclude_guests_or_external_users property.
        """
        self._exclude_guests_or_external_users = value
    
    @property
    def exclude_roles(self,) -> Optional[List[str]]:
        """
        Gets the excludeRoles property value. Role IDs excluded from scope of policy.
        Returns: Optional[List[str]]
        """
        return self._exclude_roles
    
    @exclude_roles.setter
    def exclude_roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeRoles property value. Role IDs excluded from scope of policy.
        Args:
            value: Value to set for the exclude_roles property.
        """
        self._exclude_roles = value
    
    @property
    def exclude_users(self,) -> Optional[List[str]]:
        """
        Gets the excludeUsers property value. User IDs excluded from scope of policy and/or GuestsOrExternalUsers.
        Returns: Optional[List[str]]
        """
        return self._exclude_users
    
    @exclude_users.setter
    def exclude_users(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeUsers property value. User IDs excluded from scope of policy and/or GuestsOrExternalUsers.
        Args:
            value: Value to set for the exclude_users property.
        """
        self._exclude_users = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_guests_or_external_users

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeGroups": lambda n : setattr(self, 'exclude_groups', n.get_collection_of_primitive_values(str)),
            "excludeGuestsOrExternalUsers": lambda n : setattr(self, 'exclude_guests_or_external_users', n.get_object_value(conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers)),
            "excludeRoles": lambda n : setattr(self, 'exclude_roles', n.get_collection_of_primitive_values(str)),
            "excludeUsers": lambda n : setattr(self, 'exclude_users', n.get_collection_of_primitive_values(str)),
            "includeGroups": lambda n : setattr(self, 'include_groups', n.get_collection_of_primitive_values(str)),
            "includeGuestsOrExternalUsers": lambda n : setattr(self, 'include_guests_or_external_users', n.get_object_value(conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers)),
            "includeRoles": lambda n : setattr(self, 'include_roles', n.get_collection_of_primitive_values(str)),
            "includeUsers": lambda n : setattr(self, 'include_users', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_groups(self,) -> Optional[List[str]]:
        """
        Gets the includeGroups property value. Group IDs in scope of policy unless explicitly excluded.
        Returns: Optional[List[str]]
        """
        return self._include_groups
    
    @include_groups.setter
    def include_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeGroups property value. Group IDs in scope of policy unless explicitly excluded.
        Args:
            value: Value to set for the include_groups property.
        """
        self._include_groups = value
    
    @property
    def include_guests_or_external_users(self,) -> Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers]:
        """
        Gets the includeGuestsOrExternalUsers property value. Internal guests or external users included in the policy scope. Optionally populated.
        Returns: Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers]
        """
        return self._include_guests_or_external_users
    
    @include_guests_or_external_users.setter
    def include_guests_or_external_users(self,value: Optional[conditional_access_guests_or_external_users.ConditionalAccessGuestsOrExternalUsers] = None) -> None:
        """
        Sets the includeGuestsOrExternalUsers property value. Internal guests or external users included in the policy scope. Optionally populated.
        Args:
            value: Value to set for the include_guests_or_external_users property.
        """
        self._include_guests_or_external_users = value
    
    @property
    def include_roles(self,) -> Optional[List[str]]:
        """
        Gets the includeRoles property value. Role IDs in scope of policy unless explicitly excluded.
        Returns: Optional[List[str]]
        """
        return self._include_roles
    
    @include_roles.setter
    def include_roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeRoles property value. Role IDs in scope of policy unless explicitly excluded.
        Args:
            value: Value to set for the include_roles property.
        """
        self._include_roles = value
    
    @property
    def include_users(self,) -> Optional[List[str]]:
        """
        Gets the includeUsers property value. User IDs in scope of policy unless explicitly excluded, None, All, or GuestsOrExternalUsers.
        Returns: Optional[List[str]]
        """
        return self._include_users
    
    @include_users.setter
    def include_users(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeUsers property value. User IDs in scope of policy unless explicitly excluded, None, All, or GuestsOrExternalUsers.
        Args:
            value: Value to set for the include_users property.
        """
        self._include_users = value
    
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
        writer.write_collection_of_primitive_values("excludeGroups", self.exclude_groups)
        writer.write_object_value("excludeGuestsOrExternalUsers", self.exclude_guests_or_external_users)
        writer.write_collection_of_primitive_values("excludeRoles", self.exclude_roles)
        writer.write_collection_of_primitive_values("excludeUsers", self.exclude_users)
        writer.write_collection_of_primitive_values("includeGroups", self.include_groups)
        writer.write_object_value("includeGuestsOrExternalUsers", self.include_guests_or_external_users)
        writer.write_collection_of_primitive_values("includeRoles", self.include_roles)
        writer.write_collection_of_primitive_values("includeUsers", self.include_users)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

