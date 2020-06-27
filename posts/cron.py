from django_cron import CronJobBase, Schedule
from .models import Like


class MyCronJob(CronJobBase):
    """Reset upvotese every 24 hours"""

    RUN_EVERY_MINS = 60 * 24

    schedule = Schedule(
        run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RUN_EVERY_MINS
    )
    code = "posts.my_cron_job"  # a unique code

    def do(self):
        queryset = Like.objects.all()
        for i in queryset:
            i.delete()
