#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "č, š, ž"
secret = 10
guess = int(raw_input("Vnesite skrito celo število, vrednosti 1-100:")) #vnos skrite stevilke
if guess == secret:
    print "Čestitamo. Uganili ste pravo število"
elif guess != secret:
    print "Napačno število"
