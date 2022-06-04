#!/usr/bin/env python3

from docutils.parsers.rst import roles, nodes, directives, Directive
from docutils.statemachine import StringList


def get_revision():
    import subprocess
    p = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True)
    assert p.returncode == 0
    return p.stdout.strip().decode('utf8')


def role(func):
    roles.register_local_role(func.__name__, func)


def directive(cls):
    directives.register_directive(cls.__name__, cls)


@role
def tel(role, rawtext, text, lineno, inliner, options=None, content=None):
    ref = 'tel:' + text.replace(' ', '')
    node = nodes.reference(rawtext, text, refuri=ref)
    return [node], []


@role
def github(role, rawtext, text, lineno, inliner, options=None, content=None):
    ref = f'https://github.com/{text}'
    node = nodes.reference(rawtext, '@'+text, refuri=ref)
    return [node], []


@role
def revision(role, rawtext, text, lineno, inliner, options=None, content=None):
    rev = get_revision()
    url = f'https://github.com/Akaricchi/resume/commit/{rev}'
    
    node = nodes.reference(rawtext, refuri=url)
    node += nodes.literal(text=rev[:8])
   
    return [node], []


@role
def date(role, rawtext, text, lineno, inliner, options=None, content=None):
    import datetime
    now = datetime.datetime.utcnow()
    node = nodes.inline(text=now.strftime(text))
    return [node], []


@directive
class project(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'url': directives.uri,
                   'role': directives.unchanged,
                   }
    has_content = True

    def run(self):
        import sys
        self.assert_has_content()
        
        name = self.arguments[0]
        self.options['name'] = name
        
        text = '\n'.join(self.content)
        section = nodes.section(text)
        self.add_name(section)
        
        title = nodes.title(classes=['project-title'])
        title += nodes.reference(text=name, refuri=self.options['url'])
        section += title
        
        # HACK
        role_markup = self.options['role']
        role_markup = role_markup.replace('(', '*(')
        role_markup = role_markup.replace(')', ')*')
        role = nodes.container(classes=['project-role'])
        self.state.nested_parse(StringList([role_markup]), 0, role)
        section += role
        
        desc = nodes.container(classes=['project-desc'])
        self.state.nested_parse(self.content, self.content_offset, desc)
        section += desc
        
        return [section]


if __name__ == '__main__':
    from docutils.core import publish_cmdline, default_description
    publish_cmdline(writer_name='html5', description=default_description)
