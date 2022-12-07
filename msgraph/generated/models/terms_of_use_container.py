from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agreement = lazy_import('msgraph.generated.models.agreement')
agreement_acceptance = lazy_import('msgraph.generated.models.agreement_acceptance')
entity = lazy_import('msgraph.generated.models.entity')

class TermsOfUseContainer(entity.Entity):
    @property
    def agreement_acceptances(self,) -> Optional[List[agreement_acceptance.AgreementAcceptance]]:
        """
        Gets the agreementAcceptances property value. Represents the current status of a user's response to a company's customizable terms of use agreement.
        Returns: Optional[List[agreement_acceptance.AgreementAcceptance]]
        """
        return self._agreement_acceptances
    
    @agreement_acceptances.setter
    def agreement_acceptances(self,value: Optional[List[agreement_acceptance.AgreementAcceptance]] = None) -> None:
        """
        Sets the agreementAcceptances property value. Represents the current status of a user's response to a company's customizable terms of use agreement.
        Args:
            value: Value to set for the agreementAcceptances property.
        """
        self._agreement_acceptances = value
    
    @property
    def agreements(self,) -> Optional[List[agreement.Agreement]]:
        """
        Gets the agreements property value. Represents a tenant's customizable terms of use agreement that's created and managed with Azure Active Directory (Azure AD).
        Returns: Optional[List[agreement.Agreement]]
        """
        return self._agreements
    
    @agreements.setter
    def agreements(self,value: Optional[List[agreement.Agreement]] = None) -> None:
        """
        Sets the agreements property value. Represents a tenant's customizable terms of use agreement that's created and managed with Azure Active Directory (Azure AD).
        Args:
            value: Value to set for the agreements property.
        """
        self._agreements = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TermsOfUseContainer and sets the default values.
        """
        super().__init__()
        # Represents the current status of a user's response to a company's customizable terms of use agreement.
        self._agreement_acceptances: Optional[List[agreement_acceptance.AgreementAcceptance]] = None
        # Represents a tenant's customizable terms of use agreement that's created and managed with Azure Active Directory (Azure AD).
        self._agreements: Optional[List[agreement.Agreement]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TermsOfUseContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TermsOfUseContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TermsOfUseContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "agreement_acceptances": lambda n : setattr(self, 'agreement_acceptances', n.get_collection_of_object_values(agreement_acceptance.AgreementAcceptance)),
            "agreements": lambda n : setattr(self, 'agreements', n.get_collection_of_object_values(agreement.Agreement)),
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
        writer.write_collection_of_object_values("agreementAcceptances", self.agreement_acceptances)
        writer.write_collection_of_object_values("agreements", self.agreements)
    

