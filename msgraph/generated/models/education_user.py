from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_license import AssignedLicense
    from .assigned_plan import AssignedPlan
    from .education_assignment import EducationAssignment
    from .education_class import EducationClass
    from .education_external_source import EducationExternalSource
    from .education_on_premises_info import EducationOnPremisesInfo
    from .education_rubric import EducationRubric
    from .education_school import EducationSchool
    from .education_student import EducationStudent
    from .education_teacher import EducationTeacher
    from .education_user_role import EducationUserRole
    from .entity import Entity
    from .identity_set import IdentitySet
    from .password_profile import PasswordProfile
    from .physical_address import PhysicalAddress
    from .provisioned_plan import ProvisionedPlan
    from .related_contact import RelatedContact
    from .user import User

from .entity import Entity

@dataclass
class EducationUser(Entity, Parsable):
    # True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.
    account_enabled: Optional[bool] = None
    # The licenses that are assigned to the user. Not nullable.
    assigned_licenses: Optional[list[AssignedLicense]] = None
    # The plans that are assigned to the user. Read-only. Not nullable.
    assigned_plans: Optional[list[AssignedPlan]] = None
    # Assignments belonging to the user.
    assignments: Optional[list[EducationAssignment]] = None
    # The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.
    business_phones: Optional[list[str]] = None
    # Classes to which the user belongs. Nullable.
    classes: Optional[list[EducationClass]] = None
    # The entity who created the user.
    created_by: Optional[IdentitySet] = None
    # The name for the department in which the user works. Supports $filter.
    department: Optional[str] = None
    # The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Where this user was created from. The possible values are: sis, manual.
    external_source: Optional[EducationExternalSource] = None
    # The name of the external source this resource was generated from.
    external_source_detail: Optional[str] = None
    # The given name (first name) of the user. Supports $filter.
    given_name: Optional[str] = None
    # The SMTP address for the user, for example, jeff@contoso.com. Read-Only. Supports $filter.
    mail: Optional[str] = None
    # The mail alias for the user. This property must be specified when a user is created. Supports $filter.
    mail_nickname: Optional[str] = None
    # The mail address of the user.
    mailing_address: Optional[PhysicalAddress] = None
    # The middle name of the user.
    middle_name: Optional[str] = None
    # The primary cellular telephone number for the user.
    mobile_phone: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The office location for the user.
    office_location: Optional[str] = None
    # Additional information used to associate the Microsoft Entra user with its Active Directory counterpart.
    on_premises_info: Optional[EducationOnPremisesInfo] = None
    # Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two can be specified together; for example: DisablePasswordExpiration, DisableStrongPassword.
    password_policies: Optional[str] = None
    # Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required.
    password_profile: Optional[PasswordProfile] = None
    # The preferred language for the user that should follow the ISO 639-1 code, for example, en-US.
    preferred_language: Optional[str] = None
    # The primaryRole property
    primary_role: Optional[EducationUserRole] = None
    # The plans that are provisioned for the user. Read-only. Not nullable.
    provisioned_plans: Optional[list[ProvisionedPlan]] = None
    # Any refresh tokens or sessions tokens (session cookies) issued before this time are invalid, and applications get an error when using an invalid refresh or sessions token to acquire a delegated access token (to access APIs such as Microsoft Graph).  If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Returned only on $select. Read-only.
    refresh_tokens_valid_from_date_time: Optional[datetime.datetime] = None
    # Related records associated with the user. Read-only.
    related_contacts: Optional[list[RelatedContact]] = None
    # The address where the user lives.
    residence_address: Optional[PhysicalAddress] = None
    # When set, the grading rubric attached to the assignment.
    rubrics: Optional[list[EducationRubric]] = None
    # Schools to which the user belongs. Nullable.
    schools: Optional[list[EducationSchool]] = None
    # True if the Outlook Global Address List should contain this user; otherwise, false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.
    show_in_address_list: Optional[bool] = None
    # If the primary role is student, this block will contain student specific data.
    student: Optional[EducationStudent] = None
    # The user's surname (family name or last name). Supports $filter.
    surname: Optional[str] = None
    # Classes for which the user is a teacher.
    taught_classes: Optional[list[EducationClass]] = None
    # If the primary role is teacher, this block will contain teacher specific data.
    teacher: Optional[EducationTeacher] = None
    # A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: US, JP, and GB. Not nullable. Supports $filter.
    usage_location: Optional[str] = None
    # The directory user that corresponds to this user.
    user: Optional[User] = None
    # The user principal name (UPN) of the user. The UPN is an internet-style login name for the user based on the internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of the organization. Supports $filter and $orderby.
    user_principal_name: Optional[str] = None
    # A string value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter.
    user_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_license import AssignedLicense
        from .assigned_plan import AssignedPlan
        from .education_assignment import EducationAssignment
        from .education_class import EducationClass
        from .education_external_source import EducationExternalSource
        from .education_on_premises_info import EducationOnPremisesInfo
        from .education_rubric import EducationRubric
        from .education_school import EducationSchool
        from .education_student import EducationStudent
        from .education_teacher import EducationTeacher
        from .education_user_role import EducationUserRole
        from .entity import Entity
        from .identity_set import IdentitySet
        from .password_profile import PasswordProfile
        from .physical_address import PhysicalAddress
        from .provisioned_plan import ProvisionedPlan
        from .related_contact import RelatedContact
        from .user import User

        from .assigned_license import AssignedLicense
        from .assigned_plan import AssignedPlan
        from .education_assignment import EducationAssignment
        from .education_class import EducationClass
        from .education_external_source import EducationExternalSource
        from .education_on_premises_info import EducationOnPremisesInfo
        from .education_rubric import EducationRubric
        from .education_school import EducationSchool
        from .education_student import EducationStudent
        from .education_teacher import EducationTeacher
        from .education_user_role import EducationUserRole
        from .entity import Entity
        from .identity_set import IdentitySet
        from .password_profile import PasswordProfile
        from .physical_address import PhysicalAddress
        from .provisioned_plan import ProvisionedPlan
        from .related_contact import RelatedContact
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "accountEnabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(AssignedLicense)),
            "assignedPlans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(AssignedPlan)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(EducationAssignment)),
            "businessPhones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(EducationClass)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalSource": lambda n : setattr(self, 'external_source', n.get_enum_value(EducationExternalSource)),
            "externalSourceDetail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "mailingAddress": lambda n : setattr(self, 'mailing_address', n.get_object_value(PhysicalAddress)),
            "middleName": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "onPremisesInfo": lambda n : setattr(self, 'on_premises_info', n.get_object_value(EducationOnPremisesInfo)),
            "passwordPolicies": lambda n : setattr(self, 'password_policies', n.get_str_value()),
            "passwordProfile": lambda n : setattr(self, 'password_profile', n.get_object_value(PasswordProfile)),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "primaryRole": lambda n : setattr(self, 'primary_role', n.get_enum_value(EducationUserRole)),
            "provisionedPlans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(ProvisionedPlan)),
            "refreshTokensValidFromDateTime": lambda n : setattr(self, 'refresh_tokens_valid_from_date_time', n.get_datetime_value()),
            "relatedContacts": lambda n : setattr(self, 'related_contacts', n.get_collection_of_object_values(RelatedContact)),
            "residenceAddress": lambda n : setattr(self, 'residence_address', n.get_object_value(PhysicalAddress)),
            "rubrics": lambda n : setattr(self, 'rubrics', n.get_collection_of_object_values(EducationRubric)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_object_values(EducationSchool)),
            "showInAddressList": lambda n : setattr(self, 'show_in_address_list', n.get_bool_value()),
            "student": lambda n : setattr(self, 'student', n.get_object_value(EducationStudent)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "taughtClasses": lambda n : setattr(self, 'taught_classes', n.get_collection_of_object_values(EducationClass)),
            "teacher": lambda n : setattr(self, 'teacher', n.get_object_value(EducationTeacher)),
            "usageLocation": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(User)),
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
        writer.write_bool_value("accountEnabled", self.account_enabled)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_collection_of_object_values("assignedPlans", self.assigned_plans)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_primitive_values("businessPhones", self.business_phones)
        writer.write_collection_of_object_values("classes", self.classes)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("externalSource", self.external_source)
        writer.write_str_value("externalSourceDetail", self.external_source_detail)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("mail", self.mail)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_object_value("mailingAddress", self.mailing_address)
        writer.write_str_value("middleName", self.middle_name)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_object_value("onPremisesInfo", self.on_premises_info)
        writer.write_str_value("passwordPolicies", self.password_policies)
        writer.write_object_value("passwordProfile", self.password_profile)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_enum_value("primaryRole", self.primary_role)
        writer.write_collection_of_object_values("provisionedPlans", self.provisioned_plans)
        writer.write_datetime_value("refreshTokensValidFromDateTime", self.refresh_tokens_valid_from_date_time)
        writer.write_collection_of_object_values("relatedContacts", self.related_contacts)
        writer.write_object_value("residenceAddress", self.residence_address)
        writer.write_collection_of_object_values("rubrics", self.rubrics)
        writer.write_collection_of_object_values("schools", self.schools)
        writer.write_bool_value("showInAddressList", self.show_in_address_list)
        writer.write_object_value("student", self.student)
        writer.write_str_value("surname", self.surname)
        writer.write_collection_of_object_values("taughtClasses", self.taught_classes)
        writer.write_object_value("teacher", self.teacher)
        writer.write_str_value("usageLocation", self.usage_location)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userType", self.user_type)
    

