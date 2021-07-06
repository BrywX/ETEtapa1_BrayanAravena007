# ETEtapa1_BrayanAravena007
Nota 4
Aqui la configuracion de la data base:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/orcl',
        'USER': 'cn',
        'PASSWORD': '1234',
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },
}

Aqui el superuser y contraseña de django:
Superusuario: admin
contraseña: caos1234