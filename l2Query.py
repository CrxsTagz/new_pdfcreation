import mysql.connector
from mysql.connector import Error
from fpdf import FPDF
from datetime import datetime

#wssID = 80

def l2pdfGenerator(wssID):
    try:
        connection = mysql.connector.connect(host='100.64.0.1',
                                         database='sifi',
                                         user='root',
                                         password='sifi')
        cursor = connection.cursor()
        sql_select_Query = "SELECT * FROM l2isolation where wssid = {};".format(str(wssID))
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        pdf = FPDF('P', 'mm', (300, 150))
        date = datetime.now().strftime("%Y_%m_%d-%I-%M-%S_%p")
        # Add page
        pdf.add_page()
        pdf.set_font("Arial", 'B', size= 16)
        # Loop through query payload (2D array)
        for row in records:
            payload = ''
            # Loop through each row's tuple
            for i in row:
                # Concat into single string
                payload = payload + str(i) + ' '
            # Add string to PDF
            pdf.cell(200,10, txt=payload, align= 'L')
            # Print new line into PDF
            pdf.ln(10)
            print(payload)
        # Save PDF file
        pdfFilePath = "L2_{}.pdf".format(date)
        pdf.output(pdfFilePath)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
#l2pdfGenerator(wssID)