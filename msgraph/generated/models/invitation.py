from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
invited_user_message_info = lazy_import('msgraph.generated.models.invited_user_message_info')
user = lazy_import('msgraph.generated.models.user')

class Invitation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Invitation and sets the default values.
        """
        super().__init__()
        # The user created as part of the invitation creation. Read-Only
        self._invited_user: Optional[user.User] = None
        # The display name of the user being invited.
        self._invited_user_display_name: Optional[str] = None
        # The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.
        self._invited_user_email_address: Optional[str] = None
        # Additional configuration for the message being sent to the invited user, including customizing message text, language and cc recipient list.
        self._invited_user_message_info: Optional[invited_user_message_info.InvitedUserMessageInfo] = None
        # The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.
        self._invited_user_type: Optional[str] = None
        # The URL the user can use to redeem their invitation. Read-only.
        self._invite_redeem_url: Optional[str] = None
        # The URL the user should be redirected to once the invitation is redeemed. Required.
        self._invite_redirect_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Reset the user's redemption status and reinvite a user while retaining their user identifier, group memberships, and app assignments. This property allows you to enable a user to sign-in using a different email address from the one in the previous invitation. For more information about using this property, see Reset redemption status for a guest user.
        self._reset_redemption: Optional[bool] = None
        # Indicates whether an email should be sent to the user being invited. The default is false.
        self._send_invitation_message: Optional[bool] = None
        # The status of the invitation. Possible values are: PendingAcceptance, Completed, InProgress, and Error.
        self._status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Invitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Invitation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Invitation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "invited_user": lambda n : setattr(self, 'invited_user', n.get_object_value(user.User)),
            "invited_user_display_name": lambda n : setattr(self, 'invited_user_display_name', n.get_str_value()),
            "invited_user_email_address": lambda n : setattr(self, 'invited_user_email_address', n.get_str_value()),
            "invited_user_message_info": lambda n : setattr(self, 'invited_user_message_info', n.get_object_value(invited_user_message_info.InvitedUserMessageInfo)),
            "invited_user_type": lambda n : setattr(self, 'invited_user_type', n.get_str_value()),
            "invite_redeem_url": lambda n : setattr(self, 'invite_redeem_url', n.get_str_value()),
            "invite_redirect_url": lambda n : setattr(self, 'invite_redirect_url', n.get_str_value()),
            "reset_redemption": lambda n : setattr(self, 'reset_redemption', n.get_bool_value()),
            "send_invitation_message": lambda n : setattr(self, 'send_invitation_message', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invited_user(self,) -> Optional[user.User]:
        """
        Gets the invitedUser property value. The user created as part of the invitation creation. Read-Only
        Returns: Optional[user.User]
        """
        return self._invited_user
    
    @invited_user.setter
    def invited_user(self,value: Optional[user.User] = None) -> None:
        """
        Sets the invitedUser property value. The user created as part of the invitation creation. Read-Only
        Args:
            value: Value to set for the invitedUser property.
        """
        self._invited_user = value
    
    @property
    def invited_user_display_name(self,) -> Optional[str]:
        """
        Gets the invitedUserDisplayName property value. The display name of the user being invited.
        Returns: Optional[str]
        """
        return self._invited_user_display_name
    
    @invited_user_display_name.setter
    def invited_user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the invitedUserDisplayName property value. The display name of the user being invited.
        Args:
            value: Value to set for the invitedUserDisplayName property.
        """
        self._invited_user_display_name = value
    
    @property
    def invited_user_email_address(self,) -> Optional[str]:
        """
        Gets the invitedUserEmailAddress property value. The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.
        Returns: Optional[str]
        """
        return self._invited_user_email_address
    
    @invited_user_email_address.setter
    def invited_user_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the invitedUserEmailAddress property value. The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.
        Args:
            value: Value to set for the invitedUserEmailAddress property.
        """
        self._invited_user_email_address = value
    
    @property
    def invited_user_message_info(self,) -> Optional[invited_user_message_info.InvitedUserMessageInfo]:
        """
        Gets the invitedUserMessageInfo property value. Additional configuration for the message being sent to the invited user, including customizing message text, language and cc recipient list.
        Returns: Optional[invited_user_message_info.InvitedUserMessageInfo]
        """
        return self._invited_user_message_info
    
    @invited_user_message_info.setter
    def invited_user_message_info(self,value: Optional[invited_user_message_info.InvitedUserMessageInfo] = None) -> None:
        """
        Sets the invitedUserMessageInfo property value. Additional configuration for the message being sent to the invited user, including customizing message text, language and cc recipient list.
        Args:
            value: Value to set for the invitedUserMessageInfo property.
        """
        self._invited_user_message_info = value
    
    @property
    def invited_user_type(self,) -> Optional[str]:
        """
        Gets the invitedUserType property value. The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.
        Returns: Optional[str]
        """
        return self._invited_user_type
    
    @invited_user_type.setter
    def invited_user_type(self,value: Optional[str] = None) -> None:
        """
        Sets the invitedUserType property value. The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.
        Args:
            value: Value to set for the invitedUserType property.
        """
        self._invited_user_type = value
    
    @property
    def invite_redeem_url(self,) -> Optional[str]:
        """
        Gets the inviteRedeemUrl property value. The URL the user can use to redeem their invitation. Read-only.
        Returns: Optional[str]
        """
        return self._invite_redeem_url
    
    @invite_redeem_url.setter
    def invite_redeem_url(self,value: Optional[str] = None) -> None:
        """
        Sets the inviteRedeemUrl property value. The URL the user can use to redeem their invitation. Read-only.
        Args:
            value: Value to set for the inviteRedeemUrl property.
        """
        self._invite_redeem_url = value
    
    @property
    def invite_redirect_url(self,) -> Optional[str]:
        """
        Gets the inviteRedirectUrl property value. The URL the user should be redirected to once the invitation is redeemed. Required.
        Returns: Optional[str]
        """
        return self._invite_redirect_url
    
    @invite_redirect_url.setter
    def invite_redirect_url(self,value: Optional[str] = None) -> None:
        """
        Sets the inviteRedirectUrl property value. The URL the user should be redirected to once the invitation is redeemed. Required.
        Args:
            value: Value to set for the inviteRedirectUrl property.
        """
        self._invite_redirect_url = value
    
    @property
    def reset_redemption(self,) -> Optional[bool]:
        """
        Gets the resetRedemption property value. Reset the user's redemption status and reinvite a user while retaining their user identifier, group memberships, and app assignments. This property allows you to enable a user to sign-in using a different email address from the one in the previous invitation. For more information about using this property, see Reset redemption status for a guest user.
        Returns: Optional[bool]
        """
        return self._reset_redemption
    
    @reset_redemption.setter
    def reset_redemption(self,value: Optional[bool] = None) -> None:
        """
        Sets the resetRedemption property value. Reset the user's redemption status and reinvite a user while retaining their user identifier, group memberships, and app assignments. This property allows you to enable a user to sign-in using a different email address from the one in the previous invitation. For more information about using this property, see Reset redemption status for a guest user.
        Args:
            value: Value to set for the resetRedemption property.
        """
        self._reset_redemption = value
    
    @property
    def send_invitation_message(self,) -> Optional[bool]:
        """
        Gets the sendInvitationMessage property value. Indicates whether an email should be sent to the user being invited. The default is false.
        Returns: Optional[bool]
        """
        return self._send_invitation_message
    
    @send_invitation_message.setter
    def send_invitation_message(self,value: Optional[bool] = None) -> None:
        """
        Sets the sendInvitationMessage property value. Indicates whether an email should be sent to the user being invited. The default is false.
        Args:
            value: Value to set for the sendInvitationMessage property.
        """
        self._send_invitation_message = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("invitedUser", self.invited_user)
        writer.write_str_value("invitedUserDisplayName", self.invited_user_display_name)
        writer.write_str_value("invitedUserEmailAddress", self.invited_user_email_address)
        writer.write_object_value("invitedUserMessageInfo", self.invited_user_message_info)
        writer.write_str_value("invitedUserType", self.invited_user_type)
        writer.write_str_value("inviteRedeemUrl", self.invite_redeem_url)
        writer.write_str_value("inviteRedirectUrl", self.invite_redirect_url)
        writer.write_bool_value("resetRedemption", self.reset_redemption)
        writer.write_bool_value("sendInvitationMessage", self.send_invitation_message)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status of the invitation. Possible values are: PendingAcceptance, Completed, InProgress, and Error.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status of the invitation. Possible values are: PendingAcceptance, Completed, InProgress, and Error.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

