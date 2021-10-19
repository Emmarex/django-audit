package:
	python3 -m build
	python3 -m twine upload dist/*

package_test:
	python3 -m build
	python3 -m twine upload --repository testpypi dist/*

test:
	PYTHONPATH=$$PYTHONPATH:$$PWD django-admin test dj_audit --settings=dj_audit.test_settings

coverage_test:
	PYTHONPATH=$$PYTHONPATH:$$PWD coverage run --source=dj_audit $$(which django-admin) test dj_audit --settings=dj_audit.test_settings
