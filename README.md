# Create_Invite_ListN
This project deals with creating a Customer list to invite customers within 100km of our Dublin office for some food and drinks. the output is a *.txt file with Name and User Id of the customers to be invited.

customers.txt : contains the complete customer list with names, userId and their GPS locations in JSON format
upload_customer_details.py : read customers.txt.
create_invite_list.py : Check whether the  distance between the customers location and dublin office is less than 100 km and output the result into InviteList.txt file.
calculate_distance.py : calculate the distance between the customers location and dublin office using great_circle distance formula.
InviteList.txt : final sorted list containing Names and User Id of the cuatomers to be invited.

To execute : 
1. Download and install Anaconda3 (https://docs.anaconda.com/anaconda/install/) 
2. Download all the python files and customer.txt file into a folder under Anaconda3 
3. To execute the code open the Anaconda3 prompt > move to the folder created (cd "filename") > run create_invite_list.py (python create_invite_list.py)
4. Output will be saved in the same folder.
