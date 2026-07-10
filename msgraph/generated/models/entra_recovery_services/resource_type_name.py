from enum import Enum

class ResourceTypeName(str, Enum):
    # Represents the user entity
    User = "user",
    # Represents the group entity
    Group = "group",
    # Represents the conditional access policy entity
    ConditionalAccessPolicy = "conditionalAccessPolicy",
    # Represents the named location policy entity
    NamedLocationPolicy = "namedLocationPolicy",
    # Represents the authentication method policy entity
    AuthenticationMethodPolicy = "authenticationMethodPolicy",
    # Represents the authorization policy entity
    AuthorizationPolicy = "authorizationPolicy",
    # Represents the authentication strength policy entity
    AuthenticationStrengthPolicy = "authenticationStrengthPolicy",
    # Represents the application entity
    Application = "application",
    # Represents the service principal entity
    ServicePrincipal = "servicePrincipal",
    # This will help in making this enum evolable and adding more values in the future.
    UnknownFutureValue = "unknownFutureValue",
    # Represents the oAuth2PermissionGrant entity.
    OAuth2PermissionGrant = "oAuth2PermissionGrant",
    # Represents the appRoleAssignment entity.
    AppRoleAssignment = "appRoleAssignment",
    # Represents the organization entity.
    Organization = "organization",

