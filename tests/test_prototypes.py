import os
import logging

import yaml


LOG = logging.getLogger(__name__)


def _check_library(l):
    LOG.debug('checking library %s', l)

    with open(l, 'r') as f:
        library = yaml.safe_load(f)

    assert 'description' in library, "No description field in %s" % l
    assert 'url' in library, "No url field in %s" % l
    assert 'prototypes' in library, "No prototypes field in %s" % l

    for p, prototype in library['prototypes'].iteritems():
        LOG.debug('checking prototype %s', p)
        assert 'development_status' in prototype, "No developement_status field in %s::%s" % (l, p)
        assert 'author' in prototype, "No author field in %s::%s" % (l, p)
        assert 'description' in prototype, "No description field in %s::%s" % (l, p)
        assert 'class' in prototype, "No class field in %s::%s" % (l, p)
        assert 'config' in prototype, "No config field in %s::%s" % (l, p)
        assert 'node_type' in prototype, "No node_type field in %s::%s" % (l, p)
        assert 'tags' in prototype, "No tags field in %s::%s" % (l, p)
        assert isinstance(prototype['tags'], list), "Wrong type for attribute tags in %s::%s" % (l, p)
        assert 'indicator_types' in prototype, "No indicator_types field in %s::%s" % (l, p)
        assert isinstance(prototype['indicator_types'], list), "Wrong type for attribute indicator_types in %s::%s" % (l, p)
        assert len(prototype['indicator_types']), "0 indicator_types in %s::%s" % (l, p)

def test_prototypes():
    libraries = [os.path.join('prototypes', x) for x in os.listdir('prototypes')]

    for l in libraries:
        yield _check_library, l
