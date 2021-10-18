from django.db import models
from django.contrib.auth import get_user_model


class AuditLog(models.Model):
    """ Audit log """

    user_agent = models.CharField(max_length=255,)
    ip_address = models.GenericIPAddressField(
        verbose_name="IP Address", null=True,)
    username = models.ForeignKey(
        to=get_user_model(), null=True, on_delete=models.CASCADE)
    http_accept = models.CharField(
        verbose_name="HTTP Accept", max_length=1025,)
    path_info = models.CharField(verbose_name="Path", max_length=255,)
    request_data = models.TextField(null=True)
    attempt_time = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ["-attempt_time"]

    def __str__(self) -> str:
        """ unicode value for this model """
        return f'{self.username}, {self.attempt_time}'
