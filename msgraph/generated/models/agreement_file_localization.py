from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agreement_file_properties = lazy_import('msgraph.generated.models.agreement_file_properties')
agreement_file_version = lazy_import('msgraph.generated.models.agreement_file_version')

class AgreementFileLocalization(agreement_file_properties.AgreementFileProperties):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new agreementFileLocalization and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. Customized versions of the terms of use agreement in the Azure AD tenant.
        self._versions: Optional[List[agreement_file_version.AgreementFileVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgreementFileLocalization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFileLocalization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AgreementFileLocalization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(agreement_file_version.AgreementFileVersion)),
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
        writer.write_collection_of_object_values("versions", self.versions)
    
    @property
    def versions(self,) -> Optional[List[agreement_file_version.AgreementFileVersion]]:
        """
        Gets the versions property value. Read-only. Customized versions of the terms of use agreement in the Azure AD tenant.
        Returns: Optional[List[agreement_file_version.AgreementFileVersion]]
        """
        return self._versions
    
    @versions.setter
    def versions(self,value: Optional[List[agreement_file_version.AgreementFileVersion]] = None) -> None:
        """
        Sets the versions property value. Read-only. Customized versions of the terms of use agreement in the Azure AD tenant.
        Args:
            value: Value to set for the versions property.
        """
        self._versions = value
    

