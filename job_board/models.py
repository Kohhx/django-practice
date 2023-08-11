from django.db import models

# Create your models here.
# Job posting
## title, description, company and salary

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=200)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

# Make migrations
## Create instruction telling django how db has changed

# Run migrations to create the table in DB
## Run instruction to update db

# CRUD OPERATIONS
    # Create
    # Read
    # Update
    # Delete
