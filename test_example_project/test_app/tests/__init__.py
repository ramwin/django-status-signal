#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging

from django.test import TestCase
from test_app.models import Task, post_save, normal_post_save


logger = logging.getLogger(__name__)


class TaskTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(status="start")

    def test(self):
        logger.info('test django status signal')
        post_save.send(Task, self.task.status)
        logger.info('this line should connect with previous line `test basic use`')
        self.task.status = 'success'
        self.task.save()
        # breakpoint()
        with self.assertRaises(Exception):
            post_save.send(Task, self.task.status)

    def test_normal(self):
        logger.info('test django normal signal use')
        with self.assertRaises(Exception):
            normal_post_save.send(sender=Task,
                                  instance=self.task)
        logger.info('this line should not connect with previous line `test basic use`')
        self.task.status = 'success'
        self.task.save()
        # breakpoint()
        with self.assertRaises(Exception):
            normal_post_save.send(sender=Task,
                                  instance=self.task)
            normal_post_save.send(sender=Task, instance=self.task)
