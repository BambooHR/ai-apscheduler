# coding: utf-8
import os.path

from setuptools import setup, find_packages


here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
readme = open(readme_path).read()

setup(
    name='APScheduler',
    # Removed use_scm_version as it's now configured in pyproject.toml
    description='In-process task scheduler with Cron-like capabilities',
    long_description=readme,
    author=u'Alex Grönholm',
    author_email='apscheduler@nextday.fi',
    url='https://github.com/agronholm/apscheduler',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='scheduling cron',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    # Keeping setuptools_scm in setup_requires for backward compatibility
    setup_requires=[
        'setuptools_scm>=8.0.0'
    ],
    install_requires=[
        'setuptools >= 61',
        'six >= 1.4.0',
        'pytz',
        'tzlocal >= 2.0, != 3.*'
    ],
    extras_require={
        ':python_version == "2.7"': ['futures'],
        ':python_version < "3.5"': ['funcsigs'],
        'asyncio:python_version == "2.7"': ['trollius'],
        'gevent': ['gevent'],
        'mongodb': ['pymongo >= 3.0'],
        'redis': ['redis >= 3.0'],
        'rethinkdb': ['rethinkdb >= 2.4.0'],
        'sqlalchemy': ['sqlalchemy >= 0.8'],
        'tornado': ['tornado >= 4.3'],
        'twisted': ['twisted'],
        'zookeeper': ['kazoo'],
        'testing': [
            'pytest < 6',
            'pytest-cov',
            'pytest-tornado5'
        ],
        'testing:python_version == "2.7"': ['mock'],
        'testing:python_version == "3.4"': ['pytest_asyncio < 0.6'],
        'testing:python_version >= "3.5"': ['pytest_asyncio'],
        'doc': [
            'sphinx',
            'sphinx-rtd-theme',
        ],
    },
    zip_safe=False,
    entry_points={
        'apscheduler.triggers': [
            'date = apscheduler.triggers.date:DateTrigger',
            'interval = apscheduler.triggers.interval:IntervalTrigger',
            'cron = apscheduler.triggers.cron:CronTrigger',
            'and = apscheduler.triggers.combining:AndTrigger',
            'or = apscheduler.triggers.combining:OrTrigger'
        ],
        'apscheduler.executors': [
            'debug = apscheduler.executors.debug:DebugExecutor',
            'threadpool = apscheduler.executors.pool:ThreadPoolExecutor',
            'processpool = apscheduler.executors.pool:ProcessPoolExecutor',
            'asyncio = apscheduler.executors.asyncio:AsyncIOExecutor [asyncio]',
            'gevent = apscheduler.executors.gevent:GeventExecutor [gevent]',
            'tornado = apscheduler.executors.tornado:TornadoExecutor [tornado]',
            'twisted = apscheduler.executors.twisted:TwistedExecutor [twisted]'
        ],
        'apscheduler.jobstores': [
            'memory = apscheduler.jobstores.memory:MemoryJobStore',
            'sqlalchemy = apscheduler.jobstores.sqlalchemy:SQLAlchemyJobStore [sqlalchemy]',
            'mongodb = apscheduler.jobstores.mongodb:MongoDBJobStore [mongodb]',
            'rethinkdb = apscheduler.jobstores.rethinkdb:RethinkDBJobStore [rethinkdb]',
            'redis = apscheduler.jobstores.redis:RedisJobStore [redis]',
            'zookeeper = apscheduler.jobstores.zookeeper:ZooKeeperJobStore [zookeeper]'
        ]
    }
)
