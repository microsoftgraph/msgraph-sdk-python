from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agreement_acceptance = lazy_import('msgraph.generated.models.agreement_acceptance')
agreement_file = lazy_import('msgraph.generated.models.agreement_file')
agreement_file_localization = lazy_import('msgraph.generated.models.agreement_file_localization')
entity = lazy_import('msgraph.generated.models.entity')
terms_expiration = lazy_import('msgraph.generated.models.terms_expiration')

class Agreement(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def acceptances(self,) -> Optional[List[agreement_acceptance.AgreementAcceptance]]:
        """
        Gets the acceptances property value. Read-only. Information about acceptances of this agreement.
        Returns: Optional[List[agreement_acceptance.AgreementAcceptance]]
        """
        return self._acceptances
    
    @acceptances.setter
    def acceptances(self,value: Optional[List[agreement_acceptance.AgreementAcceptance]] = None) -> None:
        """
        Sets the acceptances property value. Read-only. Information about acceptances of this agreement.
        Args:
            value: Value to set for the acceptances property.
        """
        self._acceptances = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new agreement and sets the default values.
        """
        super().__init__()
        # Read-only. Information about acceptances of this agreement.
        self._acceptances: Optional[List[agreement_acceptance.AgreementAcceptance]] = None
        # Display name of the agreement. The display name is used for internal tracking of the agreement but is not shown to end users who view the agreement. Supports $filter (eq).
        self._display_name: Optional[str] = None
        # Default PDF linked to this agreement.
        self._file: Optional[agreement_file.AgreementFile] = None
        # PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.
        self._files: Optional[List[agreement_file_localization.AgreementFileLocalization]] = None
        # Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Azure AD, if they haven't already done so. Supports $filter (eq).
        self._is_per_device_acceptance_required: Optional[bool] = None
        # Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).
        self._is_viewing_before_acceptance_required: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Expiration schedule and frequency of agreement for all users. Supports $filter (eq).
        self._terms_expiration: Optional[terms_expiration.TermsExpiration] = None
        # The duration after which the user must re-accept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq).
        self._user_reaccept_required_frequency: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Agreement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Agreement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Agreement()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the agreement. The display name is used for internal tracking of the agreement but is not shown to end users who view the agreement. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the agreement. The display name is used for internal tracking of the agreement but is not shown to end users who view the agreement. Supports $filter (eq).
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def file(self,) -> Optional[agreement_file.AgreementFile]:
        """
        Gets the file property value. Default PDF linked to this agreement.
        Returns: Optional[agreement_file.AgreementFile]
        """
        return self._file
    
    @file.setter
    def file(self,value: Optional[agreement_file.AgreementFile] = None) -> None:
        """
        Sets the file property value. Default PDF linked to this agreement.
        Args:
            value: Value to set for the file property.
        """
        self._file = value
    
    @property
    def files(self,) -> Optional[List[agreement_file_localization.AgreementFileLocalization]]:
        """
        Gets the files property value. PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.
        Returns: Optional[List[agreement_file_localization.AgreementFileLocalization]]
        """
        return self._files
    
    @files.setter
    def files(self,value: Optional[List[agreement_file_localization.AgreementFileLocalization]] = None) -> None:
        """
        Sets the files property value. PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.
        Args:
            value: Value to set for the files property.
        """
        self._files = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "acceptances": lambda n : setattr(self, 'acceptances', n.get_collection_of_object_values(agreement_acceptance.AgreementAcceptance)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(agreement_file.AgreementFile)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(agreement_file_localization.AgreementFileLocalization)),
            "is_per_device_acceptance_required": lambda n : setattr(self, 'is_per_device_acceptance_required', n.get_bool_value()),
            "is_viewing_before_acceptance_required": lambda n : setattr(self, 'is_viewing_before_acceptance_required', n.get_bool_value()),
            "terms_expiration": lambda n : setattr(self, 'terms_expiration', n.get_object_value(terms_expiration.TermsExpiration)),
            "user_reaccept_required_frequency": lambda n : setattr(self, 'user_reaccept_required_frequency', n.get_object_value(Timedelta)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_per_device_acceptance_required(self,) -> Optional[bool]:
        """
        Gets the isPerDeviceAcceptanceRequired property value. Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Azure AD, if they haven't already done so. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_per_device_acceptance_required
    
    @is_per_device_acceptance_required.setter
    def is_per_device_acceptance_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPerDeviceAcceptanceRequired property value. Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Azure AD, if they haven't already done so. Supports $filter (eq).
        Args:
            value: Value to set for the isPerDeviceAcceptanceRequired property.
        """
        self._is_per_device_acceptance_required = value
    
    @property
    def is_viewing_before_acceptance_required(self,) -> Optional[bool]:
        """
        Gets the isViewingBeforeAcceptanceRequired property value. Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).
        Returns: Optional[bool]
        """
        return self._is_viewing_before_acceptance_required
    
    @is_viewing_before_acceptance_required.setter
    def is_viewing_before_acceptance_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isViewingBeforeAcceptanceRequired property value. Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).
        Args:
            value: Value to set for the isViewingBeforeAcceptanceRequired property.
        """
        self._is_viewing_before_acceptance_required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("acceptances", self.acceptances)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("file", self.file)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_bool_value("isPerDeviceAcceptanceRequired", self.is_per_device_acceptance_required)
        writer.write_bool_value("isViewingBeforeAcceptanceRequired", self.is_viewing_before_acceptance_required)
        writer.write_object_value("termsExpiration", self.terms_expiration)
        writer.write_object_value("userReacceptRequiredFrequency", self.user_reaccept_required_frequency)
    
    @property
    def terms_expiration(self,) -> Optional[terms_expiration.TermsExpiration]:
        """
        Gets the termsExpiration property value. Expiration schedule and frequency of agreement for all users. Supports $filter (eq).
        Returns: Optional[terms_expiration.TermsExpiration]
        """
        return self._terms_expiration
    
    @terms_expiration.setter
    def terms_expiration(self,value: Optional[terms_expiration.TermsExpiration] = None) -> None:
        """
        Sets the termsExpiration property value. Expiration schedule and frequency of agreement for all users. Supports $filter (eq).
        Args:
            value: Value to set for the termsExpiration property.
        """
        self._terms_expiration = value
    
    @property
    def user_reaccept_required_frequency(self,) -> Optional[Timedelta]:
        """
        Gets the userReacceptRequiredFrequency property value. The duration after which the user must re-accept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq).
        Returns: Optional[Timedelta]
        """
        return self._user_reaccept_required_frequency
    
    @user_reaccept_required_frequency.setter
    def user_reaccept_required_frequency(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the userReacceptRequiredFrequency property value. The duration after which the user must re-accept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq).
        Args:
            value: Value to set for the userReacceptRequiredFrequency property.
        """
        self._user_reaccept_required_frequency = value
    

