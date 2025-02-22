from django.db import models
from django.utils.crypto import get_random_string

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

NB_GOV_POSITIONS = 10

def get_new_ref():
    """ Generate a new government ref """
    return get_random_string(length=32)


# Create your models here.
class User(models.Model):
    email_address = models.EmailField()
    first_name = models.CharField(max_length=32, default="")
    last_name = models.CharField(max_length=32, default="")


class Government(models.Model):
    # long enough random string, to be set at generation
    reference = models.CharField(max_length=32, blank=True, unique=True)
    save_date = models.DateTimeField('date saved', blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return "{} on {}".format(self.reference, self.save_date)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = get_new_ref()

        super(Government, self).save(*args, **kwargs)


class Candidate(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    image_file = models.ImageField(upload_to='img', blank=True, null=True)
    image_url = models.URLField(default="https://www.parrainages-primairepopulaire.fr/file/primaire_candidat_mystere.png")
    running = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Position(models.Model):
    position_name = models.CharField(max_length=128)
    slug = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.position_name


class Config(models.Model):
    government = models.ForeignKey(Government, on_delete=models.CASCADE) #if the government is deleted, its configs should be too
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return "Config {}: {} pour {}".format(self.government, self.candidate, self.position)




@receiver(pre_save, sender=Config)
def check_config(sender, instance, **kwargs):
    """ Returns True if both Position and Candidate are new, for this government

    If not True raises a custom exception
    """
    # disable the handler during fixture loading
    if kwargs['raw']:
        return
    current_id = instance.id
    current_government = instance.government
    current_candidate = instance.candidate
    current_position = instance.position

    # Get existing Config rows
    existing_rows = Config.objects.filter(government=current_government)

    # Check distinct from values in instance
    for row in existing_rows:
        if (row.candidate.id == current_candidate.id):
            if (row.id != current_id):
                raise ValidationError("Duplicate candidate in Config " + str(row.id) + ' : ' + str(current_id))

        if (row.position.id == current_position.id):
            if (row.id != current_id):
                raise ValidationError("Duplicate position in Config")

    return True
