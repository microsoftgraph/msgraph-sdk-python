from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PermissionScope(AdditionalDataHolder, Parsable):
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
    def admin_consent_description(self,) -> Optional[str]:
        """
        Gets the adminConsentDescription property value. A description of the delegated permissions, intended to be read by an administrator granting the permission on behalf of all users. This text appears in tenant-wide admin consent experiences.
        Returns: Optional[str]
        """
        return self._admin_consent_description
    
    @admin_consent_description.setter
    def admin_consent_description(self,value: Optional[str] = None) -> None:
        """
        Sets the adminConsentDescription property value. A description of the delegated permissions, intended to be read by an administrator granting the permission on behalf of all users. This text appears in tenant-wide admin consent experiences.
        Args:
            value: Value to set for the adminConsentDescription property.
        """
        self._admin_consent_description = value
    
    @property
    def admin_consent_display_name(self,) -> Optional[str]:
        """
        Gets the adminConsentDisplayName property value. The permission's title, intended to be read by an administrator granting the permission on behalf of all users.
        Returns: Optional[str]
        """
        return self._admin_consent_display_name
    
    @admin_consent_display_name.setter
    def admin_consent_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the adminConsentDisplayName property value. The permission's title, intended to be read by an administrator granting the permission on behalf of all users.
        Args:
            value: Value to set for the adminConsentDisplayName property.
        """
        self._admin_consent_display_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new permissionScope and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A description of the delegated permissions, intended to be read by an administrator granting the permission on behalf of all users. This text appears in tenant-wide admin consent experiences.
        self._admin_consent_description: Optional[str] = None
        # The permission's title, intended to be read by an administrator granting the permission on behalf of all users.
        self._admin_consent_display_name: Optional[str] = None
        # Unique delegated permission identifier inside the collection of delegated permissions defined for a resource application.
        self._id: Optional[Guid] = None
        # When creating or updating a permission, this property must be set to true (which is the default). To delete a permission, this property must first be set to false.  At that point, in a subsequent call, the permission may be removed.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The origin property
        self._origin: Optional[str] = None
        # The possible values are: User and Admin. Specifies whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator consent should always be required. While Microsoft Graph defines the default consent requirement for each permission, the tenant administrator may override the behavior in their organization (by allowing, restricting, or limiting user consent to this delegated permission). For more information, see Configure how users consent to applications.
        self._type: Optional[str] = None
        # A description of the delegated permissions, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
        self._user_consent_description: Optional[str] = None
        # A title for the permission, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
        self._user_consent_display_name: Optional[str] = None
        # Specifies the value to include in the scp (scope) claim in access tokens. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, as well as characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, are not allowed. May not begin with ..
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PermissionScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PermissionScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_consent_description": lambda n : setattr(self, 'admin_consent_description', n.get_str_value()),
            "admin_consent_display_name": lambda n : setattr(self, 'admin_consent_display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_object_value(Guid)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "user_consent_description": lambda n : setattr(self, 'user_consent_description', n.get_str_value()),
            "user_consent_display_name": lambda n : setattr(self, 'user_consent_display_name', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[Guid]:
        """
        Gets the id property value. Unique delegated permission identifier inside the collection of delegated permissions defined for a resource application.
        Returns: Optional[Guid]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the id property value. Unique delegated permission identifier inside the collection of delegated permissions defined for a resource application.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. When creating or updating a permission, this property must be set to true (which is the default). To delete a permission, this property must first be set to false.  At that point, in a subsequent call, the permission may be removed.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. When creating or updating a permission, this property must be set to true (which is the default). To delete a permission, this property must first be set to false.  At that point, in a subsequent call, the permission may be removed.
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
        Gets the origin property value. The origin property
        Returns: Optional[str]
        """
        return self._origin
    
    @origin.setter
    def origin(self,value: Optional[str] = None) -> None:
        """
        Sets the origin property value. The origin property
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
        writer.write_str_value("adminConsentDescription", self.admin_consent_description)
        writer.write_str_value("adminConsentDisplayName", self.admin_consent_display_name)
        writer.write_object_value("id", self.id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("origin", self.origin)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userConsentDescription", self.user_consent_description)
        writer.write_str_value("userConsentDisplayName", self.user_consent_display_name)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The possible values are: User and Admin. Specifies whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator consent should always be required. While Microsoft Graph defines the default consent requirement for each permission, the tenant administrator may override the behavior in their organization (by allowing, restricting, or limiting user consent to this delegated permission). For more information, see Configure how users consent to applications.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The possible values are: User and Admin. Specifies whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator consent should always be required. While Microsoft Graph defines the default consent requirement for each permission, the tenant administrator may override the behavior in their organization (by allowing, restricting, or limiting user consent to this delegated permission). For more information, see Configure how users consent to applications.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_consent_description(self,) -> Optional[str]:
        """
        Gets the userConsentDescription property value. A description of the delegated permissions, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
        Returns: Optional[str]
        """
        return self._user_consent_description
    
    @user_consent_description.setter
    def user_consent_description(self,value: Optional[str] = None) -> None:
        """
        Sets the userConsentDescription property value. A description of the delegated permissions, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
        Args:
            value: Value to set for the userConsentDescription property.
        """
        self._user_consent_description = value
    
    @property
    def user_consent_display_name(self,) -> Optional[str]:
        """
        Gets the userConsentDisplayName property value. A title for the permission, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
        Returns: Optional[str]
        """
        return self._user_consent_display_name
    
    @user_consent_display_name.setter
    def user_consent_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userConsentDisplayName property value. A title for the permission, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
        Args:
            value: Value to set for the userConsentDisplayName property.
        """
        self._user_consent_display_name = value
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Specifies the value to include in the scp (scope) claim in access tokens. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, as well as characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, are not allowed. May not begin with ..
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Specifies the value to include in the scp (scope) claim in access tokens. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, as well as characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, are not allowed. May not begin with ..
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

