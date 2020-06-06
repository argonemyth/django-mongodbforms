from djng.forms.fields import DefaultFieldMixin
from . import fields as mongo_fields


class NgCharField(DefaultFieldMixin, mongo_fields.MongoCharField):

    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_length_errors())
        return errors


class NgListField(DefaultFieldMixin, mongo_fields.ListField):
    pass

class NgReferenceField(DefaultFieldMixin, mongo_fields.ReferenceField):
    pass