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
		ddd/__init__.py
	@sed -i -r "s/version='v/version='/g" setup.py
	@sed -i -r "s/__version__ = 'v/__version__ = '/g" ddd/__init__.py

# Tag git with last release
release:
	@git add .
	@git commit -m "releasing `semver tag`"
