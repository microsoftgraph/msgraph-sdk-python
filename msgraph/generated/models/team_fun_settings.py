from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

giphy_rating_type = lazy_import('msgraph.generated.models.giphy_rating_type')

class TeamFunSettings(AdditionalDataHolder, Parsable):
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
    
    @property
    def allow_custom_memes(self,) -> Optional[bool]:
        """
        Gets the allowCustomMemes property value. If set to true, enables users to include custom memes.
        Returns: Optional[bool]
        """
        return self._allow_custom_memes
    
    @allow_custom_memes.setter
    def allow_custom_memes(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowCustomMemes property value. If set to true, enables users to include custom memes.
        Args:
            value: Value to set for the allowCustomMemes property.
        """
        self._allow_custom_memes = value
    
    @property
    def allow_giphy(self,) -> Optional[bool]:
        """
        Gets the allowGiphy property value. If set to true, enables Giphy use.
        Returns: Optional[bool]
        """
        return self._allow_giphy
    
    @allow_giphy.setter
    def allow_giphy(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowGiphy property value. If set to true, enables Giphy use.
        Args:
            value: Value to set for the allowGiphy property.
        """
        self._allow_giphy = value
    
    @property
    def allow_stickers_and_memes(self,) -> Optional[bool]:
        """
        Gets the allowStickersAndMemes property value. If set to true, enables users to include stickers and memes.
        Returns: Optional[bool]
        """
        return self._allow_stickers_and_memes
    
    @allow_stickers_and_memes.setter
    def allow_stickers_and_memes(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowStickersAndMemes property value. If set to true, enables users to include stickers and memes.
        Args:
            value: Value to set for the allowStickersAndMemes property.
        """
        self._allow_stickers_and_memes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamFunSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If set to true, enables users to include custom memes.
        self._allow_custom_memes: Optional[bool] = None
        # If set to true, enables Giphy use.
        self._allow_giphy: Optional[bool] = None
        # If set to true, enables users to include stickers and memes.
        self._allow_stickers_and_memes: Optional[bool] = None
        # Giphy content rating. Possible values are: moderate, strict.
        self._giphy_content_rating: Optional[giphy_rating_type.GiphyRatingType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamFunSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamFunSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamFunSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_custom_memes": lambda n : setattr(self, 'allow_custom_memes', n.get_bool_value()),
            "allow_giphy": lambda n : setattr(self, 'allow_giphy', n.get_bool_value()),
            "allow_stickers_and_memes": lambda n : setattr(self, 'allow_stickers_and_memes', n.get_bool_value()),
            "giphy_content_rating": lambda n : setattr(self, 'giphy_content_rating', n.get_enum_value(giphy_rating_type.GiphyRatingType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def giphy_content_rating(self,) -> Optional[giphy_rating_type.GiphyRatingType]:
        """
        Gets the giphyContentRating property value. Giphy content rating. Possible values are: moderate, strict.
        Returns: Optional[giphy_rating_type.GiphyRatingType]
        """
        return self._giphy_content_rating
    
    @giphy_content_rating.setter
    def giphy_content_rating(self,value: Optional[giphy_rating_type.GiphyRatingType] = None) -> None:
        """
        Sets the giphyContentRating property value. Giphy content rating. Possible values are: moderate, strict.
        Args:
            value: Value to set for the giphyContentRating property.
        """
        self._giphy_content_rating = value
    
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
        writer.write_bool_value("allowCustomMemes", self.allow_custom_memes)
        writer.write_bool_value("allowGiphy", self.allow_giphy)
        writer.write_bool_value("allowStickersAndMemes", self.allow_stickers_and_memes)
        writer.write_enum_value("giphyContentRating", self.giphy_content_rating)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

