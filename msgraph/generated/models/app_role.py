from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AppRole(AdditionalDataHolder, Parsable):
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
    def allowed_member_types(self,) -> Optional[List[str]]:
        """
        Gets the allowedMemberTypes property value. Specifies whether this app role can be assigned to users and groups (by setting to ['User']), to other application's (by setting to ['Application'], or both (by setting to ['User', 'Application']). App roles supporting assignment to other applications' service principals are also known as application permissions. The 'Application' value is only supported for app roles defined on application entities.
        Returns: Optional[List[str]]
        """
        return self._allowed_member_types
    
    @allowed_member_types.setter
    def allowed_member_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedMemberTypes property value. Specifies whether this app role can be assigned to users and groups (by setting to ['User']), to other application's (by setting to ['Application'], or both (by setting to ['User', 'Application']). App roles supporting assignment to other applications' service principals are also known as application permissions. The 'Application' value is only supported for app roles defined on application entities.
        Args:
            value: Value to set for the allowedMemberTypes property.
        """
        self._allowed_member_types = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appRole and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether this app role can be assigned to users and groups (by setting to ['User']), to other application's (by setting to ['Application'], or both (by setting to ['User', 'Application']). App roles supporting assignment to other applications' service principals are also known as application permissions. The 'Application' value is only supported for app roles defined on application entities.
        self._allowed_member_types: Optional[List[str]] = None
        # The description for the app role. This is displayed when the app role is being assigned and, if the app role functions as an application permission, during  consent experiences.
        self._description: Optional[str] = None
        # Display name for the permission that appears in the app role assignment and consent experiences.
        self._display_name: Optional[str] = None
        # Unique role identifier inside the appRoles collection. When creating a new app role, a new GUID identifier must be provided.
        self._id: Optional[Guid] = None
        # When creating or updating an app role, this must be set to true (which is the default). To delete a role, this must first be set to false.  At that point, in a subsequent call, this role may be removed.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies if the app role is defined on the application object or on the servicePrincipal entity. Must not be included in any POST or PATCH requests. Read-only.
        self._origin: Optional[str] = None
        # Specifies the value to include in the roles claim in ID tokens and access tokens authenticating an assigned user or service principal. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, as well as characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, are not allowed. May not begin with ..
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppRole
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppRole()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the app role. This is displayed when the app role is being assigned and, if the app role functions as an application permission, during  consent experiences.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the app role. This is displayed when the app role is being assigned and, if the app role functions as an application permission, during  consent experiences.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the permission that appears in the app role assignment and consent experiences.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the permission that appears in the app role assignment and consent experiences.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_member_types": lambda n : setattr(self, 'allowed_member_types', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_object_value(Guid)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[Guid]:
        """
        Gets the id property value. Unique role identifier inside the appRoles collection. When creating a new app role, a new GUID identifier must be provided.
        Returns: Optional[Guid]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the id property value. Unique role identifier inside the appRoles collection. When creating a new app role, a new GUID identifier must be provided.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. When creating or updating an app role, this must be set to true (which is the default). To delete a role, this must first be set to false.  At that point, in a subsequent call, this role may be removed.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. When creating or updating an app role, this must be set to true (which is the default). To delete a role, this must first be set to false.  At that point, in a subsequent call, this role may be removed.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
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
    def origin(self,) -> Optional[str]:
        """
        Gets the origin property value. Specifies if the app role is defined on the application object or on the servicePrincipal entity. Must not be included in any POST or PATCH requests. Read-only.
        Returns: Optional[str]
        """
        return self._origin
    
    @origin.setter
    def origin(self,value: Optional[str] = None) -> None:
        """
        Sets the origin property value. Specifies if the app role is defined on the application object or on the servicePrincipal entity. Must not be included in any POST or PATCH requests. Read-only.
        Args:
            value: Value to set for the origin property.
        """
        self._origin = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("allowedMemberTypes", self.allowed_member_types)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("id", self.id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("origin", self.origin)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Specifies the value to include in the roles claim in ID tokens and access tokens authenticating an assigned user or service principal. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, as well as characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, are not allowed. May not begin with ..
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Specifies the value to include in the roles claim in ID tokens and access tokens authenticating an assigned user or service principal. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, as well as characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, are not allowed. May not begin with ..
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

