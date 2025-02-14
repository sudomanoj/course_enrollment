from django.core.exceptions import ValidationError

def validate_video_size(file):
    """
    Function to validate the video size upto 50MB.
    """
    if file.size > 50 * 1024 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 50MB.")
    return file

def validate_document_size(file):
    """
    Function to validate the document size upto 10MB.
    """
    if file.size > 10 * 1024 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 10MB.")
    return file