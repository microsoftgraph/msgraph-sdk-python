from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
terms_and_conditions = lazy_import('msgraph.generated.models.terms_and_conditions')

class TermsAndConditionsAcceptanceStatus(entity.Entity):
    """
    A termsAndConditionsAcceptanceStatus entity represents the acceptance status of a given Terms and Conditions (T&C) policy by a given user. Users must accept the most up-to-date version of the terms in order to retain access to the Company Portal.
    """
    @property
    def accepted_date_time(self,) -> Optional[datetime]:
        """
        Gets the acceptedDateTime property value. DateTime when the terms were last accepted by the user.
        Returns: Optional[datetime]
        """
        return self._accepted_date_time
    
    @accepted_date_time.setter
    def accepted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the acceptedDateTime property value. DateTime when the terms were last accepted by the user.
        Args:
            value: Value to set for the acceptedDateTime property.
        """
        self._accepted_date_time = value
    
    @property
    def accepted_version(self,) -> Optional[int]:
        """
        Gets the acceptedVersion property value. Most recent version number of the T&C accepted by the user.
        Returns: Optional[int]
        """
        return self._accepted_version
    
    @accepted_version.setter
    def accepted_version(self,value: Optional[int] = None) -> None:
        """
        Sets the acceptedVersion property value. Most recent version number of the T&C accepted by the user.
        Args:
            value: Value to set for the acceptedVersion property.
        """
        self._accepted_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new termsAndConditionsAcceptanceStatus and sets the default values.
        """
        super().__init__()
        # DateTime when the terms were last accepted by the user.
        self._accepted_date_time: Optional[datetime] = None
        # Most recent version number of the T&C accepted by the user.
        self._accepted_version: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Navigation link to the terms and conditions that are assigned.
        self._terms_and_conditions: Optional[terms_and_conditions.TermsAndConditions] = None
        # Display name of the user whose acceptance the entity represents.
        self._user_display_name: Optional[str] = None
        # The userPrincipalName of the User that accepted the term.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TermsAndConditionsAcceptanceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditionsAcceptanceStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TermsAndConditionsAcceptanceStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accepted_date_time": lambda n : setattr(self, 'accepted_date_time', n.get_datetime_value()),
            "accepted_version": lambda n : setattr(self, 'accepted_version', n.get_int_value()),
            "terms_and_conditions": lambda n : setattr(self, 'terms_and_conditions', n.get_object_value(terms_and_conditions.TermsAndConditions)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("acceptedDateTime", self.accepted_date_time)
        writer.write_int_value("acceptedVersion", self.accepted_version)
        writer.write_object_value("termsAndConditions", self.terms_and_conditions)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def terms_and_conditions(self,) -> Optional[terms_and_conditions.TermsAndConditions]:
        """
        Gets the termsAndConditions property value. Navigation link to the terms and conditions that are assigned.
        Returns: Optional[terms_and_conditions.TermsAndConditions]
        """
        return self._terms_and_conditions
    
    @terms_and_conditions.setter
    def terms_and_conditions(self,value: Optional[terms_and_conditions.TermsAndConditions] = None) -> None:
        """
        Sets the termsAndConditions property value. Navigation link to the terms and conditions that are assigned.
        Args:
            value: Value to set for the termsAndConditions property.
        """
        self._terms_and_conditions = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. Display name of the user whose acceptance the entity represents.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. Display name of the user whose acceptance the entity represents.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The userPrincipalName of the User that accepted the term.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The userPrincipalName of the User that accepted the term.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

