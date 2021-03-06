export RELEASE_REMOTE ?=origin

install-semver:
	@(sudo gem install semver) || true

# Publish new release. Usage:
#   make tag VERSION=(major|minor|patch)
# You need to install https://github.com/flazz/semver/ before
tag: install-semver
	@semver inc $(VERSION)
	@echo "New release: `semver tag`"
	@echo Releasing sources
	@sed -i -r "s/([0-9]+\.[0-9]+\.[0-9]+)/`semver tag`/g" \
	    setup.py \
		ddd_domain_driven_design/__init__.py
	@sed -i -r "s/version='v/version='/g" setup.py
	@sed -i -r "s/__version__ = 'v/__version__ = '/g" ddd_domain_driven_design/__init__.py

# Tag git with last release
# https://gist.github.com/gboeing/dcfaf5e13fad16fc500717a3a324ec17
# https://github.com/pypa/twine
release:
	@git add .
	@(git commit -m "releasing `semver tag`") || true
	@(git tag --delete `semver tag`) || true
	@(git push --delete origin `semver tag`) || true
	@git tag `semver tag`
	@git push origin `semver tag`
	@GIT_CB=$(git symbolic-ref --short HEAD) && git push -u ${RELEASE_REMOTE} $(GIT_CB)
	@rm -rf dist build ddd_domain_driven_design.egg-info
	@python setup.py sdist bdist_wheel --universal
	@twine upload dist/*