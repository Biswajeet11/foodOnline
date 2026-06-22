from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    extension = os.path.splitext(value.name)[1]  #cover-image.jpg
    print(extension)
    valid_extensions = ['.png','.jpg','.jpeg']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsupported file extensions. Allowed Extensions:'+str(valid_extensions))
    

