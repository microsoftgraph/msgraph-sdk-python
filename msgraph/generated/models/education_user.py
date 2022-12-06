from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assigned_license = lazy_import('msgraph.generated.models.assigned_license')
assigned_plan = lazy_import('msgraph.generated.models.assigned_plan')
education_assignment = lazy_import('msgraph.generated.models.education_assignment')
education_class = lazy_import('msgraph.generated.models.education_class')
education_external_source = lazy_import('msgraph.generated.models.education_external_source')
education_on_premises_info = lazy_import('msgraph.generated.models.education_on_premises_info')
education_rubric = lazy_import('msgraph.generated.models.education_rubric')
education_school = lazy_import('msgraph.generated.models.education_school')
education_student = lazy_import('msgraph.generated.models.education_student')
education_teacher = lazy_import('msgraph.generated.models.education_teacher')
education_user_role = lazy_import('msgraph.generated.models.education_user_role')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
password_profile = lazy_import('msgraph.generated.models.password_profile')
physical_address = lazy_import('msgraph.generated.models.physical_address')
provisioned_plan = lazy_import('msgraph.generated.models.provisioned_plan')
related_contact = lazy_import('msgraph.generated.models.related_contact')
user = lazy_import('msgraph.generated.models.user')

class EducationUser(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def account_enabled(self,) -> Optional[bool]:
        """
        Gets the accountEnabled property value. True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.
        Returns: Optional[bool]
        """
        return self._account_enabled
    
    @account_enabled.setter
    def account_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountEnabled property value. True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.
        Args:
            value: Value to set for the accountEnabled property.
        """
        self._account_enabled = value
    
    @property
    def assigned_licenses(self,) -> Optional[List[assigned_license.AssignedLicense]]:
        """
        Gets the assignedLicenses property value. The licenses that are assigned to the user. Not nullable.
        Returns: Optional[List[assigned_license.AssignedLicense]]
        """
        return self._assigned_licenses
    
    @assigned_licenses.setter
    def assigned_licenses(self,value: Optional[List[assigned_license.AssignedLicense]] = None) -> None:
        """
        Sets the assignedLicenses property value. The licenses that are assigned to the user. Not nullable.
        Args:
            value: Value to set for the assignedLicenses property.
        """
        self._assigned_licenses = value
    
    @property
    def assigned_plans(self,) -> Optional[List[assigned_plan.AssignedPlan]]:
        """
        Gets the assignedPlans property value. The plans that are assigned to the user. Read-only. Not nullable.
        Returns: Optional[List[assigned_plan.AssignedPlan]]
        """
        return self._assigned_plans
    
    @assigned_plans.setter
    def assigned_plans(self,value: Optional[List[assigned_plan.AssignedPlan]] = None) -> None:
        """
        Sets the assignedPlans property value. The plans that are assigned to the user. Read-only. Not nullable.
        Args:
            value: Value to set for the assignedPlans property.
        """
        self._assigned_plans = value
    
    @property
    def assignments(self,) -> Optional[List[education_assignment.EducationAssignment]]:
        """
        Gets the assignments property value. Assignments belonging to the user.
        Returns: Optional[List[education_assignment.EducationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[education_assignment.EducationAssignment]] = None) -> None:
        """
        Sets the assignments property value. Assignments belonging to the user.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def business_phones(self,) -> Optional[List[str]]:
        """
        Gets the businessPhones property value. The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.
        Returns: Optional[List[str]]
        """
        return self._business_phones
    
    @business_phones.setter
    def business_phones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the businessPhones property value. The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.
        Args:
            value: Value to set for the businessPhones property.
        """
        self._business_phones = value
    
    @property
    def classes(self,) -> Optional[List[education_class.EducationClass]]:
        """
        Gets the classes property value. Classes to which the user belongs. Nullable.
        Returns: Optional[List[education_class.EducationClass]]
        """
        return self._classes
    
    @classes.setter
    def classes(self,value: Optional[List[education_class.EducationClass]] = None) -> None:
        """
        Sets the classes property value. Classes to which the user belongs. Nullable.
        Args:
            value: Value to set for the classes property.
        """
        self._classes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationUser and sets the default values.
        """
        super().__init__()
        # True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.
        self._account_enabled: Optional[bool] = None
        # The licenses that are assigned to the user. Not nullable.
        self._assigned_licenses: Optional[List[assigned_license.AssignedLicense]] = None
        # The plans that are assigned to the user. Read-only. Not nullable.
        self._assigned_plans: Optional[List[assigned_plan.AssignedPlan]] = None
        # Assignments belonging to the user.
        self._assignments: Optional[List[education_assignment.EducationAssignment]] = None
        # The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.
        self._business_phones: Optional[List[str]] = None
        # Classes to which the user belongs. Nullable.
        self._classes: Optional[List[education_class.EducationClass]] = None
        # The entity who created the user.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The name for the department in which the user works. Supports $filter.
        self._department: Optional[str] = None
        # The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.
        self._display_name: Optional[str] = None
        # Where this user was created from. Possible values are: sis, manual.
        self._external_source: Optional[education_external_source.EducationExternalSource] = None
        # The name of the external source this resource was generated from.
        self._external_source_detail: Optional[str] = None
        # The given name (first name) of the user. Supports $filter.
        self._given_name: Optional[str] = None
        # The SMTP address for the user, for example, jeff@contoso.onmicrosoft.com. Read-Only. Supports $filter.
        self._mail: Optional[str] = None
        # The mail address of the user.
        self._mailing_address: Optional[physical_address.PhysicalAddress] = None
        # The mail alias for the user. This property must be specified when a user is created. Supports $filter.
        self._mail_nickname: Optional[str] = None
        # The middle name of the user.
        self._middle_name: Optional[str] = None
        # The primary cellular telephone number for the user.
        self._mobile_phone: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The officeLocation property
        self._office_location: Optional[str] = None
        # Additional information used to associate the Azure Active Directory user with its Active Directory counterpart.
        self._on_premises_info: Optional[education_on_premises_info.EducationOnPremisesInfo] = None
        # Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two can be specified together; for example: DisablePasswordExpiration, DisableStrongPassword.
        self._password_policies: Optional[str] = None
        # Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required.
        self._password_profile: Optional[password_profile.PasswordProfile] = None
        # The preferred language for the user that should follow the ISO 639-1 code, for example, en-US.
        self._preferred_language: Optional[str] = None
        # The primaryRole property
        self._primary_role: Optional[education_user_role.EducationUserRole] = None
        # The plans that are provisioned for the user. Read-only. Not nullable.
        self._provisioned_plans: Optional[List[provisioned_plan.ProvisionedPlan]] = None
        # The refreshTokensValidFromDateTime property
        self._refresh_tokens_valid_from_date_time: Optional[datetime] = None
        # Related records associated with the user. Read-only.
        self._related_contacts: Optional[List[related_contact.RelatedContact]] = None
        # The address where the user lives.
        self._residence_address: Optional[physical_address.PhysicalAddress] = None
        # When set, the grading rubric attached to the assignment.
        self._rubrics: Optional[List[education_rubric.EducationRubric]] = None
        # Schools to which the user belongs. Nullable.
        self._schools: Optional[List[education_school.EducationSchool]] = None
        # True if the Outlook Global Address List should contain this user; otherwise, false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.
        self._show_in_address_list: Optional[bool] = None
        # If the primary role is student, this block will contain student specific data.
        self._student: Optional[education_student.EducationStudent] = None
        # The user's surname (family name or last name). Supports $filter.
        self._surname: Optional[str] = None
        # Classes for which the user is a teacher.
        self._taught_classes: Optional[List[education_class.EducationClass]] = None
        # If the primary role is teacher, this block will contain teacher specific data.
        self._teacher: Optional[education_teacher.EducationTeacher] = None
        # A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: US, JP, and GB. Not nullable. Supports $filter.
        self._usage_location: Optional[str] = None
        # The directory user that corresponds to this user.
        self._user: Optional[user.User] = None
        # The user principal name (UPN) of the user. The UPN is an internet-style login name for the user based on the internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of the organization. Supports $filter and $orderby.
        self._user_principal_name: Optional[str] = None
        # A string value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter.
        self._user_type: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The entity who created the user.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The entity who created the user.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationUser()
    
    @property
    def department(self,) -> Optional[str]:
        """
        Gets the department property value. The name for the department in which the user works. Supports $filter.
        Returns: Optional[str]
        """
        return self._department
    
    @department.setter
    def department(self,value: Optional[str] = None) -> None:
        """
        Sets the department property value. The name for the department in which the user works. Supports $filter.
        Args:
            value: Value to set for the department property.
        """
        self._department = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_source(self,) -> Optional[education_external_source.EducationExternalSource]:
        """
        Gets the externalSource property value. Where this user was created from. Possible values are: sis, manual.
        Returns: Optional[education_external_source.EducationExternalSource]
        """
        return self._external_source
    
    @external_source.setter
    def external_source(self,value: Optional[education_external_source.EducationExternalSource] = None) -> None:
        """
        Sets the externalSource property value. Where this user was created from. Possible values are: sis, manual.
        Args:
            value: Value to set for the externalSource property.
        """
        self._external_source = value
    
    @property
    def external_source_detail(self,) -> Optional[str]:
        """
        Gets the externalSourceDetail property value. The name of the external source this resource was generated from.
        Returns: Optional[str]
        """
        return self._external_source_detail
    
    @external_source_detail.setter
    def external_source_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the externalSourceDetail property value. The name of the external source this resource was generated from.
        Args:
            value: Value to set for the externalSourceDetail property.
        """
        self._external_source_detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_enabled": lambda n : setattr(self, 'account_enabled', n.get_bool_value()),
            "assigned_licenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(assigned_license.AssignedLicense)),
            "assigned_plans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(assigned_plan.AssignedPlan)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(education_assignment.EducationAssignment)),
            "business_phones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(education_class.EducationClass)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_source": lambda n : setattr(self, 'external_source', n.get_enum_value(education_external_source.EducationExternalSource)),
            "external_source_detail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
            "given_name": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailing_address": lambda n : setattr(self, 'mailing_address', n.get_object_value(physical_address.PhysicalAddress)),
            "mail_nickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "middle_name": lambda n : setattr(self, 'middle_name', n.get_str_value()),
            "mobile_phone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "on_premises_info": lambda n : setattr(self, 'on_premises_info', n.get_object_value(education_on_premises_info.EducationOnPremisesInfo)),
            "password_policies": lambda n : setattr(self, 'password_policies', n.get_str_value()),
            "password_profile": lambda n : setattr(self, 'password_profile', n.get_object_value(password_profile.PasswordProfile)),
            "preferred_language": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "primary_role": lambda n : setattr(self, 'primary_role', n.get_enum_value(education_user_role.EducationUserRole)),
            "provisioned_plans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(provisioned_plan.ProvisionedPlan)),
            "refresh_tokens_valid_from_date_time": lambda n : setattr(self, 'refresh_tokens_valid_from_date_time', n.get_datetime_value()),
            "related_contacts": lambda n : setattr(self, 'related_contacts', n.get_collection_of_object_values(related_contact.RelatedContact)),
            "residence_address": lambda n : setattr(self, 'residence_address', n.get_object_value(physical_address.PhysicalAddress)),
            "rubrics": lambda n : setattr(self, 'rubrics', n.get_collection_of_object_values(education_rubric.EducationRubric)),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_object_values(education_school.EducationSchool)),
            "show_in_address_list": lambda n : setattr(self, 'show_in_address_list', n.get_bool_value()),
            "student": lambda n : setattr(self, 'student', n.get_object_value(education_student.EducationStudent)),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "taught_classes": lambda n : setattr(self, 'taught_classes', n.get_collection_of_object_values(education_class.EducationClass)),
            "teacher": lambda n : setattr(self, 'teacher', n.get_object_value(education_teacher.EducationTeacher)),
            "usage_location": lambda n : setattr(self, 'usage_location', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(user.User)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "user_type": lambda n : setattr(self, 'user_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The given name (first name) of the user. Supports $filter.
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The given name (first name) of the user. Supports $filter.
        Args:
            value: Value to set for the givenName property.
        """
        self._given_name = value
    
    @property
    def mail(self,) -> Optional[str]:
        """
        Gets the mail property value. The SMTP address for the user, for example, jeff@contoso.onmicrosoft.com. Read-Only. Supports $filter.
        Returns: Optional[str]
        """
        return self._mail
    
    @mail.setter
    def mail(self,value: Optional[str] = None) -> None:
        """
        Sets the mail property value. The SMTP address for the user, for example, jeff@contoso.onmicrosoft.com. Read-Only. Supports $filter.
        Args:
            value: Value to set for the mail property.
        """
        self._mail = value
    
    @property
    def mailing_address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the mailingAddress property value. The mail address of the user.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._mailing_address
    
    @mailing_address.setter
    def mailing_address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the mailingAddress property value. The mail address of the user.
        Args:
            value: Value to set for the mailingAddress property.
        """
        self._mailing_address = value
    
    @property
    def mail_nickname(self,) -> Optional[str]:
        """
        Gets the mailNickname property value. The mail alias for the user. This property must be specified when a user is created. Supports $filter.
        Returns: Optional[str]
        """
        return self._mail_nickname
    
    @mail_nickname.setter
    def mail_nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the mailNickname property value. The mail alias for the user. This property must be specified when a user is created. Supports $filter.
        Args:
            value: Value to set for the mailNickname property.
        """
        self._mail_nickname = value
    
    @property
    def middle_name(self,) -> Optional[str]:
        """
        Gets the middleName property value. The middle name of the user.
        Returns: Optional[str]
        """
        return self._middle_name
    
    @middle_name.setter
    def middle_name(self,value: Optional[str] = None) -> None:
        """
        Sets the middleName property value. The middle name of the user.
        Args:
            value: Value to set for the middleName property.
        """
        self._middle_name = value
    
    @property
    def mobile_phone(self,) -> Optional[str]:
        """
        Gets the mobilePhone property value. The primary cellular telephone number for the user.
        Returns: Optional[str]
        """
        return self._mobile_phone
    
    @mobile_phone.setter
    def mobile_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the mobilePhone property value. The primary cellular telephone number for the user.
        Args:
            value: Value to set for the mobilePhone property.
        """
        self._mobile_phone = value
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. The officeLocation property
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. The officeLocation property
        Args:
            value: Value to set for the officeLocation property.
        """
        self._office_location = value
    
    @property
    def on_premises_info(self,) -> Optional[education_on_premises_info.EducationOnPremisesInfo]:
        """
        Gets the onPremisesInfo property value. Additional information used to associate the Azure Active Directory user with its Active Directory counterpart.
        Returns: Optional[education_on_premises_info.EducationOnPremisesInfo]
        """
        return self._on_premises_info
    
    @on_premises_info.setter
    def on_premises_info(self,value: Optional[education_on_premises_info.EducationOnPremisesInfo] = None) -> None:
        """
        Sets the onPremisesInfo property value. Additional information used to associate the Azure Active Directory user with its Active Directory counterpart.
        Args:
            value: Value to set for the onPremisesInfo property.
        """
        self._on_premises_info = value
    
    @property
    def password_policies(self,) -> Optional[str]:
        """
        Gets the passwordPolicies property value. Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two can be specified together; for example: DisablePasswordExpiration, DisableStrongPassword.
        Returns: Optional[str]
        """
        return self._password_policies
    
    @password_policies.setter
    def password_policies(self,value: Optional[str] = None) -> None:
        """
        Sets the passwordPolicies property value. Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two can be specified together; for example: DisablePasswordExpiration, DisableStrongPassword.
        Args:
            value: Value to set for the passwordPolicies property.
        """
        self._password_policies = value
    
    @property
    def password_profile(self,) -> Optional[password_profile.PasswordProfile]:
        """
        Gets the passwordProfile property value. Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required.
        Returns: Optional[password_profile.PasswordProfile]
        """
        return self._password_profile
    
    @password_profile.setter
    def password_profile(self,value: Optional[password_profile.PasswordProfile] = None) -> None:
        """
        Sets the passwordProfile property value. Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required.
        Args:
            value: Value to set for the passwordProfile property.
        """
        self._password_profile = value
    
    @property
    def preferred_language(self,) -> Optional[str]:
        """
        Gets the preferredLanguage property value. The preferred language for the user that should follow the ISO 639-1 code, for example, en-US.
        Returns: Optional[str]
        """
        return self._preferred_language
    
    @preferred_language.setter
    def preferred_language(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredLanguage property value. The preferred language for the user that should follow the ISO 639-1 code, for example, en-US.
        Args:
            value: Value to set for the preferredLanguage property.
        """
        self._preferred_language = value
    
    @property
    def primary_role(self,) -> Optional[education_user_role.EducationUserRole]:
        """
        Gets the primaryRole property value. The primaryRole property
        Returns: Optional[education_user_role.EducationUserRole]
        """
        return self._primary_role
    
    @primary_role.setter
    def primary_role(self,value: Optional[education_user_role.EducationUserRole] = None) -> None:
        """
        Sets the primaryRole property value. The primaryRole property
        Args:
            value: Value to set for the primaryRole property.
        """
        self._primary_role = value
    
    @property
    def provisioned_plans(self,) -> Optional[List[provisioned_plan.ProvisionedPlan]]:
        """
        Gets the provisionedPlans property value. The plans that are provisioned for the user. Read-only. Not nullable.
        Returns: Optional[List[provisioned_plan.ProvisionedPlan]]
        """
        return self._provisioned_plans
    
    @provisioned_plans.setter
    def provisioned_plans(self,value: Optional[List[provisioned_plan.ProvisionedPlan]] = None) -> None:
        """
        Sets the provisionedPlans property value. The plans that are provisioned for the user. Read-only. Not nullable.
        Args:
            value: Value to set for the provisionedPlans property.
        """
        self._provisioned_plans = value
    
    @property
    def refresh_tokens_valid_from_date_time(self,) -> Optional[datetime]:
        """
        Gets the refreshTokensValidFromDateTime property value. The refreshTokensValidFromDateTime property
        Returns: Optional[datetime]
        """
        return self._refresh_tokens_valid_from_date_time
    
    @refresh_tokens_valid_from_date_time.setter
    def refresh_tokens_valid_from_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the refreshTokensValidFromDateTime property value. The refreshTokensValidFromDateTime property
        Args:
            value: Value to set for the refreshTokensValidFromDateTime property.
        """
        self._refresh_tokens_valid_from_date_time = value
    
    @property
    def related_contacts(self,) -> Optional[List[related_contact.RelatedContact]]:
        """
        Gets the relatedContacts property value. Related records associated with the user. Read-only.
        Returns: Optional[List[related_contact.RelatedContact]]
        """
        return self._related_contacts
    
    @related_contacts.setter
    def related_contacts(self,value: Optional[List[related_contact.RelatedContact]] = None) -> None:
        """
        Sets the relatedContacts property value. Related records associated with the user. Read-only.
        Args:
            value: Value to set for the relatedContacts property.
        """
        self._related_contacts = value
    
    @property
    def residence_address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the residenceAddress property value. The address where the user lives.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._residence_address
    
    @residence_address.setter
    def residence_address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the residenceAddress property value. The address where the user lives.
        Args:
            value: Value to set for the residenceAddress property.
        """
        self._residence_address = value
    
    @property
    def rubrics(self,) -> Optional[List[education_rubric.EducationRubric]]:
        """
        Gets the rubrics property value. When set, the grading rubric attached to the assignment.
        Returns: Optional[List[education_rubric.EducationRubric]]
        """
        return self._rubrics
    
    @rubrics.setter
    def rubrics(self,value: Optional[List[education_rubric.EducationRubric]] = None) -> None:
        """
        Sets the rubrics property value. When set, the grading rubric attached to the assignment.
        Args:
            value: Value to set for the rubrics property.
        """
        self._rubrics = value
    
    @property
    def schools(self,) -> Optional[List[education_school.EducationSchool]]:
        """
        Gets the schools property value. Schools to which the user belongs. Nullable.
        Returns: Optional[List[education_school.EducationSchool]]
        """
        return self._schools
    
    @schools.setter
    def schools(self,value: Optional[List[education_school.EducationSchool]] = None) -> None:
        """
        Sets the schools property value. Schools to which the user belongs. Nullable.
        Args:
            value: Value to set for the schools property.
        """
        self._schools = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_object_value("mailingAddress", self.mailing_address)
        writer.write_str_value("mailNickname", self.mail_nickname)
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
    
    @property
    def show_in_address_list(self,) -> Optional[bool]:
        """
        Gets the showInAddressList property value. True if the Outlook Global Address List should contain this user; otherwise, false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.
        Returns: Optional[bool]
        """
        return self._show_in_address_list
    
    @show_in_address_list.setter
    def show_in_address_list(self,value: Optional[bool] = None) -> None:
        """
        Sets the showInAddressList property value. True if the Outlook Global Address List should contain this user; otherwise, false. If not set, this will be treated as true. For users invited through the invitation manager, this property will be set to false.
        Args:
            value: Value to set for the showInAddressList property.
        """
        self._show_in_address_list = value
    
    @property
    def student(self,) -> Optional[education_student.EducationStudent]:
        """
        Gets the student property value. If the primary role is student, this block will contain student specific data.
        Returns: Optional[education_student.EducationStudent]
        """
        return self._student
    
    @student.setter
    def student(self,value: Optional[education_student.EducationStudent] = None) -> None:
        """
        Sets the student property value. If the primary role is student, this block will contain student specific data.
        Args:
            value: Value to set for the student property.
        """
        self._student = value
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The user's surname (family name or last name). Supports $filter.
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The user's surname (family name or last name). Supports $filter.
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def taught_classes(self,) -> Optional[List[education_class.EducationClass]]:
        """
        Gets the taughtClasses property value. Classes for which the user is a teacher.
        Returns: Optional[List[education_class.EducationClass]]
        """
        return self._taught_classes
    
    @taught_classes.setter
    def taught_classes(self,value: Optional[List[education_class.EducationClass]] = None) -> None:
        """
        Sets the taughtClasses property value. Classes for which the user is a teacher.
        Args:
            value: Value to set for the taughtClasses property.
        """
        self._taught_classes = value
    
    @property
    def teacher(self,) -> Optional[education_teacher.EducationTeacher]:
        """
        Gets the teacher property value. If the primary role is teacher, this block will contain teacher specific data.
        Returns: Optional[education_teacher.EducationTeacher]
        """
        return self._teacher
    
    @teacher.setter
    def teacher(self,value: Optional[education_teacher.EducationTeacher] = None) -> None:
        """
        Sets the teacher property value. If the primary role is teacher, this block will contain teacher specific data.
        Args:
            value: Value to set for the teacher property.
        """
        self._teacher = value
    
    @property
    def usage_location(self,) -> Optional[str]:
        """
        Gets the usageLocation property value. A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: US, JP, and GB. Not nullable. Supports $filter.
        Returns: Optional[str]
        """
        return self._usage_location
    
    @usage_location.setter
    def usage_location(self,value: Optional[str] = None) -> None:
        """
        Sets the usageLocation property value. A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: US, JP, and GB. Not nullable. Supports $filter.
        Args:
            value: Value to set for the usageLocation property.
        """
        self._usage_location = value
    
    @property
    def user(self,) -> Optional[user.User]:
        """
        Gets the user property value. The directory user that corresponds to this user.
        Returns: Optional[user.User]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[user.User] = None) -> None:
        """
        Sets the user property value. The directory user that corresponds to this user.
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user. The UPN is an internet-style login name for the user based on the internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of the organization. Supports $filter and $orderby.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user. The UPN is an internet-style login name for the user based on the internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of the organization. Supports $filter and $orderby.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def user_type(self,) -> Optional[str]:
        """
        Gets the userType property value. A string value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter.
        Returns: Optional[str]
        """
        return self._user_type
    
    @user_type.setter
    def user_type(self,value: Optional[str] = None) -> None:
        """
        Sets the userType property value. A string value that can be used to classify user types in your directory, such as Member and Guest. Supports $filter.
        Args:
            value: Value to set for the userType property.
        """
        self._user_type = value
    

