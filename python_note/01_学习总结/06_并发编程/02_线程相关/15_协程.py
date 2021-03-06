#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"


'''
单核如何实现并发效果？
    单进程创建多线程，操作系统在不同的线程之间切换（切换之前保留线程执行状态），所以单核多线程能实现并发效果。

但是如果只有一个线程，如何实现并发效果？
    这就需要程序员自己控制了，一个线程中编写多个任务，每个任务执行一部分就保留当前任务信息并切换到写一个任务，如此交替，
    便实现了并发效果，这叫做协程。




'''




