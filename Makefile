package:
	rm dist/**
	python3 -m pip install --upgrade build
	python3 -m pip install --upgrade twine
	python3 -m build
	python3 -m twine upload dist/*

package_test:
	rm dist/**
	python3 -m pip install --upgrade build
	python3 -m pip install --upgrade twine
	python3 -m build
	python3 -m twine upload --repository testpypi dist/*

test:
	PYTHONPATH=$$PYTHONPATH:$$PWD $$(which django-admin) test dj_audit --settings=dj_audit.test_settings

coverage_test:
	PYTHONPATH=$$PYTHONPATH:$$PWD $$(which django-admin) migrate --settings=dj_audit.test_settings
	PYTHONPATH=$$PYTHONPATH:$$PWD coverage run $$(which django-admin) test dj_audit --settings=dj_audit.test_settings
	PYTHONPATH=$$PYTHONPATH:$$PWD coverage xml

run_django_server:
	PYTHONPATH=$$PYTHONPATH:$$PWD $$(which django-admin) migrate --settings=dj_audit.test_settings
	PYTHONPATH=$$PYTHONPATH:$$PWD $$(which django-admin) runserver --settings=dj_audit.test_settings

make_migrations:
	PYTHONPATH=$$PYTHONPATH:$$PWD $$(which django-admin) makemigrations --settings=dj_audit.test_settings
