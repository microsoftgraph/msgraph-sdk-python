from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .adhoc_call import AdhocCall
    from .agreement_acceptance import AgreementAcceptance
    from .app_role_assignment import AppRoleAssignment
    from .assigned_license import AssignedLicense
    from .assigned_plan import AssignedPlan
    from .authentication import Authentication
    from .authorization_info import AuthorizationInfo
    from .calendar import Calendar
    from .calendar_group import CalendarGroup
    from .chat import Chat
    from .cloud_clipboard_root import CloudClipboardRoot
    from .cloud_p_c import CloudPC
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
    from .item_insights import ItemInsights
    from .license_assignment_state import LicenseAssignmentState
    from .license_details import LicenseDetails
    from .mailbox_settings import MailboxSettings
    from .mail_folder import MailFolder
    from .managed_app_registration import ManagedAppRegistration
    from .managed_device import ManagedDevice
    from .message import Message
    from .object_identity import ObjectIdentity
    from .onenote import Onenote
    from .online_meeting import OnlineMeeting
    from .on_premises_extension_attributes import OnPremisesExtensionAttributes
    from .on_premises_provisioning_error import OnPremisesProvisioningError
    from .on_premises_sync_behavior import OnPremisesSyncBehavior
    from .outlook_user import OutlookUser
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .password_profile import PasswordProfile
    from .person import Person
    from .planner_user import PlannerUser
    from .presence import Presence
    from .profile_photo import ProfilePhoto
    from .provisioned_plan import ProvisionedPlan
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .scoped_role_membership import ScopedRoleMembership
    from .service_provisioning_error import ServiceProvisioningError
    from .sign_in_activity import SignInActivity
    from .site import Site
    from .team import Team
    from .todo import Todo
    from .user_activity import UserActivity
    from .user_data_security_and_governance import UserDataSecurityAndGovernance
    from .user_print import UserPrint
    from .user_settings import UserSettings
    from .user_solution_root import UserSolutionRoot
    from .user_teamwork import UserTeamwork

from .directory_object import DirectoryObject

