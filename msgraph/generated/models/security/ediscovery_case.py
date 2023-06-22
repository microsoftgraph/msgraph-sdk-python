from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import case, case_operation, ediscovery_case_settings, ediscovery_custodian, ediscovery_noncustodial_data_source, ediscovery_review_set, ediscovery_review_tag, ediscovery_search
    from .. import identity_set

from . import case

@dataclass
class EdiscoveryCase(case.Case):
    odata_type = "#microsoft.graph.security.ediscoveryCase"
    # The user who closed the case.
    closed_by: Optional[identity_set.IdentitySet] = None
    # The date and time when the case was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    closed_date_time: Optional[datetime] = None
    # Returns a list of case ediscoveryCustodian objects for this case.
    custodians: Optional[List[ediscovery_custodian.EdiscoveryCustodian]] = None
    # The external case number for customer reference.
    external_id: Optional[str] = None
    # Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
    noncustodial_data_sources: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]] = None
    # Returns a list of case caseOperation objects for this case.
    operations: Optional[List[case_operation.CaseOperation]] = None
    # Returns a list of eDiscoveryReviewSet objects in the case.
    review_sets: Optional[List[ediscovery_review_set.EdiscoveryReviewSet]] = None
    # Returns a list of eDiscoverySearch objects associated with this case.
    searches: Optional[List[ediscovery_search.EdiscoverySearch]] = None
    # Returns a list of eDIscoverySettings objects in the case.
    settings: Optional[ediscovery_case_settings.EdiscoveryCaseSettings] = None
    # Returns a list of ediscoveryReviewTag objects associated to this case.
    tags: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryCase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import case, case_operation, ediscovery_case_settings, ediscovery_custodian, ediscovery_noncustodial_data_source, ediscovery_review_set, ediscovery_review_tag, ediscovery_search
        from .. import identity_set

        from . import case, case_operation, ediscovery_case_settings, ediscovery_custodian, ediscovery_noncustodial_data_source, ediscovery_review_set, ediscovery_review_tag, ediscovery_search
        from .. import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "closedBy": lambda n : setattr(self, 'closed_by', n.get_object_value(identity_set.IdentitySet)),
            "closedDateTime": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "custodians": lambda n : setattr(self, 'custodians', n.get_collection_of_object_values(ediscovery_custodian.EdiscoveryCustodian)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "noncustodialDataSources": lambda n : setattr(self, 'noncustodial_data_sources', n.get_collection_of_object_values(ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(case_operation.CaseOperation)),
            "reviewSets": lambda n : setattr(self, 'review_sets', n.get_collection_of_object_values(ediscovery_review_set.EdiscoveryReviewSet)),
            "searches": lambda n : setattr(self, 'searches', n.get_collection_of_object_values(ediscovery_search.EdiscoverySearch)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(ediscovery_case_settings.EdiscoveryCaseSettings)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_object_values(ediscovery_review_tag.EdiscoveryReviewTag)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("closedBy", self.closed_by)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_collection_of_object_values("custodians", self.custodians)
        writer.write_str_value("externalId", self.external_id)
        writer.write_collection_of_object_values("noncustodialDataSources", self.noncustodial_data_sources)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("reviewSets", self.review_sets)
        writer.write_collection_of_object_values("searches", self.searches)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("tags", self.tags)
    

