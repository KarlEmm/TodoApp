from django.db import models

class Task(models.Model):
    """A task the user has to do."""
    main = models.CharField(max_length=150, null=True)
    details = models.TextField(null=True)
    isdone = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.main
