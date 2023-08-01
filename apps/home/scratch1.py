from django.db import models

# Abstract base class for SponsorshipType
class BaseSponsorshipType(models.Model):
    # Common fields shared by all sub-classes
    # Add other fields as needed for the base class
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Base class field

    class Meta:
        abstract = True

# Sub-class with additional cost field
class SubSponsorshipType(BaseSponsorshipType):
    # Additional fields specific to the sub-class
    # Add other fields as needed for the sub-class
    additional_cost = models.DecimalField(max_digits=10, decimal_places=2)  # Override cost field

    # Optional: If you want a custom property to get the total cost
    @property
    def total_cost(self):
        return self.cost + self.additional_cost

# Usage
# Creating instances of sub-class and base class
base_sponsorship = BaseSponsorshipType.objects.create(name='Base Sponsorship', cost=100)
sub_sponsorship = SubSponsorshipType.objects.create(name='Sub Sponsorship', cost=150, additional_cost=50)

# Accessing fields
print(base_sponsorship.cost)            # Output: 100
print(sub_sponsorship.cost)             # Output: 150 (overrides the base class cost field)
print(sub_sponsorship.additional_cost)  # Output: 50
print(sub_sponsorship.total_cost)       # Output: 200 (computed using the custom property)
