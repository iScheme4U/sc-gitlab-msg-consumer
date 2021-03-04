.. image:: https://badge.fury.io/py/sc-gitlab-msg-consumer.svg
    :target: https://badge.fury.io/py/sc-gitlab-msg-consumer
.. image:: https://img.shields.io/pypi/pyversions/sc-gitlab-msg-consumer
    :alt: PyPI - Python Version

A simple message consumer for Gitlab WebHook messages
=====================================================

This project provides A simple message consumer for Gitlab WebHook messages that were previously sent to a rocketmq server

Installation
------------

It is possible to install the tool with `pip`::

    pip install sc-gitlab-msg-consumer

Configuration
-------------

First, make sure /var/opt/sc directory exists, if not create this directory and make sure current user has the right
to create files in this directory.

You can copy `default.yml <https://github.com/Scott-Lau/sc-gitlab-msg-consumer/blob/master/consumer/tests/sample_config/default.yml>`_
to /var/opt/sc/.sc-gitlab-msg-consumer/production.yml to initialize the production configuration.

The default configuration file looks like this::

    dev:
      # whether this program is running is development mode
      dev_mode: False

    # rocketmq configurations
    rocketmq:
      # name server ip
      name_server_ip: "localhost"
      # name server port
      name_server_port: 9876
      # group id
      group_id: "GITLAB_WEBHOOK_MSG_CONSUMER"
      # message topic
      msg_topic: "GITLAB_WEBHOOK"



Running
-------

After installation and configuration, you can simply run this program using::

    sh sc-gitlab-msg-consumer

Logs will be saved at /tmp/logs/sc-sys.log

Dependencies
------------

* `sc-utilities <https://github.com/Scott-Lau/sc-utilities>`_ >= 0.0.2
* `sc-config <https://github.com/Scott-Lau/sc-config>`_ >= 0.0.3
* `rocketmq-client-python <https://github.com/apache/rocketmq-client-python>`_ >= 2.0.0

License
-------

The script is released under the MIT License.  The MIT License is registered
with and approved by the Open Source Initiative [1]_.

.. [1] https://opensource.org/licenses/MIT
