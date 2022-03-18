from django import __version__
from django.contrib.auth import get_user_model
from django.db import models

if __version__ >= '3.1':
    from django.db.models import JSONField
else:
    from django.contrib.postgres.fields import JSONField


LOG_STATUS_CHOICES = (
    ('success', 'success'),
    ('failed', 'failed'),
    ('warning', 'warning'),
)

RESPONSE_TYPE_CHOICES = (
    ('http', 'http'),
    ('rest', 'rest'),
)


class AuditLog(models.Model):
    """ Audit log """

    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    user_agent = models.CharField(max_length=255,)
    ip_address = models.GenericIPAddressField(
        verbose_name="IP Address", null=True,)
    host_name = models.CharField(
        verbose_name="Host Name", max_length=200, default='')
    user = models.ForeignKey(
        to=get_user_model(), null=True, on_delete=models.CASCADE)
    content_type = models.CharField(
        verbose_name="Content Type", max_length=200,)
    query_string = models.TextField(
        verbose_name="Query String")
    post_data = JSONField(
        verbose_name="Post Data", null=True, blank=True,
    )
    http_method = models.CharField(
        verbose_name="HTTP Method", max_length=20,)
    http_referer = models.TextField(verbose_name="HTTP Referer")
    path_info = models.CharField(verbose_name="Path", max_length=255,)
    request_data = models.TextField(null=True)
    response_status_code = models.IntegerField(null=True)
    response_reason_phrase = models.TextField()
    response_body = JSONField(default=dict)
    attempt_time = models.DateTimeField()  # this should serve as request time
    # this should serve as the time a response was sent back to the client if any
    response_time = models.DateTimeField(auto_now_add=True, )
    log_status = models.CharField(
        max_length=20, choices=LOG_STATUS_CHOICES, default='success')
    response_type = models.CharField(
        max_length=20, choices=RESPONSE_TYPE_CHOICES, default='http')

    class Meta:
        ordering = ["-attempt_time"]

    def __str__(self) -> str:
        """ unicode value for this model """
        return f'{self.user}, {self.attempt_time}'

    @property
    def response_duration(self):
        if self.response_time:
            diff = self.response_time - self.attempt_time
            minute, second = divmod(diff.seconds, 60)
            return f"{minute}m {second}s {diff.microseconds}ms"
        return f"N/A"
