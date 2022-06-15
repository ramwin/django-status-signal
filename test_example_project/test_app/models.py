import logging

from django.db import models
from django.dispatch.dispatcher import Signal as DjangoSignal
from django_status_signal import Signal


logger = logging.getLogger(__name__)


class Task(models.Model):
    status = models.CharField(
        choices=(
            ("start", "start"),
            ("doing", "doing"),
            ("success", "success"),
            ("fail", "fail"),
        ),
        max_length=31,
    )

    @classmethod
    def after_success(cls, sender, **kwargs):
        logger.info((
            "after_success called, "
            "so the sender's status should be success: "
            f"{sender.status}"
        ))
        raise Exception


normal_post_save = DjangoSignal()
normal_post_save.connect(Task.after_success, Task)
post_save = Signal()
post_save.connect(Task.after_success, Task, dispatch_status="success")
