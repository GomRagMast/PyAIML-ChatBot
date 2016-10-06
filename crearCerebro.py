#!usr/bin/python
# -*- coding: utf-8 -*-
import aiml 
k=aiml.Kernel();
k.learn("sara.aiml")
k.respond("Cargando el Aiml b..")
k.saveBrain("cerebro.brn")
