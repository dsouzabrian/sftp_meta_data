import pysftp
import logging
import os.path, time
import datetime
import time
import ftplib
import csv
locate="Kindly type here the location of file"
key="Mention here the location for pem file"
myHostname = "Kindly type here the ip address"
myUsername = "Kindly type here the username"
myPassword = "Kindly type here the password"
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
logging.basicConfig(level = logging.INFO, filename = time.strftime("D:\\log\\metedatalog-%Y-%m-%d.log"))
def sftpMetaData(inputname):    
    try:
        csv_file = open(inputname+'_sftp.csv','w',newline="")

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['Index_Name','Folder','File_Name','Size','Last_Modified','Last_Accessed'])
        with pysftp.Connection(host=myHostname, username="myUsername", private_key=key, private_key_pass="myPassword",cnopts = cnopts) as sftp:
            logging.info("Connection succesfully stablished ... ")
            print("Connection succesfully stablished ... ")

            check_dir = locate
            print('Mentioning the directory)
            folders = sftp.listdir(check_dir)
            for folder in folders:
                index_path_folder = check_dir+'/'+ folder
                print("Folder path "+index_path_folder)
                filesInsideFolder = sftp.listdir(index_path_folder)
                for file in filesInsideFolder:
                    print("Files inside"+folder+file) 
                    filePath = index_path_folder+'/'+file
                    info = sftp.stat(filePath)
                    #Returns the information of file
                    print("Information of file::"+info)
                    modified_time =datetime.datetime.fromtimestamp(info.st_mtime).isoformat()
                    print(modified_time)
                    accessed_time =datetime.datetime.fromtimestamp(info.st_atime).isoformat()
                    print(accessed_time)
                    csv_writer.writerow([inputname,folder,file,info.st_size,modified_time,accessed_time])
                
        csv.close()
    except Exception as e:
        logging.info("Error")
        print("Error ... "+str(e))
        logging.info(str(e))
sftpMetaData("Kindly mention the file name")
