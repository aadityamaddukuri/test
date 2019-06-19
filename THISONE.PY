#importing modules and workbooks
from openpyxl import load_workbook
import WazeRouteCalculator as wrc
wb=load_workbook('rawdata.xlsx')
sheet_ranges=wb['rawdata']
ws2=wb['output']

#for loop iterates down the rawdata sheet, using latitude and longitude as start/end points
for i in range (7,34):
    start_lat=round((sheet_ranges['P'+ str(i)].value),3)
    start_lon=round((sheet_ranges['Q'+ str(i)].value),3)
    from_address=str(start_lat)+" "+str(start_lon)
    end_lat=round((sheet_ranges['P'+ str(i+1)].value),3)
    end_lon=round((sheet_ranges['Q'+ str(i+1)].value),3)
    to_address=str(end_lat)+" "+str(end_lon)
   
    route = wrc.WazeRouteCalculator(from_address, to_address, region)
 
    time=0
    time_increment=15
    time_total=135
    #time, time_increment, time_total are used for this while loop, and finds traffic as a measure of time. 
    #When same code is replaced by a for loop it doesnt work. Don't know why.
    while time <=time_total:
        time_delta=time
        k=route.calc_route_info(time_delta)
        timetaken=round(k[0],2)
        distance=k[1]
        ws2["A"+str(i-4)]=from_address
        ws2["B"+str(i-4)]=to_address
        ws2["C"+str(i-4)] = float(str(distance))
        ws2[(chr(ord('D')+int(time/time_increment)))+str(i-4)] =float(str(timetaken)) #time/time_increment used to iterate down the alphabet
        wb.save('rawdata.xlsx')
        time=time+time_increment
