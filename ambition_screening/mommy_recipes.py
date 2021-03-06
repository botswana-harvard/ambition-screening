from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import NOT_APPLICABLE, YES, NO, MALE, NORMAL
from faker import Faker
from model_mommy.recipe import Recipe

from .models import SubjectScreening

fake = Faker()

subjectscreening = Recipe(
    SubjectScreening,
    report_datetime=get_utcnow(),
    gender=MALE,
    age_in_years=40,
    meningitis_dx=YES,
    will_hiv_test=YES,
    consent_ability=YES,
    mental_status=NORMAL,
    pregnancy=NOT_APPLICABLE,
    breast_feeding=NOT_APPLICABLE,
    previous_drug_reaction=NO,
    contraindicated_meds=NO,
    received_amphotericin=NO,
    received_fluconazole=NO,
    site=Site.objects.get_current())
