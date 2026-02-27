# FILE NAME - firewall_traffic_analyzer.py

# NAME: Nicholas Thurston
# DATE: 2/26/2026
# BRIEF DESCRIPTION: Firewall Traffic Analyzer Program  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    def traffic_analyzer():

        print('=== Network Traffic Security Analyzer ===\n')
        # Ask user for port number
        port_num = int(input('Enter the port number (e.g. 80, 22, 443, 3389): '))
        # Ask the user for transfer size
        xfer_size = int(input('Enter the data transfer size in megabytes (MB): '))

        # Firewall log message
        print(f'\nFIREWALL LOG:\nPort: {port_num}, Transfer Size: {xfer_size} MB')

        # Analyzer logic
        if (port_num == 22 or port_num == 3389) and xfer_size >= 100:
            print('HIGH RISK: Potential unauthorized remote access detected!')
        elif port_num == 80 and xfer_size > 100:
            print('MEDIUM RISK: Large unencrypted data transfer detected.')
        elif port_num == 443:
            print('LOW RISK: Secure encrypted transfer detected.')
        else:
            print('UNKNOWN: Unrecognized traffic pattern.')
    
    traffic_analyzer()
main()








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?


No, I have experience using compound expressions like that so I didn't get stuck there.




'''
