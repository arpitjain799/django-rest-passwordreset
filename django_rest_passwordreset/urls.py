""" URL Configuration for core auth """
from django.conf.urls import url

from django_rest_passwordreset.views import ResetPasswordValidateTokenViewSet, ResetPasswordConfirmViewSet, \
    ResetPasswordRequestTokenViewSet, reset_password_validate_token, reset_password_confirm, \
    reset_password_request_token

app_name = 'password_reset'


def add_reset_password_urls_to_router(router, base_path=''):
    router.register(
        base_path + r'/validate_token',
        ResetPasswordValidateTokenViewSet,
        basename='reset-password-validate'
    )
    router.register(
        base_path + r'/confirm',
        ResetPasswordConfirmViewSet,
        basename='reset-password-confirm'
    )
    router.register(
        base_path + r'',
        ResetPasswordRequestTokenViewSet,
        basename='reset-password-request'
    )


urlpatterns = [
    url(r'^validate_token/', reset_password_validate_token, name="reset-password-validate"),
    url(r'^confirm/', reset_password_confirm, name="reset-password-confirm"),
    url(r'^', reset_password_request_token, name="reset-password-request"),
]
