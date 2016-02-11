# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:12:48 2016

@author: Nico Barnafi
"""
#import threading
import sys


ideal_down = 80.
ideal_up = 40.

def listen_write(T):
    from time import time, ctime, sleep
    from speedtest_cli import speedtest
    from Twitter import Twitter

    def mean(l):
        return float(sum(l))/len(l)

    def write_to_log(m):
        f = open('log', 'r')
        texto = f.read()
        f.close()
        f = open('log','w')
        texto = texto + '%s' % m
        f.write(texto)
        f.close()

    Twt = Twitter()
    data = []
    unit = 1000000
    print 'Simulate for %.2f hours' % T
    current_T = time()
    start_T = time()
    mins_5, dia = 300, 86400
    diff_update = 0
    diff_tweet = 86400
    speeds_down, speeds_up = [], []
    while current_T - start_T <= T*3600:
        if current_T - start_T >= diff_update:
            print '%.2f/%.2f hours to go' % (current_T/3600.-start_T/3600., T)
            try:
                down, up = speedtest()
            except:
                print 'Connection error, restarting...'
                continue
            speeds_down.append(down)
            speeds_up.append(up)
            line = '%s;%.2f;%.2f\n' % (ctime(),down/unit, up/unit)
            write_to_log(line)
            #data.append('%s;%.2f;%.2f\n' % (ctime(),down/unit, up/unit))
            current_T = time()       
            diff_update += mins_5 # Update every 5 minutes
        else:
            sleep(30)
            current_T = time()
        if current_T - start_T >= diff_tweet and mean(speeds_down)/unit < ideal_down and mean(speeds_up)/unit < ideal_up:
            msge = '%.2f Down y %.2f Up (avg diario) es menos de lo acordado o no? #VTR #ParenDeCagarme' % (mean(speeds_down)/unit, mean(speeds_up)/unit)
            Twt.tweet(msge)
            diff_tweet += dia
            current_T = time()

def monitor(T):
    print "InternetSpeed monitor started. Monitoring for %.2f hours (%.0f days) " % (T, T/24.)
    f = open('log','w')
    f.close()
    D = listen_write(T)
    
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-t', type = float, dest='sim_time', help='Time to control in hours.', required = True)
    args = parser.parse_args()
    T = args.sim_time
    monitor(T)
    print 'Done... profit.'
    

