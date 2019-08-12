from django.db import models
from django.urls import reverse
from django.utils import timezone
from stdimage import StdImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Publicacion(models.Model):
    titulo = models.CharField("titulo de la publicacion",max_length=100)
    fechaHoraPublicacion = models.DateTimeField('fecha y hora de la publicacion', default=timezone.now)
    imagen = StdImageField(upload_to='documents/%Y/%m/%d', blank=True, null=True, variations={'large': (640, 480)})
    texto = RichTextUploadingField("texto de la publicacion",
                                   config_name='default',
                                   external_plugin_resources= [(
                                       'youtube',
                                        '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                        'plugin.js',
                                    )],
                                   )

    class Meta:
        ordering = ('-fechaHoraPublicacion',)

    def __str__(self):
    	return self.titulo

    def get_absolute_url(self):
        return reverse('detail', kwargs={"publicacion_id":self.id})



