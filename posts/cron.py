from django_cron import CronJobBase, Schedule
from .models import Like


class MyCronJob(CronJobBase):
    """Reset upvotese every 24 hours"""
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "posts.my_cron_job"  # a unique code

    def do(self):
        queryset = Like.objects.all()
        for i in queryset:
            i.delete()

