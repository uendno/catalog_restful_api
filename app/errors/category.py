from marshmallow import ValidationError
from ..models.category import CategoryModel


class CategoryError:
    @staticmethod
    def validate_name(name):
        if len(name) > 40:
            raise ValidationError('Name length must be equal or lower than 40.')
        elif CategoryModel.find_by_name(name):
            raise ValidationError('The category already exists.')

    @staticmethod
    def validate_description(description):
        if len(description) > 200:
            raise ValidationError('Description length must be equal or lower than 200 characters.')
