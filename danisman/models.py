from django.db import models
from django.utils import timezone
import locale
# Create your models here.
locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')

class Danisman(models.Model):
    title = models.CharField(max_length=100)  # Danışmanın unvanı (ör. Dr., Prof., vb.)
    full_name = models.CharField(max_length=255)  # Danışmanın tam adı
    specialization = models.CharField(max_length=255)  # Danışmanın uzmanlık alanı (ör. Psikolog, Terapi, vb.)
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # Danışmanlık ücretini saklamak için (ör. 150.00)
    profile_picture = models.ImageField(upload_to='consultant_images/', blank=True, null=True)  # Profil fotoğrafı (isteğe bağlı)
    bio = models.TextField(blank=True, null=True)  # Danışman hakkında açıklamalar

    created_at = models.DateTimeField(auto_now_add=True)  # Kaydın oluşturulma zamanı
    updated_at = models.DateTimeField(auto_now=True)  # Kaydın son güncellenme zamanı

    def __str__(self):
        return f"{self.title} {self.full_name} - {self.specialization}"

    class Meta:
        ordering = ['full_name']



class Uygunluk(models.Model):
    psychologist = models.ForeignKey(Danisman, on_delete=models.CASCADE, related_name="availabilities")
    day_of_week = models.CharField(max_length=10)  # Example: Monday, Tuesday, etc.
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ('psychologist', 'day_of_week', 'start_time')

    def __str__(self):
        # Türkiye saati formatında sadece saat ve dakika göster
        start_time_local = timezone.localtime(self.start_time).strftime('%H:%M')
        end_time_local = timezone.localtime(self.end_time).strftime('%H:%M')
        
        return f"{self.psychologist.full_name} - {self.day_of_week} {start_time_local} - {end_time_local}"
    