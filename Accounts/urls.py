from django.conf.urls import patterns

urlpatterns = patterns('django.contrib.auth',

    #(r'^$', 'views.index'),

    (r'^login/$',
     'views.login',
         {'template_name': 'accounts/login.html'}),

    (r'^logout/$',
     'views.logout',
         {'template_name': 'home/homepage.html'}),

    (r'^password_change/$',
     'views.password_change',
         {'template_name': 'accounts/passwordChange.html'}),

    (r'^password_change/done/$',
     'views.password_change_done',
         {'template_name': 'accounts/password_change_done.html'}),

    (r'^password_reset/$',
     'views.password_reset',
         {'template_name': 'accounts/password_reset_form.html',
          'email_template_name': 'accounts/password_reset_email.html'}),

    (r'^password_reset/done/$',
     'views.password_reset_done',
         {'template_name': 'accounts/password_reset_done.html'}),

    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
     'views.password_reset_confirm',
         {'template_name': 'accounts/password_reset_confirm.html'}),

    (r'^reset/done/$',
     'views.password_reset_complete',
         {'template_name': 'accounts/password_reset_complete.html'}),
)

urlpatterns += patterns("",
#    (r'^signup/$',
#     'accounts.views.signup',
#         {'template_name': 'accounts/signup_form.html',
#          'email_template_name': 'accounts/signup_email.html'}),
#
#    (r'^signup/done/$',
#     'accounts.views.signup_done',
#         {'template_name': 'accounts/signup_done.html'}),
#
#    (r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
#     'accounts.views.signup_confirm'),
#
#    (r'^signup/complete/$',
#     'accounts.views.signup_complete',
#         {'template_name': 'accounts/signup_complete.html'}),
)
