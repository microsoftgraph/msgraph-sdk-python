from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .invited_user_message_info import InvitedUserMessageInfo
    from .user import User

from .entity import Entity

@dataclass
class Invitation(Entity):
    # The URL the user can use to redeem their invitation. Read-only.
    invite_redeem_url: Optional[str] = None
    # The URL the user should be redirected to once the invitation is redeemed. Required.
    invite_redirect_url: Optional[str] = None
    # The user created as part of the invitation creation. Read-Only
    invited_user: Optional[User] = None
    # The display name of the user being invited.
    invited_user_display_name: Optional[str] = None
    # The email address of the user being invited. Required. The following special characters aren't permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.
    invited_user_email_address: Optional[str] = None
    # Additional configuration for the message being sent to the invited user, including customizing message text, language and cc recipient list.
    invited_user_message_info: Optional[InvitedUserMessageInfo] = None
    # The userType of the user being invited. By default, this is Guest. You can invite as Member if you're a company administrator.
    invited_user_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Reset the user's redemption status and reinvite a user while retaining their user identifier, group memberships, and app assignments. This property allows you to enable a user to sign-in using a different email address from the one in the previous invitation. For more information about using this property, see Reset redemption status for a guest user.
    reset_redemption: Optional[bool] = None
    # Indicates whether an email should be sent to the user being invited. The default is false.
    send_invitation_message: Optional[bool] = None
    # The status of the invitation. Possible values are: PendingAcceptance, Completed, InProgress, and Error.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Invitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Invitation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Invitation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .invited_user_message_info import InvitedUserMessageInfo
        from .user import User

        from .entity import Entity
        from .invited_user_message_info import InvitedUserMessageInfo
        from .user import User

        fields: Dict[str, Callable[[Any], None]] = {
            "inviteRedeemUrl": lambda n : setattr(self, 'invite_redeem_url', n.get_str_value()),
            "inviteRedirectUrl": lambda n : setattr(self, 'invite_redirect_url', n.get_str_value()),
            "invitedUser": lambda n : setattr(self, 'invited_user', n.get_object_value(User)),
            "invitedUserDisplayName": lambda n : setattr(self, 'invited_user_display_name', n.get_str_value()),
            "invitedUserEmailAddress": lambda n : setattr(self, 'invited_user_email_address', n.get_str_value()),
            "invitedUserMessageInfo": lambda n : setattr(self, 'invited_user_message_info', n.get_object_value(InvitedUserMessageInfo)),
            "invitedUserType": lambda n : setattr(self, 'invited_user_type', n.get_str_value()),
            "resetRedemption": lambda n : setattr(self, 'reset_redemption', n.get_bool_value()),
            "sendInvitationMessage": lambda n : setattr(self, 'send_invitation_message', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("inviteRedeemUrl", self.invite_redeem_url)
        writer.write_str_value("inviteRedirectUrl", self.invite_redirect_url)
        writer.write_object_value("invitedUser", self.invited_user)
        writer.write_str_value("invitedUserDisplayName", self.invited_user_display_name)
        writer.write_str_value("invitedUserEmailAddress", self.invited_user_email_address)
        writer.write_object_value("invitedUserMessageInfo", self.invited_user_message_info)
        writer.write_str_value("invitedUserType", self.invited_user_type)
        writer.write_bool_value("resetRedemption", self.reset_redemption)
        writer.write_bool_value("sendInvitationMessage", self.send_invitation_message)
        writer.write_str_value("status", self.status)
    

