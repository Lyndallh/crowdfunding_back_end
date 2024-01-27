from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_close = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
        )
    # @property
    # def sum_pledges(self):
    #     sum_pledges = self.pledges.aggregate(sum=models.Sum('amount'))['sum']
    #     if sum_pledges:
    #         return sum_pledges
    #     else:
    #         return 0

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
          'Project',
      on_delete=models.CASCADE,
      related_name='project_pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
        )
    date_created = models.DateTimeField(auto_now_add=True)