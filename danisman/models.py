from django.db import models

# Create your models here.

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