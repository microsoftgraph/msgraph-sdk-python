from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_instance_decision_item_resource = lazy_import('msgraph.generated.models.access_review_instance_decision_item_resource')
entity = lazy_import('msgraph.generated.models.entity')
identity = lazy_import('msgraph.generated.models.identity')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class AccessReviewInstanceDecisionItem(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def access_review_id(self,) -> Optional[str]:
        """
        Gets the accessReviewId property value. The identifier of the accessReviewInstance parent. Supports $select. Read-only.
        Returns: Optional[str]
        """
        return self._access_review_id
    
    @access_review_id.setter
    def access_review_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accessReviewId property value. The identifier of the accessReviewInstance parent. Supports $select. Read-only.
        Args:
            value: Value to set for the accessReviewId property.
        """
        self._access_review_id = value
    
    @property
    def applied_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the appliedBy property value. The identifier of the user who applied the decision. Read-only.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._applied_by
    
    @applied_by.setter
    def applied_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the appliedBy property value. The identifier of the user who applied the decision. Read-only.
        Args:
            value: Value to set for the appliedBy property.
        """
        self._applied_by = value
    
    @property
    def applied_date_time(self,) -> Optional[datetime]:
        """
        Gets the appliedDateTime property value. The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only.
        Returns: Optional[datetime]
        """
        return self._applied_date_time
    
    @applied_date_time.setter
    def applied_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the appliedDateTime property value. The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only.
        Args:
            value: Value to set for the appliedDateTime property.
        """
        self._applied_date_time = value
    
    @property
    def apply_result(self,) -> Optional[str]:
        """
        Gets the applyResult property value. The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.
        Returns: Optional[str]
        """
        return self._apply_result
    
    @apply_result.setter
    def apply_result(self,value: Optional[str] = None) -> None:
        """
        Sets the applyResult property value. The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.
        Args:
            value: Value to set for the applyResult property.
        """
        self._apply_result = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewInstanceDecisionItem and sets the default values.
        """
        super().__init__()
        # The identifier of the accessReviewInstance parent. Supports $select. Read-only.
        self._access_review_id: Optional[str] = None
        # The identifier of the user who applied the decision. Read-only.
        self._applied_by: Optional[user_identity.UserIdentity] = None
        # The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only.
        self._applied_date_time: Optional[datetime] = None
        # The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.
        self._apply_result: Optional[str] = None
        # Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).
        self._decision: Optional[str] = None
        # Justification left by the reviewer when they made the decision.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.
        self._principal: Optional[identity.Identity] = None
        # A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.
        self._principal_link: Optional[str] = None
        # A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. Recommend approve if sign-in is within thirty days of start of review. Recommend deny if sign-in is greater than thirty days of start of review. Recommendation not available otherwise. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.
        self._recommendation: Optional[str] = None
        # Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.
        self._resource: Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource] = None
        # A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.
        self._resource_link: Optional[str] = None
        # The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.
        self._reviewed_by: Optional[user_identity.UserIdentity] = None
        # The timestamp when the review decision occurred. Supports $select. Read-only.
        self._reviewed_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstanceDecisionItem()
    
    @property
    def decision(self,) -> Optional[str]:
        """
        Gets the decision property value. Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).
        Returns: Optional[str]
        """
        return self._decision
    
    @decision.setter
    def decision(self,value: Optional[str] = None) -> None:
        """
        Sets the decision property value. Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).
        Args:
            value: Value to set for the decision property.
        """
        self._decision = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_review_id": lambda n : setattr(self, 'access_review_id', n.get_str_value()),
            "applied_by": lambda n : setattr(self, 'applied_by', n.get_object_value(user_identity.UserIdentity)),
            "applied_date_time": lambda n : setattr(self, 'applied_date_time', n.get_datetime_value()),
            "apply_result": lambda n : setattr(self, 'apply_result', n.get_str_value()),
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(identity.Identity)),
            "principal_link": lambda n : setattr(self, 'principal_link', n.get_str_value()),
            "recommendation": lambda n : setattr(self, 'recommendation', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource)),
            "resource_link": lambda n : setattr(self, 'resource_link', n.get_str_value()),
            "reviewed_by": lambda n : setattr(self, 'reviewed_by', n.get_object_value(user_identity.UserIdentity)),
            "reviewed_date_time": lambda n : setattr(self, 'reviewed_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. Justification left by the reviewer when they made the decision.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. Justification left by the reviewer when they made the decision.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def principal(self,) -> Optional[identity.Identity]:
        """
        Gets the principal property value. Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.
        Returns: Optional[identity.Identity]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the principal property value. Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_link(self,) -> Optional[str]:
        """
        Gets the principalLink property value. A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.
        Returns: Optional[str]
        """
        return self._principal_link
    
    @principal_link.setter
    def principal_link(self,value: Optional[str] = None) -> None:
        """
        Sets the principalLink property value. A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.
        Args:
            value: Value to set for the principalLink property.
        """
        self._principal_link = value
    
    @property
    def recommendation(self,) -> Optional[str]:
        """
        Gets the recommendation property value. A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. Recommend approve if sign-in is within thirty days of start of review. Recommend deny if sign-in is greater than thirty days of start of review. Recommendation not available otherwise. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.
        Returns: Optional[str]
        """
        return self._recommendation
    
    @recommendation.setter
    def recommendation(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendation property value. A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. Recommend approve if sign-in is within thirty days of start of review. Recommend deny if sign-in is greater than thirty days of start of review. Recommendation not available otherwise. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.
        Args:
            value: Value to set for the recommendation property.
        """
        self._recommendation = value
    
    @property
    def resource(self,) -> Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource]:
        """
        Gets the resource property value. Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.
        Returns: Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource] = None) -> None:
        """
        Sets the resource property value. Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_link(self,) -> Optional[str]:
        """
        Gets the resourceLink property value. A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.
        Returns: Optional[str]
        """
        return self._resource_link
    
    @resource_link.setter
    def resource_link(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceLink property value. A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.
        Args:
            value: Value to set for the resourceLink property.
        """
        self._resource_link = value
    
    @property
    def reviewed_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the reviewedBy property value. The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._reviewed_by
    
    @reviewed_by.setter
    def reviewed_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the reviewedBy property value. The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.
        Args:
            value: Value to set for the reviewedBy property.
        """
        self._reviewed_by = value
    
    @property
    def reviewed_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewedDateTime property value. The timestamp when the review decision occurred. Supports $select. Read-only.
        Returns: Optional[datetime]
        """
        return self._reviewed_date_time
    
    @reviewed_date_time.setter
    def reviewed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewedDateTime property value. The timestamp when the review decision occurred. Supports $select. Read-only.
        Args:
            value: Value to set for the reviewedDateTime property.
        """
        self._reviewed_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("accessReviewId", self.access_review_id)
        writer.write_object_value("appliedBy", self.applied_by)
        writer.write_datetime_value("appliedDateTime", self.applied_date_time)
        writer.write_str_value("applyResult", self.apply_result)
        writer.write_str_value("decision", self.decision)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalLink", self.principal_link)
        writer.write_str_value("recommendation", self.recommendation)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceLink", self.resource_link)
        writer.write_object_value("reviewedBy", self.reviewed_by)
        writer.write_datetime_value("reviewedDateTime", self.reviewed_date_time)
    

