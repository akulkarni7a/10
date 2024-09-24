# Generated by Django 3.2.20 on 2023-09-07 01:19

from django.db import migrations, models

from sentry.new_migrations.migrations import CheckedMigration


class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production. For
    # the most part, this should only be used for operations where it's safe to run the migration
    # after your code has deployed. So this should not be used for most operations that alter the
    # schema of a table.
    # Here are some things that make sense to mark as post deployment:
    # - Large data migrations. Typically we want these to be run manually by ops so that they can
    #   be monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   have ops run this and not block the deploy. Note that while adding an index is a schema
    #   change, it's completely safe to run the operation after the code has deployed.
    is_post_deployment = False

    dependencies = [
        ("sentry", "0555_set_neglectedrule_email_date_columns_nullable"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    """
                    ALTER TABLE "sentry_organizationmapping" ADD COLUMN "require_2fa" boolean NOT NULL DEFAULT FALSE;
                    """,
                    reverse_sql="""
            ALTER TABLE "sentry_organizationmapping" DROP COLUMN "require_2fa";
            """,
                    hints={"tables": ["sentry_organizationmapping"]},
                ),
            ],
            state_operations=[
                migrations.AddField(
                    model_name="organizationmapping",
                    name="require_2fa",
                    field=models.BooleanField(default=False),
                ),
            ],
        )
    ]
