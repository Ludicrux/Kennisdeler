KennisDeler 

requirements:
  python3.6
  pip3
  postgresql


(preferable in a virtualenv)
change dir to root folder "kennisdeler"

$ python3 manage.py migrate --settings=kennisdeler.settings.base
$ python3 manage.py migrate --settings=kennisdeler.settings.base


Database connection type is assumed to be "Trust"
