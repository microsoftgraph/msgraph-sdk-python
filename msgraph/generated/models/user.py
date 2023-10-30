from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_acceptance import AgreementAcceptance
    from .app_role_assignment import AppRoleAssignment
    from .assigned_license import AssignedLicense
    from .assigned_plan import AssignedPlan
    from .authentication import Authentication
    from .authorization_info import AuthorizationInfo
    from .calendar import Calendar
    from .calendar_group import CalendarGroup
    from .chat import Chat
    from .contact import Contact
    from .contact_folder import ContactFolder
    from .custom_security_attribute_value import CustomSecurityAttributeValue
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
    from .directory_object import DirectoryObject
    from .drive import Drive
    from .employee_experience_user import EmployeeExperienceUser
    from .employee_org_data import EmployeeOrgData
    from .event import Event
    from .extension import Extension
    from .inference_classification import InferenceClassification
    from .license_assignment_state import LicenseAssignmentState
    from .license_details import LicenseDetails
    from .mailbox_settings import MailboxSettings
    from .mail_folder import MailFolder
    from .managed_app_registration import ManagedAppRegistration
    from .managed_device import ManagedDevice
    from .message import Message
    from .object_identity import ObjectIdentity
    from .office_graph_insights import OfficeGraphInsights
    from .onenote import Onenote
    from .online_meeting import OnlineMeeting
    from .on_premises_extension_attributes import OnPremisesExtensionAttributes
    from .on_premises_provisioning_error import OnPremisesProvisioningError
    from .outlook_user import OutlookUser
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .password_profile import PasswordProfile
    from .person import Person
    from .planner_user import PlannerUser
    from .presence import Presence
    from .profile_photo import ProfilePhoto
    from .provisioned_plan import ProvisionedPlan
    from .scoped_role_membership import ScopedRoleMembership
    from .service_provisioning_error import ServiceProvisioningError
    from .sign_in_activity import SignInActivity
    from .site import Site
    from .team import Team
    from .todo import Todo
    from .user_activity import UserActivity
    from .user_print import UserPrint
    from .user_settings import UserSettings
    from .user_teamwork import UserTeamwork

from .directory_object import DirectoryObject

