# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSubjectScreening',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default='ckgathi', help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('reference', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='Anonymous Reference')),
                ('screening_identifier', models.CharField(blank=True, db_index=True, editable=False, max_length=50, verbose_name='Screening Id')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('meningitis_diagoses_by_csf_or_crag', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='First episode cryptococcal meningitis diagnosed by either: CSF India Ink or CSF cryptococcal antigen (CRAG)')),
                ('consent_to_hiv_test', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Willing to consent to HIV test')),
                ('willing_to_give_informed_consent', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], db_index=True, max_length=5, verbose_name='Participant or legal guardian/representative able and willing to give informed consent.')),
                ('pregnancy_or_lactation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=15, verbose_name='Pregnancy or lactation (Urine βhCG)')),
                ('previous_adverse_drug_reaction', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Previous Adverse Drug Reaction (ADR) to study drug (e.g. rash, drug induced blood abnormality)')),
                ('medication_contraindicated_with_study_drug', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Taking concomitant medication that is contra-indicated with any study drug')),
                ('two_days_amphotericin_b', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has received >48 hours of Amphotericin B (AmB) therapy prior to screening.')),
                ('two_days_fluconazole', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has received >48 hours of fluconazole treatment (> 400mg daily dose) prior to screening.')),
                ('is_eligible', models.BooleanField(default=False, editable=False)),
                ('ineligibility', models.TextField(editable=False, max_length=150, null=True, verbose_name='Reason not eligible')),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Subject Screening',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='SubjectScreening',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default='ckgathi', help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('reference', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Anonymous Reference')),
                ('screening_identifier', models.CharField(blank=True, editable=False, max_length=50, unique=True, verbose_name='Screening Id')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('meningitis_diagoses_by_csf_or_crag', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='First episode cryptococcal meningitis diagnosed by either: CSF India Ink or CSF cryptococcal antigen (CRAG)')),
                ('consent_to_hiv_test', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Willing to consent to HIV test')),
                ('willing_to_give_informed_consent', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, unique=True, verbose_name='Participant or legal guardian/representative able and willing to give informed consent.')),
                ('pregnancy_or_lactation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=15, verbose_name='Pregnancy or lactation (Urine βhCG)')),
                ('previous_adverse_drug_reaction', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Previous Adverse Drug Reaction (ADR) to study drug (e.g. rash, drug induced blood abnormality)')),
                ('medication_contraindicated_with_study_drug', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Taking concomitant medication that is contra-indicated with any study drug')),
                ('two_days_amphotericin_b', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has received >48 hours of Amphotericin B (AmB) therapy prior to screening.')),
                ('two_days_fluconazole', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, verbose_name='Has received >48 hours of fluconazole treatment (> 400mg daily dose) prior to screening.')),
                ('is_eligible', models.BooleanField(default=False, editable=False)),
                ('ineligibility', models.TextField(editable=False, max_length=150, null=True, verbose_name='Reason not eligible')),
            ],
            options={
                'verbose_name': 'Subject Screening',
            },
        ),
    ]