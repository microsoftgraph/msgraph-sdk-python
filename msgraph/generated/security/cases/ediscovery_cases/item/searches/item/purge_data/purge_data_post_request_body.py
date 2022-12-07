from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

purge_areas = lazy_import('msgraph.generated.models.security.purge_areas')
purge_type = lazy_import('msgraph.generated.models.security.purge_type')

class PurgeDataPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the purgeData method.
    """
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
        Instantiates a new purgeDataPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The purgeAreas property
        self._purge_areas: Optional[purge_areas.PurgeAreas] = None
        # The purgeType property
        self._purge_type: Optional[purge_type.PurgeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PurgeDataPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PurgeDataPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PurgeDataPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "purge_areas": lambda n : setattr(self, 'purge_areas', n.get_enum_value(purge_areas.PurgeAreas)),
            "purge_type": lambda n : setattr(self, 'purge_type', n.get_enum_value(purge_type.PurgeType)),
        }
        return fields
    
    @property
    def purge_areas(self,) -> Optional[purge_areas.PurgeAreas]:
        """
        Gets the purgeAreas property value. The purgeAreas property
        Returns: Optional[purge_areas.PurgeAreas]
        """
        return self._purge_areas
    
    @purge_areas.setter
    def purge_areas(self,value: Optional[purge_areas.PurgeAreas] = None) -> None:
        """
        Sets the purgeAreas property value. The purgeAreas property
        Args:
            value: Value to set for the purgeAreas property.
        """
        self._purge_areas = value
    
    @property
    def purge_type(self,) -> Optional[purge_type.PurgeType]:
        """
        Gets the purgeType property value. The purgeType property
        Returns: Optional[purge_type.PurgeType]
        """
        return self._purge_type
    
    @purge_type.setter
    def purge_type(self,value: Optional[purge_type.PurgeType] = None) -> None:
        """
        Sets the purgeType property value. The purgeType property
        Args:
            value: Value to set for the purgeType property.
        """
        self._purge_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("purgeAreas", self.purge_areas)
        writer.write_enum_value("purgeType", self.purge_type)
        writer.write_additional_data_value(self.additional_data)
    