@dataclass
class User(DirectoryObject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.user"
    # A freeform text entry field for the user to describe themselves. Returned only on $select.
    about_me: Optional[str] = None
    # true if the account is enabled; otherwise, false. This property is required when a user is created. Returned only on $select. Supports $filter (eq, ne, not, and in).
    account_enabled: Optional[bool] = None
    # The user's activities across devices. Read-only. Nullable.
    activities: Optional[List[UserActivity]] = None
    # Sets the age group of the user. Allowed values: null, Minor, NotAdult and Adult. For more information, see legal age group property definitions. Returned only on $select. Supports $filter (eq, ne, not, and in).
    age_group: Optional[str] = None
    # The user's terms of use acceptance statuses. Read-only. Nullable.
    agreement_acceptances: Optional[List[AgreementAcceptance]] = None
    # Represents the app roles a user has been granted for an application. Supports $expand.
    app_role_assignments: Optional[List[AppRoleAssignment]] = None
    # The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate directly assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly assigned and inherited licenses.  Not nullable. Returned only on $select. Supports $filter (eq, not, /$count eq 0, /$count ne 0).
    assigned_licenses: Optional[List[AssignedLicense]] = None
    # The plans that are assigned to the user. Read-only. Not nullable. Returned only on $select. Supports $filter (eq and not).
    assigned_plans: Optional[List[AssignedPlan]] = None
    # The authentication methods that are supported for the user.
    authentication: Optional[Authentication] = None
    # The authorizationInfo property
    authorization_info: Optional[AuthorizationInfo] = None
    # The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned only on $select.
    birthday: Optional[datetime.datetime] = None
    # The telephone numbers for the user. NOTE: Although this is a string collection, only one number can be set for this property. Read-only for users synced from on-premises directory. Returned by default. Supports $filter (eq, not, ge, le, startsWith).
    business_phones: Optional[List[str]] = None
    # The user's primary calendar. Read-only.
    calendar: Optional[Calendar] = None
    # The user's calendar groups. Read-only. Nullable.
    calendar_groups: Optional[List[CalendarGroup]] = None
    # The calendar view for the calendar. Read-only. Nullable.
    calendar_view: Optional[List[Event]] = None
    # The user's calendars. Read-only. Nullable.
    calendars: Optional[List[Calendar]] = None
    # The chats property
    chats: Optional[List[Chat]] = None
    # The city where the user is located. Maximum length is 128 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    city: Optional[str] = None
    # The name of the company that the user is associated with. This property can be useful for describing the company that an external user comes from. The maximum length is 64 characters.Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    company_name: Optional[str] = None
    # Sets whether consent has been obtained for minors. Allowed values: null, Granted, Denied and NotRequired. Refer to the legal age group property definitions for further information. Returned only on $select. Supports $filter (eq, ne, not, and in).
    consent_provided_for_minor: Optional[str] = None
    # The user's contacts folders. Read-only. Nullable.
    contact_folders: Optional[List[ContactFolder]] = None
    # The user's contacts. Read-only. Nullable.
    contacts: Optional[List[Contact]] = None
    # The country or region where the user is located; for example, US or UK. Maximum length is 128 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    country: Optional[str] = None
    # The date and time the user was created, in ISO 8601 format and in UTC time. The value cannot be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in).
    created_date_time: Optional[datetime.datetime] = None
    # Directory objects that the user created. Read-only. Nullable.
    created_objects: Optional[List[DirectoryObject]] = None
    # Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by an external user signing up through a link that is part of a user flow (SelfServiceSignUp). Read-only.Returned only on $select. Supports $filter (eq, ne, not, in).
    creation_type: Optional[str] = None
    # An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Returned only on $select. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive.
    custom_security_attributes: Optional[CustomSecurityAttributeValue] = None
    # The name for the department in which the user works. Maximum length is 64 characters. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, and eq on null values).
    department: Optional[str] = None
    # The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.
    device_enrollment_limit: Optional[int] = None
    # The list of troubleshooting events for this user.
    device_management_troubleshooting_events: Optional[List[DeviceManagementTroubleshootingEvent]] = None
    # The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.
    direct_reports: Optional[List[DirectoryObject]] = None
    # The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial and last name. This property is required when a user is created and it cannot be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderby, and $search.
    display_name: Optional[str] = None
    # The user's OneDrive. Read-only.
    drive: Optional[Drive] = None
    # A collection of drives available for this user. Read-only.
    drives: Optional[List[Drive]] = None
    # The employeeExperience property
    employee_experience: Optional[EmployeeExperienceUser] = None
    # The date and time when the user was hired or will start work in case of a future hire. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in).
    employee_hire_date: Optional[datetime.datetime] = None
    # The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    employee_id: Optional[str] = None
    # The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs one of the following Microsoft Entra roles: Lifecycle Workflows Administrator, Global Reader, or Global Administrator. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user.
    employee_leave_date_time: Optional[datetime.datetime] = None
    # Represents organization data (for example, division and costCenter) associated with a user. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in).
    employee_org_data: Optional[EmployeeOrgData] = None
    # Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, startsWith).
    employee_type: Optional[str] = None
    # The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.
    events: Optional[List[Event]] = None
    # The collection of open extensions defined for the user. Read-only. Supports $expand. Nullable.
    extensions: Optional[List[Extension]] = None
    # For an external user invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Returned only on $select. Supports $filter (eq, ne, not , in).
    external_user_state: Optional[str] = None
    # Shows the timestamp for the latest change to the externalUserState property. Returned only on $select. Supports $filter (eq, ne, not , in).
    external_user_state_change_date_time: Optional[datetime.datetime] = None
    # The fax number of the user. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    fax_number: Optional[str] = None
    # The followedSites property
    followed_sites: Optional[List[Site]] = None
    # The given name (first name) of the user. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    given_name: Optional[str] = None
    # The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned only on $select.  Note: This property is specific to SharePoint Online. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.
    hire_date: Optional[datetime.datetime] = None
    # Represents the identities that can be used to sign in to this user account. An identity can be provided by Microsoft (also known as a local account), by organizations, or by social identity providers such as Facebook, Google, and Microsoft, and tied to a user account. May contain multiple items with the same signInType value. Returned only on $select. Supports $filter (eq) including on null values, only where the signInType is not userPrincipalName.
    identities: Optional[List[ObjectIdentity]] = None
    # The instant message voice over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Returned only on $select. Supports $filter (eq, not, ge, le, startsWith).
    im_addresses: Optional[List[str]] = None
    # Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
    inference_classification: Optional[InferenceClassification] = None
    # The insights property
    insights: Optional[OfficeGraphInsights] = None
    # A list for the user to describe their interests. Returned only on $select.
    interests: Optional[List[str]] = None
    # Do not use – reserved for future use.
    is_resource_account: Optional[bool] = None
    # The user's job title. Maximum length is 128 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    job_title: Optional[str] = None
    # The joinedTeams property
    joined_teams: Optional[List[Team]] = None
    # The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned only on $select.
    last_password_change_date_time: Optional[datetime.datetime] = None
    # Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult and Adult. Refer to the legal age group property definitions for further information. Returned only on $select.
    legal_age_group_classification: Optional[str] = None
    # State of license assignments for this user. Also indicates licenses that are directly assigned or the user has inherited through group memberships. Read-only. Returned only on $select.
    license_assignment_states: Optional[List[LicenseAssignmentState]] = None
    # A collection of this user's license details. Read-only.
    license_details: Optional[List[LicenseDetails]] = None
    # The SMTP address for the user, for example, jeff@contoso.onmicrosoft.com. Changes to this property will also update the user's proxyAddresses collection to include the value as an SMTP address. This property can't contain accent characters.  NOTE: We don't recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).
    mail: Optional[str] = None
    # The user's mail folders. Read-only. Nullable.
    mail_folders: Optional[List[MailFolder]] = None
    # The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    mail_nickname: Optional[str] = None
    # Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale and time zone. Returned only on $select.
    mailbox_settings: Optional[MailboxSettings] = None
    # Zero or more managed app registrations that belong to the user.
    managed_app_registrations: Optional[List[ManagedAppRegistration]] = None
    # The managed devices associated with the user.
    managed_devices: Optional[List[ManagedDevice]] = None
    # The user or contact that is this user's manager. Read-only. (HTTP Methods: GET, PUT, DELETE.). Supports $expand.
    manager: Optional[DirectoryObject] = None
    # The groups and directory roles that the user is a member of. Read-only. Nullable. Supports $expand.
    member_of: Optional[List[DirectoryObject]] = None
    # The messages in a mailbox or folder. Read-only. Nullable.
    messages: Optional[List[Message]] = None
    # The primary cellular telephone number for the user. Read-only for users synced from on-premises directory. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values) and $search.
    mobile_phone: Optional[str] = None
    # The URL for the user's personal site. Returned only on $select.
    my_site: Optional[str] = None
    # The oauth2PermissionGrants property
    oauth2_permission_grants: Optional[List[OAuth2PermissionGrant]] = None
    # The office location in the user's place of business. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    office_location: Optional[str] = None
    # Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select.
    on_premises_distinguished_name: Optional[str] = None
    # Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select.
    on_premises_domain_name: Optional[str] = None
    # Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Returned only on $select. Supports $filter (eq, ne, not, in).
    on_premises_extension_attributes: Optional[OnPremisesExtensionAttributes] = None
    # This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ characters can't be used when specifying this property. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in)..
    on_premises_immutable_id: Optional[str] = None
    # Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in).
    on_premises_last_sync_date_time: Optional[datetime.datetime] = None
    # Errors when using Microsoft synchronization product during provisioning. Returned only on $select. Supports $filter (eq, not, ge, le).
    on_premises_provisioning_errors: Optional[List[OnPremisesProvisioningError]] = None
    # Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith).
    on_premises_sam_account_name: Optional[str] = None
    # Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Returned only on $select.  Supports $filter (eq including on null values).
    on_premises_security_identifier: Optional[str] = None
    # true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Microsoft Entra ID. Read-only. Returned only on $select. Supports $filter (eq, ne, not, in, and eq on null values).
    on_premises_sync_enabled: Optional[bool] = None
    # Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith).
    on_premises_user_principal_name: Optional[str] = None
    # The onenote property
    onenote: Optional[Onenote] = None
    # Information about a meeting, including the URL used to join a meeting, the attendees' list, and the description.
    online_meetings: Optional[List[OnlineMeeting]] = None
    # A list of additional email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. NOTE: This property can't contain accent characters. Returned only on $select. Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).
    other_mails: Optional[List[str]] = None
    # The outlook property
    outlook: Optional[OutlookUser] = None
    # Devices that are owned by the user. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owned_devices: Optional[List[DirectoryObject]] = None
    # Directory objects that are owned by the user. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owned_objects: Optional[List[DirectoryObject]] = None
    # Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two may be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. Returned only on $select. For more information on the default password policies, see Microsoft Entra password policies. Supports $filter (ne, not, and eq on null values).
    password_policies: Optional[str] = None
    # Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Returned only on $select. Supports $filter (eq, ne, not, in, and eq on null values).
    password_profile: Optional[PasswordProfile] = None
    # A list for the user to enumerate their past projects. Returned only on $select.
    past_projects: Optional[List[str]] = None
    # People that are relevant to the user. Read-only. Nullable.
    people: Optional[List[Person]] = None
    # The user's profile photo. Read-only.
    photo: Optional[ProfilePhoto] = None
    # The photos property
    photos: Optional[List[ProfilePhoto]] = None
    # Entry-point to the Planner resource that might exist for a user. Read-only.
    planner: Optional[PlannerUser] = None
    # The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    postal_code: Optional[str] = None
    # The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.
    preferred_data_location: Optional[str] = None
    # The preferred language for the user. The preferred language format is based on RFC 4646. The name is a combination of an ISO 639 two-letter lowercase culture code associated with the language, and an ISO 3166 two-letter uppercase subculture code associated with the country or region. Example: 'en-US', or 'es-ES'. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values)
    preferred_language: Optional[str] = None
    # The preferred name for the user. Not Supported. This attribute returns an empty string.Returned only on $select.
    preferred_name: Optional[str] = None
    # The presence property
    presence: Optional[Presence] = None
    # The print property
    print: Optional[UserPrint] = None
    # The plans that are provisioned for the user. Read-only. Not nullable. Returned only on $select. Supports $filter (eq, not, ge, le).
    provisioned_plans: Optional[List[ProvisionedPlan]] = None
    # For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property will also update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address while those prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of 10 unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Returned only on $select. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
    proxy_addresses: Optional[List[str]] = None
    # Devices that are registered for the user. Read-only. Nullable. Supports $expand and returns up to 100 objects.
    registered_devices: Optional[List[DirectoryObject]] = None
    # A list for the user to enumerate their responsibilities. Returned only on $select.
    responsibilities: Optional[List[str]] = None
    # A list for the user to enumerate the schools they have attended. Returned only on $select.
    schools: Optional[List[str]] = None
    # The scopedRoleMemberOf property
    scoped_role_member_of: Optional[List[ScopedRoleMembership]] = None
    # Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).
    security_identifier: Optional[str] = None
    # The serviceProvisioningErrors property
    service_provisioning_errors: Optional[List[ServiceProvisioningError]] = None
    # The settings property
    settings: Optional[UserSettings] = None
    # Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.
    show_in_address_list: Optional[bool] = None
    # Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Returned only on $select. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note: Details for this property require a Microsoft Entra ID P1 or P2 license and the AuditLog.Read.All permission.This property is not returned for a user who has never signed in or last signed in before April 2020.
    sign_in_activity: Optional[SignInActivity] = None
    # Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application needs to acquire a new refresh token by making a request to the authorize endpoint. Read-only. Use revokeSignInSessions to reset. Returned only on $select.
    sign_in_sessions_valid_from_date_time: Optional[datetime.datetime] = None
    # A list for the user to enumerate their skills. Returned only on $select.
    skills: Optional[List[str]] = None
    # The state or province in the user's address. Maximum length is 128 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    state: Optional[str] = None
    # The street address of the user's place of business. Maximum length is 1024 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    street_address: Optional[str] = None
    # The user's surname (family name or last name). Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    surname: Optional[str] = None
    # A container for Microsoft Teams features available for the user. Read-only. Nullable.
    teamwork: Optional[UserTeamwork] = None
    # Represents the To Do services available to a user.
    todo: Optional[Todo] = None
    # The groups, including nested groups, and directory roles that a user is a member of. Nullable.
    transitive_member_of: Optional[List[DirectoryObject]] = None
    # A two letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirement to check for availability of services in countries.  Examples include: US, JP, and GB. Not nullable. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    usage_location: Optional[str] = None
    # The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property can't contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderby.
    user_principal_name: Optional[str] = None
    # A string value that can be used to classify user types in your directory, such as Member and Guest. Returned only on $select. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for member and guest users, see What are the default user permissions in Microsoft Entra ID?
    user_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> User:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return User()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .agreement_acceptance import AgreementAcceptance
        from .app_role_assignment import AppRoleAssignment
        from .assigned_license import AssignedLicense
        from .assigned_plan import AssignedPlan
        from .authentication import Authentication
        from .authorization_info import AuthorizationInfo
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .chat import Chat
        from .contact import Contact
        from .contact_folder import ContactFolder
        from .custom_security_attribute_value import CustomSecurityAttributeValue
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .directory_object import DirectoryObject
        from .drive import Drive
        from .employee_experience_user import EmployeeExperienceUser
        from .employee_org_data import EmployeeOrgData
        from .event import Event
        from .extension import Extension
        from .inference_classification import InferenceClassification
        from .license_assignment_state import LicenseAssignmentState
        from .license_details import LicenseDetails
        from .mailbox_settings import MailboxSettings
        from .mail_folder import MailFolder
        from .managed_app_registration import ManagedAppRegistration
        from .managed_device import ManagedDevice
        from .message import Message
        from .object_identity import ObjectIdentity
        from .office_graph_insights import OfficeGraphInsights
        from .onenote import Onenote
        from .online_meeting import OnlineMeeting
        from .on_premises_extension_attributes import OnPremisesExtensionAttributes
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .outlook_user import OutlookUser
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_profile import PasswordProfile
        from .person import Person
        from .planner_user import PlannerUser
        from .presence import Presence
        from .profile_photo import ProfilePhoto
        from .provisioned_plan import ProvisionedPlan
        from .scoped_role_membership import ScopedRoleMembership
        from .service_provisioning_error import ServiceProvisioningError
        from .sign_in_activity import SignInActivity
        from .site import Site
        from .team import Team
        from .todo import Todo
        from .user_activity import UserActivity
        from .user_print import UserPrint
        from .user_settings import UserSettings
        from .user_teamwork import UserTeamwork

        from .agreement_acceptance import AgreementAcceptance
        from .app_role_assignment import AppRoleAssignment
        from .assigned_license import AssignedLicense
        from .assigned_plan import AssignedPlan
        from .authentication import Authentication
        from .authorization_info import AuthorizationInfo
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .chat import Chat
        from .contact import Contact
        from .contact_folder import ContactFolder
        from .custom_security_attribute_value import CustomSecurityAttributeValue
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .directory_object import DirectoryObject
        from .drive import Drive
        from .employee_experience_user import EmployeeExperienceUser
        from .employee_org_data import EmployeeOrgData
        from .event import Event
        from .extension import Extension
        from .inference_classification import InferenceClassification
        from .license_assignment_state import LicenseAssignmentState
        from .license_details import LicenseDetails
        from .mailbox_settings import MailboxSettings
        from .mail_folder import MailFolder
        from .managed_app_registration import ManagedAppRegistration
        from .managed_device import ManagedDevice
        from .message import Message
        from .object_identity import ObjectIdentity
        from .office_graph_insights import OfficeGraphInsights
        from .onenote import Onenote
        from .online_meeting import OnlineMeeting
        from .on_premises_extension_attributes import OnPremisesExtensionAttributes
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .outlook_user import OutlookUser
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_profile import PasswordProfile
        from .person import Person
        from .planner_user import PlannerUser
        from .presence import Presence
        from .profile_photo import ProfilePhoto
        from .provisioned_plan import ProvisionedPlan
        from .scoped_role_membership import ScopedRoleMembership
        from .service_provisioning_error import ServiceProvisioningError
        from .sign_in_activity import SignInActivity
        from .site import Site
        from .team import Team
        from .todo import Todo
        from .user_activity import UserActivity
        from .user_print import UserPrint
        from .user_settings import UserSettings
        from .user_teamwork import UserTeamwork

        fields: Dict[str, Callable[[Any], None]] = {
            "about_me": lambda n : setattr(self, 'about_me', n.get_str_value()),
            "account_enabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(UserActivity)),
            "age_group": lambda n : setattr(self, 'age_group', n.get_str_value()),
            "agreement_acceptances": lambda n : setattr(self, 'agreement_acceptances', n.get_collection_of_object_values(AgreementAcceptance)),
            "app_role_assignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(AppRoleAssignment)),
            "assigned_licenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(AssignedLicense)),
            "assigned_plans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(AssignedPlan)),
            "authentication": lambda n : setattr(self, 'authentication', n.get_object_value(Authentication)),
            "authorization_info": lambda n : setattr(self, 'authorization_info', n.get_object_value(AuthorizationInfo)),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "business_phones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(Calendar)),
            "calendar_groups": lambda n : setattr(self, 'calendar_groups', n.get_collection_of_object_values(CalendarGroup)),
            "calendar_view": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(Event)),
            "calendars": lambda n : setattr(self, 'calendars', n.get_collection_of_object_values(Calendar)),
            "chats": lambda n : setattr(self, 'chats', n.get_collection_of_object_values(Chat)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "company_name": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "consent_provided_for_minor": lambda n : setattr(self, 'consent_provided_for_minor', n.get_str_value()),
            "contact_folders": lambda n : setattr(self, 'contact_folders', n.get_collection_of_object_values(ContactFolder)),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(Contact)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "created_objects": lambda n : setattr(self, 'created_objects', n.get_collection_of_object_values(DirectoryObject)),
            "creation_type": lambda n : setattr(self, 'creation_type', n.get_str_value()),
            "custom_security_attributes": lambda n : setattr(self, 'custom_security_attributes', n.get_object_value(CustomSecurityAttributeValue)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "device_enrollment_limit": lambda n : setattr(self, 'device_enrollment_limit', n.get_int_value()),
            "device_management_troubleshooting_events": lambda n : setattr(self, 'device_management_troubleshooting_events', n.get_collection_of_object_values(DeviceManagementTroubleshootingEvent)),
            "direct_reports": lambda n : setattr(self, 'direct_reports', n.get_collection_of_object_values(DirectoryObject)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(Drive)),
            "employee_experience": lambda n : setattr(self, 'employee_experience', n.get_object_value(EmployeeExperienceUser)),
            "employee_hire_date": lambda n : setattr(self, 'employee_hire_date', n.get_datetime_value()),
            "employee_id": lambda n : setattr(self, 'employee_id', n.get_str_value()),
            "employee_leave_date_time": lambda n : setattr(self, 'employee_leave_date_time', n.get_datetime_value()),
            "employee_org_data": lambda n : setattr(self, 'employee_org_data', n.get_object_value(EmployeeOrgData)),
            "employee_type": lambda n : setattr(self, 'employee_type', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(Event)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "external_user_state": lambda n : setattr(self, 'external_user_state', n.get_str_value()),
            "external_user_state_change_date_time": lambda n : setattr(self, 'external_user_state_change_date_time', n.get_datetime_value()),
            "fax_number": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "followed_sites": lambda n : setattr(self, 'followed_sites', n.get_collection_of_object_values(Site)),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "hire_date": lambda n : setattr(self, 'hire_date', n.get_datetime_value()),
            "identities": lambda n : setattr(self, 'identities', n.get_collection_of_object_values(ObjectIdentity)),
            "im_addresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "inference_classification": lambda n : setattr(self, 'inference_classification', n.get_object_value(InferenceClassification)),
            "insights": lambda n : setattr(self, 'insights', n.get_object_value(OfficeGraphInsights)),
            "interests": lambda n : setattr(self, 'interests', n.get_collection_of_primitive_values(str)),
            "is_resource_account": lambda n : setattr(self, 'is_resource_account', n.get_bool_value()),
            "job_title": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "joined_teams": lambda n : setattr(self, 'joined_teams', n.get_collection_of_object_values(Team)),
            "last_password_change_date_time": lambda n : setattr(self, 'last_password_change_date_time', n.get_datetime_value()),
            "legal_age_group_classification": lambda n : setattr(self, 'legal_age_group_classification', n.get_str_value()),
            "license_assignment_states": lambda n : setattr(self, 'license_assignment_states', n.get_collection_of_object_values(LicenseAssignmentState)),
            "license_details": lambda n : setattr(self, 'license_details', n.get_collection_of_object_values(LicenseDetails)),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mail_folders": lambda n : setattr(self, 'mail_folders', n.get_collection_of_object_values(MailFolder)),
            "mail_nickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "mailbox_settings": lambda n : setattr(self, 'mailbox_settings', n.get_object_value(MailboxSettings)),
            "managed_app_registrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(ManagedAppRegistration)),
            "managed_devices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(DirectoryObject)),
            "member_of": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(Message)),
            "mobile_phone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "my_site": lambda n : setattr(self, 'my_site', n.get_str_value()),
            "oauth2_permission_grants": lambda n : setattr(self, 'oauth2_permission_grants', n.get_collection_of_object_values(OAuth2PermissionGrant)),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "on_premises_distinguished_name": lambda n : setattr(self, 'on_premises_distinguished_name', n.get_str_value()),
            "on_premises_domain_name": lambda n : setattr(self, 'on_premises_domain_name', n.get_str_value()),
            "on_premises_extension_attributes": lambda n : setattr(self, 'on_premises_extension_attributes', n.get_object_value(OnPremisesExtensionAttributes)),
            "on_premises_immutable_id": lambda n : setattr(self, 'on_premises_immutable_id', n.get_str_value()),
            "on_premises_last_sync_date_time": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "on_premises_provisioning_errors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(OnPremisesProvisioningError)),
            "on_premises_sam_account_name": lambda n : setattr(self, 'on_premises_sam_account_name', n.get_str_value()),
            "on_premises_security_identifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "on_premises_sync_enabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "on_premises_user_principal_name": lambda n : setattr(self, 'on_premises_user_principal_name', n.get_str_value()),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(Onenote)),
            "online_meetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(OnlineMeeting)),
            "other_mails": lambda n : setattr(self, 'other_mails', n.get_collection_of_primitive_values(str)),
            "outlook": lambda n : setattr(self, 'outlook', n.get_object_value(OutlookUser)),
            "owned_devices": lambda n : setattr(self, 'owned_devices', n.get_collection_of_object_values(DirectoryObject)),
            "owned_objects": lambda n : setattr(self, 'owned_objects', n.get_collection_of_object_values(DirectoryObject)),
            "password_policies": lambda n : setattr(self, 'password_policies', n.get_str_value()),
            "password_profile": lambda n : setattr(self, 'password_profile', n.get_object_value(PasswordProfile)),
            "past_projects": lambda n : setattr(self, 'past_projects', n.get_collection_of_primitive_values(str)),
            "people": lambda n : setattr(self, 'people', n.get_collection_of_object_values(Person)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "photos": lambda n : setattr(self, 'photos', n.get_collection_of_object_values(ProfilePhoto)),
            "planner": lambda n : setattr(self, 'planner', n.get_object_value(PlannerUser)),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "preferred_data_location": lambda n : setattr(self, 'preferred_data_location', n.get_str_value()),
            "preferred_language": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "preferred_name": lambda n : setattr(self, 'preferred_name', n.get_str_value()),
            "presence": lambda n : setattr(self, 'presence', n.get_object_value(Presence)),
            "print": lambda n : setattr(self, 'print', n.get_object_value(UserPrint)),
            "provisioned_plans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(ProvisionedPlan)),
            "proxy_addresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "registered_devices": lambda n : setattr(self, 'registered_devices', n.get_collection_of_object_values(DirectoryObject)),
            "responsibilities": lambda n : setattr(self, 'responsibilities', n.get_collection_of_primitive_values(str)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_primitive_values(str)),
            "scoped_role_member_of": lambda n : setattr(self, 'scoped_role_member_of', n.get_collection_of_object_values(ScopedRoleMembership)),
            "security_identifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
            "service_provisioning_errors": lambda n : setattr(self, 'service_provisioning_errors', n.get_collection_of_object_values(ServiceProvisioningError)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(UserSettings)),
            "show_in_address_list": lambda n : setattr(self, 'show_in_address_list', n.get_bool_value()),
            "sign_in_activity": lambda n : setattr(self, 'sign_in_activity', n.get_object_value(SignInActivity)),
            "sign_in_sessions_valid_from_date_time": lambda n : setattr(self, 'sign_in_sessions_valid_from_date_time', n.get_datetime_value()),
            "skills": lambda n : setattr(self, 'skills', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street_address": lambda n : setattr(self, 'street_address', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "teamwork": lambda n : setattr(self, 'teamwork', n.get_object_value(UserTeamwork)),
            "todo": lambda n : setattr(self, 'todo', n.get_object_value(Todo)),
            "transitive_member_of": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
            "usage_location": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "user_type": lambda n : setattr(self, 'user_type', n.get_str_value()),
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
        writer.write_str_value("about_me", self.about_me)
        writer.write_bool_value("account_enabled", self.account_enabled)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_str_value("age_group", self.age_group)
        writer.write_collection_of_object_values("agreement_acceptances", self.agreement_acceptances)
        writer.write_collection_of_object_values("app_role_assignments", self.app_role_assignments)
        writer.write_collection_of_object_values("assigned_licenses", self.assigned_licenses)
        writer.write_collection_of_object_values("assigned_plans", self.assigned_plans)
        writer.write_object_value("authentication", self.authentication)
        writer.write_object_value("authorization_info", self.authorization_info)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_collection_of_primitive_values("business_phones", self.business_phones)
        writer.write_object_value("calendar", self.calendar)
        writer.write_collection_of_object_values("calendar_groups", self.calendar_groups)
        writer.write_collection_of_object_values("calendar_view", self.calendar_view)
        writer.write_collection_of_object_values("calendars", self.calendars)
        writer.write_collection_of_object_values("chats", self.chats)
        writer.write_str_value("city", self.city)
        writer.write_str_value("company_name", self.company_name)
        writer.write_str_value("consent_provided_for_minor", self.consent_provided_for_minor)
        writer.write_collection_of_object_values("contact_folders", self.contact_folders)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("country", self.country)
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_collection_of_object_values("created_objects", self.created_objects)
        writer.write_str_value("creation_type", self.creation_type)
        writer.write_object_value("custom_security_attributes", self.custom_security_attributes)
        writer.write_str_value("department", self.department)
        writer.write_int_value("device_enrollment_limit", self.device_enrollment_limit)
        writer.write_collection_of_object_values("device_management_troubleshooting_events", self.device_management_troubleshooting_events)
        writer.write_collection_of_object_values("direct_reports", self.direct_reports)
        writer.write_str_value("display_name", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_object_value("employee_experience", self.employee_experience)
        writer.write_datetime_value("employee_hire_date", self.employee_hire_date)
        writer.write_str_value("employee_id", self.employee_id)
        writer.write_datetime_value("employee_leave_date_time", self.employee_leave_date_time)
        writer.write_object_value("employee_org_data", self.employee_org_data)
        writer.write_str_value("employee_type", self.employee_type)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("external_user_state", self.external_user_state)
        writer.write_datetime_value("external_user_state_change_date_time", self.external_user_state_change_date_time)
        writer.write_str_value("fax_number", self.fax_number)
        writer.write_collection_of_object_values("followed_sites", self.followed_sites)
        writer.write_str_value("given_name", self.given_name)
        writer.write_datetime_value("hire_date", self.hire_date)
        writer.write_collection_of_object_values("identities", self.identities)
        writer.write_collection_of_primitive_values("im_addresses", self.im_addresses)
        writer.write_object_value("inference_classification", self.inference_classification)
        writer.write_object_value("insights", self.insights)
        writer.write_collection_of_primitive_values("interests", self.interests)
        writer.write_bool_value("is_resource_account", self.is_resource_account)
        writer.write_str_value("job_title", self.job_title)
        writer.write_collection_of_object_values("joined_teams", self.joined_teams)
        writer.write_datetime_value("last_password_change_date_time", self.last_password_change_date_time)
        writer.write_str_value("legal_age_group_classification", self.legal_age_group_classification)
        writer.write_collection_of_object_values("license_assignment_states", self.license_assignment_states)
        writer.write_collection_of_object_values("license_details", self.license_details)
        writer.write_str_value("mail", self.mail)
        writer.write_collection_of_object_values("mail_folders", self.mail_folders)
        writer.write_str_value("mail_nickname", self.mail_nickname)
        writer.write_object_value("mailbox_settings", self.mailbox_settings)
        writer.write_collection_of_object_values("managed_app_registrations", self.managed_app_registrations)
        writer.write_collection_of_object_values("managed_devices", self.managed_devices)
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("member_of", self.member_of)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_str_value("mobile_phone", self.mobile_phone)
        writer.write_str_value("my_site", self.my_site)
        writer.write_collection_of_object_values("oauth2_permission_grants", self.oauth2_permission_grants)
        writer.write_str_value("office_location", self.office_location)
        writer.write_str_value("on_premises_distinguished_name", self.on_premises_distinguished_name)
        writer.write_str_value("on_premises_domain_name", self.on_premises_domain_name)
        writer.write_object_value("on_premises_extension_attributes", self.on_premises_extension_attributes)
        writer.write_str_value("on_premises_immutable_id", self.on_premises_immutable_id)
        writer.write_datetime_value("on_premises_last_sync_date_time", self.on_premises_last_sync_date_time)
        writer.write_collection_of_object_values("on_premises_provisioning_errors", self.on_premises_provisioning_errors)
        writer.write_str_value("on_premises_sam_account_name", self.on_premises_sam_account_name)
        writer.write_str_value("on_premises_security_identifier", self.on_premises_security_identifier)
        writer.write_bool_value("on_premises_sync_enabled", self.on_premises_sync_enabled)
        writer.write_str_value("on_premises_user_principal_name", self.on_premises_user_principal_name)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("online_meetings", self.online_meetings)
        writer.write_collection_of_primitive_values("other_mails", self.other_mails)
        writer.write_object_value("outlook", self.outlook)
        writer.write_collection_of_object_values("owned_devices", self.owned_devices)
        writer.write_collection_of_object_values("owned_objects", self.owned_objects)
        writer.write_str_value("password_policies", self.password_policies)
        writer.write_object_value("password_profile", self.password_profile)
        writer.write_collection_of_primitive_values("past_projects", self.past_projects)
        writer.write_collection_of_object_values("people", self.people)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("photos", self.photos)
        writer.write_object_value("planner", self.planner)
        writer.write_str_value("postal_code", self.postal_code)
        writer.write_str_value("preferred_data_location", self.preferred_data_location)
        writer.write_str_value("preferred_language", self.preferred_language)
        writer.write_str_value("preferred_name", self.preferred_name)
        writer.write_object_value("presence", self.presence)
        writer.write_object_value("print", self.print)
        writer.write_collection_of_object_values("provisioned_plans", self.provisioned_plans)
        writer.write_collection_of_primitive_values("proxy_addresses", self.proxy_addresses)
        writer.write_collection_of_object_values("registered_devices", self.registered_devices)
        writer.write_collection_of_primitive_values("responsibilities", self.responsibilities)
        writer.write_collection_of_primitive_values("schools", self.schools)
        writer.write_collection_of_object_values("scoped_role_member_of", self.scoped_role_member_of)
        writer.write_str_value("security_identifier", self.security_identifier)
        writer.write_collection_of_object_values("service_provisioning_errors", self.service_provisioning_errors)
        writer.write_object_value("settings", self.settings)
        writer.write_bool_value("show_in_address_list", self.show_in_address_list)
        writer.write_object_value("sign_in_activity", self.sign_in_activity)
        writer.write_datetime_value("sign_in_sessions_valid_from_date_time", self.sign_in_sessions_valid_from_date_time)
        writer.write_collection_of_primitive_values("skills", self.skills)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street_address", self.street_address)
        writer.write_str_value("surname", self.surname)
        writer.write_object_value("teamwork", self.teamwork)
        writer.write_object_value("todo", self.todo)
        writer.write_collection_of_object_values("transitive_member_of", self.transitive_member_of)
        writer.write_str_value("usage_location", self.usage_location)
        writer.write_str_value("user_principal_name", self.user_principal_name)
        writer.write_str_value("user_type", self.user_type)
    

