#!/usr/bin/env python

# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.
import random 
import email
import getpass, imaplib
import os
f = open('/home/pi/currentDEVICESET', 'r') 
DEVICE = f.read()
f.close()
import sys
import time
from boto import dynamodb2
from boto.dynamodb2.table import Table
from boto.s3.connection import S3Connection

TABLE_NAME = ""
REGION = "us-west-2"
conn = dynamodb2.connect_to_region(
	REGION,
	aws_access_key_id='AKIAICN44BGVRGEMGI3Q',
	aws_secret_access_key='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')

table = Table('aecdevice', connection=conn)
try:
	item = table.get_item(deviceName=DEVICE)
	print item
except:
	item = False

if (item):
	print "yes, We have a match"
	# we have a print
	# now we need to retrieve and download that print along with upadte that user that his print is currently being printed
	item['Data']['BatteryPercentage'] = random.randint(0,100)
	item.save(overwrite=True)
	time.sleep(5)
	
	# here we grab from the s3 bucket
	# conns3 = S3Connection('AKIAICN44BGVRGEMGI3Q', 'ugchXirJEneSZA0xfSFRCqUeLUZr7yERGTNkUEY0')
	# print item['queue'][0]
	# fileName = ''
	# emailAddress = ''
	# for x in item['queue'][0]:
	# 	print x
	# 	if (x[-1:] == 'l' or x[-1:] == 'L' or x[-1:] == 'e' or x[-1:] == 'E'):
	# 		fileName = x
	# 	elif (x[-1:] == 'm' or x[-1:] == 'u'):
	# 		emailAddress = x
	# print emailAddress, fileName		
			
	# for bucket in conns3.get_all_buckets():
	# 	#here we grab the file from the item queue
	# 	if (bucket.name == 'mobiumsprinter'):
	# 		filePath = '/'+PRINTER+'/prints/' + fileName
	# 		filePut = '/home/pi/Mobiumsv0.3RaspUltimaker/Prints/' + fileName
	# 		key = bucket.get_key(filePath)
	# 		print key
	# 		key.get_contents_to_filename(filePut)
	# # here we update the users account
	# tableuser = Table('mobiums', connection=conn)
	# itemUser = tableuser.get_item(
	# 		userID=emailAddress)
	# # we need to update the user by decresing the inQueue and increasing the printed.
	# #print itemUser['prints']
	# itemUser['prints']['inQueue'] = itemUser['prints']['inQueue'] - 1
	# itemUser['prints']['inProgress'] = itemUser['prints']['inProgress'] + 1
	# #print itemUser['prints']['inQueue'], itemUser['prints']['inProgress'] 
	# itemUser.save(overwrite=True)
	# # we can also send a notification to it's social data base here.
	# tablesocial = Table('mobiumssocial', connection=conn)
	# itemSocial = tablesocial.get_item(
	# 		userID=emailAddress)
	# notification = 'Print Started for ' + PRINTER
	# print itemSocial['notificationList'] 
	# try:
	# 	itemSocial['notificationList'] = itemSocial['notificationList'].append(notification)
	# except:
	# 	itemSocial['notificationList'] = [notification]
	# itemSocial['notifications'] = itemSocial['notifications'] + 1
	# itemSocial.save(overwrite=True)
	# f = open('/home/pi/Mobiumsv0.3RaspUltimaker/currentPrintFile', 'w')
	# f.write(fileName)
	# f.close()

	# here we email the user
	#still under dev.
	# var from = 'admin@mobiumsolutions.com';
  
#   var to1 = userID;
#   var body = "Your printer has indicated that it has started to print your file. Your file should be completed in approximately " + item.queue.L[0].SS[2] + " minutes. We'll notify you when it's ready for pickup!";
#   var subject = "New print has started on " + 'mobiumSolutions';
#   var mailOptions1 = {
#     to: to1,
#     from: from,
#     subject: subject,
#     text: body
#   };
#   transporter.sendMail(mailOptions1, function(err) {
#       # we emailed the user!
#   });
