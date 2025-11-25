% Django M.E.T. Syllabus

This file is a Markdown-converted copy of the original "Django MET Syallabus.txt" provided in the repository. It groups the course topics into a single, easy-to-read document under the `docs/` folder.

## Table of Contents

- Understanding of Framework
- Django Web App Framework
- Pre-requisites and Setup
- Django Project Structure
- Applications and Views
- URL Dispatcher and Routing
- Templates and Static Files
- Django Template Language (DTL)
- Models and Admin
- Forms and Validation
- ORM and Querysets
- Authentication & Authorization
- Sessions, Cookies, Cache, Signals, Middleware
- Class-Based Views
- Pagination, Security, Database Configuration

---

## Understanding of Framework

- Why is Framework?
- What is a Web App Framework?
- What is MVC Architecture?
- Understanding of Django Web App Framework

## Pre-requisites and Setup

- Python installation
- Virtual Environment
- Django installation
- Uninstallation of Django and Python
- VS Code and recommended extensions

## Django Project Creation

- Creating a new Django project
- Understanding Django project directory
  - `settings.py`
  - `asgi.py`
  - `wsgi.py`
  - `manage.py`
  - `urls.py`

## Creating Applications

- Creating an app inside a Django project
- Files inside an application
- Starting and stopping the development server

## Request and Response

- Understanding HTTP request and response cycle
- Function-Based Views (FBV)
- MVT architecture overview

## URL Dispatcher / URL Patterns

- `path()` and routing
- `name` for URLs
- Templates and rendering
- Dynamic URLs and custom path converters
- `include()` and namespaces
- App registration

## Templates

- Template folder structure
- Setup template path in `settings.py`
- `TEMPLATES` configuration and `INSTALLED_APPS`
- Rendering templates with context and `HttpResponse`
- Application-wise templates
- Injecting CSS and JavaScript

## Static Files

- `STATICFILES_DIRS` and `static` template tag
- Serving static files in development

## Django Template Language (DTL)

- `{{ variable }}` and expression output
- `{% for %}` loops and loop variables
- `{% if %}` conditionals
- Filters and `{% include %}`
- Template inheritance: `{% extends %}`, `{% block %}`

## Using Bootstrap & JS in Templates

- Adding Bootstrap, jQuery, Popper

## Models and the Admin

- Creating models
- Model fields and model inheritance
- Migrations and `makemigrations` / `migrate`
- Creating superuser and registering models with admin

## Forms

- `forms.Form` and `forms.ModelForm`
- Form widgets and attributes (id, label, ordering)
- Handling GET and POST, CSRF protection
- Validation: field validators and form-level validation
- Displaying form errors

## ORM and Querysets

- QuerySet methods: `all()`, `get()`, `filter()`, `values()`, `values_list()`
- Set operations: `union`, `intersection`
- Field lookups, aggregation, and annotations
- Model relations: OneToOne, ForeignKey, ManyToMany
- Model managers and custom querysets

## Messages Framework

- Levels and tags

## CRUD Project with Function-Based Views

- Building CRUD operations using FBVs

## Authentication & Authorization

- `django.contrib.auth`
- Creating users, groups, permissions
- Login, logout, authentication helpers (`authenticate()`, `login()`, `logout()`)
- `UserCreationForm`, `AuthenticationForm`, `is_authenticated`
- Profiles and admin user management

## Pagination

- Pagination with function-based views
- Pagination with class-based views

## Sessions, Cookies, Cache

- Cookies and session framework
- Session expiry and file-based sessions
- Page and site caching, cache per view, template fragment caching, low-level cache

## Signals and Middleware

- Built-in and custom signals
- Middleware hooks and `get_response()` flow
- Writing custom middleware (function/class based)

## Class-Based Views (CBV)

- `View`, `TemplateView`, `RedirectView`, `FormView`, `ListView`, `CreateView`, `UpdateView`, `DeleteView`, `DetailView`
- Authentication decorators and mixins like `login_required` and customization

## Database Configuration

- PostgreSQL and MongoDB connections (overview)

## Security in Django

- Best practices and common settings

---

### Notes

- This document is a cleaned and organized conversion of the original syllabus text file. Keep this file under `docs/` so the repository root remains tidy and ready for adding new projects under separate folders (e.g., `projects/`).
