from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement import Agreement
    from .agreement_acceptance import AgreementAcceptance
    from .entity import Entity

from .entity import Entity

@dataclass
class TermsOfUseContainer(Entity):
    # Represents the current status of a user's response to a company's customizable terms of use agreement.
    agreement_acceptances: Optional[List[AgreementAcceptance]] = None
    # Represents a tenant's customizable terms of use agreement that's created and managed with Microsoft Entra ID Governance.
    agreements: Optional[List[Agreement]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TermsOfUseContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TermsOfUseContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TermsOfUseContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .agreement import Agreement
        from .agreement_acceptance import AgreementAcceptance
        from .entity import Entity

        from .agreement import Agreement
        from .agreement_acceptance import AgreementAcceptance
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "agreementAcceptances": lambda n : setattr(self, 'agreement_acceptances', n.get_collection_of_object_values(AgreementAcceptance)),
            "agreements": lambda n : setattr(self, 'agreements', n.get_collection_of_object_values(Agreement)),
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
        writer.write_collection_of_object_values("agreementAcceptances", self.agreement_acceptances)
        writer.write_collection_of_object_values("agreements", self.agreements)
    

