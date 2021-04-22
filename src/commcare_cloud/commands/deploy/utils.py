from commcare_cloud.alias import commcare_cloud
from commcare_cloud.colors import color_summary
from commcare_cloud.commands.terraform.aws import get_default_username


def announce_deploy_start(environment, system_name):
    mail_admins(
        environment,
        subject="{user} has initiated a {system_name} deploy to {environment}".format(
            user=get_default_username(),
            system_name=system_name,
            environment=environment.meta_config.deploy_env,
        ),
    )


def announce_deploy_failed(environment):
    mail_admins(
        environment,
        subject=f"Formplayer deploy to {environment.name} failed",
    )


def announce_deploy_success(environment, diff_ouptut):
    mail_admins(
        environment,
        subject=f"Formplayer deploy successful - {environment.name}",
        message=diff_ouptut
    )


def mail_admins(environment, subject, message=''):
    if environment.fab_settings_config.email_enabled:
        print(color_summary(f">> Sending email: {subject}"))
        commcare_cloud(
            environment.name, 'django-manage', '--quiet', 'mail_admins',
            '--subject', subject,
            '--environment', environment.meta_config.deploy_env,
            '--html',
            message,
            show_command=False
        )