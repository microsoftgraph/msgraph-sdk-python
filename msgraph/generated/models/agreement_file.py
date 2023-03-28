from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agreement_file_localization = lazy_import('msgraph.generated.models.agreement_file_localization')
agreement_file_properties = lazy_import('msgraph.generated.models.agreement_file_properties')

class AgreementFile(agreement_file_properties.AgreementFileProperties):
    def __init__(self,) -> None:
        """
        Instantiates a new AgreementFile and sets the default values.
        """
        super().__init__()
        # The localized version of the terms of use agreement files attached to the agreement.
        self._localizations: Optional[List[agreement_file_localization.AgreementFileLocalization]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgreementFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AgreementFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(agreement_file_localization.AgreementFileLocalization)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def localizations(self,) -> Optional[List[agreement_file_localization.AgreementFileLocalization]]:
        """
        Gets the localizations property value. The localized version of the terms of use agreement files attached to the agreement.
        Returns: Optional[List[agreement_file_localization.AgreementFileLocalization]]
        """
        return self._localizations
    
    @localizations.setter
    def localizations(self,value: Optional[List[agreement_file_localization.AgreementFileLocalization]] = None) -> None:
        """
        Sets the localizations property value. The localized version of the terms of use agreement files attached to the agreement.
        Args:
            value: Value to set for the localizations property.
        """
        self._localizations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("localizations", self.localizations)
    

