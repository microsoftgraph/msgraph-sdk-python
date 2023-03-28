from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import agreement, agreement_acceptance, entity

from . import entity

class TermsOfUseContainer(entity.Entity):
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
            value: Value to set for the agreement_acceptances property.
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
        from . import agreement, agreement_acceptance, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "agreements": lambda n : setattr(self, 'agreements', n.get_collection_of_object_values(agreement.Agreement)),
            "agreementAcceptances": lambda n : setattr(self, 'agreement_acceptances', n.get_collection_of_object_values(agreement_acceptance.AgreementAcceptance)),
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
        writer.write_collection_of_object_values("agreements", self.agreements)
        writer.write_collection_of_object_values("agreementAcceptances", self.agreement_acceptances)
    

