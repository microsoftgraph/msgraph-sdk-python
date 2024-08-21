from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_modes import AuthenticationMethodModes

@dataclass
class UpdateAllowedCombinationsResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Information about why the updateAllowedCombinations action was successful or failed.
    additional_information: Optional[str] = None
    # References to existing Conditional Access policies that use this authentication strength.
    conditional_access_references: Optional[List[str]] = None
    # The list of current authentication method combinations allowed by the authentication strength.
    current_combinations: Optional[List[AuthenticationMethodModes]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of former authentication method combinations allowed by the authentication strength before they were updated through the updateAllowedCombinations action.
    previous_combinations: Optional[List[AuthenticationMethodModes]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateAllowedCombinationsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateAllowedCombinationsResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateAllowedCombinationsResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_modes import AuthenticationMethodModes

        from .authentication_method_modes import AuthenticationMethodModes

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "conditionalAccessReferences": lambda n : setattr(self, 'conditional_access_references', n.get_collection_of_primitive_values(str)),
            "currentCombinations": lambda n : setattr(self, 'current_combinations', n.get_collection_of_enum_values(AuthenticationMethodModes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previousCombinations": lambda n : setattr(self, 'previous_combinations', n.get_collection_of_enum_values(AuthenticationMethodModes)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_collection_of_primitive_values("conditionalAccessReferences", self.conditional_access_references)
        writer.write_collection_of_enum_values("currentCombinations", self.current_combinations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_enum_values("previousCombinations", self.previous_combinations)
        writer.write_additional_data_value(self.additional_data)
    

