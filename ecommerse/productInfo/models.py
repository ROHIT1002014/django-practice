from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('S', 'Style & Fashion'),
    ('SW', 'Sport wear'),
    ('MH', 'Medical Helth'),
    ('MT', 'Mobiles and Tablets'),
    ('CE', 'Consumer Electronics'),
    ('BK', 'Books'),
    ('HF', 'Home Furnishings')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
  title = models.CharField(max_length=100)
  price = models.FloatField()
  discount_price = models.FloatField(blank=True, null=True)
  category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
  label = models.CharField(choices=LABEL_CHOICES, max_length=1)
  description = models.TextField()
  image = models.ImageField()

  def __str__(self):
    return self.title


