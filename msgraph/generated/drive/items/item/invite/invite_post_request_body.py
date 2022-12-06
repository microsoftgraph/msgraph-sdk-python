from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

drive_recipient = lazy_import('msgraph.generated.models.drive_recipient')

class InvitePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the invite method.
    """
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
        Instantiates a new invitePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expirationDateTime property
        self._expiration_date_time: Optional[str] = None
        # The message property
        self._message: Optional[str] = None
        # The password property
        self._password: Optional[str] = None
        # The recipients property
        self._recipients: Optional[List[drive_recipient.DriveRecipient]] = None
        # The requireSignIn property
        self._require_sign_in: Optional[bool] = None
        # The retainInheritedPermissions property
        self._retain_inherited_permissions: Optional[bool] = None
        # The roles property
        self._roles: Optional[List[str]] = None
        # The sendInvitation property
        self._send_invitation: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvitePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InvitePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InvitePostRequestBody()
    
    @property
    def expiration_date_time(self,) -> Optional[str]:
        """
        Gets the expirationDateTime property value. The expirationDateTime property
        Returns: Optional[str]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the expirationDateTime property value. The expirationDateTime property
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(drive_recipient.DriveRecipient)),
            "require_sign_in": lambda n : setattr(self, 'require_sign_in', n.get_bool_value()),
            "retain_inherited_permissions": lambda n : setattr(self, 'retain_inherited_permissions', n.get_bool_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "send_invitation": lambda n : setattr(self, 'send_invitation', n.get_bool_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The message property
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The message property
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The password property
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The password property
        Args:
            value: Value to set for the password property.
        """
        self._password = value
    
    @property
    def recipients(self,) -> Optional[List[drive_recipient.DriveRecipient]]:
        """
        Gets the recipients property value. The recipients property
        Returns: Optional[List[drive_recipient.DriveRecipient]]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[List[drive_recipient.DriveRecipient]] = None) -> None:
        """
        Sets the recipients property value. The recipients property
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
    @property
    def require_sign_in(self,) -> Optional[bool]:
        """
        Gets the requireSignIn property value. The requireSignIn property
        Returns: Optional[bool]
        """
        return self._require_sign_in
    
    @require_sign_in.setter
    def require_sign_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireSignIn property value. The requireSignIn property
        Args:
            value: Value to set for the requireSignIn property.
        """
        self._require_sign_in = value
    
    @property
    def retain_inherited_permissions(self,) -> Optional[bool]:
        """
        Gets the retainInheritedPermissions property value. The retainInheritedPermissions property
        Returns: Optional[bool]
        """
        return self._retain_inherited_permissions
    
    @retain_inherited_permissions.setter
    def retain_inherited_permissions(self,value: Optional[bool] = None) -> None:
        """
        Sets the retainInheritedPermissions property value. The retainInheritedPermissions property
        Args:
            value: Value to set for the retainInheritedPermissions property.
        """
        self._retain_inherited_permissions = value
    
    @property
    def roles(self,) -> Optional[List[str]]:
        """
        Gets the roles property value. The roles property
        Returns: Optional[List[str]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roles property value. The roles property
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
    @property
    def send_invitation(self,) -> Optional[bool]:
        """
        Gets the sendInvitation property value. The sendInvitation property
        Returns: Optional[bool]
        """
        return self._send_invitation
    
    @send_invitation.setter
    def send_invitation(self,value: Optional[bool] = None) -> None:
        """
        Sets the sendInvitation property value. The sendInvitation property
        Args:
            value: Value to set for the sendInvitation property.
        """
        self._send_invitation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("message", self.message)
        writer.write_str_value("password", self.password)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_bool_value("requireSignIn", self.require_sign_in)
        writer.write_bool_value("retainInheritedPermissions", self.retain_inherited_permissions)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_bool_value("sendInvitation", self.send_invitation)
        writer.write_additional_data_value(self.additional_data)
    

