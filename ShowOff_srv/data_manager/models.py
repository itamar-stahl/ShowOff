from enum import unique
from django.db import connection, models
from django.db.models.base import Model
from numpy import record
from django.db import DatabaseError


from user_manager.models import Group, User

class MissingRecords(Exception):
    """TODO"""
    pass


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="records")
    date = models.DateField(blank=False, null=False)
    overall_time = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    distracting_time = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    original_data = models.BooleanField(default=True)
    
    @staticmethod
    def get_user_usage(user, first_day, last_day, function=None):
        try: 
            records = Record.objects.filter(user=user, date__range=(first_day, last_day))
            if function is not None:       
                num_of_days, num_of_records = (last_day-first_day).days+1, records.count()
                if num_of_records != num_of_days:
                    raise MissingRecords()
                overall = list(records.aggregate(function('overall_time')).values())[0]
                distracting = list(records.aggregate(function('distracting_time')).values())[0]
                return  [round(float(overall), 2), round(float(distracting), 2)]
            return records
        except DatabaseError:
            return None
        
    @staticmethod
    def get_group_usage(group_, first_day, last_day, function=None):
        group_members = User.objects.filter(group=group_)
        records = Record.objects.none()
        for user in group_members:
            records = records.union(Record.get_user_usage(user, first_day, last_day, function))
        return records
   
    def __str__(self):
        return f"id: {self.id}, {self.date}, {self.user_id}: overall: {self.overall_time}, distracting: {self.distracting_time}"
    
    class Meta:
        unique_together = ('user_id', 'date')
    


   
