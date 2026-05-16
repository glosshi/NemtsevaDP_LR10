from django.db import models

class SuspiciousIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    threat_level = models.CharField(max_length=20, choices=[
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
        ('critical', 'Критический'),
    ])
    first_detected = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Подозрительный IP'
        verbose_name_plural = 'Подозрительные IP'

    def __str__(self):
        return f'{self.ip_address} ({self.threat_level})'


class TrafficLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    protocol = models.CharField(max_length=10, choices=[
        ('TLS', 'TLS'),
        ('DTLS', 'DTLS'),
        ('HTTP', 'HTTP'),
        ('OTHER', 'Другой'),
    ])
    entropy = models.FloatField(help_text='Энтропия трафика (0-8)')
    encrypted = models.BooleanField(default=False)
    suspicious = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Лог трафика'
        verbose_name_plural = 'Логи трафика'
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.source_ip} -> {self.destination_ip} ({self.timestamp})'


class SecurityIncident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=[
        ('info', 'Информация'),
        ('warning', 'Предупреждение'),
        ('critical', 'Критический'),
    ])
    detected_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    related_ip = models.ForeignKey(
        SuspiciousIP,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Инцидент безопасности'
        verbose_name_plural = 'Инциденты безопасности'
        ordering = ['-detected_at']

    def __str__(self):
        return f'{self.title} ({self.severity})'
