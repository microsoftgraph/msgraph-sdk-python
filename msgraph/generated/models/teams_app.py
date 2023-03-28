from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, teams_app_definition, teams_app_distribution_method

from . import entity

class TeamsApp(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new teamsApp and sets the default values.
        """
        super().__init__()
        # The details for each version of the app.
        self._app_definitions: Optional[List[teams_app_definition.TeamsAppDefinition]] = None
        # The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.
        self._display_name: Optional[str] = None
        # The method of distribution for the app. Read-only.
        self._distribution_method: Optional[teams_app_distribution_method.TeamsAppDistributionMethod] = None
        # The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.
        self._external_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def app_definitions(self,) -> Optional[List[teams_app_definition.TeamsAppDefinition]]:
        """
        Gets the appDefinitions property value. The details for each version of the app.
        Returns: Optional[List[teams_app_definition.TeamsAppDefinition]]
        """
        return self._app_definitions
    
    @app_definitions.setter
    def app_definitions(self,value: Optional[List[teams_app_definition.TeamsAppDefinition]] = None) -> None:
        """
        Sets the appDefinitions property value. The details for each version of the app.
        Args:
            value: Value to set for the app_definitions property.
        """
        self._app_definitions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsApp()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def distribution_method(self,) -> Optional[teams_app_distribution_method.TeamsAppDistributionMethod]:
        """
        Gets the distributionMethod property value. The method of distribution for the app. Read-only.
        Returns: Optional[teams_app_distribution_method.TeamsAppDistributionMethod]
        """
        return self._distribution_method
    
    @distribution_method.setter
    def distribution_method(self,value: Optional[teams_app_distribution_method.TeamsAppDistributionMethod] = None) -> None:
        """
        Sets the distributionMethod property value. The method of distribution for the app. Read-only.
        Args:
            value: Value to set for the distribution_method property.
        """
        self._distribution_method = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.
        Args:
            value: Value to set for the external_id property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, teams_app_definition, teams_app_distribution_method

        fields: Dict[str, Callable[[Any], None]] = {
            "appDefinitions": lambda n : setattr(self, 'app_definitions', n.get_collection_of_object_values(teams_app_definition.TeamsAppDefinition)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "distributionMethod": lambda n : setattr(self, 'distribution_method', n.get_enum_value(teams_app_distribution_method.TeamsAppDistributionMethod)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("appDefinitions", self.app_definitions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("distributionMethod", self.distribution_method)
        writer.write_str_value("externalId", self.external_id)
    

