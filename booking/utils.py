from django.contrib.auth.models import User

def get_trainers():
    trainers = User.objects.filter(is_staff=True, is_superuser=False)
    return [(str(trainer.username), str(trainer.username)) for trainer in trainers]
