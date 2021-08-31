from django.db import models
from django.core.validators import RegexValidator

KEY_REQUIERMENTS = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{50}$"

   
def delete_admin(self):
    #TODO
    return None


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, blank=True, null=True, related_name="members")
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}, group_id: {self.group_id}"
     

class Group(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50, validators=[RegexValidator(KEY_REQUIERMENTS)], blank=False, null=False)
    admin = models.ForeignKey(User, blank=True, null=True, on_delete=models.RESTRICT, related_name="managed_group") # TODO
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, key: {self.key}. admin_id: {self.admin}"