@dataclass
class User(DirectoryObject, Parsable):
    """
    Represents a Microsoft Entra user account.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.user"
    # A freeform text entry field for the user to describe themselves. Returned only on $select.
    about_me: Optional[str] = None
    # true if the account is enabled; otherwise, false. This property is required when a user is created. Returned only on $select. Supports $filter (eq, ne, not, and in).
    account_enabled: Optional[bool] = None
    # The user's activities across devices. Read-only. Nullable.
    activities: Optional[list[UserActivity]] = None
    # Ad hoc calls associated with the user. Read-only. Nullable.
    adhoc_calls: Optional[list[AdhocCall]] = None
    # Sets the age group of the user. Allowed values: null, Minor, NotAdult, and Adult. For more information, see legal age group property definitions. Returned only on $select. Supports $filter (eq, ne, not, and in).
    age_group: Optional[str] = None
    # The user's terms of use acceptance statuses. Read-only. Nullable.
    agreement_acceptances: Optional[list[AgreementAcceptance]] = None
    # Represents the app roles a user is granted for an application. Supports $expand.
    app_role_assignments: Optional[list[AppRoleAssignment]] = None
    # The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate between directly assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly assigned and inherited licenses. Not nullable. Returned only on $select. Supports $filter (eq, not, /$count eq 0, /$count ne 0).
    assigned_licenses: Optional[list[AssignedLicense]] = None
    # The plans that are assigned to the user. Read-only. Not nullable. Returned only on $select. Supports $filter (eq and not).
    assigned_plans: Optional[list[AssignedPlan]] = None
    # The authentication methods that are supported for the user.
    authentication: Optional[Authentication] = None
    # The authorizationInfo property
    authorization_info: Optional[AuthorizationInfo] = None
    # The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Returned only on $select.
    birthday: Optional[datetime.datetime] = None
    # The telephone numbers for the user. NOTE: Although it's a string collection, only one number can be set for this property. Read-only for users synced from the on-premises directory. Returned by default. Supports $filter (eq, not, ge, le, startsWith).
    business_phones: Optional[list[str]] = None
    # The user's primary calendar. Read-only.
    calendar: Optional[Calendar] = None
    # The user's calendar groups. Read-only. Nullable.
    calendar_groups: Optional[list[CalendarGroup]] = None
    # The calendar view for the calendar. Read-only. Nullable.
    calendar_view: Optional[list[Event]] = None
    # The user's calendars. Read-only. Nullable.
    calendars: Optional[list[Calendar]] = None
    # The chats property
    chats: Optional[list[Chat]] = None
    # The city where the user is located. Maximum length is 128 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    city: Optional[str] = None
    # The cloudClipboard property
    cloud_clipboard: Optional[CloudClipboardRoot] = None
    # The user's Cloud PCs. Read-only. Nullable.
    cloud_p_cs: Optional[list[CloudPC]] = None
    # The name of the company that the user is associated with. This property can be useful for describing the company that a guest comes from. The maximum length is 64 characters.Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    company_name: Optional[str] = None
    # Sets whether consent was obtained for minors. Allowed values: null, Granted, Denied, and NotRequired. For more information, see legal age group property definitions. Returned only on $select. Supports $filter (eq, ne, not, and in).
    consent_provided_for_minor: Optional[str] = None
    # The user's contacts folders. Read-only. Nullable.
    contact_folders: Optional[list[ContactFolder]] = None
    # The user's contacts. Read-only. Nullable.
    contacts: Optional[list[Contact]] = None
    # The country or region where the user is located; for example, US or UK. Maximum length is 128 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    country: Optional[str] = None
    # The date and time the user was created, in ISO 8601 format and UTC. The value can't be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in).
    created_date_time: Optional[datetime.datetime] = None
    # Directory objects that the user created. Read-only. Nullable.
    created_objects: Optional[list[DirectoryObject]] = None
    # Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by a guest signing up through a link that is part of a user flow (SelfServiceSignUp). Read-only.Returned only on $select. Supports $filter (eq, ne, not, in).
    creation_type: Optional[str] = None
    # An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Returned only on $select. Supports $filter (eq, ne, not, startsWith). The filter value is case-sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.
    custom_security_attributes: Optional[CustomSecurityAttributeValue] = None
    # The data security and governance settings for the user. Read-only. Nullable.
    data_security_and_governance: Optional[UserDataSecurityAndGovernance] = None
    # The name of the department in which the user works. Maximum length is 64 characters. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, and eq on null values).
    department: Optional[str] = None
    # The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.
    device_enrollment_limit: Optional[int] = None
    # The list of troubleshooting events for this user.
    device_management_troubleshooting_events: Optional[list[DeviceManagementTroubleshootingEvent]] = None
    # The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.
    direct_reports: Optional[list[DirectoryObject]] = None
    # The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and family name. This property is required when a user is created and it can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderby, and $search.
    display_name: Optional[str] = None
    # The user's OneDrive. Read-only.
    drive: Optional[Drive] = None
    # A collection of drives available for this user. Read-only.
    drives: Optional[list[Drive]] = None
    # The employeeExperience property
    employee_experience: Optional[EmployeeExperienceUser] = None
    # The date and time when the user was hired or will start work in a future hire. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in).
    employee_hire_date: Optional[datetime.datetime] = None
    # The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    employee_id: Optional[str] = None
    # The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs at least one of the following Microsoft Entra roles: Lifecycle Workflows Administrator (least privilege), Global Reader. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user.
    employee_leave_date_time: Optional[datetime.datetime] = None
    # Represents organization data (for example, division and costCenter) associated with a user. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in).
    employee_org_data: Optional[EmployeeOrgData] = None
    # Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, startsWith).
    employee_type: Optional[str] = None
    # The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.
    events: Optional[list[Event]] = None
    # The collection of open extensions defined for the user. Read-only. Supports $expand. Nullable.
    extensions: Optional[list[Extension]] = None
    # For a guest invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Returned only on $select. Supports $filter (eq, ne, not , in).
    external_user_state: Optional[str] = None
    # Shows the timestamp for the latest change to the externalUserState property. Returned only on $select. Supports $filter (eq, ne, not , in).
    external_user_state_change_date_time: Optional[datetime.datetime] = None
    # The fax number of the user. Returned only on $select. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    fax_number: Optional[str] = None
    # The followedSites property
    followed_sites: Optional[list[Site]] = None
    # The given name (first name) of the user. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    given_name: Optional[str] = None
    # The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Returned only on $select.  Note: This property is specific to SharePoint in Microsoft 365. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.
    hire_date: Optional[datetime.datetime] = None
    # Represents the identities that can be used to sign in to this user account. Microsoft (also known as a local account), organizations, or social identity providers such as Facebook, Google, and Microsoft can provide identity and tie it to a user account. It might contain multiple items with the same signInType value. Returned only on $select.  Supports $filter (eq) with limitations.
    identities: Optional[list[ObjectIdentity]] = None
    # The instant message voice-over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Returned only on $select. Supports $filter (eq, not, ge, le, startsWith).
    im_addresses: Optional[list[str]] = None
    # Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
    inference_classification: Optional[InferenceClassification] = None
    # Represents relationships between a user and items such as OneDrive for work or school documents, calculated using advanced analytics and machine learning techniques. Read-only. Nullable.
    insights: Optional[ItemInsights] = None
    # A list for the user to describe their interests. Returned only on $select.
    interests: Optional[list[str]] = None
    # true if the user is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a user who is a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Returned only on $select.
    is_management_restricted: Optional[bool] = None
    # Don't use – reserved for future use.
    is_resource_account: Optional[bool] = None
    # The user's job title. Maximum length is 128 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    job_title: Optional[str] = None
    # The joinedTeams property
    joined_teams: Optional[list[Team]] = None
    # The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned only on $select.
    last_password_change_date_time: Optional[datetime.datetime] = None
    # Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, Undefined,  MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult, and Adult. For more information, see legal age group property definitions. Returned only on $select.
    legal_age_group_classification: Optional[str] = None
    # State of license assignments for this user. Also indicates licenses that are directly assigned or the user inherited through group memberships. Read-only. Returned only on $select.
    license_assignment_states: Optional[list[LicenseAssignmentState]] = None
    # A collection of this user's license details. Read-only.
    license_details: Optional[list[LicenseDetails]] = None
    # The SMTP address for the user, for example, jeff@contoso.com. Changes to this property update the user's proxyAddresses collection to include the value as an SMTP address. This property can't contain accent characters.  NOTE: We don't recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).
    mail: Optional[str] = None
    # The user's mail folders. Read-only. Nullable.
    mail_folders: Optional[list[MailFolder]] = None
    # The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    mail_nickname: Optional[str] = None
    # Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Returned only on $select.
    mailbox_settings: Optional[MailboxSettings] = None
    # Zero or more managed app registrations that belong to the user.
    managed_app_registrations: Optional[list[ManagedAppRegistration]] = None
    # The managed devices associated with the user.
    managed_devices: Optional[list[ManagedDevice]] = None
    # The user or contact that is this user's manager. Read-only. Supports $expand.
    manager: Optional[DirectoryObject] = None
    # The groups and directory roles that the user is a member of. Read-only. Nullable. Supports $expand.
    member_of: Optional[list[DirectoryObject]] = None
    # The messages in a mailbox or folder. Read-only. Nullable.
    messages: Optional[list[Message]] = None
    # The primary cellular telephone number for the user. Read-only for users synced from the on-premises directory. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values) and $search.
    mobile_phone: Optional[str] = None
    # The URL for the user's site. Returned only on $select.
    my_site: Optional[str] = None
    # The oauth2PermissionGrants property
    oauth2_permission_grants: Optional[list[OAuth2PermissionGrant]] = None
    # The office location in the user's place of business. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    office_location: Optional[str] = None
    # Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select.
    on_premises_distinguished_name: Optional[str] = None
    # Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select.
    on_premises_domain_name: Optional[str] = None
    # Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. Each attribute can store up to 1024 characters. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during the creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Returned only on $select. Supports $filter (eq, ne, not, in).
    on_premises_extension_attributes: Optional[OnPremisesExtensionAttributes] = None
    # This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ characters can't be used when specifying this property. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in).
    on_premises_immutable_id: Optional[str] = None
    # Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in).
    on_premises_last_sync_date_time: Optional[datetime.datetime] = None
    # Errors when using Microsoft synchronization product during provisioning. Returned only on $select. Supports $filter (eq, not, ge, le).
    on_premises_provisioning_errors: Optional[list[OnPremisesProvisioningError]] = None
    # Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith).
    on_premises_sam_account_name: Optional[str] = None
    # Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Returned only on $select. Supports $filter (eq including on null values).
    on_premises_security_identifier: Optional[str] = None
    # The onPremisesSyncBehavior property
    on_premises_sync_behavior: Optional[OnPremisesSyncBehavior] = None
    # true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Microsoft Entra ID. Read-only. Returned only on $select. Supports $filter (eq, ne, not, in, and eq on null values).
    on_premises_sync_enabled: Optional[bool] = None
    # Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith).
    on_premises_user_principal_name: Optional[str] = None
    # The onenote property
    onenote: Optional[Onenote] = None
    # Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.
    online_meetings: Optional[list[OnlineMeeting]] = None
    # A list of other email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Can store up to 250 values, each with a limit of 250 characters. NOTE: This property can't contain accent characters. Returned only on $select. Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).
    other_mails: Optional[list[str]] = None
    # The outlook property
    outlook: Optional[OutlookUser] = None
    # Devices the user owns. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owned_devices: Optional[list[DirectoryObject]] = None
    # Directory objects the user owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
    owned_objects: Optional[list[DirectoryObject]] = None
    # Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two might be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. Returned only on $select. For more information on the default password policies, see Microsoft Entra password policies. Supports $filter (ne, not, and eq on null values).
    password_policies: Optional[str] = None
    # Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Returned only on $select. Supports $filter (eq, ne, not, in, and eq on null values). To update this property:  User-PasswordProfile.ReadWrite.All is the least privileged permission to update this property.  In delegated scenarios, the User Administrator Microsoft Entra role is the least privileged admin role supported to update this property for nonadmin users. Privileged Authentication Administrator is the least privileged role that's allowed to update this property for all administrators in the tenant. In general, the signed-in user must have a higher privileged administrator role as indicated in Who can reset passwords.  In app-only scenarios, the calling app must be assigned a supported permission and at least the User Administrator Microsoft Entra role.
    password_profile: Optional[PasswordProfile] = None
    # A list for the user to enumerate their past projects. Returned only on $select.
    past_projects: Optional[list[str]] = None
    # People that are relevant to the user. Read-only. Nullable.
    people: Optional[list[Person]] = None
    # List all resource-specific permission grants of a user.
    permission_grants: Optional[list[ResourceSpecificPermissionGrant]] = None
    # The user's profile photo. Read-only.
    photo: Optional[ProfilePhoto] = None
    # The collection of the user's profile photos in different sizes. Read-only.
    photos: Optional[list[ProfilePhoto]] = None
    # Entry-point to the Planner resource that might exist for a user. Read-only.
    planner: Optional[PlannerUser] = None
    # The postal code for the user's postal address. The postal code is specific to the user's country or region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
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
    provisioned_plans: Optional[list[ProvisionedPlan]] = None
    # For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address, while those addresses prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of 10 unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Returned only on $select. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
    proxy_addresses: Optional[list[str]] = None
    # Devices that are registered for the user. Read-only. Nullable. Supports $expand and returns up to 100 objects.
    registered_devices: Optional[list[DirectoryObject]] = None
    # A list for the user to enumerate their responsibilities. Returned only on $select.
    responsibilities: Optional[list[str]] = None
    # A list for the user to enumerate the schools they attended. Returned only on $select.
    schools: Optional[list[str]] = None
    # The scopedRoleMemberOf property
    scoped_role_member_of: Optional[list[ScopedRoleMembership]] = None
    # Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).
    security_identifier: Optional[str] = None
    # Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a user object.  Supports $filter (eq, not, for isResolved and serviceInstance).
    service_provisioning_errors: Optional[list[ServiceProvisioningError]] = None
    # The settings property
    settings: Optional[UserSettings] = None
    # Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.
    show_in_address_list: Optional[bool] = None
    # Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Returned only on $select. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note: Details for this property require a Microsoft Entra ID P1 or P2 license and the AuditLog.Read.All permission.This property isn't returned for a user who never signed in or last signed in before April 2020.
    sign_in_activity: Optional[SignInActivity] = None
    # Any refresh tokens or session tokens (session cookies) issued before this time are invalid. Applications get an error when using an invalid refresh or session token to acquire a delegated access token (to access APIs such as Microsoft Graph). If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Read-only. Use revokeSignInSessions to reset. Returned only on $select.
    sign_in_sessions_valid_from_date_time: Optional[datetime.datetime] = None
    # A list for the user to enumerate their skills. Returned only on $select.
    skills: Optional[list[str]] = None
    # The identifier that relates the user to the working time schedule triggers. Read-Only. Nullable
    solutions: Optional[UserSolutionRoot] = None
    # The users and groups responsible for this guest's privileges in the tenant and keeping the guest's information and access updated. (HTTP Methods: GET, POST, DELETE.). Supports $expand.
    sponsors: Optional[list[DirectoryObject]] = None
    # The state or province in the user's address. Maximum length is 128 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    state: Optional[str] = None
    # The street address of the user's place of business. Maximum length is 1,024 characters. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    street_address: Optional[str] = None
    # The user's surname (family name or last name). Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    surname: Optional[str] = None
    # A container for Microsoft Teams features available for the user. Read-only. Nullable.
    teamwork: Optional[UserTeamwork] = None
    # Represents the To Do services available to a user.
    todo: Optional[Todo] = None
    # The groups, including nested groups, and directory roles that a user is a member of. Nullable.
    transitive_member_of: Optional[list[DirectoryObject]] = None
    # A two-letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirements to check for availability of services in countries/regions. Examples include: US, JP, and GB. Not nullable. Returned only on $select. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    usage_location: Optional[str] = None
    # The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822. By convention, this value should map to the user's email name. The general format is alias@domain, where the domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property can't contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderby.
    user_principal_name: Optional[str] = None
    # A string value that can be used to classify user types in your directory. The possible values are Member and Guest. Returned only on $select. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for members and guests, see What are the default user permissions in Microsoft Entra ID?
    user_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> User:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return User()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .adhoc_call import AdhocCall
        from .agreement_acceptance import AgreementAcceptance
        from .app_role_assignment import AppRoleAssignment
        from .assigned_license import AssignedLicense
        from .assigned_plan import AssignedPlan
        from .authentication import Authentication
        from .authorization_info import AuthorizationInfo
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .chat import Chat
        from .cloud_clipboard_root import CloudClipboardRoot
        from .cloud_p_c import CloudPC
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
        from .item_insights import ItemInsights
        from .license_assignment_state import LicenseAssignmentState
        from .license_details import LicenseDetails
        from .mailbox_settings import MailboxSettings
        from .mail_folder import MailFolder
        from .managed_app_registration import ManagedAppRegistration
        from .managed_device import ManagedDevice
        from .message import Message
        from .object_identity import ObjectIdentity
        from .onenote import Onenote
        from .online_meeting import OnlineMeeting
        from .on_premises_extension_attributes import OnPremisesExtensionAttributes
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .outlook_user import OutlookUser
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_profile import PasswordProfile
        from .person import Person
        from .planner_user import PlannerUser
        from .presence import Presence
        from .profile_photo import ProfilePhoto
        from .provisioned_plan import ProvisionedPlan
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .scoped_role_membership import ScopedRoleMembership
        from .service_provisioning_error import ServiceProvisioningError
        from .sign_in_activity import SignInActivity
        from .site import Site
        from .team import Team
        from .todo import Todo
        from .user_activity import UserActivity
        from .user_data_security_and_governance import UserDataSecurityAndGovernance
        from .user_print import UserPrint
        from .user_settings import UserSettings
        from .user_solution_root import UserSolutionRoot
        from .user_teamwork import UserTeamwork

        from .adhoc_call import AdhocCall
        from .agreement_acceptance import AgreementAcceptance
        from .app_role_assignment import AppRoleAssignment
        from .assigned_license import AssignedLicense
        from .assigned_plan import AssignedPlan
        from .authentication import Authentication
        from .authorization_info import AuthorizationInfo
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .chat import Chat
        from .cloud_clipboard_root import CloudClipboardRoot
        from .cloud_p_c import CloudPC
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
        from .item_insights import ItemInsights
        from .license_assignment_state import LicenseAssignmentState
        from .license_details import LicenseDetails
        from .mailbox_settings import MailboxSettings
        from .mail_folder import MailFolder
        from .managed_app_registration import ManagedAppRegistration
        from .managed_device import ManagedDevice
        from .message import Message
        from .object_identity import ObjectIdentity
        from .onenote import Onenote
        from .online_meeting import OnlineMeeting
        from .on_premises_extension_attributes import OnPremisesExtensionAttributes
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .outlook_user import OutlookUser
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .password_profile import PasswordProfile
        from .person import Person
        from .planner_user import PlannerUser
        from .presence import Presence
        from .profile_photo import ProfilePhoto
        from .provisioned_plan import ProvisionedPlan
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .scoped_role_membership import ScopedRoleMembership
        from .service_provisioning_error import ServiceProvisioningError
        from .sign_in_activity import SignInActivity
        from .site import Site
        from .team import Team
        from .todo import Todo
        from .user_activity import UserActivity
        from .user_data_security_and_governance import UserDataSecurityAndGovernance
        from .user_print import UserPrint
        from .user_settings import UserSettings
        from .user_solution_root import UserSolutionRoot
        from .user_teamwork import UserTeamwork

        fields: dict[str, Callable[[Any], None]] = {
            "aboutMe": lambda n : setattr(self, 'about_me', n.get_str_value()),
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(UserActivity)),
            "adhocCalls": lambda n : setattr(self, 'adhoc_calls', n.get_collection_of_object_values(AdhocCall)),
            "ageGroup": lambda n : setattr(self, 'age_group', n.get_str_value()),
            "agreementAcceptances": lambda n : setattr(self, 'agreement_acceptances', n.get_collection_of_object_values(AgreementAcceptance)),
            "appRoleAssignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(AppRoleAssignment)),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(AssignedLicense)),
            "assignedPlans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(AssignedPlan)),
            "authentication": lambda n : setattr(self, 'authentication', n.get_object_value(Authentication)),
            "authorizationInfo": lambda n : setattr(self, 'authorization_info', n.get_object_value(AuthorizationInfo)),
            "birthday": lambda n : setattr(self, 'birthday', n.get_datetime_value()),
            "businessPhones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(Calendar)),
            "calendarGroups": lambda n : setattr(self, 'calendar_groups', n.get_collection_of_object_values(CalendarGroup)),
            "calendarView": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(Event)),
            "calendars": lambda n : setattr(self, 'calendars', n.get_collection_of_object_values(Calendar)),
            "chats": lambda n : setattr(self, 'chats', n.get_collection_of_object_values(Chat)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "cloudClipboard": lambda n : setattr(self, 'cloud_clipboard', n.get_object_value(CloudClipboardRoot)),
            "cloudPCs": lambda n : setattr(self, 'cloud_p_cs', n.get_collection_of_object_values(CloudPC)),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "consentProvidedForMinor": lambda n : setattr(self, 'consent_provided_for_minor', n.get_str_value()),
            "contactFolders": lambda n : setattr(self, 'contact_folders', n.get_collection_of_object_values(ContactFolder)),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(Contact)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdObjects": lambda n : setattr(self, 'created_objects', n.get_collection_of_object_values(DirectoryObject)),
            "creationType": lambda n : setattr(self, 'creation_type', n.get_str_value()),
            "customSecurityAttributes": lambda n : setattr(self, 'custom_security_attributes', n.get_object_value(CustomSecurityAttributeValue)),
            "dataSecurityAndGovernance": lambda n : setattr(self, 'data_security_and_governance', n.get_object_value(UserDataSecurityAndGovernance)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "deviceEnrollmentLimit": lambda n : setattr(self, 'device_enrollment_limit', n.get_int_value()),
            "deviceManagementTroubleshootingEvents": lambda n : setattr(self, 'device_management_troubleshooting_events', n.get_collection_of_object_values(DeviceManagementTroubleshootingEvent)),
            "directReports": lambda n : setattr(self, 'direct_reports', n.get_collection_of_object_values(DirectoryObject)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(Drive)),
            "employeeExperience": lambda n : setattr(self, 'employee_experience', n.get_object_value(EmployeeExperienceUser)),
            "employeeHireDate": lambda n : setattr(self, 'employee_hire_date', n.get_datetime_value()),
            "employeeId": lambda n : setattr(self, 'employee_id', n.get_str_value()),
            "employeeLeaveDateTime": lambda n : setattr(self, 'employee_leave_date_time', n.get_datetime_value()),
            "employeeOrgData": lambda n : setattr(self, 'employee_org_data', n.get_object_value(EmployeeOrgData)),
            "employeeType": lambda n : setattr(self, 'employee_type', n.get_str_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(Event)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "externalUserState": lambda n : setattr(self, 'external_user_state', n.get_str_value()),
            "externalUserStateChangeDateTime": lambda n : setattr(self, 'external_user_state_change_date_time', n.get_datetime_value()),
            "faxNumber": lambda n : setattr(self, 'fax_number', n.get_str_value()),
            "followedSites": lambda n : setattr(self, 'followed_sites', n.get_collection_of_object_values(Site)),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "hireDate": lambda n : setattr(self, 'hire_date', n.get_datetime_value()),
            "identities": lambda n : setattr(self, 'identities', n.get_collection_of_object_values(ObjectIdentity)),
            "imAddresses": lambda n : setattr(self, 'im_addresses', n.get_collection_of_primitive_values(str)),
            "inferenceClassification": lambda n : setattr(self, 'inference_classification', n.get_object_value(InferenceClassification)),
            "insights": lambda n : setattr(self, 'insights', n.get_object_value(ItemInsights)),
            "interests": lambda n : setattr(self, 'interests', n.get_collection_of_primitive_values(str)),
            "isManagementRestricted": lambda n : setattr(self, 'is_management_restricted', n.get_bool_value()),
            "isResourceAccount": lambda n : setattr(self, 'is_resource_account', n.get_bool_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "joinedTeams": lambda n : setattr(self, 'joined_teams', n.get_collection_of_object_values(Team)),
            "lastPasswordChangeDateTime": lambda n : setattr(self, 'last_password_change_date_time', n.get_datetime_value()),
            "legalAgeGroupClassification": lambda n : setattr(self, 'legal_age_group_classification', n.get_str_value()),
            "licenseAssignmentStates": lambda n : setattr(self, 'license_assignment_states', n.get_collection_of_object_values(LicenseAssignmentState)),
            "licenseDetails": lambda n : setattr(self, 'license_details', n.get_collection_of_object_values(LicenseDetails)),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailFolders": lambda n : setattr(self, 'mail_folders', n.get_collection_of_object_values(MailFolder)),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "mailboxSettings": lambda n : setattr(self, 'mailbox_settings', n.get_object_value(MailboxSettings)),
            "managedAppRegistrations": lambda n : setattr(self, 'managed_app_registrations', n.get_collection_of_object_values(ManagedAppRegistration)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(DirectoryObject)),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(Message)),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "mySite": lambda n : setattr(self, 'my_site', n.get_str_value()),
            "oauth2PermissionGrants": lambda n : setattr(self, 'oauth2_permission_grants', n.get_collection_of_object_values(OAuth2PermissionGrant)),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "onPremisesDistinguishedName": lambda n : setattr(self, 'on_premises_distinguished_name', n.get_str_value()),
            "onPremisesDomainName": lambda n : setattr(self, 'on_premises_domain_name', n.get_str_value()),
            "onPremisesExtensionAttributes": lambda n : setattr(self, 'on_premises_extension_attributes', n.get_object_value(OnPremisesExtensionAttributes)),
            "onPremisesImmutableId": lambda n : setattr(self, 'on_premises_immutable_id', n.get_str_value()),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesProvisioningErrors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(OnPremisesProvisioningError)),
            "onPremisesSamAccountName": lambda n : setattr(self, 'on_premises_sam_account_name', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "onPremisesSyncBehavior": lambda n : setattr(self, 'on_premises_sync_behavior', n.get_object_value(OnPremisesSyncBehavior)),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "onPremisesUserPrincipalName": lambda n : setattr(self, 'on_premises_user_principal_name', n.get_str_value()),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(Onenote)),
            "onlineMeetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(OnlineMeeting)),
            "otherMails": lambda n : setattr(self, 'other_mails', n.get_collection_of_primitive_values(str)),
            "outlook": lambda n : setattr(self, 'outlook', n.get_object_value(OutlookUser)),
            "ownedDevices": lambda n : setattr(self, 'owned_devices', n.get_collection_of_object_values(DirectoryObject)),
            "ownedObjects": lambda n : setattr(self, 'owned_objects', n.get_collection_of_object_values(DirectoryObject)),
            "passwordPolicies": lambda n : setattr(self, 'password_policies', n.get_str_value()),
            "passwordProfile": lambda n : setattr(self, 'password_profile', n.get_object_value(PasswordProfile)),
            "pastProjects": lambda n : setattr(self, 'past_projects', n.get_collection_of_primitive_values(str)),
            "people": lambda n : setattr(self, 'people', n.get_collection_of_object_values(Person)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(ResourceSpecificPermissionGrant)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "photos": lambda n : setattr(self, 'photos', n.get_collection_of_object_values(ProfilePhoto)),
            "planner": lambda n : setattr(self, 'planner', n.get_object_value(PlannerUser)),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "preferredDataLocation": lambda n : setattr(self, 'preferred_data_location', n.get_str_value()),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "preferredName": lambda n : setattr(self, 'preferred_name', n.get_str_value()),
            "presence": lambda n : setattr(self, 'presence', n.get_object_value(Presence)),
            "print": lambda n : setattr(self, 'print', n.get_object_value(UserPrint)),
            "provisionedPlans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(ProvisionedPlan)),
            "proxyAddresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "registeredDevices": lambda n : setattr(self, 'registered_devices', n.get_collection_of_object_values(DirectoryObject)),
            "responsibilities": lambda n : setattr(self, 'responsibilities', n.get_collection_of_primitive_values(str)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_primitive_values(str)),
            "scopedRoleMemberOf": lambda n : setattr(self, 'scoped_role_member_of', n.get_collection_of_object_values(ScopedRoleMembership)),
            "securityIdentifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
            "serviceProvisioningErrors": lambda n : setattr(self, 'service_provisioning_errors', n.get_collection_of_object_values(ServiceProvisioningError)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(UserSettings)),
            "showInAddressList": lambda n : setattr(self, 'show_in_address_list', n.get_bool_value()),
            "signInActivity": lambda n : setattr(self, 'sign_in_activity', n.get_object_value(SignInActivity)),
            "signInSessionsValidFromDateTime": lambda n : setattr(self, 'sign_in_sessions_valid_from_date_time', n.get_datetime_value()),
            "skills": lambda n : setattr(self, 'skills', n.get_collection_of_primitive_values(str)),
            "solutions": lambda n : setattr(self, 'solutions', n.get_object_value(UserSolutionRoot)),
            "sponsors": lambda n : setattr(self, 'sponsors', n.get_collection_of_object_values(DirectoryObject)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "streetAddress": lambda n : setattr(self, 'street_address', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "teamwork": lambda n : setattr(self, 'teamwork', n.get_object_value(UserTeamwork)),
            "todo": lambda n : setattr(self, 'todo', n.get_object_value(Todo)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
            "usageLocation": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("aboutMe", self.about_me)
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_collection_of_object_values("adhocCalls", self.adhoc_calls)
        writer.write_str_value("ageGroup", self.age_group)
        writer.write_collection_of_object_values("agreementAcceptances", self.agreement_acceptances)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_collection_of_object_values("assignedPlans", self.assigned_plans)
        writer.write_object_value("authentication", self.authentication)
        writer.write_object_value("authorizationInfo", self.authorization_info)
        writer.write_datetime_value("birthday", self.birthday)
        writer.write_collection_of_primitive_values("businessPhones", self.business_phones)
        writer.write_object_value("calendar", self.calendar)
        writer.write_collection_of_object_values("calendarGroups", self.calendar_groups)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_collection_of_object_values("calendars", self.calendars)
        writer.write_collection_of_object_values("chats", self.chats)
        writer.write_str_value("city", self.city)
        writer.write_object_value("cloudClipboard", self.cloud_clipboard)
        writer.write_collection_of_object_values("cloudPCs", self.cloud_p_cs)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("consentProvidedForMinor", self.consent_provided_for_minor)
        writer.write_collection_of_object_values("contactFolders", self.contact_folders)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("country", self.country)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("createdObjects", self.created_objects)
        writer.write_str_value("creationType", self.creation_type)
        writer.write_object_value("customSecurityAttributes", self.custom_security_attributes)
        writer.write_object_value("dataSecurityAndGovernance", self.data_security_and_governance)
        writer.write_str_value("department", self.department)
        writer.write_int_value("deviceEnrollmentLimit", self.device_enrollment_limit)
        writer.write_collection_of_object_values("deviceManagementTroubleshootingEvents", self.device_management_troubleshooting_events)
        writer.write_collection_of_object_values("directReports", self.direct_reports)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_object_value("employeeExperience", self.employee_experience)
        writer.write_datetime_value("employeeHireDate", self.employee_hire_date)
        writer.write_str_value("employeeId", self.employee_id)
        writer.write_datetime_value("employeeLeaveDateTime", self.employee_leave_date_time)
        writer.write_object_value("employeeOrgData", self.employee_org_data)
        writer.write_str_value("employeeType", self.employee_type)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_str_value("externalUserState", self.external_user_state)
        writer.write_datetime_value("externalUserStateChangeDateTime", self.external_user_state_change_date_time)
        writer.write_str_value("faxNumber", self.fax_number)
        writer.write_collection_of_object_values("followedSites", self.followed_sites)
        writer.write_str_value("givenName", self.given_name)
        writer.write_datetime_value("hireDate", self.hire_date)
        writer.write_collection_of_object_values("identities", self.identities)
        writer.write_collection_of_primitive_values("imAddresses", self.im_addresses)
        writer.write_object_value("inferenceClassification", self.inference_classification)
        writer.write_object_value("insights", self.insights)
        writer.write_collection_of_primitive_values("interests", self.interests)
        writer.write_bool_value("isManagementRestricted", self.is_management_restricted)
        writer.write_bool_value("isResourceAccount", self.is_resource_account)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_collection_of_object_values("joinedTeams", self.joined_teams)
        writer.write_datetime_value("lastPasswordChangeDateTime", self.last_password_change_date_time)
        writer.write_str_value("legalAgeGroupClassification", self.legal_age_group_classification)
        writer.write_collection_of_object_values("licenseAssignmentStates", self.license_assignment_states)
        writer.write_collection_of_object_values("licenseDetails", self.license_details)
        writer.write_str_value("mail", self.mail)
        writer.write_collection_of_object_values("mailFolders", self.mail_folders)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_object_value("mailboxSettings", self.mailbox_settings)
        writer.write_collection_of_object_values("managedAppRegistrations", self.managed_app_registrations)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("mySite", self.my_site)
        writer.write_collection_of_object_values("oauth2PermissionGrants", self.oauth2_permission_grants)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("onPremisesDistinguishedName", self.on_premises_distinguished_name)
        writer.write_str_value("onPremisesDomainName", self.on_premises_domain_name)
        writer.write_object_value("onPremisesExtensionAttributes", self.on_premises_extension_attributes)
        writer.write_str_value("onPremisesImmutableId", self.on_premises_immutable_id)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_collection_of_object_values("onPremisesProvisioningErrors", self.on_premises_provisioning_errors)
        writer.write_str_value("onPremisesSamAccountName", self.on_premises_sam_account_name)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_object_value("onPremisesSyncBehavior", self.on_premises_sync_behavior)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_str_value("onPremisesUserPrincipalName", self.on_premises_user_principal_name)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_collection_of_primitive_values("otherMails", self.other_mails)
        writer.write_object_value("outlook", self.outlook)
        writer.write_collection_of_object_values("ownedDevices", self.owned_devices)
        writer.write_collection_of_object_values("ownedObjects", self.owned_objects)
        writer.write_str_value("passwordPolicies", self.password_policies)
        writer.write_object_value("passwordProfile", self.password_profile)
        writer.write_collection_of_primitive_values("pastProjects", self.past_projects)
        writer.write_collection_of_object_values("people", self.people)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("photos", self.photos)
        writer.write_object_value("planner", self.planner)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("preferredDataLocation", self.preferred_data_location)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_str_value("preferredName", self.preferred_name)
        writer.write_object_value("presence", self.presence)
        writer.write_object_value("print", self.print)
        writer.write_collection_of_object_values("provisionedPlans", self.provisioned_plans)
        writer.write_collection_of_primitive_values("proxyAddresses", self.proxy_addresses)
        writer.write_collection_of_object_values("registeredDevices", self.registered_devices)
        writer.write_collection_of_primitive_values("responsibilities", self.responsibilities)
        writer.write_collection_of_primitive_values("schools", self.schools)
        writer.write_collection_of_object_values("scopedRoleMemberOf", self.scoped_role_member_of)
        writer.write_str_value("securityIdentifier", self.security_identifier)
        writer.write_collection_of_object_values("serviceProvisioningErrors", self.service_provisioning_errors)
        writer.write_object_value("settings", self.settings)
        writer.write_bool_value("showInAddressList", self.show_in_address_list)
        writer.write_object_value("signInActivity", self.sign_in_activity)
        writer.write_datetime_value("signInSessionsValidFromDateTime", self.sign_in_sessions_valid_from_date_time)
        writer.write_collection_of_primitive_values("skills", self.skills)
        writer.write_object_value("solutions", self.solutions)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
        writer.write_str_value("state", self.state)
        writer.write_str_value("streetAddress", self.street_address)
        writer.write_str_value("surname", self.surname)
        writer.write_object_value("teamwork", self.teamwork)
        writer.write_object_value("todo", self.todo)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_str_value("usageLocation", self.usage_location)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userType", self.user_type)
    

