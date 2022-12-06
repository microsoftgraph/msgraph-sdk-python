from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_external_source = lazy_import('msgraph.generated.models.education_external_source')
entity = lazy_import('msgraph.generated.models.entity')

class EducationOrganization(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new educationOrganization and sets the default values.
        """
        super().__init__()
        # Organization description.
        self._description: Optional[str] = None
        # Organization display name.
        self._display_name: Optional[str] = None
        # Source where this organization was created from. Possible values are: sis, manual.
        self._external_source: Optional[education_external_source.EducationExternalSource] = None
        # The name of the external source this resources was generated from.
        self._external_source_detail: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationOrganization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationOrganization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationOrganization()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Organization description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Organization description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Organization display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Organization display name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_source(self,) -> Optional[education_external_source.EducationExternalSource]:
        """
        Gets the externalSource property value. Source where this organization was created from. Possible values are: sis, manual.
        Returns: Optional[education_external_source.EducationExternalSource]
        """
        return self._external_source
    
    @external_source.setter
    def external_source(self,value: Optional[education_external_source.EducationExternalSource] = None) -> None:
        """
        Sets the externalSource property value. Source where this organization was created from. Possible values are: sis, manual.
        Args:
            value: Value to set for the externalSource property.
        """
        self._external_source = value
    
    @property
    def external_source_detail(self,) -> Optional[str]:
        """
        Gets the externalSourceDetail property value. The name of the external source this resources was generated from.
        Returns: Optional[str]
        """
        return self._external_source_detail
    
    @external_source_detail.setter
    def external_source_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the externalSourceDetail property value. The name of the external source this resources was generated from.
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_source": lambda n : setattr(self, 'external_source', n.get_enum_value(education_external_source.EducationExternalSource)),
            "external_source_detail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("externalSource", self.external_source)
        writer.write_str_value("externalSourceDetail", self.external_source_detail)
    

