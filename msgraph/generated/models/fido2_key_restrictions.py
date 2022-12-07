from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

fido2_restriction_enforcement_type = lazy_import('msgraph.generated.models.fido2_restriction_enforcement_type')

class Fido2KeyRestrictions(AdditionalDataHolder, Parsable):
    @property
    def aa_guids(self,) -> Optional[List[str]]:
        """
        Gets the aaGuids property value. A collection of Authenticator Attestation GUIDs. AADGUIDs define key types and manufacturers.
        Returns: Optional[List[str]]
        """
        return self._aa_guids
    
    @aa_guids.setter
    def aa_guids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the aaGuids property value. A collection of Authenticator Attestation GUIDs. AADGUIDs define key types and manufacturers.
        Args:
            value: Value to set for the aaGuids property.
        """
        self._aa_guids = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new fido2KeyRestrictions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A collection of Authenticator Attestation GUIDs. AADGUIDs define key types and manufacturers.
        self._aa_guids: Optional[List[str]] = None
        # Enforcement type. Possible values are: allow, block.
        self._enforcement_type: Optional[fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType] = None
        # Determines if the configured key enforcement is enabled.
        self._is_enforced: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Fido2KeyRestrictions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Fido2KeyRestrictions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Fido2KeyRestrictions()
    
    @property
    def enforcement_type(self,) -> Optional[fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType]:
        """
        Gets the enforcementType property value. Enforcement type. Possible values are: allow, block.
        Returns: Optional[fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType]
        """
        return self._enforcement_type
    
    @enforcement_type.setter
    def enforcement_type(self,value: Optional[fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType] = None) -> None:
        """
        Sets the enforcementType property value. Enforcement type. Possible values are: allow, block.
        Args:
            value: Value to set for the enforcementType property.
        """
        self._enforcement_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aa_guids": lambda n : setattr(self, 'aa_guids', n.get_collection_of_primitive_values(str)),
            "enforcement_type": lambda n : setattr(self, 'enforcement_type', n.get_enum_value(fido2_restriction_enforcement_type.Fido2RestrictionEnforcementType)),
            "is_enforced": lambda n : setattr(self, 'is_enforced', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_enforced(self,) -> Optional[bool]:
        """
        Gets the isEnforced property value. Determines if the configured key enforcement is enabled.
        Returns: Optional[bool]
        """
        return self._is_enforced
    
    @is_enforced.setter
    def is_enforced(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnforced property value. Determines if the configured key enforcement is enabled.
        Args:
            value: Value to set for the isEnforced property.
        """
        self._is_enforced = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("aaGuids", self.aa_guids)
        writer.write_enum_value("enforcementType", self.enforcement_type)
        writer.write_bool_value("isEnforced", self.is_enforced)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

