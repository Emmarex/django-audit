from django.contrib.auth import get_user_model
from django.db import models


class AuditLog(models.Model):
    """ Audit log """

    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    user_agent = models.CharField(max_length=255,)
    ip_address = models.GenericIPAddressField(
        verbose_name="IP Address", null=True,)
    user = models.ForeignKey(
        to=get_user_model(), null=True, on_delete=models.CASCADE)
    content_type = models.CharField(
        verbose_name="Content Type", max_length=200,)
    query_string = models.TextField(
        verbose_name="Query String")
    http_method = models.CharField(
        verbose_name="HTTP Method", max_length=20,)
    http_referer = models.CharField(
        verbose_name="HTTP Method", max_length=500,)
    path_info = models.CharField(verbose_name="Path", max_length=255,)
    request_data = models.TextField(null=True)
    response_status_code = models.IntegerField(null=True)
    response_reason_phrase = models.TextField()
    attempt_time = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ["-attempt_time"]

    def __str__(self) -> str:
        """ unicode value for this model """
        return f'{self.user}, {self.attempt_time}'
