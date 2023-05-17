from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import allow_invites_from, default_user_role_permissions, policy_base

from . import policy_base

class AuthorizationPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthorizationPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.authorizationPolicy"
        # Indicates whether a user can join the tenant by email validation.
        self._allow_email_verified_users_to_join_organization: Optional[bool] = None
        # Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone.  everyone is the default setting for all cloud environments except US Government. For more details, see allowInvitesFrom values.
        self._allow_invites_from: Optional[allow_invites_from.AllowInvitesFrom] = None
        # Indicates whether user consent for risky apps is allowed. We recommend to keep this as false. Default value is false.
        self._allow_user_consent_for_risky_apps: Optional[bool] = None
        # Indicates whether users can sign up for email based subscriptions.
        self._allowed_to_sign_up_email_based_subscriptions: Optional[bool] = None
        # Indicates whether users can use the Self-Serve Password Reset feature on the tenant.
        self._allowed_to_use_s_s_p_r: Optional[bool] = None
        # To disable the use of MSOL PowerShell, set this property to true. This also disables user-based access to the legacy service endpoint used by MSOL PowerShell. This does not affect Azure Active Directory Connect or Microsoft Graph.
        self._block_msol_power_shell: Optional[bool] = None
        # The defaultUserRolePermissions property
        self._default_user_role_permissions: Optional[default_user_role_permissions.DefaultUserRolePermissions] = None
        # Represents role templateId for the role that should be granted to guest user. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
        self._guest_user_role_id: Optional[UUID] = None
    
    @property
    def allow_email_verified_users_to_join_organization(self,) -> Optional[bool]:
        """
        Gets the allowEmailVerifiedUsersToJoinOrganization property value. Indicates whether a user can join the tenant by email validation.
        Returns: Optional[bool]
        """
        return self._allow_email_verified_users_to_join_organization
    
    @allow_email_verified_users_to_join_organization.setter
    def allow_email_verified_users_to_join_organization(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowEmailVerifiedUsersToJoinOrganization property value. Indicates whether a user can join the tenant by email validation.
        Args:
            value: Value to set for the allow_email_verified_users_to_join_organization property.
        """
        self._allow_email_verified_users_to_join_organization = value
    
    @property
    def allow_invites_from(self,) -> Optional[allow_invites_from.AllowInvitesFrom]:
        """
        Gets the allowInvitesFrom property value. Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone.  everyone is the default setting for all cloud environments except US Government. For more details, see allowInvitesFrom values.
        Returns: Optional[allow_invites_from.AllowInvitesFrom]
        """
        return self._allow_invites_from
    
    @allow_invites_from.setter
    def allow_invites_from(self,value: Optional[allow_invites_from.AllowInvitesFrom] = None) -> None:
        """
        Sets the allowInvitesFrom property value. Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone.  everyone is the default setting for all cloud environments except US Government. For more details, see allowInvitesFrom values.
        Args:
            value: Value to set for the allow_invites_from property.
        """
        self._allow_invites_from = value
    
    @property
    def allow_user_consent_for_risky_apps(self,) -> Optional[bool]:
        """
        Gets the allowUserConsentForRiskyApps property value. Indicates whether user consent for risky apps is allowed. We recommend to keep this as false. Default value is false.
        Returns: Optional[bool]
        """
        return self._allow_user_consent_for_risky_apps
    
    @allow_user_consent_for_risky_apps.setter
    def allow_user_consent_for_risky_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUserConsentForRiskyApps property value. Indicates whether user consent for risky apps is allowed. We recommend to keep this as false. Default value is false.
        Args:
            value: Value to set for the allow_user_consent_for_risky_apps property.
        """
        self._allow_user_consent_for_risky_apps = value
    
    @property
    def allowed_to_sign_up_email_based_subscriptions(self,) -> Optional[bool]:
        """
        Gets the allowedToSignUpEmailBasedSubscriptions property value. Indicates whether users can sign up for email based subscriptions.
        Returns: Optional[bool]
        """
        return self._allowed_to_sign_up_email_based_subscriptions
    
    @allowed_to_sign_up_email_based_subscriptions.setter
    def allowed_to_sign_up_email_based_subscriptions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToSignUpEmailBasedSubscriptions property value. Indicates whether users can sign up for email based subscriptions.
        Args:
            value: Value to set for the allowed_to_sign_up_email_based_subscriptions property.
        """
        self._allowed_to_sign_up_email_based_subscriptions = value
    
    @property
    def allowed_to_use_s_s_p_r(self,) -> Optional[bool]:
        """
        Gets the allowedToUseSSPR property value. Indicates whether users can use the Self-Serve Password Reset feature on the tenant.
        Returns: Optional[bool]
        """
        return self._allowed_to_use_s_s_p_r
    
    @allowed_to_use_s_s_p_r.setter
    def allowed_to_use_s_s_p_r(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowedToUseSSPR property value. Indicates whether users can use the Self-Serve Password Reset feature on the tenant.
        Args:
            value: Value to set for the allowed_to_use_s_s_p_r property.
        """
        self._allowed_to_use_s_s_p_r = value
    
    @property
    def block_msol_power_shell(self,) -> Optional[bool]:
        """
        Gets the blockMsolPowerShell property value. To disable the use of MSOL PowerShell, set this property to true. This also disables user-based access to the legacy service endpoint used by MSOL PowerShell. This does not affect Azure Active Directory Connect or Microsoft Graph.
        Returns: Optional[bool]
        """
        return self._block_msol_power_shell
    
    @block_msol_power_shell.setter
    def block_msol_power_shell(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockMsolPowerShell property value. To disable the use of MSOL PowerShell, set this property to true. This also disables user-based access to the legacy service endpoint used by MSOL PowerShell. This does not affect Azure Active Directory Connect or Microsoft Graph.
        Args:
            value: Value to set for the block_msol_power_shell property.
        """
        self._block_msol_power_shell = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthorizationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthorizationPolicy()
    
    @property
    def default_user_role_permissions(self,) -> Optional[default_user_role_permissions.DefaultUserRolePermissions]:
        """
        Gets the defaultUserRolePermissions property value. The defaultUserRolePermissions property
        Returns: Optional[default_user_role_permissions.DefaultUserRolePermissions]
        """
        return self._default_user_role_permissions
    
    @default_user_role_permissions.setter
    def default_user_role_permissions(self,value: Optional[default_user_role_permissions.DefaultUserRolePermissions] = None) -> None:
        """
        Sets the defaultUserRolePermissions property value. The defaultUserRolePermissions property
        Args:
            value: Value to set for the default_user_role_permissions property.
        """
        self._default_user_role_permissions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import allow_invites_from, default_user_role_permissions, policy_base

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedToSignUpEmailBasedSubscriptions": lambda n : setattr(self, 'allowed_to_sign_up_email_based_subscriptions', n.get_bool_value()),
            "allowedToUseSSPR": lambda n : setattr(self, 'allowed_to_use_s_s_p_r', n.get_bool_value()),
            "allowEmailVerifiedUsersToJoinOrganization": lambda n : setattr(self, 'allow_email_verified_users_to_join_organization', n.get_bool_value()),
            "allowInvitesFrom": lambda n : setattr(self, 'allow_invites_from', n.get_enum_value(allow_invites_from.AllowInvitesFrom)),
            "allowUserConsentForRiskyApps": lambda n : setattr(self, 'allow_user_consent_for_risky_apps', n.get_bool_value()),
            "blockMsolPowerShell": lambda n : setattr(self, 'block_msol_power_shell', n.get_bool_value()),
            "defaultUserRolePermissions": lambda n : setattr(self, 'default_user_role_permissions', n.get_object_value(default_user_role_permissions.DefaultUserRolePermissions)),
            "guestUserRoleId": lambda n : setattr(self, 'guest_user_role_id', n.get_uuid_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def guest_user_role_id(self,) -> Optional[UUID]:
        """
        Gets the guestUserRoleId property value. Represents role templateId for the role that should be granted to guest user. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
        Returns: Optional[UUID]
        """
        return self._guest_user_role_id
    
    @guest_user_role_id.setter
    def guest_user_role_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the guestUserRoleId property value. Represents role templateId for the role that should be granted to guest user. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
        Args:
            value: Value to set for the guest_user_role_id property.
        """
        self._guest_user_role_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowedToSignUpEmailBasedSubscriptions", self.allowed_to_sign_up_email_based_subscriptions)
        writer.write_bool_value("allowedToUseSSPR", self.allowed_to_use_s_s_p_r)
        writer.write_bool_value("allowEmailVerifiedUsersToJoinOrganization", self.allow_email_verified_users_to_join_organization)
        writer.write_enum_value("allowInvitesFrom", self.allow_invites_from)
        writer.write_bool_value("allowUserConsentForRiskyApps", self.allow_user_consent_for_risky_apps)
        writer.write_bool_value("blockMsolPowerShell", self.block_msol_power_shell)
        writer.write_object_value("defaultUserRolePermissions", self.default_user_role_permissions)
        writer.write_uuid_value("guestUserRoleId", self.guest_user_role_id)
    

