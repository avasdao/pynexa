from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='PyNexa',
    url='https://github.com/avasdao/pynexa',
    author='Ava\'s DAO',
    author_email='support@avasdao.org',

    # Needed to actually package something
    packages=['nexa'],

    # Needed for dependencies
    install_requires=['numpy'],

    # *strongly* suggested for sharing
    version='22.12.26',

    # The license can be anything you like
    license='MIT',
    description='A complete toolkit to develop Nexa application(s) in Python.',

    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
)
