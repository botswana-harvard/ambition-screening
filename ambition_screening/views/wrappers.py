from django.apps import apps as django_apps

from edc_base.utils import get_uuid
from edc_dashboard.wrappers.model_wrapper import ModelWrapper
from ambition_subject.views.wrappers import SubjectConsentModelWrapper


class SubjectScreeningModelWrapper(ModelWrapper):

    model_name = 'ambition_screening.subjectscreening'
    next_url_name = django_apps.get_app_config(
        'ambition_screening').listboard_url_name
    next_url_attrs = {
        'ambition_screening.subjectscreening': ['screening_identifier']}
    extra_querystring_attrs = {
        'ambition_screening.subjectscreening': ['sex']}
    url_instance_attrs = [
        'screening_identifier', 'sex']

    consent_model_wrapper_class = SubjectConsentModelWrapper

    @property
    def is_consented(self):
        return self._original_object.is_consented

    @property
    def consent(self):
        """Returns a wrapped saved or unsaved consent.
        """
        # FIXME: self._original_object.consent_object should
        # return a consent object
        if self._original_object.consent:
            consent = self._original_object.consent
        else:
            try:
                model = self._original_object.consent_object.model
                print(model, 'model')
            except AttributeError:
                consent = None
            else:
                try:
                    consent = model.objects.get(
                        version=self._original_object.consent_object.version,
                        subject_screening=self._original_object,)
                except model.DoesNotExist:
                    consent = model(
                        subject_identifier=self._original_object.subject_identifier,
                        consent_identifier=get_uuid(),
                        subject_screening=self._original_object,
                        version=self._original_object.consent_object.version)
                consent = self.consent_model_wrapper_class(consent)
        return consent
