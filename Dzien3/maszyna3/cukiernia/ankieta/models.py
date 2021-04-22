from django.db import models

# Create your models here.


class Pytanie(models.Model):
    tekst_pytania = models.CharField(max_length=200)
    data_publikacji = models.DateTimeField(
        "data publikacji", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Pytanie"
        verbose_name_plural = "Pytania"

    def __str__(self):
        return self.tekst_pytania

    def get_absolute_url(self):
        return reverse("_Pytanie", kwargs={"pk": self.pk})


class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie,  on_delete=models.CASCADE)
    tekst_odpowiedzi = models.CharField(max_length=200)
    glosy = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Odpowiedź"
        verbose_name_plural = "Odpowiedzi"

    def __str__(self):
        return self.tekst_odpowiedzi

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
