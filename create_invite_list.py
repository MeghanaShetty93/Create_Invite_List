#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
from upload_customer_details import get_details
from calculate_distance import calculate_great_circle
from operator import itemgetter

def invite_list():
    custList = []
    inviteList = []
    dublin_office_lat = 53.339428
    dublin_office_long = -6.257664

    #Upload text file
    custList = get_details()

    #calculate the customers within 100km of Dublin Office 
    print("Invite List saved in InviteList.txt\n")
    for customer in custList:
        calc_distance = calculate_great_circle(dublin_office_long, dublin_office_lat,float(customer["longitude"]),float(customer["latitude"]))
        if calc_distance < 100:        
        
            #Print the customers name and user_id
            inviteDict =  {"Name" : customer["name"], "User Id" : customer["user_id"]}
            inviteList.append(inviteDict)

    #sorted customer list according to user_id 
    sortedInviteList = sorted(inviteList, key=itemgetter('User Id')) 

    for final_list in sortedInviteList:
        #Final list saved in InviteList.txt
        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        print("Name : %s\tUser ID : %s " %(final_list['Name'],final_list['User Id']), file=open(os.path.join(currentDirectory, 'InviteList.txt'),'a'))

if __name__ == "__main__":
    invite_list()


# In[ ]:




